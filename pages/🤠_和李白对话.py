import openai
import streamlit as st
from message_log import message_log
api_key = "{YOU_API_KEY}"
openai.api_key = "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"


def generate_response(message_log):
    # Use OpenAI's ChatCompletion API to get the chatbot's response
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # The name of the OpenAI chatbot model to use
        # The conversation history up to this point, as a list of dictionaries
        messages=message_log,
        # max_tokens=4096,        # The maximum number of tokens (words or subwords) in the generated response
        # stop=None,              # The stopping sequence for the generated response, if any (not used here)
        # The "creativity" of the generated response (higher temperature = more creative)
        temperature=0.7,
    )

    # Find the first response from the chatbot that has text in it (some responses may not have text)
    for choice in response.choices:
        if "text" in choice:
            return choice.text

    # If no response with text is found, return the first response's content (which may be empty)
    return response.choices[0].message.content


st.markdown("# 绣口一吐，就是半个盛唐")

if 'generated' not in st.session_state:
    st.session_state['generated'] = []
if 'past' not in st.session_state:
    st.session_state['past'] = []
user_input = st.text_area("输入你想说的话O(∩_∩)O", key='input')
# 设置一个发送消息的按钮
st.button('点我点我')


if user_input:
    if st.button('点这里发送跨越千年的对话~'):
    # print(message_log)
        message_log.append({"role": "user", "content": user_input})
        output = generate_response(message_log)
        message_log.append({"role": "assistant", "content": output})
        # store the output
        st.session_state['past'].append(user_input)
        st.session_state['generated'].append(output)

if st.session_state['generated']:
    for i in range(len(st.session_state['generated'])-1, -1, -1):
        # message(st.session_state["generated"][i], key=str(i))
        st.markdown('-----------------------------------------')
        st.markdown(f'''**你:** {st.session_state['past'][i]}''')
        st.markdown(f'''**李白:** {st.session_state["generated"][i]}''')
        # message(st.session_state['past'][i], is_user=True, key=str(i) + '_user')
        
st.markdown("<style> footer {visibility: hidden;} </style>", unsafe_allow_html=True)