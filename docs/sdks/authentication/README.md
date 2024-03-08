# Authentication
(*authentication*)

## Overview

The authentication endpoints.

### Available Operations

* [login](#login) - Authenticate with the API by providing a username and password.

## login

Authenticate with the API by providing a username and password.

### Example Usage

```python
import speakeasybar
from speakeasybar.models import operations

s = speakeasybar.Speakeasybar()

req = operations.LoginRequestBody(
    type=operations.Type.API_KEY,
)

res = s.authentication.login(req, operations.LoginSecurity(
    password="<PASSWORD>",
    username="<USERNAME>",
))

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                  | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `request`                                                                  | [operations.LoginRequestBody](../../models/operations/loginrequestbody.md) | :heavy_check_mark:                                                         | The request object to use for the request.                                 |
| `security`                                                                 | [operations.LoginSecurity](../../models/operations/loginsecurity.md)       | :heavy_check_mark:                                                         | The security requirements to use for the request.                          |


### Response

**[operations.LoginResponse](../../models/operations/loginresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.APIError  | 5XX              | application/json |
| errors.SDKError  | 4x-5xx           | */*              |
