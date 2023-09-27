"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import error as shared_error
from ..shared import ingredient as shared_ingredient
from typing import Optional



@dataclasses.dataclass
class ListIngredientsRequest:
    ingredients: Optional[list[str]] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'ingredients', 'style': 'form', 'explode': False }})
    r"""A list of ingredients to filter by. If not provided all ingredients will be returned."""
    




@dataclasses.dataclass
class ListIngredientsResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    error: Optional[shared_error.Error] = dataclasses.field(default=None)
    r"""An unknown error occurred interacting with the API."""
    ingredients: Optional[list[shared_ingredient.Ingredient]] = dataclasses.field(default=None)
    r"""A list of ingredients."""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    
