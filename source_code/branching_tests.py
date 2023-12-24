from llm_client import get_client
from prompt_templates import create_function_prompt
from langchain.output_parsers import PydanticOutputParser
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableBranch
from langchain.prompts import PromptTemplate

from models import FunctionCaller
from functions_config import whitelisted_functions



def setup_branching():
    model = get_client()

    prompt_branching = PromptTemplate.from_template('''
Classify the given user question as either 'shopkeeper_funcs' or 'general_funcs' based on the nature of the question. If the question is related to shopkeeping activities like buying, selling, or checking inventory, classify it as 'shopkeeper_funcs'. Otherwise, classify it as 'general_funcs'.

List of shopkeeper functions:
  * retrieve_inventory

Question:
{question}

Classification:''')

    chain = (prompt_branching | model | StrOutputParser())
    return chain
    

def setup_chain():
    # TODO: Rename my parsers from 'models' to 'langchain_parsers'.
    # Then, rename 'llm_client' to 'models'
    
    # Get the ChatOpenAI object, but with the base_url set to our local API server 
    model = get_client()

    # Create a prompt to handle functions
    prompt = create_function_prompt()

    parser_for_func_call = PydanticOutputParser(pydantic_object=FunctionCaller)

    return prompt | model | parser_for_func_call

if __name__ == "__main__":
    chain = setup_chain()
    branching_chain = setup_branching()

    # Original FunctionCaller chain
    while False:
        query =  input("User: ").strip()
        function_to_call: FunctionCaller = chain.invoke({"query":query, "whitelisted_functions": whitelisted_functions})
        result = function_to_call.invoke()

        print(result)
        print()

    while True:
        query = input("User: ").strip()
        response = branching_chain.invoke({'question': query})
        print(response)