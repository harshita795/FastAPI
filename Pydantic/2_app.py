from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):
  name: Annotated[str, Field(max_length=50, title="Name of the patient", description="Give the name of the patient in less than 50 characters", examples=["Harshita"])]
  email: EmailStr
  linkedin_url: AnyUrl
  age: int = Field(gt = 0, lt = 120)
  weight: Annotated[float, Field(gt = 0, strict=True)]
  married: Annotated[bool, Field(default=None, description="Is the patient married or not")]
  allergies: Annotated[Optional[List[str]], Field(default=None, max_length=5)]
  contact_details: Dict[str, str]

def insert_patient_data(patient1):
  print(patient1.name)
  print(patient1.age)
  print("Inserted")

def update_patient_data(patient1):
  print(patient1.name)
  print(patient1.age)
  print("Updated")

patient_info = {"name": "Harshita", "email": "abc@gmail.com", "linkedin_url": "http://linkedin.com/453", "age": 24, "weight": 50.2, "married": False, "allergies": ["pollen", "dust"], "contact_details": {"phone": "57395738"} }

patient1 = Patient(**patient_info)

insert_patient_data(patient1)
update_patient_data(patient1)
