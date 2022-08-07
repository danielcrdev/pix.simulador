from flask import Response
import xmltodict
import scenery

# import json
# print(json.dumps(dict_format, sort_keys=True, indent=4))

#------------------------------------------------------------------------------------------------#
# Start Streaming
#------------------------------------------------------------------------------------------------#


def start(ispb):

    resp = Response()
    resp.headers['PI-ResourceId'] = 'UEkBbgR78VqKK/uvuq9O0r9bqXyBH9Ur'
    resp.headers['PI-Pull-Next'] = '/api/v1/out/12345678/stream/f0d744d792d6'
    resp.status = 200

    return resp

#------------------------------------------------------------------------------------------------#
# Stop Streaming
#------------------------------------------------------------------------------------------------#


def stop(ispb, next):

    resp = Response()
    resp.status = 200

    return resp


#------------------------------------------------------------------------------------------------#
# Next Streaming
#------------------------------------------------------------------------------------------------#


def pull_next(ispb, next):

    resp = Response()

    existe_registro = True
    # existe_registro = False

    if existe_registro:
        with open('docs/pacs.008.xml') as fd:
            dict_format = xmltodict.parse(fd.read())

        dict_format['Envelope']['AppHdr']['Fr']['FIId']['FinInstnId']['Othr']['Id'] = scenery.EXTERNAL_ISPB_PSP

        resp.status = 200
        resp.headers['PI-ResourceId'] = 'UEkBbgR78VqKK/uvuq9O0r9bqXyBH9Ur'
        resp.headers['PI-Pull-Next'] = '/api/v1/out/12345678/stream/f0d744d792d6'
        resp.mimetype = 'text/xml'
        resp.data = xmltodict.unparse(dict_format, pretty=True)
    else:
        resp.status = 204
        resp.headers['PI-Pull-Next'] = '/api/v1/out/12345678/stream/f0d744d792d6'

    return resp
