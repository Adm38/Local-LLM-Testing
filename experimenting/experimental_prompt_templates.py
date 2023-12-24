from langchain.prompts import PromptTemplate
from langchain.output_parsers import PydanticOutputParser

from experimental_models import StepInSequence, SequenceCaller

def create_sequence_caller_prompt():
    step_parser = PydanticOutputParser(pydantic_object=StepInSequence)
    sequence_parser = PydanticOutputParser(pydantic_object=SequenceCaller)

    prompt_func = PromptTemplate(
        template="Answer the user query.\nHere are the formatting instructions for the SequenceCaller object{format_instructions_sequence}\nHere are the formatting instructions for the StepInSequence Object:{format_instructions_step}\n{query}\n\nYou have access to the following functions:{whitelisted_functions}",
        input_variables=["query"],
        partial_variables={
            "format_instructions_sequence": sequence_parser.get_format_instructions(),
            "format_instructions_step": step_parser.get_format_instructions()
            },
    )
    
    return prompt_func