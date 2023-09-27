from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_async_session
from app.core.user import current_superuser, current_user
from app.crud.donation import donation_crud
from app.models import User
from app.schemas.donation import DonationCreate, DonationDB
from ...utils import DONATION_EXCLUDE_FIELS, investing

donation_router = APIRouter()


@donation_router.get(
    '/',
    response_model=list[DonationDB],
    dependencies=[Depends(current_superuser)],
    response_model_exclude_none=True
)
async def get_all_donations(
    session: AsyncSession = Depends(get_async_session)
):
    """Только для суперюзеров."""
    return await donation_crud.get_multi(session)


@donation_router.post(
    '/',
    response_model=DonationDB,
    response_model_exclude={*DONATION_EXCLUDE_FIELS},
    response_model_exclude_none=True
)
async def create_donation(
    donation: DonationCreate,
    session: AsyncSession = Depends(get_async_session),
    user: User = Depends(current_user),
):
    new_donation = await donation_crud.create_if_not_exists(
        donation, session, user
    )
    await investing(new_donation, session)
    return new_donation


@donation_router.get(
    '/my',
    response_model=list[DonationDB],
    response_model_exclude={*DONATION_EXCLUDE_FIELS}
)
async def get_user_donations(
    session: AsyncSession = Depends(get_async_session),
    user: User = Depends(current_user)
):
    return await donation_crud.get_by_user(
        session=session, user=user
    )
