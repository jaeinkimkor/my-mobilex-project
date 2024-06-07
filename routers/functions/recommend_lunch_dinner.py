import os

from fastapi import APIRouter

from llm.chat import build
from llm.store import LLMStore
from models.recommend_lunch_dinner import InputModel, OutputModel

# Configure API router
router = APIRouter(
    tags=['functions'],
)

# Configure metadata
NAME = os.path.basename(__file__)[:-3]

# Configure resources
store = LLMStore()

###############################################
#                   Actions                   #
###############################################


@router.post(f'/func/{NAME}')
async def call_acrostic_generator(model: InputModel) -> OutputModel:
    # Create a LLM chain
    chain = build(
        name=NAME,
        llm=store.get(model.llm_type),
    )

    input = f'''
    - name: {model.name},
    - weather: {model.weather},
    - food_type: {model.food_type},
    - situation: {model.situation},
    - number of people: {model.number_of_people},
    - additional content: {model.additional_content}
    '''

    return OutputModel(
        output=chain.invoke({
            'input_context': input
        }),
    )
