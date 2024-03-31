import os
from constants import openai_key
from langchain_community.llms import OpenAI
import streamlit as st

os.environ["OPENAI_API_KEY"] = openai_key

st.title('Langchain chatbot')
input_text = st.text_input("Enter your prompt")

llm = OpenAI(temperature=0.8)

previous_prompts = st.session_state.get("previous_prompts", [])  # Retrieve previous prompts from session state

if input_text:
    previous_prompts.append(input_text)  # Add current prompt to previous prompts list
    st.session_state["previous_prompts"] = previous_prompts  # Update session state with new list
    
    prompt_text = "\n".join(previous_prompts) + "\n" + input_text  # Concatenate previous prompts and current input
    response = llm.invoke(prompt_text)  # Invoke language model with concatenated prompt
    
    st.write(response.strip())  # Write the generated text to Streamlit
