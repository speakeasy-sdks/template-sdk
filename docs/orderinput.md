# OrderInput

An order for a drink or ingredient.


## Fields

| Field                                                    | Type                                                     | Required                                                 | Description                                              | Example                                                  |
| -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- |
| `productCode`                                            | *string*                                                 | :heavy_check_mark:                                       | The product code of the drink or ingredient.             | AC-A2DF3                                                 |
| `quantity`                                               | *number*                                                 | :heavy_check_mark:                                       | The number of units of the drink or ingredient to order. |                                                          |
| `type`                                                   | [models.OrderType](../models/ordertype.md)               | :heavy_check_mark:                                       | The type of order.                                       |                                                          |