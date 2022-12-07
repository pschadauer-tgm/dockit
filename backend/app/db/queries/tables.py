from datetime import datetime
from typing import Optional

from pypika import Parameter as CommonParameter, Query, Table


class Parameter(CommonParameter):
    def __init__(self, count: int) -> None:
        super().__init__("${0}".format(count))


class TypedTable(Table):
    __table__ = ""

    def __init__(
        self,
        name: Optional[str] = None,
        schema: Optional[str] = None,
        alias: Optional[str] = None,
        query_cls: Optional[Query] = None,
    ) -> None:
        if name is None:
            if self.__table__:
                name = self.__table__
            else:
                name = self.__class__.__name__

        super().__init__(name, schema, alias, query_cls)


class Users(TypedTable):
    __table__ = "users"

    id: int
    username: str

class Containers(TypedTable):
    __table__ = "containers"

    id: int
    name: str
    container_id: str
    description: str
    created_at: datetime
    student: str


users = Users()
container = Containers()
