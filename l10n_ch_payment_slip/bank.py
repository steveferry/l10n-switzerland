# -*- coding: utf-8 -*-
##############################################################################
#
#    Author: Nicolas Bessi. Copyright Camptocamp SA
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
from openerp.osv import orm, fields


class ResPartnerBank(orm.Model):
    """
    Inherit res.partner.bank class in order to add swiss specific fields
    such as:
     - BVR data
     - BVR print options for company accounts
     We leave it here in order
    """

    _inherit = "res.partner.bank"
    _columns = {
        'print_bank': fields.boolean('Print Bank on BVR'),
        'print_account': fields.boolean('Print Account Number on BVR'),
        'print_partner': fields.boolean('Print Partner Address on BVR'),
    }
