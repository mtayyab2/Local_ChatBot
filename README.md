# Local_ChatBot
A Chatbot application that uses open-source LLMs for chatting that can be used for General Chat, Code Generation, and all other use cases of Chatbots like ChatGPT.

Following Video shows the working of the chatbot. The response is very fast on a local PC with 16gb DDR4 Ram and an RTX 3060m with Microsoft [Phi3](https://huggingface.co/microsoft/Phi-3-mini-128k-instruct) model.

https://github.com/mtayyab2/Local_ChatBot/assets/100469515/06243bcc-9c8b-4335-933a-37363333a54d


## Prerequisites
### This repo assumes that you already have [Ollama](https://ollama.com/) and [Phi3](https://ollama.com/library/phi3) model installed.

To get started with this project:
1. Have Python installed on your machine (version 3.6 or above).
2. Install the necessary packages by running:
   ```bash
   pip install streamlit ollama
   ```

## Setup Instructions

Follow these steps to set up and run the chatbot locally:

### Clone Repository

Clone this repository to your local machine. 
```bash
git clone https://github.com/mtayyab2/Local_ChatBot/
```
Then navigate into the project directory:
```bash
cd Local_ChatBot
```
Execute the following command to start the Chatbot:

```bash
streamlit run local_chat.py
```

## Features Overview

Our chatbot provides various features for an engaging user experience, including:

- **Selecting Models**: Choose from multiple pre-trained OLLAMA models to customize the conversation's tone and
style.
- **Chat History**: View past conversations with options to edit or delete entries.
- **Saving Chats**: Save individual chat sessions for future reference, allowing users to revisit their
interactions.
- **New Chat**: Initiate fresh conversations with the selected model and save the conversation if desired.

## Contributing
Feel free to contribute to this repository by forking and by a pull request.

## For any issues, suggestions, or feature requests, please open an issue in the repository.
