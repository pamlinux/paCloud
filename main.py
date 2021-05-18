"""

with body list example :

[
    {
        "url" : "https://www.rts.ch/info/12200906-le-canton-de-vaud-ouvre-la-vaccination-aux-jeunes-des-16-ans.html",
        "name" : "RTS"
    },
    {
        "url" : "https://www.rts.ch/info/12200906-le-canton-de-vaud-ouvre-la-vaccination-aux-jeunes-des-16-ans.html",
        "name" : "RTS2"
    }
]

"""
from typing import List

from fastapi import FastAPI
from pydantic import BaseModel, HttpUrl

app = FastAPI()


class Image(BaseModel):
    url: HttpUrl
    name: str


@app.post("/images/multiple/")
async def create_multiple_images(images: List[Image]):
    for image in images:
        print(image.url)
    return images
