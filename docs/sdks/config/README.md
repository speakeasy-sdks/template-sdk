# Config
(*config*)

### Available Operations

* [subscribe_to_webhooks](#subscribe_to_webhooks) - Subscribe to webhooks.

## subscribe_to_webhooks

Subscribe to webhooks.

### Example Usage

```python
import speakeasybar
from speakeasybar.models import operations, shared

s = speakeasybar.Speakeasybar(
    security=shared.Security(
        api_key="<YOUR_API_KEY>",
    ),
)

req = [
    operations.RequestBody(),
]

res = s.config.subscribe_to_webhooks(req)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [List[operations.RequestBody]](../../models/.md)                    | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |


### Response

**[operations.SubscribeToWebhooksResponse](../../models/operations/subscribetowebhooksresponse.md)**
### Errors

| Error Object      | Status Code       | Content Type      |
| ----------------- | ----------------- | ----------------- |
| errors.BadRequest | 400               | application/json  |
| errors.APIError   | 5XX               | application/json  |
| errors.SDKError   | 400-600           | */*               |
