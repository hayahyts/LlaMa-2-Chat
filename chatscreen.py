import utils
import streamlit as st
from togetherai import TogetherLLM

from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.memory import ConversationBufferWindowMemory

st.set_page_config(page_title="AryeeteyGPT", page_icon="⭐")
st.header("AryeeteyGPT")
st.write("Let's talk about anything you're interested in!")


class ContextChatbot:

    def __init__(self):
        self.together_ai_model = "togethercomputer/llama-2-70b-chat"

    @st.cache_resource
    def setup_chain(_self):
        api_key = st.secrets["TOGETHER_AI_KEY"]
        template = utils.get_prompt()
        prompt = PromptTemplate(
            input_variables=["chat_history", "user_input"],
            template=template,
        )
        llm = TogetherLLM(
            model=_self.together_ai_model,
            api_key=api_key,
            temperature=0.7,
            max_tokens=250
        )
        memory = ConversationBufferWindowMemory(memory_key="chat_history", k=3)
        chain = LLMChain(
            llm=llm,
            prompt=prompt,
            verbose=True,
            memory=memory,
        )
        return chain

    @utils.enable_chat_history
    def main(self):
        chain = self.setup_chain()
        user_query = st.chat_input(placeholder="Ask me about Bridge in Agriculture!")
        if user_query:
            utils.display_msg(user_query, 'user')
            with st.spinner("Typing..."):
                bot_response = chain.predict(user_input=user_query)
                utils.display_msg(bot_response, 'assistant')


if __name__ == "__main__":
    obj = ContextChatbot()
    obj.main()
