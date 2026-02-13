# -*- coding: utf-8 -*-
# from odoo import http


# class AboutUs(http.Controller):
#     @http.route('/about_us/about_us', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/about_us/about_us/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('about_us.listing', {
#             'root': '/about_us/about_us',
#             'objects': http.request.env['about_us.about_us'].search([]),
#         })

#     @http.route('/about_us/about_us/objects/<model("about_us.about_us"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('about_us.object', {
#             'object': obj
#         })

