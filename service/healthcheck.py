from flask import abort, Response
import xmltodict

#------------------------------------------------------------------------------------------------#
# Lista movimento financeiro da base
#------------------------------------------------------------------------------------------------#


def status():

    resp = {
        'status': 'UP'
    }

    return Response(xmltodict.unparse(resp, pretty=True), status=200, mimetype='text/xml')
