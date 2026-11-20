{
    "name": "Shop Floor Full Product Names",
    "version": "18.0.1.0.0",
    "category": "Manufacturing/Manufacturing",
    "summary": "Show full product names in the Shop Floor interface",
    "author": "Arga Dwiki Suwandi",
    "maintainer": "Arga Dwiki Suwandi",
    "support": "argadwiki632@gmail.com",
    "license": "OPL-1",
    "price": 5.0,
    "currency": "USD",
    "images": ["static/description/banner.png"],
    "depends": ["mrp_workorder"],
    "assets": {
        "web.assets_backend": [
            "arga_shopfloor_product_full_name/static/src/xml/shopfloor_product_full_name.xml",
            "arga_shopfloor_product_full_name/static/src/scss/shopfloor_product_full_name.scss",
        ],
    },
    "installable": True,
}
