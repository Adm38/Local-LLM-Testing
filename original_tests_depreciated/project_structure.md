ChatGPT's recommendation for how to structure my project.

# main.py
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

from langchain.output_parsers import PydanticOutputParser
from functions import Function_Caller, valid_functions_to_call

# ... (rest of your code)

if __name__ == "__main__":
    # ... (your existing execution code)

# functions.py
import inspect
from langchain_core.pydantic_v1 import BaseModel, Field, validator

# ... (rest of your function-related code)

# models.py
from langchain_core.pydantic_v1 import BaseModel, Field, validator

# ... (your Pydantic models)

# prompt_templates.py
from langchain.prompts import PromptTemplate

# ... (your prompt templates)
