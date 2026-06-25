from pydantic import BaseModel

class Address(BaseModel):
  city: str
  state: str
  pin: str

class Patient(BaseModel):
  name: str
  gender: str
  age: int
  address: Address

address_dict = {"city" : "gurgaon", "state": "haryana", "pin": "122001"}

address1 = Address(**address_dict)

patient_dict = {"name": "Harshita", "gender": "female", "age": 24, "address": address1}

patient1 = Patient(**patient_dict)

print(patient1)
print(patient1.address.city)

# Better organization
# Reusablity
# Readability
# Validation
