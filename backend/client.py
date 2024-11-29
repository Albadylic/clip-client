from clip_client import Client
from docarray import Document
from fastapi import FastAPI

app = FastAPI()

c = Client('grpc://192.168.100.181:51000')

@app.post("/post")
def rank_animals(uri):
    # This looks through the options provided and ranks which are most likely

    d = Document(
        uri='uri',
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
