"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import error as shared_error
from ..shared import order as shared_order
from typing import Optional



@dataclasses.dataclass
class CreateOrderRequest:
    request_body: list[shared_order.OrderInput] = dataclasses.field(metadata={'request': { 'media_type': 'application/json' }})
    callback_url: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'callback_url', 'style': 'form', 'explode': True }})
    r"""The url to call when the order is updated."""
    




@dataclasses.dataclass
class CreateOrderResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    error: Optional[shared_error.Error] = dataclasses.field(default=None)
    r"""An unknown error occurred interacting with the API."""
    order: Optional[shared_order.Order] = dataclasses.field(default=None)
    r"""The order was created successfully."""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    
