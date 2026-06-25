from pydantic import BaseModel, EmailStr, computed_field
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):
  name: str
  email: EmailStr
  age: int
  weight: float
  height: float
  married: bool
  allergies: List[str]
  contact_details: Dict[str, str]

  @computed_field
  @property
  def bmi(self) -> float:
    bmi = round(self.weight/(self.height ** 2),2)
    return bmi


def insert_patient_data(patient1):
  print(patient1.name)
  print(patient1.age)
  print("BMI", patient1.bmi)
  print("Inserted")


patient_info = {"name": "Harshita", "email": "abc@hdfc.com", "linkedin_url": "http://linkedin.com/453", "age": 24, "weight": 50.2, "height": 1.54, "married": False, "allergies": ["pollen", "dust"], "contact_details": {"phone": "57395738", "emergency": "985628762"} }

patient1 = Patient(**patient_info) 

insert_patient_data(patient1)