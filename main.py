#importing fastapi from lib file
from fastapi import Body, FastAPI

app = FastAPI()

#path operation 
#made up of the dectorator which is the http path and... 
@app.get("/")
#...a function 
#fast api converts the message below to json which is how you send data to an api
def root():
    return {"message": "Hello bb"}

@app.get("/posts")
def get_posts():
    return {"data": "This is your posts"}

@app.post("/createposts")
def create_posts(payLoad: dict = Body(...)):
    print(payLoad)
    return {"new_post": f"title{payLoad['title']} content: {payLoad['content']}"}
