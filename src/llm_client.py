from langchain.chat_models import ChatOpenAI

def get_client():
    model = ChatOpenAI(
        openai_api_key="none",
        base_url="http://localhost:1234/v1",
        temperature=0.1
    ) 
    return model