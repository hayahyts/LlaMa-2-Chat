from langchain.memory import ConversationBufferMemory
from langchain import LLMChain, PromptTemplate
from togetherai import TogetherLLM

B_INST, E_INST = "[INST]", "[/INST]"
B_SYS, E_SYS = "<<SYS>>\n", "\n<</SYS>>\n\n"
DEFAULT_SYSTEM_PROMPT = """
You are a helpful, respectful and honest assistant. Always answer as helpfully as 
possible, while being safe. Your answers should not include any harmful, unethical, racist, sexist, toxic, dangerous, 
or illegal content. Please ensure that your responses are socially unbiased and positive in nature. 

If a question does not make any sense, or is not factually coherent, explain why instead of answering something not 
correct. If you don't know the answer to a question, please don't share false information. """


def get_prompt(instruction, new_system_prompt=DEFAULT_SYSTEM_PROMPT):
    system_prompt = B_SYS + new_system_prompt + E_SYS
    prompt_template = B_INST + system_prompt + instruction + E_INST
    return prompt_template


instruction = "Chat History:\n\n{chat_history} \n\nHuman: {user_input}\n\n Assistant:"
system_prompt = "You are a helpful assistant, you always only answer for the assistant then you stop. read the " \
                "chat history to get context "
template = get_prompt(instruction, system_prompt)

prompt = PromptTemplate(
    input_variables=["chat_history", "user_input"], template=template
)
memory = ConversationBufferMemory(memory_key="chat_history")

llm = TogetherLLM(
    model="togethercomputer/llama-2-70b-chat",
    temperature=0.1,
    max_tokens=512
)

llm_chain = LLMChain(
    llm=llm,
    prompt=prompt,
    verbose=True,
    memory=memory,
)


def chat_with_model(new_user_message):
    response = llm_chain.predict(user_input=new_user_message)
    print(f"AI Response: {response}")


if __name__ == '__main__':
    user_input = ''
    while True:
        user_message = input("Your input :  ")
        chat_with_model(user_message)
