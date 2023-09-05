# ingredients

## Overview

The ingredients endpoints.

### Available Operations

* [list_ingredients](#list_ingredients) - Get a list of ingredients.

## list_ingredients

Get a list of ingredients, if authenticated this will include stock levels and product codes otherwise it will only include public information.

### Example Usage

```python
import petstore
from petstore.models import operations, shared

s = petstore.Petstore(
    security=shared.Security(
        api_key="",
    ),
)

req = operations.ListIngredientsRequest(
    ingredients=[
        'placeat',
        'voluptatum',
        'iusto',
        'excepturi',
    ],
)

res = s.ingredients.list_ingredients(req)

if res.ingredients is not None:
    # handle response
```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.ListIngredientsRequest](../../models/operations/listingredientsrequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |


### Response

**[operations.ListIngredientsResponse](../../models/operations/listingredientsresponse.md)**

