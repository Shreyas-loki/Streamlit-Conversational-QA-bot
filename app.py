## Conversational Q&A Chatbot
import streamlit as st

from langchain.schema import HumanMessage, SystemMessage, AIMessage
# from openai import AzureChatOpenAI
from langchain_openai import AzureChatOpenAI
import os
# import dotenv
# dotenv.load_dotenv()

# Initialize the Azure OpenAI client
llm = AzureChatOpenAI(
        azure_endpoint="https://azureopenai16.openai.azure.com/",
        api_key="75db73a3b9da40b0b6e0e98273a6029f",  
        api_version="2024-05-01-preview",
        deployment_name="gpt35turbo",
        temperature=0.5
    )

# '''
## Streamlit UI
st.set_page_config(page_title="Conversational Q&A Chatbot")
st.header("Hey, Let's Chat")


if 'flow_messages' not in st.session_state:
    st.session_state['flow_messages'] = [
        SystemMessage(content="You are an AI assitant who answers the questions asked truthfully!")
    ]

## Function to load OpenAI model and get respones
def get_chatmodel_response(question):
    st.session_state['flow_messages'].append(HumanMessage(content=question))
    
    response = llm(st.session_state['flow_messages'])

    st.session_state['flow_messages'].append(AIMessage(content=response.content))
    return response.content


input = st.text_input("Input: ", key="input")
response = get_chatmodel_response(input)

submit = st.button("Ask the question")

## If ask button is clicked
if submit:
    st.subheader("The Response is")
    st.write(response)
