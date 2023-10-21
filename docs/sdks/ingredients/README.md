# Ingredients
(*ingredients*)

## Overview

The ingredients endpoints.

### Available Operations

* [list_ingredients](#list_ingredients) - Get a list of ingredients.

## list_ingredients

Get a list of ingredients, if authenticated this will include stock levels and product codes otherwise it will only include public information.

### Example Usage

```python
import speakeasybar
from speakeasybar.models import operations, shared

s = speakeasybar.Speakeasybar(
    security=shared.Security(
        api_key="",
    ),
)


res = s.ingredients.list_ingredients(ingredients=[
    'string',
])

if res.ingredients is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                             | Type                                                                                  | Required                                                                              | Description                                                                           |
| ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| `ingredients`                                                                         | List[*str*]                                                                           | :heavy_minus_sign:                                                                    | A list of ingredients to filter by. If not provided all ingredients will be returned. |


### Response

**[operations.ListIngredientsResponse](../../models/operations/listingredientsresponse.md)**

