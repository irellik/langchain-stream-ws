FROM python:3.11

WORKDIR /app

COPY * .

RUN pip install -r requirements.txt

EXPOSE 8765

# ENV OPENAI_API_KEY=your api key

ENTRYPOINT ["python", "app.py", "--host", "0.0.0.0", "--port", "8765"]