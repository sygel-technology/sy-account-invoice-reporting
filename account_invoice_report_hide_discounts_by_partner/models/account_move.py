# Copyright 2025 Ángel García de la Chica Herrera <angel.garcia@sygel.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import api, fields, models


class AccountMove(models.Model):
    _inherit = "account.move"

    show_discounts = fields.Boolean(
        compute="_compute_show_discounts",
        store=True,
        readonly=False,
        string="Show Discounts in Invoice",
    )

    @api.depends("partner_id")
    def _compute_show_discounts(self):
        for sel in self:
            res = False
            if sel.partner_id:
                res = sel.partner_id.show_invoice_discounts
            sel.show_discounts = res


class AccountMoveLine(models.Model):
    _inherit = "account.move.line"

    invoice_price_unit_with_discount = fields.Float(
        compute="_compute_unit_price_with_discounts",
        digits="Invoice Price Unit With Discount",
        string="Price Unit With Discount",
    )

    def _compute_unit_price_with_discounts(self):
        for sel in self:
            res = 0.0
            if sel.env.user.has_group("account.group_show_line_subtotals_tax_included"):
                res = sel.price_total / sel.quantity
            elif sel.env.user.has_group(
                "account.group_show_line_subtotals_tax_excluded"
            ):
                res = sel.price_subtotal / sel.quantity
            sel.invoice_price_unit_with_discount = res
