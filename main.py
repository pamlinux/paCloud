"""
Deeply nested models

with the following body example :

{
    "name": "Foo",
    "description": "Canal+",
    "price": 84.0,
    "items": [
        {
            "name": "Canal enfants",
            "description": "Pour les enfants",
            "price": 40.0,
            "tax": 3.2,
            "tags": [
                "bar",
                "rock"
            ]
        },
        {
            "name": "Canal rose",
            "description": "Pour les adultes",
            "price": 44.0,
            "tax": 3.2,
            "tags": [
                "bar",
                "classic"
            ],
            "images" : [
                {
                    "url": "http://example.com/baz.jpg",
                    "name": "The Foo live"
                },
                {
                    "url": "http://example.com/dave.jpg",
                    "name": "The Baz"
                }
            ]
        }
    ]
}


"""

from typing import List, Optional, Set

from fastapi import FastAPI
from pydantic import BaseModel, HttpUrl

app = FastAPI()


class Image(BaseModel):
    url: HttpUrl
    name: str


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None
    tags: Set[str] = set()
    images: Optional[List[Image]] = None


class Offer(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    items: List[Item]


@app.post("/offers/")
async def create_offer(offer: Offer):
    results = {"offer" : offer, "Total price" : offer.price + offer.items[0].tax + offer.items[1].tax}
    return results
