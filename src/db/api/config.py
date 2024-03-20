from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):

    @classmethod
    def get_columns(cls) -> list:
        '''
        Получить все колонки, связанные только с тем инстансом класса, из которого вызван метод
        :return:
        '''

        # Не нравится история с аннотейшнами, но чот хз - ок ли так исключать все атрибуты (через мро и удаление
        # атрибутов всех родителей, результат одинаковый
        bases = list(cls.__mro__)
        bases.remove(cls)
        not_needed_cols = (key for basecls in bases for key in basecls.__dict__.keys())
        cols = [col for col in cls.__mapper__.columns.keys() if col not in not_needed_cols]

        return list(cls.__dict__.get('__annotations__', {}).keys())
