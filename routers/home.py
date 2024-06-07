from fastapi import APIRouter

# Configure API router
router = APIRouter(
    tags=['home'],
)


@router.get('/')
async def get_root():
    return {
        'name': 'MobileX-Experience-Lab-Recommending_Menu_for_the_Meal',
    }
