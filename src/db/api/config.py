from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):

    @classmethod
    def get_columns(cls):
        return cls.__dict__.get('__annotations__', {}).keys()
