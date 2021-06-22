from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


@app.get('/blog')
def index(limit=10, published: bool = True, sort: Optional[str] = None):
    # only get 10 published blogs
    if published:
        return {'data': f'{limit} published blogs from the db'}
    else:
        return {'data': f'{limit} blogs from the db'}


# This one _has_ to be above app.get('/blog/{id}) because it reads down the page, so 
# /blog/unpublished will match the id, but won't match it being an integer
# so it will throw an error
@app.get('/blog/unpublished')
def unpublished():
    # fetch a list of all unpublished blogs
    return {'data': 'all unpublished blogs'}


@app.get('/blog/{id}')
def show(id: int):
    # fetch blog with id = id
    return {'data': id}


@app.get('/blog/{id}/comments')
def comments(id, limit=10):
    # fetch comments of blog with id = id
    # my_list = []
    # for i in range(1, id + 1):
    #     my_list.append({'comment_number': i})

    return {'data': {'1', '2'}}


class Blog(BaseModel):
    title: str
    body: str
    published_at: Optional[bool]


@app.post('/blog')
def create_blog(request: Blog):
    return {'data': f'blog is created with title as {request.title}'}
