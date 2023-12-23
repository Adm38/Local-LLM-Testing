from llm_client import get_client
from prompt_templates import create_function_prompt
from langchain.output_parsers import PydanticOutputParser

from models import FunctionCaller
from functions_config import whitelisted_functions

def setup_chain():
    # TODO: Rename my parsers from 'models' to 'langchain_parsers'.
    # Then, rename 'llm_client' to 'models'
    
    # Get the ChatOpenAI object, but with the base_url set to our local API server 
    model = get_client()

    # Create a prompt to handle functions
    prompt = create_function_prompt()

    parser_for_func_call = PydanticOutputParser(pydantic_object=FunctionCaller)
    print(f"full prompt: {prompt}")

    return prompt | model | parser_for_func_call

if __name__ == "__main__":
    chain = setup_chain()

    while True:
        query =  input("User: ").strip()
        function_to_call: FunctionCaller = chain.invoke({"query":query, "whitelisted_functions": whitelisted_functions})
        result = function_to_call.invoke()

        print(result)
        print()