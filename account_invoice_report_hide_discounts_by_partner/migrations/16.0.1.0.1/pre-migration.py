from openupgradelib import openupgrade


def _rename_fields(env):
    openupgrade.rename_fields(
        env,
        [
            (
                "res.partner",
                "res_partner",
                "show_discounts",
                "show_invoice_discounts",
            ),
        ],
    )


@openupgrade.migrate()
def migrate(env, version):
    _rename_fields(env)
