<!-- Start SDK Example Usage -->


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
    username='Larue_Rau85',
)

res = s.authentication.authenticate(req)

if res.authenticate_200_application_json_object is not None:
    # handle response
```
<!-- End SDK Example Usage -->