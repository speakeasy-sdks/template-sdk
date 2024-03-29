"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .ingredienttype import IngredientType
from dataclasses_json import Undefined, dataclass_json
from speakeasybar import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class IngredientInput:
    name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name') }})
    r"""The name of the ingredient."""
    type: IngredientType = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type') }})
    r"""The type of ingredient."""
    product_code: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('productCode'), 'exclude': lambda f: f is None }})
    r"""The product code of the ingredient, only available when authenticated."""
    

