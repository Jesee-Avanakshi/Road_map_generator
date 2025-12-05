import asyncio

# Fix: Create event loop for Streamlit thread
try:
    asyncio.get_event_loop()
except RuntimeError:
    asyncio.set_event_loop(asyncio.new_event_loop())

import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Load API key
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")
print(api_key)
if not api_key:
    raise ValueError("API key not found")

# Initialize Gemini 2.5 Flash model
chat_model = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    api_key=api_key,
    temperature=0.7
)

# Loading user prompt
def load_user_prompt():
    try:
        with open("prompts/roadmap_prompt.txt", "r") as f:
            return f.read()
    except FileNotFoundError:
        raise FileNotFoundError("Could not find prompt file")

# generating road map using LLM chain
def generate_roadmap(name, experience, target_role, career_goal):
    
    prompt_text = load_user_prompt()
    # Build Prompt
    prompt = ChatPromptTemplate.from_messages([
        ("user", prompt_text)
    ])

    # connecting together with chain
    chain = prompt | chat_model | StrOutputParser()

    #Invoking chain
    response = chain.invoke({"name": name,
        "experience": experience,
        "target_role": target_role,
        "career_goal": career_goal
        })
    return response

