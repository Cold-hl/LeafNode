import time
import json
from django.utils.deprecation import MiddlewareMixin
import urllib.parse
# 获取日志logger
import logging

logger = logging.getLogger(__name__)


class LogMiddle(MiddlewareMixin):

    # 日志处理请求中间件
    def process_request(self, request):

        # 获取请求ip
        if 'HTTP_X_FORWARDED_FOR' in request.META.keys():
            ip = request.META['HTTP_X_FORWARDED_FOR']
        else:
            ip = request.META['REMOTE_ADDR']
        request_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

        # 请求路径
        path = request.path

        # 请求方式
        method = request.method

        message = '%s: [%s] \'%s\' %s' % (ip, request_time, path, method)
        logger.info(message)
        return None

    # 日志处理返回中间件
    def process_response(self, request, response):

        # 获取请求ip
        if 'HTTP_X_FORWARDED_FOR' in request.META.keys():
            ip = request.META['HTTP_X_FORWARDED_FOR']
        else:
            ip = request.META['REMOTE_ADDR']

        localtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        # 请求路径
        path = request.path
        # 请求方式
        method = request.method
        # 响应状态码
        status_code = response.status_code
        # 响应内容
        content = response.content

        # 记录信息
        content = str(content.decode('utf-8'))
        content = urllib.parse.unquote(content)
        try:
            content = (json.loads(content))
        except json.decoder.JSONDecodeError:
            # 如果错误类型异常
            if status_code in [404, 500]:
                content = "ERROR"
                message = '-- %s error ip：%s url:\'%s\' %s [%s] SYSTEM_RESPONSE :: %s' % (
                    localtime, ip, path, method, status_code, content)
                logger.error(message)
                return response
            elif '<!DOCTYPE html>' in content:
                content = "DATA IS HTML"
            else:
                content = "DATA NOT JSON"

        message = '%s: [%s] \'%s\' %s [%s] SYSTEM_RESPONSE :: %s' % (ip, localtime, path, method, status_code, content)
        logger.info(message)
        return response
