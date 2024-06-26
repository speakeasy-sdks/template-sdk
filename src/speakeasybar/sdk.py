"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

import requests as requests_http
from .authentication import Authentication
from .config import Config
from .drinks import Drinks
from .ingredients import Ingredients
from .orders import Orders
from .sdkconfiguration import SDKConfiguration, ServerEnvironment
from .utils.retries import RetryConfig
from speakeasybar import utils
from speakeasybar._hooks import SDKHooks
from speakeasybar.models import shared
from typing import Callable, Dict, Optional, Union

class Speakeasybar:
    r"""The Speakeasy Bar: A bar that serves drinks.
    A secret underground bar that serves drinks to those in the know.
    https://docs.speakeasy.bar - The Speakeasy Bar Documentation.
    """
    authentication: Authentication
    r"""The authentication endpoints."""
    drinks: Drinks
    r"""The drinks endpoints."""
    ingredients: Ingredients
    r"""The ingredients endpoints."""
    orders: Orders
    r"""The orders endpoints."""
    config: Config

    sdk_configuration: SDKConfiguration

    def __init__(self,
                 security: Union[shared.Security,Callable[[], shared.Security]] = None,
                 environment: ServerEnvironment = None,
                 organization: str = None,
                 server: Optional[str] = None,
                 server_url: Optional[str] = None,
                 url_params: Optional[Dict[str, str]] = None,
                 client: Optional[requests_http.Session] = None,
                 retry_config: Optional[RetryConfig] = None
                 ) -> None:
        """Instantiates the SDK configuring it with the provided parameters.

        :param security: The security details required for authentication
        :type security: Union[shared.Security,Callable[[], shared.Security]]
        :param environment: Allows setting the environment variable for url substitution
        :type environment: ServerEnvironment
        :param organization: Allows setting the organization variable for url substitution
        :type organization: str
        :param server: The server by name to use for all operations
        :type server: str
        :param server_url: The server URL to use for all operations
        :type server_url: str
        :param url_params: Parameters to optionally template the server URL with
        :type url_params: Dict[str, str]
        :param client: The requests.Session HTTP client to use for all operations
        :type client: requests_http.Session
        :param retry_config: The utils.RetryConfig to use globally
        :type retry_config: RetryConfig
        """
        if client is None:
            client = requests_http.Session()

        if server_url is not None:
            if url_params is not None:
                server_url = utils.template_url(server_url, url_params)

        server_defaults = {
            'prod': {
            },
            'staging': {
            },
            'customer': {
                'environment': environment or 'prod',
                'organization': organization or 'api',
            },
        }

        self.sdk_configuration = SDKConfiguration(
            client,
            security,
            server_url,
            server,
            server_defaults,
            retry_config=retry_config
        )

        hooks = SDKHooks()

        current_server_url, *_ = self.sdk_configuration.get_server_details()
        server_url, self.sdk_configuration.client = hooks.sdk_init(current_server_url, self.sdk_configuration.client)
        if current_server_url != server_url:
            self.sdk_configuration.server_url = server_url

        # pylint: disable=protected-access
        self.sdk_configuration._hooks = hooks

        self._init_sdks()


    def _init_sdks(self):
        self.authentication = Authentication(self.sdk_configuration)
        self.drinks = Drinks(self.sdk_configuration)
        self.ingredients = Ingredients(self.sdk_configuration)
        self.orders = Orders(self.sdk_configuration)
        self.config = Config(self.sdk_configuration)
