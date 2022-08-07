from flask import Blueprint, request
from service import healthcheck, get_msgs, send_msgs


api = Blueprint('api', __name__, url_prefix='/pixsm/api')


def get_blueprint():
    return api

#------------------------------------------------------------------------------------------------#
# healthcheck
#------------------------------------------------------------------------------------------------#


@api.route('/v1/healthcheck/status', methods=['GET'])
def get_healthcheck_v1_status():
    return healthcheck.status(), 200


@api.route('/v1/out/<ispb>/stream/start', methods=['GET'])
def get_msgs_start(ispb):
    return get_msgs.start(ispb)


@api.route('/v1/out/<ispb>/stream/<next>', methods=['GET'])
def get_msgs_pull_next(ispb, next):
    return get_msgs.pull_next(ispb, next)


@api.route('/v1/out/<ispb>/stream/<next>', methods=['DELETE'])
def get_msgs_stop(ispb, next):
    return get_msgs.stop(ispb, next)


@api.route('/v1/in/<ispb>/msgs', methods=['POST'])
def send_msgs_send(ispb):
    return send_msgs.send(ispb, request.data)
