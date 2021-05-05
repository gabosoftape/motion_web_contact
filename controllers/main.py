import json
import logging
import time
from werkzeug.utils import redirect
from odoo.tools.translate import _
from odoo import http, tools
from odoo.http import content_disposition, dispatch_rpc, request, Response
from odoo.exceptions import AccessError, UserError, AccessDenied, MissingError

from odoo.addons.web.controllers.main import ensure_db, Home


#----------------------------------------------------------
# Odoo Web web Controllers
#----------------------------------------------------------
class ContactHome(Home):
    _logger = logging.getLogger(__name__)

    def error_response(self, error, msg, code):
        return {
            "jsonrpc": "2.0",
            "id": None,
            "error": {
                "code": code,
                "message": msg,
                "data": {
                    "name": str(error),
                    "debug": "",
                    "message": msg,
                }
            }
        }

    # ------------------------------------------------------------
    # AGREGAR Mensaje de contacto
    # ------------------------------------------------------------
    @http.route(['/contacto/new'], auth="none", type='http', method="POST")
    def contact_add(self, nombre, telefono, asunto, solicitud, email, empresa):
        # recibimos las variables de post
        # en caso de que se cuenten con los minimos datos
        if request.httprequest.method == 'POST':
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
                    response = request.env['motion.crm_contact'].sudo().create(values)
                except (AccessError, MissingError):
                    er = {'error': _('Invalid Creation.')}
                    return request.make_response(json.dumps(er))
                # redirigimos a okas morrocas xD
                # time.sleep(1)  # espera en segundos
                # return request.redirect("/contacto")
                res = {
                    "count": 1,
                    "result_id": response.id
                }
                return http.Response(
                    json.dumps(res),
                    status=200,
                    mimetype='application/json'
                )
            else:
                # redirigimos a error o a ok dependiendo las validaciones
                # detectamos los factores de error comunes.
                # time.sleep(1)
                er = {'error': _('Invalid Creation... Required fields missing')}
                return request.make_response(json.dumps(er))
        else:
            msg = "El metodo que usaste no esta permitido"
            res = self.error_response(request.httprequest.method, msg, 403)
            return http.Response(
                json.dumps(res),
                status=403,
                mimetype='application/json'
            )
