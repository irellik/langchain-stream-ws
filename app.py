import asyncio
import websockets
from langchain.chains import LLMChain
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.callbacks.base import AsyncCallbackHandler

# 定义异步处理器
class StreamOut(AsyncCallbackHandler):
    def __init__(self, websocket):
        # ws 对象
        self.websocket = websocket
    # 处理回调
    async def on_llm_new_token(self, token: str, **kwargs: any) -> None:
        await self.websocket.send(token)
async def echo(websocket, path):
    # 选择 stream 方式、回调函数
    chat = ChatOpenAI(streaming=True, callbacks=[StreamOut(websocket)], temperature=0, model_name='gpt-3.5-turbo')
    async for message in websocket:
        chain = LLMChain(llm=chat, prompt = PromptTemplate(
        input_variables=["message"],
        template="{message}",
    ))
        await chain.arun(message=message)

def main():
    asyncio.get_event_loop().run_until_complete(
    websockets.serve(echo, '0.0.0.0', 8765))
    asyncio.get_event_loop().run_forever()

if __name__ == '__main__':
    main()