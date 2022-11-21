from odoo import models, fields
from datetime import datetime


class ProductViewXlsx(models.AbstractModel):
    _name = 'report.sale_reports.report_product_view_xls'
    _inherit = 'report.report_xlsx.abstract'

    def generate_xlsx_report(self, workbook, data, saleorder):
        sheet = workbook.add_worksheet("Sales Tax Input")
        bold = workbook.add_format({'bold': True, 'align': 'center', 'bg_color': 'black', 'color': 'white'})
        center = workbook.add_format({'align': 'center'})
        format = workbook.add_format({'align': 'center', 'bg_color': 'black', 'color': 'white'})
        row = 0
        col = 0
        sheet.set_column('A:C', 20)
        sheet.set_column('D:D', 22)
        sheet.set_column('E:F', 20)
        sheet.set_column('G:H', 24)
        sheet.set_column('I:Z', 20)

        sheet.write(row, col, 'NTN of Vendor', bold)
        sheet.write(row, col + 1, 'Vendor Name', bold)
        sheet.write(row, col + 2, "Type(Goods/Services)", bold)
        sheet.write(row, col + 3, 'Invoice no.', bold)
        sheet.write(row, col + 4, 'Invoice Date', bold)
        sheet.write(row, col + 5, 'Nature of Goods/Services Procured', bold)
        sheet.write(row, col + 6, 'Invoice Value Excl. Sales Tax', bold)
        sheet.write(row, col + 7, 'Sales Tax Rate %', bold)
        sheet.write(row, col + 8, 'Sales Tax Amount', bold)
        sheet.write(row, col + 9, 'Sales Tax Withhled', bold)
        sheet.write(row, col + 10, 'Territory', bold)

        invoice_lines = []
        if data['date_from']:
            invoice_lines = self.env['account.move'].search(
                [('invoice_date', '>=', data['date_from']),
                 ('invoice_date', '<=', data['date_to'])])
        else:
            invoice_lines = self.env['account.move'].search(
                [('invoice_date', '>=', data['date_from']),
                 ('invoice_date', '<=', data['date_to'])])

        record = invoice_lines.filtered(lambda rec: 'BILL' in rec.name)
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
                sheet.write(row, col, rec.partner_id.vat, center)
                sheet.write(row, col + 1, rec.partner_id.name, center)
                sheet.write(row, col + 2, line.tax_ids.tax_scope, center)
                sheet.write(row, col + 3, rec.name, center)
                sheet.write(row, col + 4, str(rec.invoice_date), center)
                sheet.write(row, col + 5, line.product_id.categ_id.name, center)
                sheet.write(row, col + 6, line.price_subtotal, center)
                for tax in line.tax_ids:
                    sheet.write(row, col + 7, tax.amount, center)
                sheet.write(row, col + 8, line.price_subtotal * (list(line.tax_ids)[0].amount / 100), center)
                sheet.write(row, col + 9, "Witheld", center)
                for province in line.tax_ids.territory:
                    if province[0] == line.tax_ids.territory:
                        print('#############################', province[1])
                        sheet.write(row, col + 10, province[1], center)
                # sheet.write(row, col + 10, line.tax_ids.territory, center)

        sheet.write(row + 1, 0, '', format)
        sheet.write(row + 1, 1, '', format)
        sheet.write(row + 1, 2, '', format)
        sheet.write(row + 1, 3, '', format)
        sheet.write(row + 1, 4, '', format)
        sheet.write(row + 1, 5, '', format)
        sheet.write(row + 1, 6, price_subtotal, format)
        sheet.write(row + 1, 7, '', format)
        sheet.write(row + 1, 8, total_tax, format)
        sheet.write(row + 1, 9, '', format)
        sheet.write(row + 1, 10, '', format)
