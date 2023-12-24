import source_code

from source_code.llm_client import get_client

from source_code.llm_client import get_client
from langchain.output_parsers import PydanticOutputParser

from experimental_models import StepInSequence, SequenceCaller
from experimental_prompt_templates import create_sequence_caller_prompt

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

    while True:
        query =  input("User: ").strip()
        sequence: SequenceCaller  = chain.invoke({"query":query})
        result = sequence.invoke()

        print(result)
        print()

if __name__ == "__main__":
    run_experiment()

...
# I'm going to create a new prompt and a new model (I think the FormulaCaller object. I hate that they named it model.)
# The goal of this new functionality is to test the ability of langchain to resolve a nested json into a SequenceCaller object
# This SequenceCaller object is going to basically hold a list of other objects.
# I guess 