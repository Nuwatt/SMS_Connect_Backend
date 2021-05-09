from rest_framework.compat import SHORT_SEPARATORS, LONG_SEPARATORS, INDENT_SEPARATORS
from rest_framework.renderers import JSONRenderer
from rest_framework.utils import json


class CustomJSONRenderer(JSONRenderer):
    """
    Custom Renderer which serializes to JSON.
    """

    def render(self, data, accepted_media_type=None, renderer_context=None):
        """
        Render `data` into JSON, returning a bytestring.
        """
        if data is None:
            return b''

        renderer_context = renderer_context or {}
        indent = self.get_indent(accepted_media_type, renderer_context)

        if indent is None:
            separators = SHORT_SEPARATORS if self.compact else LONG_SEPARATORS
        else:
            separators = INDENT_SEPARATORS

        # custom_format
        status_code = renderer_context.get('response').status_code

        # 1. custom json format
        custom_formatted_data = {
            'success': False,
            'error_message': None,
            'data': data
        }

        # 2. if status_code is between 200 - 299
        if 200 <= status_code < 300:
            custom_formatted_data['success'] = True
        # 2. if status_code is between 400 - 499
        elif 400 <= status_code < 500:
            key = list(data.keys())[0]
            if key in ['message', 'detail', 'non_field_errors']:
                message = data.get(key)
            else:
                value = data.get(key)
                message = '{} - {}'.format(
                    key,
                    value if isinstance(value, str) else value[0]
                )
            custom_formatted_data['success'] = False
            custom_formatted_data['error_message'] = message

        ret = json.dumps(
            custom_formatted_data, cls=self.encoder_class,
            indent=indent, ensure_ascii=self.ensure_ascii,
            allow_nan=not self.strict, separators=separators
        )

        # We always fully escape \u2028 and \u2029 to ensure we output JSON
        # that is a strict javascript subset.
        # See: http://timelessrepo.com/json-isnt-a-javascript-subset
        ret = ret.replace('\u2028', '\\u2028').replace('\u2029', '\\u2029')
        return ret.encode()


