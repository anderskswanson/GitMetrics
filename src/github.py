import requests

class Github:
    
    def __init__(self, token='', base='https://api.github.com'):
        self._token = token
        self._base = base

    def _format_target(self, part, params):
        return '{}{}?access_token={}{}'.format(self._base, part, self._token, params)

    def get(self, part, params='', *args, **kwargs):
        return requests.get(
            url=self._format_target(part, params),
            *args,
            **kwargs
        )

    def post(self, part, params='', *args, **kwargs):
        return requests.post(
            url=self._format_target(part, params),
            *args,
            **kwargs
        )
    