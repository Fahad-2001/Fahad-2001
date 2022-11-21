# -*- coding: utf-8 -*-
# from odoo import http


# class SalereportExcel(http.Controller):
#     @http.route('/salereport_excel/salereport_excel', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/salereport_excel/salereport_excel/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('salereport_excel.listing', {
#             'root': '/salereport_excel/salereport_excel',
#             'objects': http.request.env['salereport_excel.salereport_excel'].search([]),
#         })

#     @http.route('/salereport_excel/salereport_excel/objects/<model("salereport_excel.salereport_excel"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('salereport_excel.object', {
#             'object': obj
#         })
