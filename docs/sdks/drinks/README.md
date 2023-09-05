# drinks

## Overview

The drinks endpoints.

### Available Operations

* [get_drink](#get_drink) - Get a drink.
* [list_drinks](#list_drinks) - Get a list of drinks.

## get_drink

Get a drink by name, if authenticated this will include stock levels and product codes otherwise it will only include public information.

### Example Usage

```python
import petstore
from petstore.models import operations, shared

s = petstore.Petstore(
    security=shared.Security(
        api_key="",
    ),
)

req = operations.GetDrinkRequest(
    name='Larry Windler',
)

res = s.drinks.get_drink(req)

if res.drink is not None:
    # handle response
```

### Parameters

| Parameter                                                                | Type                                                                     | Required                                                                 | Description                                                              |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| `request`                                                                | [operations.GetDrinkRequest](../../models/operations/getdrinkrequest.md) | :heavy_check_mark:                                                       | The request object to use for the request.                               |


### Response

**[operations.GetDrinkResponse](../../models/operations/getdrinkresponse.md)**


## list_drinks

Get a list of drinks, if authenticated this will include stock levels and product codes otherwise it will only include public information.

### Example Usage

```python
import petstore
from petstore.models import operations, shared

s = petstore.Petstore(
    security=shared.Security(
        api_key="",
    ),
)

req = operations.ListDrinksRequest(
    type=shared.DrinkType.BEER,
)

res = s.drinks.list_drinks(req)

if res.drinks is not None:
    # handle response
```

### Parameters

| Parameter                                                                    | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `request`                                                                    | [operations.ListDrinksRequest](../../models/operations/listdrinksrequest.md) | :heavy_check_mark:                                                           | The request object to use for the request.                                   |


### Response

**[operations.ListDrinksResponse](../../models/operations/listdrinksresponse.md)**

