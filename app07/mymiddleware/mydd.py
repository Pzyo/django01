from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import HttpResponse

class MyMiddleware1(MiddlewareMixin):
    def process_request(self, request):
        print('我是第一个自定义中间件里面的process_request方法')


    def process_response(self, request, response):
        """

        :param request:
        :param response: 就是django后端返回给浏览器的内容
        :return:
        """
        print('我是第一个自定义中间件里面的process_reponse方法')
        return response

    def process_view(self, request, view_name, *args, **kwargs):
        print(view_name, args, kwargs)
        print('我是第一个自定义中间件里面的process_view方法')

    def process_template_response(self, request, response):
        print('我是第一个自定义中间件里面的process_template_response方法')
        return response

    def process_exception(self, request, exception):
        print('我是第一个自定义中间件里面的process_exception方法')
        print(exception)

class MyMiddleware2(MiddlewareMixin):
    def process_request(self, request):
        print('我是第二个自定义中间件里面的process_request方法')
        # return HttpResponse('baby!')

    def process_response(self, request, response):
        print('我是第二个自定义中间件里面的process_reponse方法')
        return response

    def process_view(self, request, view_name, *args, **kwargs):
        print(view_name, args, kwargs)
        print('我是第二个自定义中间件里面的process_view方法')

    def process_template_response(self, request, response):
        print('我是第二个自定义中间件里面的process_template_response方法')
        return response

    def process_exception(self, request, exception):
        print('我是第二个自定义中间件里面的process_exception方法')
        print(exception)