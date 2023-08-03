import logging
from ast import literal_eval
import json

logger = logging.getLogger('observer')


class RequestObserverMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        body = request.body.decode('utf-8')
        request_info = {
            'method': request.method,
            'body': json.loads(body) if body else {},
        }

        response_obj = self.get_response(request)
        response_content = response_obj.content.decode('utf-8')
        response_info = {
            'status_code': response_obj.status_code,
            'content': json.loads(response_content) if response_content else '',
        }

        logger.info(msg=request.build_absolute_uri(), extra=request_info)
        logger.info(msg=request.build_absolute_uri(), extra=response_info)

        return response_obj
