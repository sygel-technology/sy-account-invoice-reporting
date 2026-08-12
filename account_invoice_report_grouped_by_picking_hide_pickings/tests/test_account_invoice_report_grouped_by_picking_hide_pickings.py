# Copyright 2025 Alberto Martínez <alberto.martinez@sygel.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
# pylint: disable=E501
from odoo.addons.account_invoice_report_grouped_by_picking.tests import (
    test_account_invoice_group_picking,
)

TestAccountInvoiceGroupPicking = (
    test_account_invoice_group_picking.TestAccountInvoiceGroupPicking
)


class SomethingCase(TestAccountInvoiceGroupPicking):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()

    def test_hide_return(self):
        self.sale.order_line[1].unlink()
        self.sale.action_confirm()
        picking = self.sale.picking_ids[:1]
        picking.action_confirm()
        picking.action_assign()
        picking.move_ids.write({"quantity": 2})
        picking.button_validate()
        wiz_return = self.get_return_picking_wizard(picking)
        wiz_return.product_return_moves.write({"quantity": 2})
        res = wiz_return.action_create_returns()
        picking_return = self.env["stock.picking"].browse(res["res_id"])
        picking_return.action_confirm()
        picking_return.action_assign()
        picking_return.move_ids.write({"quantity": 2})
        picking_return.button_validate()
        final_picking = picking.copy()
        final_picking.action_confirm()
        final_picking.action_assign()
        final_picking.move_ids.write({"quantity": 2})
        final_picking.button_validate()
        invoice = self.sale._create_invoices()
        (picking + picking_return).write({"hide_on_invoice": True})
        report_lines = invoice.lines_grouped_by_picking()
        self.assertEqual(len(report_lines), 1)
        self.assertEqual(report_lines[0]["quantity"], 2)

    def test_hide_single_picking(self):
        self.sale.order_line[1].unlink()
        self.sale.action_confirm()
        picking = self.sale.picking_ids[:1]
        picking.action_confirm()
        picking.action_assign()
        picking.move_ids.write({"quantity": 2})
        picking.write({"hide_on_invoice": True})
        picking.button_validate()
        invoice = self.sale._create_invoices()
        invoice.invoice_line_ids.write({"quantity": 5})
        report_lines = invoice.lines_grouped_by_picking()
        self.assertEqual(len(report_lines), 1)
        self.assertEqual(report_lines[0]["quantity"], 5)

    def test_all_pickings_hidden_show_lines_without_picking(self):
        self.sale.order_line[1].unlink()
        self.sale.action_confirm()
        picking = self.sale.picking_ids[:1]
        picking.action_confirm()
        picking.action_assign()
        picking.move_ids.write({"quantity": 2})
        picking.button_validate()
        invoice = self.sale._create_invoices()
        picking.write({"hide_on_invoice": True})
        report_lines = invoice.lines_grouped_by_picking()
        self.assertEqual(len(report_lines), 1)
        self.assertFalse(report_lines[0]["picking"])
        self.assertEqual(report_lines[0]["quantity"], 2)

    def test_full_return_with_cancelled_move(self):
        self.sale.action_confirm()
        picking = self.sale.picking_ids[:1]
        picking.action_confirm()
        picking.action_assign()
        move_to_deliver = picking.move_ids[:1]
        move_to_cancel = picking.move_ids[1:]
        move_to_cancel._action_cancel()
        move_to_deliver.write({"quantity": move_to_deliver.product_uom_qty})
        picking.button_validate()
        wiz_return = self.get_return_picking_wizard(picking)
        wiz_return.product_return_moves.write({"quantity": move_to_deliver.quantity})
        self.assertTrue(wiz_return.is_full_return)
        wiz_return.hide_return_on_invoice = True
        res = wiz_return.action_create_returns()
        picking_return = self.env["stock.picking"].browse(res["res_id"])
        self.assertTrue(picking.hide_on_invoice)
        self.assertTrue(picking_return.hide_on_invoice)
