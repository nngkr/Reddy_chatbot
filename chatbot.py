from dotenv import load_dotenv
import streamlit as st
from langchain_groq import ChatGroq

#load the env variables
load_dotenv()

#streamlit page setup
st.set_page_config(
    page_title="chatbot",
    page_icon="🤖",
    layout="centered"
)
st.title("💬 Reddy AI Chatbot")

#initiate chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history=[]


#show chat history

for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

#llm initiate

llm=ChatGroq(
    groq_api_key=st.secrets["GROQ_API_KEY"],
    model="openai/gpt-oss-20b",
    temperature=0.0,
)

#input box
user_prompt=st.chat_input("Ask anything......")

if user_prompt:
    st.chat_message("user").markdown(user_prompt)
    st.session_state.chat_history.append({"role":"user","content":user_prompt})
    
    response=llm.invoke(
        input=[{"role":"assistant","content":"you are a helpful assistant"},*st.session_state.chat_history]
    )
    assistant_response=response.content
    st.session_state.chat_history.append({"role":"system","content":assistant_response})
    
    with st.chat_message("assistant"):
        st.markdown(assistant_response)
