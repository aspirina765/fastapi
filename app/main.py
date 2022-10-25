from fastapi import FastAPI


import publish_topic
import receiver_topic
import SparkJob
import blob

sj = SparkJob()
pt = publish_topic() 
rt = receiver_topic() 
b = blob() 


app = FastAPI()


@app.get("/")
def hello_world():
    return {"message": "OK"}
