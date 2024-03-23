from langchain.prompts import HumanMessagePromptTemplate, ChatPromptTemplate, MessagesPlaceholder
from langchain_openai import ChatOpenAI
from langchain.chains import LLMChain
from langchain.memory import ConversationBufferMemory, FileChatMessageHistory

from dotenv import load_dotenv

load_dotenv()

memory = ConversationBufferMemory(
    chat_memory = FileChatMessageHistory("message.json"),
    memory_key="messages",  
    return_messages=True
    )

def chat(content):
    chat = ChatOpenAI()

    chatprompt = ChatPromptTemplate(
        input_variables=["content","messages"],
        messages = [
            MessagesPlaceholder(variable_name="messages"),
            HumanMessagePromptTemplate.from_template("{content}")
        ]
    )

    chatchain = LLMChain(
        llm = chat,
        prompt = chatprompt,
        memory = memory
    )

    result_chat = chatchain.invoke({"content": content})

    return result_chat["text"]