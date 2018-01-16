# -*- coding: utf-8 -*-
# Copyright (C) 2013-Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# @author Julien WESTE
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    'name': 'GRAP - Change Views',
    'version': '8.0.7.0.0',
    'category': 'GRAP - Custom',
    'description': """
Show / Hide / change views for users
====================================

Functionality:
--------------
    * Hide a lot of field from 'basic users';
    * Change size of some columns;
    * Add product's function field in pos_category;

TODO: update description

Copyright, Authors and Licence:
-------------------------------
    * Copyright: 2013, GRAP: Groupement Régional Alimentaire de Proximité;
    * Author:
        * Julien WESTE;
        * Sylvain LE GAL (https://twitter.com/legalsylvain);
    * Licence: AGPL-3 (http://www.gnu.org/licenses/);""",
    'author': 'GRAP',
    'website': 'http://www.grap.coop',
    'license': 'AGPL-3',
    'depends': [
        'account',
        'account_statement_reconciliation',
        'base_vat',
        'crm',
        'delivery',
        'mail',
        'email_template',
        'sale_food',
        'point_of_sale',
        'product',
        'product_margin',
        'product_margin_improve',
        # 'product_average_consumption',
        'product_standard_margin',
        'procurement',
        'purchase',
        'sale',
        'sale_margin',
        'sale_stock',
        'stock',
        'knowledge',
        'pos_multicompany',
        'product_taxes_group',
        'sale_eshop',
        'product_to_scale_bizerba',
        'product_fiscal_company',
        'product_category_recursive_property',
        'l10n_fr',
        'sale_order_dates',
        'sale_recovery_moment',
        'pos_order_pricelist_change',
        'grap_cooperative',
        'web_dashboard_tile',
        'stock_picking_mass_action',
        'product_ean_duplicates',
        'simple_tax_account',
        'simple_tax_sale',
        'simple_tax_purchase',
        'purchase_discount',
        'intercompany_trade_base',
        'recurring_consignment',
        # 'purchase_compute_order',
        'grap_change_access',
        # 'grap_reporting',
        'grap_print_product',
        'barcodes_generator_product',
    ],
    'data': [
        'security/res_groups.yml',
        'views/view_account_bank_statement.xml',
        'views/view_account_invoice.xml',
        'views/view_account_invoice_line.xml',
        'views/view_account_move.xml',
        'views/view_account_move_line.xml',
        'views/view_account_tax_template.xml',
        'views/view_account_voucher.xml',
        'views/view_ir_values.xml',
        'views/view_mail_compose_message.xml',
        'views/view_stock_inventory.xml',
        'views/view_stock_move.xml',
        'views/view_stock_picking.xml',
        'views/view_stock_picking_type.xml',
        'views/view_pos_category.xml',
        'views/view_pos_order.xml',
        'views/view_pos_order_line.xml',
        'views/view_pos_session.xml',
        'views/view_product_product.xml',
        'views/view_product_category.xml',
        'views/view_product_pricelist_item.xml',
        'views/view_product_supplierinfo.xml',
        'views/view_res_company.xml',
        'views/view_res_partner.xml',
        'views/view_res_users.xml',
        'views/view_sale_order.xml',
        'views/view_workflow_instance.xml',
        'views/view_workflow_workitem.xml',
        'views/action.xml',
        'views/menu.xml',
    ],
    'css': [
        'static/src/css/css.css',
    ],
}
