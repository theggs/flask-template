import logging
from flask import jsonify, request

logger = logging


class RError(Exception):
    status_code = 400

    def __init__(self, code, message, payload=None, e=None, **kwargs):
        Exception.__init__(self)
        self.message = message
        if code is not None:
            self.status_code = code
        self.payload = payload
        self.kwargs = kwargs

        if e is not None:
            logger.exception(e)

    def to_dict(self):
        rv = dict(self.payload or ())
        rv.update(code=self.status_code)
        rv.update(**self.kwargs)
        if isinstance(self.message, str):
            rv.update(message=self.message)
        else:
            rv.update(message=repr(self.message))
        return rv


def response_json_200(message='ok', jsonify_func=jsonify, **kwargs):
    return jsonify_func(
        code=200,
        message=message,
        **kwargs,
    )


def response_json_xxx(code, message=None, jsonify_func=jsonify, **kwargs):
    response = jsonify_func(
        code=code,
        message=message,
        **kwargs,
    )
    response.status_code = code
    return response


def get_request_arg(arg: str) -> str:
    try:
        result = request.args[arg]
    except KeyError:
        raise RError(400, '请求参数缺少 {}。'.format(arg))
    return result


def get_request_json_prams(*verify_args):
    result = request.get_json()
    for arg in verify_args:
        if arg not in result:
            raise RError(
                400, '请求参数缺少 {}。'.format(arg)
            )
    return result
