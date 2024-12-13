from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Todo(_message.Message):
    __slots__ = ("id", "name", "completed", "day")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    COMPLETED_FIELD_NUMBER: _ClassVar[int]
    DAY_FIELD_NUMBER: _ClassVar[int]
    id: int
    name: str
    completed: bool
    day: int
    def __init__(self, id: _Optional[int] = ..., name: _Optional[str] = ..., completed: bool = ..., day: _Optional[int] = ...) -> None: ...

class CreateTodoRequest(_message.Message):
    __slots__ = ("name", "completed", "day")
    NAME_FIELD_NUMBER: _ClassVar[int]
    COMPLETED_FIELD_NUMBER: _ClassVar[int]
    DAY_FIELD_NUMBER: _ClassVar[int]
    name: str
    completed: bool
    day: int
    def __init__(self, name: _Optional[str] = ..., completed: bool = ..., day: _Optional[int] = ...) -> None: ...

class CreateTodoResponse(_message.Message):
    __slots__ = ("todo",)
    TODO_FIELD_NUMBER: _ClassVar[int]
    todo: Todo
    def __init__(self, todo: _Optional[_Union[Todo, _Mapping]] = ...) -> None: ...

class ReadTodoRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class ReadTodoResponse(_message.Message):
    __slots__ = ("todo",)
    TODO_FIELD_NUMBER: _ClassVar[int]
    todo: Todo
    def __init__(self, todo: _Optional[_Union[Todo, _Mapping]] = ...) -> None: ...

class ListTodosRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListTodosResponse(_message.Message):
    __slots__ = ("todos",)
    TODOS_FIELD_NUMBER: _ClassVar[int]
    todos: _containers.RepeatedCompositeFieldContainer[Todo]
    def __init__(self, todos: _Optional[_Iterable[_Union[Todo, _Mapping]]] = ...) -> None: ...
