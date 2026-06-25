# Type validation problem

def insert_patient_data(name: str, age: int):

  if type(name) == str and type(age) == int:
    print(name)
    print(age)
    print("inserted into database")
  else:
    raise TypeError("Incorrect data type")

insert_patient_data("Harshita", 24)

#  Data validation problem

def insert_patient_data(name: str, age: int):

  if type(name) == str and type(age) == int:
    if age < 0:
      raise ValueError("Age cant be negative")
    else:   
      print(name)
      print(age)
      print("inserted into database")
  else:
    raise TypeError("Incorrect data type")


