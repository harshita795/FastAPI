from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hello():
  return {"message":  "Hello World"}

@app.get("/about")
def about():
  return {"message" : "Hi, I am Harshita, an Integration Engineer, exploring AI engineering."}