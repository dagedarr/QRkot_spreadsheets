from datetime import datetime
from typing import Union

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models import CharityProject, Donation

DONATION_EXCLUDE_FIELS = [
    'user_id',
    'invested_amount',
    'fully_invested',
    'close_date'
]


async def investing(
    input_obj: Union[CharityProject, Donation],
    session: AsyncSession
):
    # Определение целевой модели и выборка объектов
    target_model = CharityProject if isinstance(input_obj, Donation) else Donation
    objects = await session.execute(
        select(target_model)
        .where(target_model.fully_invested == 0)
        .order_by(target_model.create_date)
    )

    all_money = input_obj.full_amount

    # Итерация по объектам
    for obj in objects.scalars().all():
        needed_money = obj.full_amount - obj.invested_amount
        to_invest = min(needed_money, all_money)

        # Обновление сумм и доступного баланса
        obj.invested_amount += to_invest
        input_obj.invested_amount += to_invest
        all_money -= to_invest

        # Проверка на полное инвестирование
        if obj.full_amount == obj.invested_amount:
            obj.fully_invested = 1

        # Проверка на полное инвестирование всех проектов
        if not all_money:
            input_obj.fully_invested = 1
            input_obj.close_date = datetime.now()
            break

    # Завершение транзакции
    await session.commit()
    await session.refresh(input_obj)
    return input_obj
