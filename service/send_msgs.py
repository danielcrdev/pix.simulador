from flask import Response, abort
import xmltodict

# import json
# print(json.dumps(data, sort_keys=True, indent=4))


def send(ispb, request_data):

    data = xmltodict.parse(request_data)

    resp = Response()
    resp.status = 201
    resp.headers['PI-ResourceId'] = 'UEkBbgR78VqKK/uvuq9O0r9bqXyBH9Ur'

    return resp