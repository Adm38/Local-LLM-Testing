import source_code

from source_code.llm_client import get_client

from source_code.llm_client import get_client
from langchain.output_parsers import PydanticOutputParser

from experimenting.exp_models import StepInSequence, SequenceCaller
from .experimental_prompt_templates import create_sequence_caller_prompt

from .exp_functions import create_fake_whitelist

def setup_sequence():
    # TODO: Rename my parsers from 'models' to 'langchain_parsers'.
    # Then, rename 'llm_client' to 'models'
    
    # Get the ChatOpenAI object, but with the base_url set to our local API server 
    model = get_client()

    # Create a prompt to handle functions
    prompt = create_sequence_caller_prompt()

    parser_for_sequence = PydanticOutputParser(pydantic_object=SequenceCaller)
    print(f"full prompt: {prompt}")

    return prompt | model | parser_for_sequence

def run_experiment():
    sequence = setup_sequence()

    query = "how would you respond to a user who wants to buy an item from you, but doesn't know what they want?"
    #query =  input("User: ").strip()
    print("STARTING EXPERIMENT: LAYERED_LCEL")
    sequence_caller: SequenceCaller  = sequence.invoke(input={"query":query, "whitelisted_functions": create_fake_whitelist()})
    print(f"Sequence created! Sequence consists of: {sequence_caller.sequence}")
    result = sequence_caller.invoke()

    print(result)
    print()
    print("EXPERIMENT EXITING.")

if __name__ == "__main__":
    run_experiment()

...
# I'm going to create a new prompt and a new model (I think the FormulaCaller object. I hate that they named it model.)
# The goal of this new functionality is to test the ability of langchain to resolve a nested json into a SequenceCaller object
# This SequenceCaller object is going to basically hold a list of other objects.
# I guess 