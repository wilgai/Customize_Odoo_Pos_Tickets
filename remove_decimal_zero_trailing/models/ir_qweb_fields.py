# -*- coding: utf-8 -*-
# Copyright 2020 CorTex IT Solutions Ltd. (<https://cortexsolutions.net/>)
# License OPL-1

from odoo import api, models
from odoo.tools import  float_utils, pycompat
import re

class MonetaryConverter(models.AbstractModel):
    _inherit = 'ir.qweb.field.monetary'

    @api.model
    def value_to_html(self, value, options):
        display_currency = options['display_currency']

        # lang.format mandates a sprintf-style format. These formats are non-
        # minimal (they have a default fixed precision instead), and
        # lang.format will not set one by default. currency.round will not
        # provide one either. So we need to generate a precision value
        # (integer > 0) from the currency's rounding (a float generally < 1.0).
        fmt = "%.{0}f".format(display_currency.decimal_places)

        if options.get('from_currency'):
            value = options['from_currency'].compute(value, display_currency)

        lang = self.user_lang()
        formatted_amount = lang.format(fmt, display_currency.round(value),
                                       grouping=True, monetary=True).replace(r' ', u'\N{NO-BREAK SPACE}').replace(r'-',
                                                                                                                  u'-\N{ZERO WIDTH NO-BREAK SPACE}')

        pre = post = u''
        if display_currency.position == 'before':
            pre = u'{symbol}\N{NO-BREAK SPACE}'.format(symbol=display_currency.symbol or '')
        else:
            post = u'\N{NO-BREAK SPACE}{symbol}'.format(symbol=display_currency.symbol or '')

        return u'{pre}<span class="oe_currency_value">{0}</span>{post}'.format(formatted_amount.rstrip('0').rstrip('.'), pre=pre, post=post)


class FloatConverter(models.AbstractModel):
    _inherit = 'ir.qweb.field.float'

    @api.model
    def value_to_html(self, value, options):
        if 'decimal_precision' in options:
            precision = self.env['decimal.precision'].search([('name', '=', options['decimal_precision'])]).digits
        else:
            precision = options['precision']

        if precision is None:
            fmt = '%f'
        else:
            value = float_utils.float_round(value, precision_digits=precision)
            fmt = '%.{precision}f'.format(precision=precision)

        formatted = self.user_lang().format(fmt, value, grouping=True).replace(r'-', u'-\N{ZERO WIDTH NO-BREAK SPACE}')

        # %f does not strip trailing zeroes. %g does but its precision causes
        # it to switch to scientific notation starting at a million *and* to
        # strip decimals. So use %f and if no precision was specified manually
        # strip trailing 0.
        if precision is None:
            formatted = re.sub(r'(?:(0|\d+?)0+)$', r'\1', formatted)

        return pycompat.to_text(formatted.rstrip('0').rstrip('.'))