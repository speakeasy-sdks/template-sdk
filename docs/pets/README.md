# pets

### Available Operations

* [create_pets](#create_pets) - Create a pet
* [list_pets](#list_pets) - List all pets
* [show_pet_by_id](#show_pet_by_id) - Info for a specific pet

## create_pets

Create a pet

### Example Usage

```python
import petstore


s = petstore.Petstore()


res = s.pets.create_pets()

if res.status_code == 200:
    # handle response
```

## list_pets

List all pets

### Example Usage

```python
import petstore
from petstore.models import operations

s = petstore.Petstore()

req = operations.ListPetsRequest(
    limit=548814,
)

res = s.pets.list_pets(req)

if res.pets is not None:
    # handle response
```

## show_pet_by_id

Info for a specific pet

### Example Usage

```python
import petstore
from petstore.models import operations

s = petstore.Petstore()

req = operations.ShowPetByIDRequest(
    pet_id='provident',
)

res = s.pets.show_pet_by_id(req)

if res.pet is not None:
    # handle response
```
