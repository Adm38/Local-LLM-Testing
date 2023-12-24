from langchain.prompts import PromptTemplate
from langchain.output_parsers import PydanticOutputParser

from .exp_models import StepInSequence, SequenceCaller

def create_sequence_caller_prompt():
    step_parser = PydanticOutputParser(pydantic_object=StepInSequence)
    sequence_parser = PydanticOutputParser(pydantic_object=SequenceCaller)

    prompt_func = PromptTemplate(
        template="Answer the user query.\nHere are the formatting instructions for the SequenceCaller object{format_instructions_sequence}\n \
        \n{query}\n\n.Here are the functions you have available to you: {whitelisted_functions}. \
            Ensure these function calls (located under the 'sequence' property of SequenceCaller), are ordered sequentially in list format. Do not respond with sentences. Do not explain your reasoning.\n \
            Ensure your respond follows valid JSON schema, using double quotes instead of single quotes. Ensure you include \"sequence\": to start your response.",
        input_variables=["query"],
        partial_variables={
            "format_instructions_sequence": sequence_parser.get_format_instructions()
            },
    )
    
    return prompt_func


# Ideas for good prompts:
# Option A:
#  1. Have the AI handle the required input, breaking down the response into steps in plain english
#  2. Have the AI turn each step into the appropriate function call.
#  3. Return as a list

"""Here are the formatting instructions for the StepInSequence Object:{format_instructions_step}"""