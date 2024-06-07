from typing import Literal

from pydantic import BaseModel, Field

MIN_LENGTH = 2
MAX_LENGTH = 4

class InputModel(BaseModel):
    name: str = Field(
        # alias='Name',
        description='이름을 입력해주세요 (2~4자)',
        min_lengt=MIN_LENGTH,
        max_length=MAX_LENGTH,
    )
    weather: Literal['맑음', '구름적음', '구름많음', '흐림', '약한 비', '비', '강한 비', '약한 바람', '강한 바람'] = Field(
        # alias='The Weather',
    )
    food_type: Literal['한식', '일식', '양식', '중식'] = Field(
        # alias='Food Type',
    )
    situation: Literal['혼자', '연인과', '친구들끼리', '선후배끼리', '교수님과'] = Field(
        # alias='Situation',
        description='어떤 사람들이랑 밥을 먹으러 가는지 선택해주세요',
    )
    number_of_people: str = Field(
        # alais='Number Of People',
        description='식사하는 사람의 수를 적어주세요',
    )
    additional_content: str = Field(
        # alias='Additional content',
        description='추가적으로 고려했으면 하는 내용을 적어주세요',
    )
    llm_type: str = Field(
        # alias='Large Language Model Type',
        description='사용할 LLM 종류',
        default='chatgpt',
    )


class OutputModel(BaseModel):
    output: str = Field(
        description='Recommending Menu for the Meal',
    )
