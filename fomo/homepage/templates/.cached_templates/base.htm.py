# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1485382770.870718
_enable_loop = True
_template_filename = '/Users/JairoMan/Desktop/Winter2017/IS411_413/assignments/fomo/homepage/templates/base.htm'
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
        __M_writer('        <script src="http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js"></script>\n\n')
        __M_writer('        ')
        __M_writer(str( get_template_css(self, request, context) ))
        __M_writer('\n\n    </head>\n    <body>\n\n        <header>\n            <h1>Welcome to the homepage app!<h1>\n        </header>\n\n        ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\n\n')
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
        __M_writer('\n            Site content goes here in sub-templates.\n        ')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/JairoMan/Desktop/Winter2017/IS411_413/assignments/fomo/homepage/templates/base.htm", "uri": "base.htm", "source_encoding": "utf-8", "line_map": {"18": 4, "20": 0, "29": 2, "30": 4, "31": 15, "32": 18, "33": 18, "34": 18, "39": 29, "40": 32, "41": 32, "42": 32, "48": 27, "54": 27, "60": 54}}
__M_END_METADATA
"""
