from dotenv import load_dotenv
load_dotenv()

from langchain_google_genai import ChatGoogleGenerativeAI
import streamlit as st
llm=ChatGoogleGenerativeAI(model="gemini-3.6-flash")

st.title("Welcome back to QNA ChatBot")
st.session_state.history = []
query=st.chat_input("What can I help you with today?")

if(query):
    st.chat_message("user").markdown(query)
    res=llm.invoke(query)
    value=res.text
    st.chat_message("ai").markdown(res.text)
    st.session_state.history.append(("human", query))
    st.session_state.history.append(("ai",value))
    
