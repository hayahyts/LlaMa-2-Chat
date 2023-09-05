import utils
import streamlit as st
from togetherai import TogetherLLM

from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.memory import ConversationBufferWindowMemory

st.set_page_config(page_title="BIA chatbot", page_icon="⭐")
st.header('Bridge-in-Agriculture chatbot')
st.write('Enhancing Chatbot Interactions through Context Awareness')


class ContextChatbot:

    def __init__(self):
        self.together_ai_model = "togethercomputer/llama-2-70b-chat"

    @st.cache_resource
    def setup_chain(_self):
        template = utils.get_prompt()
        prompt = PromptTemplate(
            input_variables=["chat_history", "user_input"],
            template=template,
        )
        llm = TogetherLLM(
            model=_self.together_ai_model,
            temperature=0.1,
            max_tokens=512
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
