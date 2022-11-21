from odoo import models, fields


class ProductViewXlsx(models.AbstractModel):
    _name = 'report.sale_reports.report_invoice_view_xls'
    _inherit = 'report.report_xlsx.abstract'

    def generate_xlsx_report(self, workbook, data, saleorder):
        sheet = workbook.add_worksheet("Sale Tax Output")
        bold = workbook.add_format({'bold': True, 'align': 'center'})
        center = workbook.add_format({'align': 'center'})
        format = workbook.add_format({'align': 'center', 'bg_color': 'black', 'color': 'white'})
        row = 0
        col = 0
        sheet.set_column('A:C', 18)
        sheet.set_column('D:D', 20)
        sheet.set_column('E:E', 18)
        sheet.set_column('F:F', 35)
        sheet.set_column('G:Z', 19)
        sheet.write(row, col, 'Tax Period', bold)
        sheet.write(row, col + 1, 'NTN', bold)
        sheet.write(row, col + 2, 'Name of Buyer', bold)
        sheet.write(row, col + 3, 'Invoice Number', bold)
        sheet.write(row, col + 4, 'Invoice Date', bold)
        sheet.write(row, col + 5, 'Value of supplies/services (Excl. Sales Tax)', bold)
        sheet.write(row, col + 6, 'Sales Tax Rate %', bold)
        sheet.write(row, col + 7, 'Sales Tax', bold)
        sheet.write(row, col + 8, 'Territory', bold)

        order_lines = []
        if data['date_from']:
            order_lines = self.env['account.move'].search(
                [('invoice_date', '>=', data['date_from']),
                 ('invoice_date', '<=', data['date_to'])])
        else:
            order_lines = self.env['account.move'].search(
                [('invoice_date', '>=', data['date_from']),
                 ('invoice_date', '<=', data['date_to'])])

        record = order_lines.filtered(lambda rec: 'INV' in rec.name)
        total_tax = 0
        price_subtotal = 0
        for rec in record:
            for line in rec.invoice_line_ids:
                if not line.tax_ids:
                    return False
                else:
                    total_tax += line.price_subtotal * (list(line.tax_ids)[0].amount / 100)
                price_subtotal += line.price_subtotal
                col = 0
                row += 1
                sheet.write(row, col, 'Tax Period', center)
                sheet.write(row, col + 1, rec.partner_id.vat, center)
                sheet.write(row, col + 2, rec.partner_id.name, center)
                sheet.write(row, col + 3, rec.name, center)
                sheet.write(row, col + 4, str(rec.invoice_date), center)
                sheet.write(row, col + 5, line.price_subtotal, center)
                for tax in line.tax_ids:
                    sheet.write(row, col + 6, tax.amount, center)
                sheet.write(row, col + 7, line.price_subtotal * (list(line.tax_ids)[0].amount / 100), center)
                sheet.write(row, col + 8, line.tax_ids.territory, center)
                # sheet.write(row, col + 8, "" , center)
#dict(self.env['account.tax'].fields_get(allfields=['territory'])['territory']['selection'])
        sheet.write(row + 1, 0, '', format)
        sheet.write(row + 1, 1, '', format)
        sheet.write(row + 1, 2, '', format)
        sheet.write(row + 1, 3, '', format)
        sheet.write(row + 1, 4, '', format)
        sheet.write(row + 1, 5, price_subtotal, format)
        sheet.write(row + 1, 6, '', format)
        sheet.write(row + 1, 7, total_tax, format)
        sheet.write(row + 1, 8, '', format)
