import streamlit as st
from model import generate_roadmap

# Streamlit Page Config
st.set_page_config(
    page_title="AI Career Roadmap Generator",
    page_icon="🎯",
    layout="centered"
)

st.title("AI-Powered Career Roadmap Generator")
st.write("Generate a personalized career roadmap based on your experience and goals.")


# Input Form
with st.form("roadmap_form"):
    name = st.text_input("Enter your Name")
    
    experience = st.selectbox(
        "Current Experience Level",
        ["Beginner", "Intermediate", "Expert"]
    )
    
    target_role = st.text_input("Target Job Role (e.g., Data Analyst, AI Engineer, Full Stack Developer)")
    
    career_goal = st.text_area("Describe your Career Goal briefly")
    
    submit = st.form_submit_button("Generate Roadmap")

# Output
if submit:
    if not name or not experience or not target_role or not career_goal:
        st.error("Please fill all required fields.")
    else:
        st.success("Generating your roadmap... Please wait ⏳")
        
        roadmap = generate_roadmap(name, experience, target_role, career_goal)
        
        st.subheader("📘 Your Personalized Career Roadmap")
        st.write(roadmap)
