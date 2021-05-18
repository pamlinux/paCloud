"""
Bodies of arbitrary dicts with dict :

{
    "1" : 1,
    "2" : 2,
    "3" : 3
}
"""

from typing import Dict

from fastapi import FastAPI

app = FastAPI()


@app.post("/index-weights/")
async def create_index_weights(weights: Dict[int, float]):
    for key in weights:
        print(type(key))
    return weights
