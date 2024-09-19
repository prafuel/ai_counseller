from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import ChatPromptTemplate

from dotenv import load_dotenv
load_dotenv()

# Initialize the AI model
model = ChatGoogleGenerativeAI(model="gemini-1.5-flash")

def clean_output(response: any) -> str:
    return response.content.replace("*", "")

def get_ai_response(prompt_template, query: str) -> str:
    chain = prompt_template | model | clean_output
    return chain.invoke({"query": query})

chat_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful and informative AI assistant. Provide responses with a maximum of 20 words"),
    ("human", "Tell me a random fact about '{query}'")
])

if __name__ == "__main__":
    query = "rabbit"
    result = get_ai_response(chat_prompt, query)
    print(result)
