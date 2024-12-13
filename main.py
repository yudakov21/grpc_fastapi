import typing 
from fastapi import FastAPI, Depends, HTTPException
from fastapi.responses import JSONResponse
from clients import grpc_client
from protos import todo_pb2
from google.protobuf.json_format import MessageToDict
from grpc.aio._call import AioRpcError

app = FastAPI(
    title= 'gRPC-Project',

)

@app.post("/todo")
async def create_todo(
    name: str,
    completed: bool,
    day: int,
    client: typing.Any = Depends(grpc_client),
) -> JSONResponse:
    try:
        todo = await client.CreateTodo(
            todo_pb2.CreateTodoRequest(name=name, completed=completed, day=day),
            timeout=5,
        )
    except AioRpcError as e:
        raise HTTPException(status_code=400, detail=e.details())

    return JSONResponse(MessageToDict(todo))

@app.get("/todo")
async def list_todos(client: typing.Any = Depends(grpc_client)) -> JSONResponse:
    try:
        todos = await client.ListTodos(todo_pb2.ListTodosRequest())
    except AioRpcError as e:
        raise HTTPException(status_code=400, detail=e.details())

    return JSONResponse(MessageToDict(todos))


@app.get("/todo/{id}")
async def get_todo_by_id(id: int, client: typing.Any = Depends(grpc_client)) -> JSONResponse:
    try:
        todo = await client.ReadTodo(todo_pb2.ReadTodoRequest(id=id))
        
    except AioRpcError as e:
        raise HTTPException(status_code=400, detail=e.details())

    return JSONResponse(MessageToDict(todo))
# app.include_router()