from odoo import models, fields, api


class InheritSaleOrder(models.Model):
    _inherit = 'account.move'


class ProductViewWizard(models.TransientModel):
    _name = "product.view.wizard"
    _description = "Product View Wizard"
    _rec_name = "date_from"

    date_from = fields.Date(string='Date From', required=1)
    date_to = fields.Date(string='Date To', required=1)

    def action_product_excel_report(self):
        data = {
            'date_from': self.date_from,
            'date_to': self.date_to,
            'form_data': self.read()[0]
        }
        return self.env.ref('sale_reports.report_sale_product_view_xls').report_action(self, data=data)
