from clip_client import Client
from docarray import Document

c = Client('grpc://192.168.100.181:51000')

# This looks through the options provided and ranks which are most likely

d = Document(
    uri='CowChicken.png',
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
print(top_result)
