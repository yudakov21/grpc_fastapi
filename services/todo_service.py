import grpc
from grpc import aio 

from protos import todo_pb2
from protos import todo_pb2_grpc

from model.todo import Todo


class TodoService(todo_pb2_grpc.TodoServiceServicer):

    # create todo
    async def CreateTodo(self, request, context):
        todo = await Todo.insert(
            Todo(name=request.name, completed=request.completed, day=request.day, )
        )
        print("CreateTodo")
        return todo_pb2.CreateTodoResponse(todo=todo[0])
    
    async def ListTodos(self, request, context):
        todo = await Todo.select()
        print("ListTodos")
        return todo_pb2.ListTodosResponse(todos=todo)
    
    async def ReadTodo(self, request, context):
        todo = await Todo.select().where(Todo.id == request.id).first()
        print("ReadTodo")
        return todo_pb2.ReadTodoResponse(todo=todo)


async def start(addr):
    await Todo.create_table(if_not_exists=True)
    server = aio.server()
    todo_pb2_grpc.add_TodoServiceServicer_to_server(
        TodoService(), server
    )
    server.add_insecure_port(addr)
    print(f"It works on {addr}")
    await server.start()
    await server.wait_for_termination()
