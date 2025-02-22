from pydantic import BaseModel


class UserScheme(BaseModel):
    id: int | None = None
    name: str
    description: str

