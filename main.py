from openai import OpenAI

# load environment variables from .env file
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# use the OpenAI responses API to generate a response to a question
response = client.responses.create(
    model="gpt-5-nano",
    input="What is the capital of France?",
    instructions="You are a helpful assistant that provides concise answers to questions.",
)
print(response.output_text)
