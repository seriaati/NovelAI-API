from pydantic import BaseModel


class User(BaseModel):
    """
    NovelAI credentials for user account authentication.
    """

    username: str | None = None
    password: str | None = None
    token: str | None = None

    def __str__(self):
        return f"User(username={self.username})"

    __repr__ = __str__
