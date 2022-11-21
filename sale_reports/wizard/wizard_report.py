from odoo import models, fields, api


class InheritTax(models.Model):
    _inherit = 'account.tax'


class InvoiceViewWizard(models.TransientModel):
    _name = "invoice.view.wizard"
    _description = "Invoice View Wizard"
    _rec_name = "date_from"

    date_from = fields.Date(string='Date From', required=1)
    date_to = fields.Date(string='Date To', required=1)

    def action_invoice_excel_report(self):
        data = {
            'date_from': self.date_from,
            'date_to': self.date_to
        }
        return self.env.ref('sale_reports.report_invoice_view_xls').report_action(self, data=data)
