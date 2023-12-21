# Example: reuse your existing OpenAI setup
import os
import openai

system_prompt = ""
user_prompt = ""

def get_current_weather(desired_location):
    if desired_location["location"] is not None:
        print(f"Oh I've gotten the latest weather! Here it is for {desired_location['location']}")
    else:
        print("Invalid location")

def file_to_string(file_name):
    output_str = ""
    with open(file_name, "r") as f:
        
        _lines = f.readlines()
        for line in _lines:
            # if not the first one add a newline
            if len(output_str) > 0:
                output_str += "\n"
            output_str += line

    return output_str

def create_player_msg(input_string):
    message = {
        "role": "user",
        "content": input_string
    }
    return message

def create_ai_msg(completion_obj):
    response_content = completion.choices[0].message.content
    response_content = response_content.strip()

    # test for function
    if "get_current_weather" in response_content:
        print("Function found! Attempting to run...")
        eval(response_content)    

    message = {
        "role": "assistant",
        "content": response_content
    }

    return message

#system_prompt = file_to_string("system-prompt.txt")
system_prompt = file_to_string("tool_calling_sys_prompt.txt") 
user_prompt = file_to_string("user-prompt.txt")

client = openai.OpenAI(
    base_url = "http://localhost:1234/v1",
    api_key = "hello there"
)

#openai.api_base = "http://localhost:1234/v1" # point to the local server
#openai.api_key = "" # no need for an API key



message_log = [
    {"role": "system", "content": system_prompt}
]

while True:
    print()
    player_input = input("User: ")
    player_input = player_input.strip()

    message_log.append(create_player_msg(player_input))

    #process player input
    completion = client.chat.completions.create(
        model="gpt-4",
        messages=message_log
    )

    #log response
    message_log.append(create_ai_msg(completion_obj=completion))
    print()
    print("AI: ", end="")
    print(completion.choices[0].message.content)



print(completion.id)
print(completion.choices[0].message.content)
print(completion.choices[0].message)