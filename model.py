import os
from dotenv import load_dotenv
from langchain_google_genai.chat_models import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Load API key
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

# Initialize Gemini 2.5 Flash model
chat_model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.7,
    google_api_key=api_key
)

# Loading user prompt
def load_user_prompt():
    with open("prompts/roadmap_prompt.txt", "r") as f:
        return f.read()

# generating road map
def generate_roadmap(name, experience, target_role, career_goal):
    
    prompt_text = load_user_prompt()
    # TURN TEXT INTO A ChatPromptTemplate
    prompt = ChatPromptTemplate.from_messages([
        ("user", prompt_text)
    ])

    # connecting together with chain
    chain = prompt | chat_model | StrOutputParser()

    #Invoking chain
    response = chain.invoke({"name": name,
        "experience": experience,
        "target_role": target_role,
        "career_goal": career_goal})
    return response

