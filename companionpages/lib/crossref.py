import logging

import requests

logger = logging.getLogger(__name__)

"""

Publishers return information in unixref1.0 or unixref1.1.

http://doi.crossref.org/schemas/unixref1.1.xsd
http://doi.crossref.org/schemas/unixref1.0.xsd

The crossref servlet provides unixsd which provides the publisher
content along with crossref-specific metadata.

http://www.crossref.org/schemas/crossref_query_output3.0.xsd
http://help.crossref.org/#unixsd

"""


def query(pid, doi, timeout=0.60):
    """ returns a dictionary optionally populated with Article and Collaborator attributes

    pid: a validated username for the crossref query service
    doi: a validated doi string
    timeout: time in seconds that we are willing to wait for an answer. default is 60 milliseconds.

    exceptions: no exception or error from this call should affect the client.
    It catches problems and moves on.
    """

    try:
        r = requests.get('http://doi.crossref.org/servlet/query', params={
            'pid': pid,
            'noredirect': True,
            'id': doi,
            'format': 'unixsd', },
            timeout=timeout)
    except requests.exceptions.RequestException:
        logger.debug('crossref requests exception')
        logger.warning('crossref requests exception')
        return {'msg': 'requests exception', 'status': 500}

    if not r.ok:
        logger.warning('crossref exception %s', r)
        return {'msg': 'crossref exception', 'status': r.status_code, 'xml': r.text}

    # todo
    return {'msg': 'ok', 'status': r.status_code, 'xml': r.text}
