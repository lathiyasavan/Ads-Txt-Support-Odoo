from odoo import http
from odoo.http import Response

class AdsTxtController(http.Controller):
    @http.route('/ads.txt', type='http', auth='public', website=True)
    def ads_txt(self, **kwargs):
        content = "google.com, ca-pub-2840119816393977, DIRECT, f08c47fec0942fa0"
        return Response(content, content_type='text/plain')