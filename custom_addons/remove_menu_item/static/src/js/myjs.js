

odoo.define('remove_menu_item.models', function (require) {
    "use strict";
    var models = require('point_of_sale.models');
    var core = require('web.core');
    var rpc = require('web.rpc');
    models.load_fields('res.company', ['street', 'street2', 'city', 'state_id', 'country_id', 'zip','email','phone','website']);

    return models;
});
