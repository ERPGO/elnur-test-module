# -*- coding: utf-8 -*-
# from odoo import http


# class AcademyTest(http.Controller):
#     @http.route('/academy_test/academy_test/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/academy_test/academy_test/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('academy_test.listing', {
#             'root': '/academy_test/academy_test',
#             'objects': http.request.env['academy_test.academy_test'].search([]),
#         })

#     @http.route('/academy_test/academy_test/objects/<model("academy_test.academy_test"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('academy_test.object', {
#             'object': obj
#         })
