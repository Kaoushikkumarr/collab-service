"""request_controller module"""

import requests
from urllib3.util import Retry
from requests.adapters import HTTPAdapter


class RequestsController:
    """ class for request_controller."""

    def __init__(
            self,
            default_timeout,
            max_retries,
            pool_connections,
            pool_max_size,
            pool_block,
            backoff_factor=1,
            status_forcelist=None,
            method_whitelist=None,
    ):
        if status_forcelist is None:
            status_forcelist = [429, 500, 502, 503, 504]
        if method_whitelist is None:
            method_whitelist = ["POST", "HEAD", "GET", "PUT", "DELETE", "OPTIONS", "TRACE"]
        retry_strategy = Retry(
            total=int(max_retries),
            status_forcelist=status_forcelist,
            method_whitelist=method_whitelist,
            backoff_factor=int(backoff_factor)
        )
        self.req = requests.session()
        self.req.mount('http://', CustomHTTPAdapter(
            max_retries=retry_strategy,
            timeout=int(default_timeout),
            pool_connections=int(pool_connections),
            pool_maxsize=int(pool_max_size),
            pool_block=pool_block
        ))
        self.req.mount('https://', CustomHTTPAdapter(
            max_retries=retry_strategy,
            timeout=int(default_timeout),
            pool_connections=int(pool_connections),
            pool_maxsize=int(pool_max_size),
            pool_block=pool_block
        ))


class CustomHTTPAdapter(HTTPAdapter):
    """class for custom_http_adapter."""

    def __init__(self, *args, **kwargs):
        if "timeout" in kwargs:
            self.timeout = kwargs["timeout"]
            del kwargs["timeout"]
        super().__init__(*args, **kwargs)

    def send(self, request, **kwargs):
        """method to send request"""
        timeout = kwargs.get("timeout")
        if timeout is None:
            kwargs["timeout"] = self.timeout
        return super().send(request, **kwargs)

