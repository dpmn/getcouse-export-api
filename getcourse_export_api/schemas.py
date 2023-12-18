from pydantic import BaseModel, Field
from datetime import datetime
from decimal import Decimal


class DealsSchema(BaseModel):
    """
    Заказы из системы.
    Список полей: https://getcourse.ru/blog/457215
    """
    def __init__(self, **data):
        for key, val in data.items():
            if val == '':
                data[key] = None

        super().__init__(**data)

    order_id: str | None = Field(
        alias='ID заказа'
    )
    order_number: str | None = Field(
        alias='Номер'
    )
    user_id: str | None = Field(
        alias='ID пользователя'
    )
    username: str | None = Field(
        alias='Пользователь'
    )
    user_email: str | None = Field(
        alias='Email'
    )
    user_phone: str | None = Field(
        alias='Телефон'
    )
    creation_date: datetime | None = Field(
        alias='Дата создания'
    )
    payment_date: datetime | None = Field(
        alias='Дата оплаты'
    )
    offer_title: str | None = Field(
        alias='Title'
    )
    order_status: str | None = Field(
        alias='Статус'
    )
    price: Decimal | None = Field(
        alias='Стоимость, RUB'
    )
    paid: Decimal | None = Field(
        alias='Оплачено'
    )
    payment_system_fee: Decimal | None = Field(
        alias='Комиссия платежной системы'
    )
    received_amount: Decimal | None = Field(
        alias='Получено'
    )
    tax: Decimal | None = Field(
        alias='Налог'
    )
    net_amount: Decimal | None = Field(
        alias='Осталось после вычета комиссии платежной системы и налога'
    )
    other_fees: Decimal | None = Field(
        alias='Другие комиссии'
    )
    earned: Decimal | None = Field(
        alias='Заработано'
    )
    currency: str | None = Field(
        alias='Валюта'
    )
    manager: str | None = Field(
        alias='Менеджер'
    )
    city: str | None = Field(
        alias='Город'
    )
    payment_system: str | None = Field(
        alias='Платежная система'
    )
    promo_code: str | None = Field(
        alias='Использован промокод'
    )
    promo_name: str | None = Field(
        alias='Промоакция'
    )
    order_partner_id: str | None = Field(
        alias='ID партнера заказа'
    )
    order_partner_email: str | None = Field(
        alias='Email партнера заказа'
    )
    order_partner_name: str | None = Field(
        alias='ФИО партнера заказа'
    )
    user_partner_id: str | None = Field(
        alias='ID партнера пользователя'
    )
    user_partner_email: str | None = Field(
        alias='Email партнера пользователя'
    )
    user_partner_name: str | None = Field(
        alias='ФИО партнера пользователя'
    )
    utm_source: str | None = Field(
        alias='utm_source'
    )
    utm_medium: str | None = Field(
        alias='utm_medium'
    )
    utm_campaign: str | None = Field(
        alias='utm_campaign'
    )
    utm_content: str | None = Field(
        alias='utm_content'
    )
    utm_term: str | None = Field(
        alias='utm_term'
    )
    utm_group: str | None = Field(
        alias='utm_group'
    )
    partner_source: str | None = Field(
        alias='Партнерский источник'
    )
    partner_code: str | None = Field(
        alias='Партнерский код'
    )
    session_partner: str | None = Field(
        alias='Партнер (сессия)'
    )
    user_utm_source: str | None = Field(
        alias='user_utm_source'
    )
    user_utm_medium: str | None = Field(
        alias='user_utm_medium'
    )
    user_utm_campaign: str | None = Field(
        alias='user_utm_campaign'
    )
    user_utm_content: str | None = Field(
        alias='user_utm_content'
    )
    user_utm_term: str | None = Field(
        alias='user_utm_term'
    )
    user_utm_group: str | None = Field(
        alias='user_utm_group'
    )
    user_gcpc: str | None = Field(
        alias='user_gcpc'
    )
    tags: list | None = Field(
        alias='Теги'
    )
    offer_tags: list | None = Field(
        alias='Теги предложений'
    )


class PaymentsSchema(BaseModel):
    """
    Платежи.
    Список полей: https://getcourse.ru/blog/457215
    """
    pass


class UsersSchema(BaseModel):
    """
    Пользователи.
    Список полей: https://getcourse.ru/blog/276069#ltBlock11772746
    """
    pass


class GroupsSchema(BaseModel):
    """
    Группы пользователей.
    Список полей: https://getcourse.ru/blog/276069#ltBlock11772746
    + ID группы и дата добавления в группу
    """
    pass
