#!/usr/bin/env python
import argparse
import json
from os.path import isfile
import requests


"""
Utility script for calling verification api from command line

Here is an example of how you would call it from the command line. In this example, we
are passing parameters to "Pizza Meetup Ordering Algorithm", which is compendia 11. $ is the
command line.

$ ./verify.py 11 --host=labs.researchcompendia.org --parameters=pizza.json

This request results in this output:


{
  "message": "ok",
  "output_dir": "/tmp/compendiaSjNQzA/hellopizza/compendiaoutput",
  "output_files": [
    {
      "bytes": 101,
      "file": "pizza_order.json",
      "size": "101B"
    }
  ],
  "path_to_zipped_output": "/tmp/compendiaSjNQzA/hellopizza/compendiaoutput.zip",
  "requestid": "messageidnotusedyet",
  "status": 201,
  "stderr": "",
  "stdout": "{'attending': 33, 'pizzas': {'cheese': 3, 'meat': 3, 'vegan': 1, 'veg': 4}}\n\n    33 people will show up (guess)\n    3 cheese pizzas\n    3 meat pizzas\n    4 vegetarian pizzas\n    1 vegan pizzas\n    \n",  # noqa
  "zipbytes": 199,
  "zipsize": "199B"
}
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
