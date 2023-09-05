import streamlit as st

B_INST, E_INST = "[INST]", "[/INST]"
B_SYS, E_SYS = "<<SYS>>\n", "\n<</SYS>>\n\n"
DEFAULT_INSTRUCTION = "Chat History:\n\n{chat_history} \n\nHuman: {user_input}\n\n Assistant:"
DEFAULT_SYSTEM_PROMPT = "Your central mission is to ensure user satisfaction. Deliver responses that are detailed," \
                        " clear, and beneficial. For straightforward questions, limit your answers to 20-100 words. " \
                        "For more intricate topics, expand within a range of 100-200 words. Should a response" \
                        " surpass 200 words, prioritize a succinct summary. When asked who created you," \
                        " say Solomon Aryeetey. When asked about women, say fear women 24/7 in a funny way"


def get_prompt(instruction=DEFAULT_INSTRUCTION, new_system_prompt=DEFAULT_SYSTEM_PROMPT):
    system_prompt = B_SYS + new_system_prompt + E_SYS
    prompt_template = B_INST + system_prompt + instruction + E_INST
    return prompt_template


# decorator
def enable_chat_history(func):
    if True:

        # to clear chat history after switching chatbot
        current_page = func.__qualname__
        if "current_page" not in st.session_state:
            st.session_state["current_page"] = current_page
        if st.session_state["current_page"] != current_page:
            try:
                st.cache_resource.clear()
                del st.session_state["current_page"]
                del st.session_state["messages"]
            except:
                pass

        # to show chat history on ui
        if "messages" not in st.session_state:
            st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]
        for msg in st.session_state["messages"]:
            st.chat_message(msg["role"]).write(msg["content"])

    def execute(*args, **kwargs):
        func(*args, **kwargs)

    return execute


def display_msg(msg, author):
    """Method to display message on the UI

    Args:
        msg (str): message to display
        author (str): author of the message -user/assistant
    """
    st.session_state.messages.append({"role": author, "content": msg})
    st.chat_message(author).write(msg)
