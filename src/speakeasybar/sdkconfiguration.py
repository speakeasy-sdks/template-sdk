"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""


import requests as requests_http
from ._hooks import SDKHooks
from .utils import utils
from .utils.retries import RetryConfig
from dataclasses import dataclass, field
from enum import Enum
from speakeasybar.models import shared
from typing import Callable, Dict, Optional, Tuple, Union


SERVER_PROD = 'prod'
r"""The production server."""
SERVER_STAGING = 'staging'
r"""The staging server."""
SERVER_CUSTOMER = 'customer'
r"""A per-organization and per-environment API."""
SERVERS = {
	SERVER_PROD: 'https://speakeasy.bar',
	SERVER_STAGING: 'https://staging.speakeasy.bar',
	SERVER_CUSTOMER: 'https://{organization}.{environment}.speakeasy.bar',
}
"""Contains the list of servers available to the SDK"""



class ServerEnvironment(str, Enum):
    r"""The environment name. Defaults to the production environment."""
    PROD = 'prod'
    STAGING = 'staging'
    DEV = 'dev'


@dataclass
class SDKConfiguration:
    client: requests_http.Session
    security: Union[shared.Security,Callable[[], shared.Security]] = None
    server_url: Optional[str] = ''
    server: Optional[str] = ''
    server_defaults: Dict[str, Dict[str, str]] = field(default_factory=Dict)
    language: str = 'python'
    openapi_doc_version: str = '1.0.0'
    sdk_version: str = '4.4.0'
    gen_version: str = '2.347.8'
    user_agent: str = 'speakeasy-sdk/python 4.4.0 2.347.8 1.0.0 speakeasybar'
    retry_config: Optional[RetryConfig] = None

    def __post_init__(self):
        self._hooks = SDKHooks()

    def get_server_details(self) -> Tuple[str, Dict[str, str]]:
        if self.server_url is not None and self.server_url != '':
            return utils.remove_suffix(self.server_url, '/'), {}
        if not self.server:
            self.server = SERVER_PROD

        if self.server not in SERVERS:
            raise ValueError(f"Invalid server \"{self.server}\"")

        return SERVERS[self.server], self.server_defaults.get(self.server, {})


    def get_hooks(self) -> SDKHooks:
        return self._hooks
