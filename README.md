# langchain-stream-ws

Langchain Stream 方式获取 openai 数据，提供 websocket 服务器，此项目为 demo，仅供参考

## 使用

1. docker build -t langchain-stream-ws .
2. docker run -d -e OPENAI_API_KEY=your-openai-api-key -p 8080:8765 langchain-stream-ws
3. 随便一个 websocket 客户端连接 ws://ip:8080 就可以了

## 报错
目前运行的时候会出现报错（不影响使用）：Error in on_llm callback: 'StreamOut' object has no attribute 'on_llm'，可能是 langchain 的问题：https://github.com/hwchase17/langchain/issues/4714