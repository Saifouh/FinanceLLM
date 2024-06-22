from textwrap import dedent
from phi.assistant import Assistant
from phi.tools.serpapi_tools import SerpApiTools
import streamlit as st
from phi.llm.openai import OpenAIChat

# setup streamlit
st.title("AI Personal Finance Planner")
st.caption("Manage your finances with AI Personal Finance Manager by creating personalized budgets, investment plans, and saving strategies using GPT-4")
# Get OpenAI API key from user
openai_api_key = st.text_input("Enterr OpenAI API Key to access GPT-4", type="password")
# Get SerpAPI key from user
serp_api_key = st.text_input("Enter Serp API Key to access GPT-4", type="password")
if openai_api_key and serp_api_key:
    researcher = Assistant(...)
    planner = Assistant(...)
    # Input fields for users goals and situation
    financial_goals = st.text_input("what are your financial goals?")
    current_situation = st.text_area("Describe your current financial situation")

    if st.button("Generate Financial Plan"):
        with st.spinner("processing..."):
            # get response from assistant
            response = planner.run(f"Financial goals: {financial_goals}, Current situation: {current_situation}", stream=False)
            st.write(response)


            
