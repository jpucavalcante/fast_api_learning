from fastapi import FastAPI
from models import Todo

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

todos = []

# get todos
@app.get("/todos")
async def get_todos():
    return {"todos": todos}
 
# create todo
@app.post("/todos")
async def create_todo(todo: Todo):
    todos.append(todo)
    return {"message": "todo added"}

# get a todo
@app.get("/todos/{todo_id}")
async def get_todo(todo_id: int):
    for todo in todos:
        if todo.id == todo_id:
            return {"todo": todo}
    return {"message": "todo does not exist"}

# update a todo
@app.put("/todos/{todo_id}")
async def update_todo(todo_id: int, item_dic: dict):
    for todo in todos:
        if todo.id == todo_id:
            todo.item = item_dic["item"]
            return {"message": "todo updated"}
    return {"message": "todo does not exist"}

# delete todo
@app.delete("/todos/{todo_id}")
async def delete_todo(todo_id: int):
    for todo in todos:
        if todo.id == todo_id:
            todos.remove(todo)
            return {"message": "todo removed"}
    return {"message": "todo does not exist"}

# delete all todo
@app.delete("/todos")
async def delete_all_todos():
    global todos 
    todos = []
    return {"message": "all todos removed"}

