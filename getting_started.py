from dotenv import load_dotenv

from langchain_openai import OpenAI, ChatOpenAI # llm 모델 그 자체와 ChatGPT 가져옴
from langchain_core.messages import SystemMessage, HumanMessage

load_dotenv()

llm = OpenAI()
chat_model = ChatOpenAI()

text = "한국어로된 개발자 닉네임을 짓고싶어. 어떤게 좋을까?"

print(llm.invoke(text))

messages = [SystemMessage(content="You are the name maker."), HumanMessage(content=text)]
print(chat_model.invoke(messages))
