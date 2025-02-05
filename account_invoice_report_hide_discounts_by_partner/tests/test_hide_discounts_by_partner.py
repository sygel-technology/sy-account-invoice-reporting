# Copyright 2025 Ángel García de la Chica Herrera <angel.garcia@sygel.es>
# License AGPL-3 - See https://www.gnu.org/licenses/agpl-3.0

from odoo.tests import tagged

from odoo.addons.account.tests.common import AccountTestInvoicingCommon


@tagged("post_install", "-at_install")
class TestHideDiscountsByPartner(AccountTestInvoicingCommon):
    @classmethod
    def setUpClass(cls):
        super(TestHideDiscountsByPartner, cls).setUpClass()
        cls.partner1 = cls.env["res.partner"].create(
            {
                "name": "Test partner 1",
                "show_invoice_discounts": False,
            }
        )
        cls.partner2 = cls.env["res.partner"].create(
            {
                "name": "Test partner 2",
                "show_invoice_discounts": True,
            }
        )

    def test_child_partner_show_discounts(self):
        child = self.env["res.partner"].create(
            {"name": "Test partner", "parent_id": self.partner1.id}
        )
        self.assertEqual(
            child.show_invoice_discounts,
            self.partner1.show_invoice_discounts,
        )

    def test_invoice_creation(self):
        invoice = self._create_invoice(partner_id=self.partner1.id)
        self.assertEqual(invoice.show_discounts, self.partner1.show_invoice_discounts)

    def test_invoice_change_partner(self):
        invoice = self._create_invoice(partner_id=self.partner1.id)
        invoice.partner_id = self.partner2
        self.assertEqual(invoice.show_discounts, self.partner2.show_invoice_discounts)

    def test_user_group_show_line_subtotals_tax_excluded(self):
        """Before checks, we make sure:
        * The user belongs to the tax group account.group_show_line_subtotals_tax_excluded
        * The line has a discount -> discount = 10
        * The tax is non-zero -> self.tax_sale_a.amount = 15.0
        """
        if (
            self.env.user
            not in self.env.ref("account.group_show_line_subtotals_tax_excluded").users
        ):
            self.env.ref("account.group_show_line_subtotals_tax_included").write(
                {"users": [(3, self.env.user.id)]}
            )
            self.env.ref("account.group_show_line_subtotals_tax_excluded").write(
                {"users": [(4, self.env.user.id)]}
            )
        invoice = self._create_invoice(
            partner_id=self.partner1.id, taxes=self.tax_sale_a
        )
        invoice.invoice_line_ids[0].discount = 10
        self.assertEqual(
            invoice.invoice_line_ids[0].invoice_price_unit_with_discount,
            invoice.invoice_line_ids[0].price_subtotal
            / invoice.invoice_line_ids[0].quantity,
        )

    def test_user_group_show_line_subtotals_tax_included(self):
        """Before checks, we make sure:
        * The user belongs to the tax group account.group_show_line_subtotals_tax_included
        * The line has a discount -> discount = 10
        * The tax is non-zero -> self.tax_sale_a.amount = 15.0
        """
        if (
            self.env.user
            not in self.env.ref("account.group_show_line_subtotals_tax_included").users
        ):
            self.env.ref("account.group_show_line_subtotals_tax_excluded").write(
                {"users": [(3, self.env.user.id)]}
            )
            self.env.ref("account.group_show_line_subtotals_tax_included").write(
                {"users": [(4, self.env.user.id)]}
            )
        invoice = self._create_invoice(
            partner_id=self.partner1.id, taxes=self.tax_sale_a
        )
        invoice.invoice_line_ids[0].discount = 10
        self.assertEqual(
            invoice.invoice_line_ids[0].invoice_price_unit_with_discount,
            invoice.invoice_line_ids[0].price_total
            / invoice.invoice_line_ids[0].quantity,
        )
