from services.todo_service import start
import asyncio
from config import TODO_GRPC_SERVER_ADDR

if __name__ == "__main__":
    asyncio.run(start(TODO_GRPC_SERVER_ADDR))