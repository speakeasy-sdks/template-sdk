# CreateOrderResponse


## Fields

| Field                                                                 | Type                                                                  | Required                                                              | Description                                                           |
| --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- |
| `contentType`                                                         | *string*                                                              | :heavy_check_mark:                                                    | HTTP response content type for this operation                         |
| `error`                                                               | [models.ErrorT](../models/errort.md)                                  | :heavy_minus_sign:                                                    | An unknown error occurred interacting with the API.                   |
| `order`                                                               | [models.Order](../models/order.md)                                    | :heavy_minus_sign:                                                    | The order was created successfully.                                   |
| `statusCode`                                                          | *number*                                                              | :heavy_check_mark:                                                    | HTTP response status code for this operation                          |
| `rawResponse`                                                         | [Response](https://developer.mozilla.org/en-US/docs/Web/API/Response) | :heavy_check_mark:                                                    | Raw HTTP response; suitable for custom response parsing               |