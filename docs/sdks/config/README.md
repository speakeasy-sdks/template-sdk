# config

### Available Operations

* [subscribe_to_webhooks](#subscribe_to_webhooks) - Subscribe to webhooks.

## subscribe_to_webhooks

Subscribe to webhooks.

### Example Usage

```python
import petstore
from petstore.models import operations, shared

s = petstore.Petstore(
    security=shared.Security(
        api_key="",
    ),
)

req = [
    operations.SubscribeToWebhooksRequestBody(
        url='iure',
        webhook=operations.SubscribeToWebhooksRequestBodyWebhook.STOCK_UPDATE,
    ),
    operations.SubscribeToWebhooksRequestBody(
        url='magnam',
        webhook=operations.SubscribeToWebhooksRequestBodyWebhook.STOCK_UPDATE,
    ),
]

res = s.config.subscribe_to_webhooks(req)

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                            | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `request`                                                            | [list[operations.SubscribeToWebhooksRequestBody]](../../models//.md) | :heavy_check_mark:                                                   | The request object to use for the request.                           |


### Response

**[operations.SubscribeToWebhooksResponse](../../models/operations/subscribetowebhooksresponse.md)**

