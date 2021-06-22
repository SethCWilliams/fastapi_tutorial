from fastapi import FastAPI


app = FastAPI()


@app.get('/')
def index():
    return {'data': 'blog list'}


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
def comments(id: int):
    # fetch comments of blog with id = id
    my_list = []
    for i in range(1, id + 1):
        my_list.append({'comment_number': i})
    print(my_list)

    return {'data': my_list}