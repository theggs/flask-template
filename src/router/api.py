from flask import Blueprint, jsonify
from utils import RError, logger, response_json_xxx
from service.example import example as example_func

main = Blueprint('api', __name__)


@main.errorhandler(RError)
def handle_rerror(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response


@main.errorhandler(Exception)
def handle_exception(error):
    logger.exception(error)
    message = repr(error)
    try:
        code = error.response
    except AttributeError:
        code = 500
    response = response_json_xxx(code, message)
    return response


@main.route('/example')
def example():
    example_result = example_func()
    return jsonify(example_result)
