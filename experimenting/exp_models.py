from typing import List
from langchain_core.pydantic_v1 import BaseModel, Field, validator

from .exp_functions import create_fake_whitelist

class StepInSequence(BaseModel):
    function_name: str = Field(description="The name of a function that would complete the next step of the user's query.")

    def invoke(self):
        whitelist = create_fake_whitelist()
        print(f"Invoking function '{self.function_name}'")
        whitelist[self.function_name]()
    
    def __str__(self) -> str:
        return f"{self.function_name}"



class SequenceCaller(BaseModel):
    sequence: List[StepInSequence] = Field(description="List of StepInSequence objects in sequence that will fulfill the user's request. \
                                           use your best judgement when ordering the sequence. the sequence should be between 2-5 StepInSequence long.")

    @validator("sequence")
    def is_valid_list(cls, field: List[StepInSequence]):
        if not isinstance(field, List):
             raise TypeError(f"SequenceCaller did not receive a list. Received {type(field)} instead.")
        if len(field) == 0:
            raise ValueError("Length of sequence is 0.")
        if not isinstance(field[0], StepInSequence):
            raise TypeError(f"SequenceCaller was expecting 'field' to be a list of StepInSequence, but \
                            received List[{type(field[0])}].")
        return field

    def invoke(self):
        for step in self.sequence:
            print(f"Running {step.function_name}")
            step.invoke()

        print("Sequence finished!")
