# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1485845099.3685272
_enable_loop = True
_template_filename = '/Users/JairoMan/Desktop/Winter2017/IS411_413/assignments/fomo/fomo/homepage/templates/base.htm'
_template_uri = 'base.htm'
_source_encoding = 'utf-8'
import os, os.path, re, json
from django_mako_plus.filters import django_syntax, jinja2_syntax, template_syntax
_exports = ['content']


from django_mako_plus import get_template_css, get_template_js 

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def content():
            return render_content(context._locals(__M_locals))
        request = context.get('request', UNDEFINED)
        self = context.get('self', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('\n\n\n<!DOCTYPE html>\n<html>\n    <meta charset="UTF-8">\n    <head>\n\n        <title>homepage</title>\n\n')
        __M_writer('        <script src="http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js"></script>\n        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css"\n              integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">\n\n')
        __M_writer('        ')
        __M_writer(str( get_template_css(self, request, context) ))
        __M_writer('\n\n    </head>\n    <body>\n    <div class="row warning">Webpage under maintenance</div>\n        <nav class="navbar navbar-default">\n              <div class="container-fluid">\n                <!-- Brand and toggle get grouped for better mobile display -->\n                <div class="navbar-header">\n                  <button type="button" class="navbar-toggle collapsed" data-toggle="collapse"\n                          data-target="#bs-example-navbar-collapse-1" aria-expanded="false">\n                    <span class="sr-only">Toggle navigation</span>\n                    <span class="icon-bar"></span>\n                    <span class="icon-bar"></span>\n                    <span class="icon-bar"></span>\n                  </button>\n                  <a class="navbar-brand" href="#">FOMO</a>\n                </div>\n\n                <!-- Collect the nav links, forms, and other content for toggling -->\n                <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">\n                  <ul class="nav navbar-nav">\n                    <li ><a href="#">Home</a></li>\n                    <li><a href="#">Contact</a></li>\n                    <li><a href="#">About</a></li>\n                    <li><a href="#">FAQ</a></li>\n                    <li><a href="#">Terms</a></li>\n                  </ul>\n                    <ul class="nav navbar-nav navbar-right">\n                            <li><a href="#">Login</a></li>\n                    </ul>\n\n                </div><!-- /.navbar-collapse -->\n              </div><!-- /.container-fluid -->\n        </nav>\n\n        <div class="container-fluid">\n            <div class="row">\n                <header>\n                     <h1>Welcome to the homepage app!</h1>\n                </header>\n            </div>\n\n            <div class="col-md-2 left">\n\n            </div>\n\n             <div class="col-md-8 center">\n                ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\n            </div>\n\n             <div class="col-md-2 right">\n\n            </div>\n\n        </div>\n\n\n')
        __M_writer('        ')
        __M_writer(str( get_template_js(self, request, context) ))
        __M_writer('\n\n    </body>\n</html>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\n                        Site content goes here in sub-templates.\n                ')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/JairoMan/Desktop/Winter2017/IS411_413/assignments/fomo/fomo/homepage/templates/base.htm", "uri": "base.htm", "source_encoding": "utf-8", "line_map": {"18": 4, "20": 0, "29": 2, "30": 4, "31": 15, "32": 20, "33": 20, "34": 20, "39": 70, "40": 81, "41": 81, "42": 81, "48": 68, "54": 68, "60": 54}}
__M_END_METADATA
"""
