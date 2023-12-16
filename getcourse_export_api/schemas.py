from pydantic import BaseModel


class DealsSchema(BaseModel):
    """
    Заказы из системы.
    Список полей: https://getcourse.ru/blog/457215
    """
    # order_id - ID заказа
    # order_number - Номер
    # user_id - ID пользователя
    # username - Пользователь
    # user_email - Email
    # user_phone - Телефон
    # creation_date - Дата создания
    # payment_date - Дата оплаты
    # offer_title - Title
    # order_status - Статус
    # price - Стоимость, RUB
    # paid - Оплачено
    # payment_system_fee - Комиссия платежной системы
    # received_amount - Получено
    # tax - Налог
    # net_amount - Осталось после вычета комиссии платежной системы и налога
    # other_fees - Другие комиссии
    # earned - Заработано
    # currency - Валюта
    # manager - Менеджер
    # city - Город
    # payment_system - Платежная система
    # partner_id - ID
    # партнера
    # promo_code - Использован промокод
    # promo_name - Промоакция
    # order_partner_id - ID партнера заказа
    # order_partner_email - Email партнера заказа
    # order_partner_name - ФИО партнера заказа
    # user_partner_id - ID партнера пользователя
    # user_partner_email - Email партнера пользователя
    # user_partner_name - ФИО партнера пользователя
    # utm_source - utm_source
    # utm_medium - utm_medium
    # utm_campaign - utm_campaign
    # utm_content - utm_content
    # utm_term - utm_term
    # utm_group - utm_group
    # partner_source - Партнерский источник
    # partner_code - Партнерский код
    # session_partner - Партнер(сессия)
    # user_utm_source - user_utm_source
    # user_utm_medium - user_utm_medium
    # user_utm_campaign - user_utm_campaign
    # user_utm_content - user_utm_content
    # user_utm_term - user_utm_term
    # user_utm_group - user_utm_group
    # user_gcpc - user_gcpc
    # tags - Теги
    # offer_tags - Теги предложений
    pass


class PaymentsSchema(BaseModel):
    """
    Платежи.
    Список полей, как в заказах.
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
