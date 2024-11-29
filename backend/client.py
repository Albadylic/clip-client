from clip_client import Client
from docarray import Document
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi import Request

from pydantic import BaseModel

class ImageRequest(BaseModel):
    imageURL: str


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000/", "http://127.0.0.1:3000/"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

c = Client('grpc://192.168.100.181:51000')

# Define a simple GET endpoint for testing
@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/post")
async def rank_animals(request: Request):
    try:
        data = await request.json()
        
    # This looks through the options provided and ranks which are most likely

        url = data['imageURL']
        print (url)

        d = Document(
            uri=url,
            matches=[
                Document(text=f'a photo of a {p}')
                for p in (
                    'chicken',
                    'cow',
                    'turtle',
                    'lion',
                    'duck',
                )
            ],
        )

        r = c.rank([d])

        top_result = r['@m', ['text', 'scores__clip_score__value']][0][0]

        return top_result
    except Exception as e:
        print("Error: ", e)
