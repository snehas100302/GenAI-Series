from dotenv import load_dotenv
load_dotenv()

from langchain_google_genai import ChatGoogleGenerativeAI
import streamlit as st
llm=ChatGoogleGenerativeAI(model="gemini-3.5-flash-lite")

st.title("Welcome back to QNA ChatBot")
if "messages" not in st.session_state:
    st.session_state.messages=[]
    
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])
        
#for message in st.session_state.messages:
    #with st.chat_message("ai"):
        #st.write(message)
        
query=st.chat_input("What can I help you with today?")

if(query):
    #st.chat_message("user").markdown(query)
    res=llm.invoke(query)
    value=res.text
    #st.chat_message("ai").markdown(res.text)
    #st.session_state.messages.append(("user", query))
    st.session_state.messages.append({"role":"user", "content":query})
    st.session_state.messages.append({"role":"ai","content":value})
    
    with st.chat_message("user"):
        st.write(query)
    with st.chat_message("ai"):
        st.write(value)
