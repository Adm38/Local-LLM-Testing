import inspect

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
    function_to_call: str = Field(description="name of function to invoke. This should be the name (like hello_world) without parentheses.")
    function_arguments: dict = Field(description="kwarg dictionary to pass to the function.")

    @validator("function_to_call")
    def is_valid_function(cls, field):
        if field not in valid_functions_to_call.keys():
            raise ValueError("Function not in whitelist!")
        return field

    @validator("function_arguments")
    def is_valid_kwards(cls, field):
        if not isinstance(field, dict):
            raise ValueError("Function arguments must be a dictionary.")
        return field

    def test_valid_kwards_for_func(self, func:callable, kwargs:dict):
        # Get func signature
        signature = inspect.signature(func)

        # Extract parameter names
        parameter_names = list(signature.parameters.keys())

        # Check if all parameter names in kwargs
        for parameter_name in parameter_names:
            if parameter_name not in kwargs:
                raise ValueError(f"Missing required keyword argument: {parameter_name}")
            # additional checks here
            ...
        print("[i] - passed kwargs check")
        return True


    def invoke(self):
        print(f"[i] - Calling func: {self.function_to_call} with arguments: {self.function_arguments}")
        func = valid_functions_to_call[self.function_to_call]["func"]
        if self.test_valid_kwards_for_func(func, self.function_arguments):
            return func(**self.function_arguments)
        raise ValueError("Was unable to call function!")

def hello_world():
    print("hello world!")

def print_to_console(output_str):
    print(output_str)
    
def add_two_numbers(num1, num2):
    return num1+num2

valid_functions_to_call = {
    "hello_world": {
        "func": hello_world,
        "description": "Say hello to the world!",
        "properties": [],
    },
    "print_to_console": {
        "func": print_to_console,
        "description": "",
        "properties": [
            {
                "property_name": "output_str",
                "description": "The string to print to the console",
                "type": "str",
                "default_value": None
            }
        ]
    },
    "add_two_numbers": {
        "func": add_two_numbers,
        "description": "",
        "properties": [
            {
                "property_name": "num1",
                "description": "The first number to add. Must be an int.",
                "type": "int",
                "default_value": None
            },
            {
                "property_name": "num2",
                "description": "The second number to add. Must be an int.",
                "type": "int",
                "default_value": None
            }
        ]
    },
    "scrape_webpage": None,
    "walk_to_store": None
}

# Set up a parser + inject instructions into the prompt template.
parser_joke = PydanticOutputParser(pydantic_object=Joke)
parser_function = PydanticOutputParser(pydantic_object=Function_Caller)

prompt_joke = PromptTemplate(
    template="Answer the user query.\n{format_instructions}\n{query}\n",
    input_variables=["query"],
    partial_variables={"format_instructions": parser_joke.get_format_instructions()},
)

prompt_func = PromptTemplate(
    template="Answer the user query.\n{format_instructions}\n{query}\n\nYou have access to the following functions:{whitelisted_functions}",
    input_variables=["query"],
    partial_variables={"format_instructions": parser_function.get_format_instructions()},
)

model = ChatOpenAI(
    openai_api_key="none",
    base_url="http://localhost:1234/v1",
    temperature=0.0
)


chain = prompt_joke | model | parser_joke
chain_formula = prompt_func | model | parser_function

#joke = chain.invoke({"query": "Tell me a joke about cars."})
#print(joke.setup)
while True:
    query = input("User: ").strip()
    function_to_call = chain_formula.invoke({"query": query, "whitelisted_functions":valid_functions_to_call})
    result = function_to_call.invoke()
    print(result)
#Trying to get the function to be called. If it's a valid function, invoke the method that it is referring to
#Then, work on getting the function to pass along kwargs.
