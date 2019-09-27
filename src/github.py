import requests

class GithubException(Exception):
    pass

class Github:
    """
    Python 'requests' wrapper to hold URI and Token data
    requests wrapper methods append URI part to base URI:
        base + part
    Additionally inserts token into request parameters
    """

    _PARAMS = 'params'
    _TOKEN_PARAM_NAME = 'access_token'
    _HTTP_METHODS = {
        'get': requests.get,
        'put': requests.put,
        'post': requests.post,
        'patch': requests.patch,
        'delete': requests.delete,
        'options': requests.options
    }

    def __init__(self, token='', base='https://api.github.com'):
        self._token = token
        self._base = base

    def _format_target(self, part):
        """
        Combine base + part to get an API URI
        """
        return '{}{}'.format(self._base, part)

    def _add_token(self, kwargs):
        """
        Enhance the 'params' field of a request with a token
        """
        params = None
        try:
            params = kwargs[self._PARAMS]
        except KeyError:
            params = dict()
        params[self._TOKEN_PARAM_NAME] = self._token
        kwargs[self._PARAMS] = params

        return kwargs

    def _wrapper(self, method, part, *args, **kwargs):
        kwargs = self._add_token(kwargs)
        rv = None
        try:
            rv = self._HTTP_METHODS[method](
                url=self._format_target(part),
                *args,
                **kwargs
            )
        except KeyError as ke:
            raise ke
        except Exception as e:
            raise GithubException('Error making request: {}'.format(e))
        return rv

    def get(self, part, *args, **kwargs):
        return self._wrapper('get', part, *args, **kwargs)

    def put(self, part, *args, **kwargs):
        return self._wrapper('put', part, *args, **kwargs)

    def post(self, part, *args, **kwargs):
        return self._wrapper('post', part, *args, **kwargs)

    def patch(self, part, *args, **kwargs):
        return self._wrapper('patch', part, *args, **kwargs)

    def delete(self, part, *args, **kwargs):
        return self._wrapper('delete', part, *args, **kwargs)

    def options(self, part, *args, **kwargs):
        return self._wrapper('options', part, *args, **kwargs)
