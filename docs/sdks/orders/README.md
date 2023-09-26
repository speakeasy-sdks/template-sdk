# Orders

## Overview

The orders endpoints.

### Available Operations

* [create_order](#create_order) - Create an order.

## create_order

Create an order for a drink.

### Example Usage

```python
import speakeasybar
from speakeasybar.models import callbacks, operations, shared

s = speakeasybar.Speakeasybar(
    security=shared.Security(
        api_key="",
    ),
)


res = s.orders.create_order(request_body=[
    shared.OrderInput(
        product_code='NAC-3F2D1',
        quantity=297534,
        type=shared.OrderType.INGREDIENT,
    ),
], callback_url='ipsa')

if res.order is not None:
    # handle response
```

### Parameters

| Parameter                                                    | Type                                                         | Required                                                     | Description                                                  |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| `request_body`                                               | list[[shared.OrderInput](../../models/shared/orderinput.md)] | :heavy_check_mark:                                           | N/A                                                          |
| `callback_url`                                               | *Optional[str]*                                              | :heavy_minus_sign:                                           | The url to call when the order is updated.                   |


### Response

**[operations.CreateOrderResponse](../../models/operations/createorderresponse.md)**

