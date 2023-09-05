# AryeeteyGPT Chatbot 🤖

An interactive chatbot powered by the Llama 2 AI model, brought to life using Streamlit. Dive in and have a conversation on any topic of interest!

## Features 🌟

- Built upon the Llama 2 AI model
- Context-aware conversations using a rolling window conversation buffer
- Interactive user interface using Streamlit
- Dynamic prompt templates to guide AI responses

## How to Use 🔧

1. Ensure you have all the required dependencies installed (refer to the **Dependencies** section below).
2. Clone the repository and navigate to the project folder.
3. Run the Streamlit app with:
```bash
streamlit run <filename.py>
```

## Dependencies 📚

Make sure to install the required libraries:
```bash
pip install langchain~=0.0.279
pip install streamlit~=1.26.0
pip install together~=0.1.7
```

## Structure 🏗️

- **Streamlit Interface**: Provides a dynamic interface to interact with the chatbot.
- **TogetherLLM**: Custom LLM class to interface with the Together API for model completions.
- **Utils**: Contains utility functions such as dynamic prompt generation, chat history management, and message display methods.

## Contribute 🤝

Feel free to raise issues, provide feedback, or contribute to the codebase. Your insights and contributions are welcome!

## License 📄

Please refer to the repository's license for usage rights and limitations.
