odoo.define('custom_pos_receipt.models', function (require) {
    "use strict";
    var models = require("point_of_sale.models");
    var rpc = require('web.rpc');
      models.load_fields('res.company', ['street', 'street2', 'city', 'state_id', 'country_id', 'zip','email','phone','website']);
    });