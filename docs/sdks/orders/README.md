# orders

## Overview

The orders endpoints.

### Available Operations

* [create_order](#create_order) - Create an order.

## create_order

Create an order for a drink.

### Example Usage

```python
import petstore
from petstore.models import callbacks, operations, shared

s = petstore.Petstore(
    security=shared.Security(
        api_key="",
    ),
)

req = operations.CreateOrderRequest(
    request_body=[
        shared.OrderInput(
            product_code='APM-1F2D3',
            quantity=836079,
            type=shared.OrderType.DRINK,
        ),
        shared.OrderInput(
            product_code='NAC-3F2D1',
            quantity=87129,
            type=shared.OrderType.INGREDIENT,
        ),
    ],
    callback_url='perferendis',
)

res = s.orders.create_order(req)

if res.order is not None:
    # handle response
```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `request`                                                                      | [operations.CreateOrderRequest](../../models/operations/createorderrequest.md) | :heavy_check_mark:                                                             | The request object to use for the request.                                     |


### Response

**[operations.CreateOrderResponse](../../models/operations/createorderresponse.md)**

