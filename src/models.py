# File contains my Pydantic models
import inspect

from langchain_core.pydantic_v1 import BaseModel, Field, validator

from functions_config import whitelisted_functions

class FunctionCaller(BaseModel):
    function_to_call: str = Field(description="name of function to invoke. This should be the name (like hello_world) without parentheses.")
    function_arguments: dict = Field(description="kwarg dictionary to pass to the function.")

    @validator("function_to_call")
    def is_valid_function(cls, field):
        if field not in whitelisted_functions.keys():
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
        func = whitelisted_functions[self.function_to_call]["func"]
        if self.test_valid_kwards_for_func(func, self.function_arguments):
            return func(**self.function_arguments)
        raise ValueError("Was unable to call function!")