import streamlit as st
from streamlit_chat import message

import openai
from config import open_api_key
openai.api_key = open_api_key

# openAI code
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


def chatgpt_clone(input, history):
    history = history or []
    s = list(sum(history, ()))
    print(s)
    s.append(input)
    inp = ' '.join(s)
    output = openai_create(inp)
    history.append(output)
    return history

# Streamlit App
st.set_page_config(
    page_title="Streamlit Chat - Demo",
    page_icon=":robot:"
)

st.header("ChatGPT Clone with Streamlit")

history_input = []

if 'generated' not in st.session_state:
    st.session_state['generated'] = []

if 'past' not in st.session_state:
    st.session_state['past'] = []



def get_text():
    input_text = st.text_input("You: ", key="input")
    return input_text 


user_input = get_text()


if user_input:
    output = chatgpt_clone(user_input, history_input) 
        #appended as output, so the generated session state will create nested dict
    history_input.append([user_input, output])
    st.session_state.generated.append(output[0])
    st.session_state.past.append(user_input)





if st.session_state['generated']:

    for i in range(0, len(st.session_state['generated'])):
        message(st.session_state['past'][i], is_user=True, key=str(i) + '_user')
        message(st.session_state["generated"][i], key=str(i))



"st.session_state object", st.session_state

st.write(len(st.session_state['generated']))

st.write("generated", st.session_state['generated'])
st.write("past", st.session_state['past'])