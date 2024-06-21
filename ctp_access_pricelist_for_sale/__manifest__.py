# -*- coding: utf-8 -*-
###################################################################################
#
#    Cybernetics Plus Co., Ltd.
#    Print Envelope in Contact
#
#    Copyright (C) 2021-TODAY Cybernetics Plus Technologies (<https://www.cybernetics.plus>).
#    Author: Cybernetics Plus Techno Solutions (<https://www.cybernetics.plus>)
#
###################################################################################

{
    "name": "Access Pricelist For Sale",
    "version": "17.0.1.0.1",
    "description": "Access Pricelist For Sale",
    "author": "Cybernetics+",
    "website": "https://www.cybernetics.plus",
    "live_test_url": "https://www.cybernetics.plus",
    "category": "Sales",
    "license": "AGPL-3",
    "application": True,
    "auto_install": False,
    "installable": True,
    "depends": [
       "base", "sale", "product",
    ],
    "data": [
        'views/product_pricelist.xml',
        'views/sale_order.xml',
        'views/res_partner_view.xml',
    ],
}