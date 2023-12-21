from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

from langchain.output_parsers import PydanticOutputParser
from langchain_core.pydantic_v1 import BaseModel, Field, validator



# Define your desired data structure.
class Joke(BaseModel):
    setup: str = Field(description="question to set up a joke")
    punchline: str = Field(description="answer to resolve the joke")

    # You can add custom validation logic easily with Pydantic.
    @validator("setup")
    def question_ends_with_question_mark(cls, field):
        if field[-1] != "?":
            raise ValueError("Badly formed question!")
        return field
    
    def say_setup(self):
        print(self.setup)
    
    def say_punchline(self):
        print(self.punchline)


class Function_Caller(BaseModel):
    _function_to_call: callable = Field(description="function to invoke")
    _function_arguments: dict = Field(description="kwarg dictionary to pass to the function")

    @validator("_function_to_call")
    def is_valid_function(cls, field):
        if field not in valid_functions_to_call.keys():
            raise ValueError("Not a valid function!")
        return field

def hello_world():
    print("hello world!")
    

valid_functions_to_call = {
    "hello_world": hello_world,
}

# Set up a parser + inject instructions into the prompt template.
parser = PydanticOutputParser(pydantic_object=Joke)

prompt = PromptTemplate(
    template="Answer the user query.\n{format_instructions}\n{query}\n",
    input_variables=["query"],
    partial_variables={"format_instructions": parser.get_format_instructions()},
)

model = ChatOpenAI(
    openai_api_key="none",
    base_url="http://localhost:1234/v1",
    temperature=0.0
)


chain = prompt | model | parser

joke = chain.invoke({"query": "Tell me a joke about cars."})
print(joke.setup)

#Trying to get the function to be called. If it's a valid function, invoke the method that it is referring to
#Then, work on getting the function to pass along kwargs.
