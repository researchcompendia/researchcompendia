#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
from tempfile import mkdtemp
from os import path, stat, walk, pardir
import re
import subprocess
from zipfile import is_zipfile, ZipFile, ZIP_DEFLATED, ZIP_STORED

try:
    import zlib  # noqa
    compression = ZIP_DEFLATED
except:
    compression = ZIP_STORED

logger = logging.getLogger('researchcompendia.verify')


def verify(request):
    """ runs code for an article if code is available and checks that results match

    right now all it's going to do is unarchive archives it gets from a url and and run main

    request: a dictionary with request information
        {
            id: request id
            path_to_target: string that is a path. we will a nicer representation that is storage agnostic
            parameters: { parameter dictionary }
        }

    returns: reponse dictionary
        {
            id: response id
            requestid: request id
            message: human readable status that is translatable
            output_files: [ { path: path to file, size: size in bytes } ... ]
        }
    """

    logger.debug("request: %s", request)
    requestid = request.get('id', None)
    path_to_target = request.get('path_to_target', None)

    response = {}

    valid, reason = validate(request)
    if not valid:
        response.update({'status': 400, 'message': reason})
        logger.debug(response)
        return response

    tmpdir = mkdtemp(prefix='compendia')
    with ZipFile(path_to_target) as zf:
        zf.extractall(path=tmpdir)

    zip_basename = get_zip_basename(path_to_target)
    rundir = path.join(tmpdir, zip_basename)
    outputdir = path.join(rundir, 'compendiaoutput')
    main = path.join(rundir, 'main')

    if not path.isfile(main):
        response.update({'status': 400, 'message': 'main entrypoint is not a valid file'})
        logger.debug(response)
        return response

    # call main
    subprocess.call(['chmod', '755', main])
    #chmod(main, 755) # executable permissions
    p = subprocess.Popen([main], cwd=rundir, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = p.communicate()

    zip_response_info = zip_and_get_info(outputdir)
    response.update(zip_response_info)
    response.update({
        'status': 201,
        'message': 'ok',
        'output_dir': outputdir,
        'stdout': stdout,
        'stderr': stderr,
        'requestid': requestid,
    })
    logger.debug(response)
    return response


def zip_and_get_info(outputdir):
    """ zips files and returns path to zip file with some additional information

    WARNING: flattens directories. files with the same name will be clobbered.
    """
    parentdir = path.abspath(path.join(outputdir, pardir))
    path_to_zip = path.join(parentdir, 'compendiaoutput.zip')
    output_files = []
    with ZipFile(path_to_zip, 'w', compression) as zf:
        for root, dirs, files in walk(outputdir):
            for f in files:
                fpath = path.join(root, f)
                zf.write(fpath, f)
                statinfo = stat(fpath)
                output_files.append({'file': f, 'size': bytes2human(statinfo.st_size), 'bytes': statinfo.st_size})
    zstat = stat(path_to_zip)
    return {
        'output_files': output_files,
        'path_to_zipped_output': path_to_zip,
        'zipsize': bytes2human(zstat.st_size),
        'zipbytes': zstat.st_size,
    }


def validate(request):
    """ validates request

    returns (True,) or (False, reason)
    """
    requestid = request.get('id', None)
    path_to_target = request.get('path_to_target', None)

    if requestid is None or path_to_target is None:
        return False, 'missing information in request'

    if not is_zipfile(path_to_target):
        # you can have any archive format that you want as long as it is zip
        return False, 'target is not a zipfile'

    match = re.search(r'(?P<unzip>.*)(.zip$)', path.basename(path_to_target))
    if match is None or 'unzip' not in match.groupdict():
        return False, 'unable to find archive directory'

    return True, 'ok'


def get_zip_basename(filepath):
    """ returns base part of filename with .zip suffix removed
    this becomes the the directory name where 'main' is
    """
    filename = path.basename(filepath)
    match = re.search(r'(?P<unzip>.*)(.zip$)', filename)
    if match is None or 'unzip' not in match.groupdict():
        return filename
    return match.groupdict()['unzip']


# http://goo.gl/zeJZl
def bytes2human(n, format="%(value)i%(symbol)s"):
    """
    >>> bytes2human(10000)
    '9K'
    >>> bytes2human(100001221)
    '95M'
    """
    symbols = ('B', 'K', 'M', 'G', 'T', 'P', 'E', 'Z', 'Y')
    prefix = {}
    for i, s in enumerate(symbols[1:]):
        prefix[s] = 1 << (i + 1) * 10
    for symbol in reversed(symbols[1:]):
        if n >= prefix[symbol]:
            value = float(n) / prefix[symbol]
            return format % locals()
    return format % dict(symbol=symbols[0], value=n)


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--id', help='request id')
    parser.add_argument('zipfile', help='path to zipfile')
    args = parser.parse_args()
    logger.setLevel(logging.DEBUG)
    logger.addHandler(logging.StreamHandler())
    r = verify({'id': args.id, 'path_to_target': args.zipfile})
