import json
import routes

erros = routes.get_blueprint()


@erros.errorhandler(400)
def handle_400_error(e):
    resp = e.get_response()
    resp.content_type = "application/json"
    resp.data = json.dumps({
        "information_code": e.information_code,
        "description_code": e.description_code,
    })
    return resp
