from pydantic import BaseModel, EmailStr, AnyUrl, Field, field_validator
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):
  name: str
  email: EmailStr
  age: int
  weight: float
  married: bool
  allergies: List[str]
  contact_details: Dict[str, str]

  @field_validator('email')
  @classmethod
  def email_validator(cls, value):
    valid_domains = ['hdfc.com', 'icici.com']
    domain_name = value.split('@')[-1]

    if domain_name not in valid_domains:
      raise ValueError("Not a valid domain")
    return value
  
  @field_validator("name")
  @classmethod
  def transform_name(cls, value):
    return value.upper()
  
  @field_validator('age', mode="after")
  @classmethod
  def validate_age(cls, value):
    if 0 < value < 100:
      return value
    else:
      raise ValueError("Age should be in between 0 and 100")





def insert_patient_data(patient1):
  print(patient1.name)
  print(patient1.age)
  print("Inserted")


patient_info = {"name": "Harshita", "email": "abc@hdfc.com", "linkedin_url": "http://linkedin.com/453", "age": 24, "weight": 50.2, "married": False, "allergies": ["pollen", "dust"], "contact_details": {"phone": "57395738"} }

patient1 = Patient(**patient_info) #validation -> type coersion

insert_patient_data(patient1)