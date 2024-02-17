import json
import re
import hashlib
from pydantic import BaseModel, Field, field_validator
from datetime import datetime, date
from decimal import Decimal


def do_hash(input_value: str):
    return hashlib.md5(input_value.strip().lower().encode()).hexdigest()


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

    @field_validator(
        'tags',
        'offer_tags',
        mode='before'
    )
    @classmethod
    def list_to_json_string(cls, value):
        return json.dumps(value)

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
    tags: str | None = Field(
        alias='Теги'
    )
    offer_tags: str | None = Field(
        alias='Теги предложений'
    )

    @field_validator(
        'user_email',
        'user_phone',
        'order_partner_email',
        'user_partner_email'
    )
    def hash_sensitive_data(cls, v):
        """
        Хеширование персональных данных пользователя.
        :param v: Значение поля.
        :return:
        """
        if v == '':
            v = None

        if v is not None:
            return do_hash(str(v))
        return v


class PaymentsSchema(BaseModel):
    """
    Платежи.
    Список полей: https://getcourse.ru/blog/579878
    """
    def __init__(self, **data):
        for key, val in data.items():
            if val == '':
                data[key] = None

        super().__init__(**data)

    @field_validator(
        'amount',
        'commissions',
        'received',
        mode='before'
    )
    @classmethod
    def parse_amount(cls, value):
        return float(re.sub(r'[^\d.]', '', value)[:-1])

    payment_number: str | None = Field(
        alias='Номер',
        description='Номер платежа'
    )
    user_name: str | None = Field(alias='Пользователь')
    user_email: str | None = Field(alias='Эл. почта')
    order_id: str | None = Field(alias='Заказ')
    created_at: datetime | None = Field(alias='Дата создания')
    order_type: str | None = Field(alias='Тип')
    payment_status: str | None = Field(alias='Статус')
    amount: Decimal | None = Field(alias='Сумма')
    commissions: Decimal | None = Field(alias='Комиссии')
    received: Decimal | None = Field(alias='Получено')
    payment_code: str | None = Field(alias='Код платежа')
    title: str | None = Field(
        alias='Название',
        description='Название предложения'
    )

    @field_validator('user_email')
    def hash_sensitive_data(cls, v):
        """
        Хеширование персональных данных пользователя.
        :param v: Значение поля.
        :return:
        """
        if v == '':
            v = None

        if v is not None:
            return do_hash(str(v))
        return v


class UsersSchema(BaseModel):
    """
    Пользователи.
    Список полей: https://getcourse.ru/blog/276069#ltBlock11772746
    """
    def __init__(self, **data):
        for key, val in data.items():
            if val == '':
                data[key] = None

        super().__init__(**data)

    id: str | None = Field(alias='id')
    email: str | None = Field(alias='Email')
    registration_type: str | None = Field(alias='Тип регистрации')
    created_at: datetime | None = Field(alias='Создан')
    last_activity_at: datetime | None = Field(alias='Последняя активность')
    first_name: str | None = Field(alias='Имя')
    last_name: str | None = Field(alias='Фамилия')
    phone: str | None = Field(alias='Телефон')
    birthdate: date | None = Field(alias='Дата рождения')
    age: int | None = Field(alias='Возраст')
    country: str | None = Field(alias='Страна')
    city: str | None = Field(alias='Город')
    from_partner: str | None = Field(alias='От партнера')
    referral: str | None = Field(alias='Откуда пришел')
    utm_source: str | None = Field(alias='utm_source')
    utm_medium: str | None = Field(alias='utm_medium')
    utm_campaign: str | None = Field(alias='utm_campaign')
    utm_term: str | None = Field(alias='utm_term')
    utm_content: str | None = Field(alias='utm_content')
    utm_group: str | None = Field(alias='utm_group')
    partner_id: str | None = Field(alias='ID партнера')
    partner_email: str | None = Field(alias='Email партнера')
    partner_full_name: str | None = Field(alias='ФИО партнера')
    manager_full_name: str | None = Field(alias='ФИО менеджера')
    vk_id: str | None = Field(alias='VK-ID')

    @field_validator(
        'email',
        'phone',
        'partner_email'
    )
    def hash_sensitive_data(cls, v):
        """
        Хеширование персональных данных пользователя.
        :param v: Значение поля.
        :return:
        """
        if v == '':
            v = None

        if v is not None:
            return do_hash(str(v))
        return v


class GroupsSchema(BaseModel):
    id: str | None = Field(alias='id')
    name: str | None = Field(alias='name')
    last_added_at: datetime | None = Field(alias='last_added_at')


class UsersGroupSchema(UsersSchema):
    """
    Группы пользователей.
    Список полей: https://getcourse.ru/blog/276069#ltBlock11772746
    + ID группы и дата добавления в группу
    """
    group_id: str | None = Field(alias='ID группы')
    group_added_at: datetime | None = Field(alias='Добавлен в группу')
