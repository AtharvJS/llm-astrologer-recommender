# Astrologer Engine 

import os
import ollama
import streamlit as st

from langchain_community.llms import Ollama
from langchain_core.output_parsers import StrOutputParser
from streamlit.runtime.state import session_state


# Streamlit framework
st.title('Interactive Chat Session – AI Astrologer')
st.markdown("✨ *Welcome seeker of the stars...* ✨", unsafe_allow_html=True)
st.markdown('Ask about life, future or advice that you need. \nThe AI astrologer is more than ready to answer all your questions.')
input_text = st.chat_input('Ask the astrologer')


# Session state
if 'messages' not in st.session_state:
  st.session_state.messages = [
  {
    'role': 'system',
    'content': (
      'You are a wise and thoughtful AI astrologer.'
      'The user will provide readings or horoscope summaries or life experiences.'
      'Reply with gentle, insightful life advice in 3-48 sentences. '
      'Keep your tone mystical, encouraging and grounded in astrology themes.'
      'Make a closing remark with a caution and pleasant advice.'
    )
  }
]


# Chat history
for msg in st.session_state.messages[1:]:
  with st.chat_message(msg['role']):
    st.markdown(msg['content'])


# User Input Handling
if input_text:
  st.session_state.messages.append({'role':'user','content':input_text})
  with st.chat_message('user'):
    st.markdown(input_text)


# Streaming Response from Ollama
response_placeholder = st.empty()
full_response = ''

try:
  stream = ollama.chat(model='llama3', messages=st.session_state.messages, stream=True)

  for chunk in stream:
    if 'content' in chunk['message']:
      full_response += chunk['message']['content']
      response_placeholder.markdown(full_response)

  st.session_state.messages.append({'role':'assistant', 'content':full_response})

except Exception as e:
  print(e)

