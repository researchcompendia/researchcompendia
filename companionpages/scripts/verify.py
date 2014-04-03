#!/usr/bin/env python
import argparse, json
from os.path import isfile
import requests

"""
Utility script for calling verification api from command line
"""

def verify(parameters, compendia, host='localhost:8000'):
    url = 'http://{}/api/v1/verification/{}/'.format(host, compendia)
    payload = json.dumps({'parameters': parameters})
    r = requests.post(url, data=payload, headers={'content-type': 'application/json'})
    return r.json()


def pretty_json(uglyjson):
    return json.dumps(uglyjson, sort_keys=True, indent=2)


def build_parser():
    parser = argparse.ArgumentParser(description="""
    """)
    parser.add_argument('compendia', help='compendia id')
    parser.add_argument('--parameters', help='json parameters file')
    parser.add_argument('--host', default='localhost:8000', help='host, default localhost:8000')
    return parser


if __name__ == '__main__':
    parser = build_parser()
    args = parser.parse_args()
    if args.parameters:
        assert isfile(args.parameters), 'parameters are not in a valid file'
    with open(args.parameters) as paramfile:
        parameters = json.load(paramfile)
    r = verify(parameters, args.compendia, host=args.host)
    print(pretty_json(r))
