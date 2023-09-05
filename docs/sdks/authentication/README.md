# authentication

## Overview

The authentication endpoints.

### Available Operations

* [authenticate](#authenticate) - Authenticate with the API by providing a username and password.

## authenticate

Authenticate with the API by providing a username and password.

### Example Usage

```python
import petstore
from petstore.models import operations, shared

s = petstore.Petstore(
    security=shared.Security(
        api_key="",
    ),
)

req = operations.AuthenticateRequestBody(
    password='corrupti',
    username='Roselyn_Kassulke',
)

res = s.authentication.authenticate(req)

if res.authenticate_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.AuthenticateRequestBody](../../models/operations/authenticaterequestbody.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |


### Response

**[operations.AuthenticateResponse](../../models/operations/authenticateresponse.md)**

