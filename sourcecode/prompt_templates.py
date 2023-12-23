from langchain.prompts import PromptTemplate
from langchain.output_parsers import PydanticOutputParser

from models import FunctionCaller

def create_function_prompt():
    parser_function = PydanticOutputParser(pydantic_object=FunctionCaller)

    prompt_func = PromptTemplate(
        template="Answer the user query.\n{format_instructions}\n{query}\n\nYou have access to the following functions:{whitelisted_functions}",
        input_variables=["query"],
        partial_variables={"format_instructions": parser_function.get_format_instructions()},
    )
    
    return prompt_func