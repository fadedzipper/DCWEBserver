from rest_framework.renderers import JSONRenderer

class CustomJsonRender(JSONRenderer):

    def render(self, data, accepted_media_type=None, renderer_context=None):

        if renderer_context:
            response = renderer_context['response']
            code = response.status_code
            msg = "ok"
            if isinstance(data, dict):
                msg = data.pop('detail', msg)
                code = data.pop('code', code)
                data = data.pop('data', data)
                if code != 200 and data and code != 201:
                    msg = data.pop('detail', 'failed')
                res = {
                    'code': code,
                    'message': msg,
                    'data': data
                }
                return super().render(res, accepted_media_type, renderer_context)
            else:
                return super().render(data, accepted_media_type, renderer_context)

