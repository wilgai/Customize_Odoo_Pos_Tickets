odoo.define('smile_decimal_precision.field_utils', function (require) {
    "use strict";

var core = require('web.core');
var field_utils = require('web.field_utils');
var utils = require('web.utils');
var session = require('web.session');

function formatFloat(value, field, options) {
    if (value === false) {
        return "";
    }
    var l10n = core._t.database.parameters;
    var precision;
    if (options && options.digits) {
        precision = options.digits[1];
    } else if (field && field.digits) {
        precision = field.digits[1];
    } else {
        precision = 2;
    }
    var formatted = _.str.sprintf('%.' + precision + 'f', value || 0).split('.');
    formatted[0] = utils.insert_thousand_seps(formatted[0]);
    return formatted.join(l10n.decimal_point).replace(/0+$/g, "0").replace(/[.]$/,".0");
}

function formatMonetary(value, field, options) {
    if (value === false) {
        return "";
    }
    options = options || {};

    var currency = options.currency;
    if (!currency) {
        var currency_id = options.currency_id;
        if (!currency_id && options.data) {
            var currency_field = options.currency_field || field.currency_field || 'currency_id';
            currency_id = options.data[currency_field] && options.data[currency_field].res_id;
        }
        currency = session.get_currency(currency_id);
    }

    var digits = (currency && currency.digits) || options.digits;
    if (options.field_digits === true) {
        digits = field.digits || digits;
    }

    var formatted_value = formatFloat(value, field, {
        digits: digits,
    });

    if (!currency || options.noSymbol) {
        return formatted_value;
    }
    if (currency.position === "after") {
        return formatted_value += '&nbsp;' + currency.symbol;
    } else {
        return currency.symbol + '&nbsp;' + formatted_value;
    }
}

field_utils.format.float = formatFloat;
field_utils.format.monetary = formatMonetary;

});
