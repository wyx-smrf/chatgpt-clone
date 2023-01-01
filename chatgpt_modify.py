import streamlit as st
from streamlit_chat import message

import openai
from config import open_api_key
openai.api_key = open_api_key

# openAI code (gets na)
def openai_create(prompt):

    response = openai.Completion.create(
    model="text-davinci-003",
    prompt=prompt,
    temperature=0.9,
    max_tokens=150,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0.6,
    stop=[" Human:", " AI:"]
    )

    return response.choices[0].text

# gets na
def chatgpt_clone(input, history):
    history = history or []
    s = list(sum(history, ()))
    print(s)
    s.append(input)
    inp = ' '.join(s)
    output = openai_create(inp)
    history.append((input, output))
    return history, history



# Streamlit App Configurations
st.set_page_config(
    page_title="Streamlit / OpenAI", # Title of the webpage
    page_icon="🤖",
    menu_items={
        'Get Help': None,
        'Report a bug': None,
        'About': "Author: [Roi Jacob C. Olfindo](https://github.com/wyx-smrf)"
    }    
)

st.header("ChatGPT Clone with Streamlit")
st.markdown('---')

history_input = []

if 'generated' not in st.session_state:
    st.session_state['generated'] = []

if 'past' not in st.session_state:
    st.session_state['past'] = []


def get_text():
    input_text = st.text_input("You: ", key="input")
    return input_text 


user_input = get_text()
# what is the equation for first law of thermodynamics?

if user_input:
    output = chatgpt_clone(user_input, history_input)
    history_input.append([user_input, output])
    st.session_state.past.append(user_input)
    st.session_state.generated.append(output[0])





if st.session_state['generated']:

    for i in range(len(st.session_state['generated'])-1, -1, -1):
        message(st.session_state["generated"][i], key=str(i))
        message(st.session_state['past'][i], is_user=True, key=str(i) + '_user')