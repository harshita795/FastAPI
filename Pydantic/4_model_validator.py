from pydantic import BaseModel, EmailStr, model_validator
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):
  name: str
  email: EmailStr
  age: int
  weight: float
  married: bool
  allergies: List[str]
  contact_details: Dict[str, str]

  @model_validator(mode="after")
  def validate_emergency_contact(cls, model):
    if model.age > 60 and 'emergency' not in model.contact_details:
      raise ValueError("Patients older than 60 must have an emergency contact")
    return model


def insert_patient_data(patient1):
  print(patient1.name)
  print(patient1.age)
  print("Inserted")


patient_info = {"name": "Harshita", "email": "abc@hdfc.com", "linkedin_url": "http://linkedin.com/453", "age": 65, "weight": 50.2, "married": False, "allergies": ["pollen", "dust"], "contact_details": {"phone": "57395738", "emergency": "985628762"} }

patient1 = Patient(**patient_info) 

insert_patient_data(patient1)