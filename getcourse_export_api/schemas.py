from pydantic import BaseModel


class Deals(BaseModel):
    """
    Заказы из системы.
    Список полей: https://getcourse.ru/blog/457215
    """
    pass


class Payments(BaseModel):
    """
    Платежи.
    Список полей, как в заказах.
    """
    pass


class Users(BaseModel):
    """
    Пользователи.
    Список полей: https://getcourse.ru/blog/276069#ltBlock11772746
    """
    pass


class Groups(BaseModel):
    """
    Группы пользователей.
    Список полей: https://getcourse.ru/blog/276069#ltBlock11772746
    + ID группы и дата добавления в группу
    """
    pass
