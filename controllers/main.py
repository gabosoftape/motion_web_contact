# -*- encoding: utf-8 -*-
##############################################################################
#
#    Samples module for Odoo Web Login Screen
#    Copyright (C) 2017- XUBI.ME (http://www.xubi.me)
#    @author binhnguyenxuan (https://www.linkedin.com/in/binhnguyenxuan)
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
#
##############################################################################


import babel.messages.pofile
import base64
import copy
import datetime
import functools
import glob
import hashlib
import io
import itertools
import jinja2
import json
import logging
import operator
import os
import re
import sys
import tempfile
import time

import werkzeug
import werkzeug.exceptions
import werkzeug.utils
import werkzeug.wrappers
import werkzeug.wsgi
from collections import OrderedDict, defaultdict, Counter
from werkzeug.urls import url_decode, iri_to_uri
from lxml import etree
import unicodedata


import odoo
import odoo.modules.registry
from odoo.api import call_kw, Environment
from odoo.modules import get_module_path, get_resource_path
from odoo.tools import image_process, topological_sort, html_escape, pycompat, ustr, apply_inheritance_specs, lazy_property
from odoo.tools.mimetypes import guess_mimetype
from odoo.tools.translate import _
from odoo.tools.misc import str2bool, xlsxwriter, file_open
from odoo.tools.safe_eval import safe_eval
from odoo import http, tools
from odoo.http import content_disposition, dispatch_rpc, request, serialize_exception as _serialize_exception, Response
from odoo.exceptions import AccessError, UserError, AccessDenied, MissingError
from odoo.models import check_method_name
from odoo.service import db, security

from odoo.addons.web.controllers.main import ensure_db, Home

_logger = logging.getLogger(__name__)


#----------------------------------------------------------
# Odoo Web web Controllers
#----------------------------------------------------------
class ContactHome(Home):

    @http.route('/contacto', type='http', auth="none", website=True)
    def web_contact(self, redirect=None, **kw):
        response = request.render("motion_web_contact.portal_contact_form")
        response.headers['X-Frame-Options'] = 'DENY'
        return response

    # ------------------------------------------------------------
    # AGREGAR Mensaje de contacto
    # ------------------------------------------------------------
    @http.route(['/contacto/new'], auth="none", type='http', website=True)
    def contact_add(self, **post):
        # recibimos las variables de post
        nombre = post.get('nombre')
        telefono = post.get('telefono')
        asunto = post.get('asunto')
        solicitud = post.get('solicitud')
        email = post.get('email')
        empresa = post.get('empresa')
        medio = post.get('medio')
        # en caso de que se cuenten con los minimos datos
        if nombre and telefono and asunto and solicitud and email:
            print('parece que todo ok')
            values = {
                'nombre': nombre,
                'telefono': telefono,
                'asunto': asunto,
                'solicitud': solicitud,
                'email': email,
                'empresa': empresa,
                'medio': 'sw',
                'state': 'nuevo'
            }
            # creamos nuevo mensaje de contacto
            try:
                request.env['motion.crm_contact'].sudo().create(values)
            except (AccessError, MissingError):
                er = {'error': _('Invalid Creation.')}
                return request.make_response(json.dumps(er))
            # redirigimos a okas morrocas xD
            res = {'msg': 'okas morrocas'}
            return request.make_response(json.dumps(res))
        else:
            # redirigimos a error o a ok dependiendo las validaciones
            # detectamos los factores de error comunes.
            er = {'error': 'No se pudo crear contacto.'}
            return request.make_response(json.dumps(er))

