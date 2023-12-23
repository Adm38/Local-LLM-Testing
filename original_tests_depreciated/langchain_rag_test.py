#Currently cannot install llama-cpp-python because I don't have the prereqs to install CMAKE.
#Follow directions here to install that:
#https://stackoverflow.com/questions/77267346/error-while-installing-python-package-llama-cpp-python

from langchain.chat_models import ChatOpenAI
from langchain.embeddings import LlamaCppEmbeddings
from langchain.prompts import ChatPromptTemplate
from langchain.vectorstores import DocArrayInMemorySearch
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel, RunnablePassthrough

openai_api_key = "none"
local_base_url="http://localhost:1234/v1"

vectorstore = DocArrayInMemorySearch.from_texts(
    ["harrison worked at kensho", "bears like to eat honey"],
    embedding=LlamaCppEmbeddings(model_path="C:/Users/Cullen/.cache/lm-studio/models/TheBloke/Athena-v4-GGUF/athena-v4.Q6_K.gguf"),
)
retriever = vectorstore.as_retriever()

template = """Answer the question based only on the following context:
{context}

Question: {question}
"""
prompt = ChatPromptTemplate.from_template(template)
model = ChatOpenAI(
    openai_api_key=openai_api_key,
    base_url=local_base_url
)
output_parser = StrOutputParser()

setup_and_retrieval = RunnableParallel(
    {"context": retriever, "question": RunnablePassthrough()}
)
chain = setup_and_retrieval | prompt | model | output_parser

chain.invoke("where did harrison work?")