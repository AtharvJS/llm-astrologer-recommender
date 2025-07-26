# Astrologer Engine 

import os
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
      'Reply with gentle, insightful life advice in 2-3 sentences. '
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
  st.session_state.messages.append({'role':'system','content':input_text})












































