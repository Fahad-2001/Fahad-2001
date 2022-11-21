from odoo import models, fields, api


class SaleReportXlsx(models.Model):
    _name = 'sales.report'


class InheritPurchaseOrder(models.Model):
    _inherit = 'account.move'

    def GetYear(self, date):
        print(date)
        return str(date.year) + '-' + str(int(date.year) + 1)
