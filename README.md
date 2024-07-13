# Property-Investment-Advisor

This project is a Property Investment Advisor model built using Microsoft AutoGen, LangChain, and OpenAI's GPT-3.5-turbo model. The model leverages Retrieval-Augmented Generation (RAG) to provide comprehensive advice on property investments.

## Features
RAG Setup: Uses FAISS for vector storage and OpenAI embeddings to enable efficient document search.
AutoGen Agents: Configures agents for different roles such as Property Analyst and Financial Advisor to provide detailed and specialized advice.
Group Chat: Implements a group chat where the user can interact with different agents to get property investment advice.

## Prerequisites
Python 3.7 or higher

OpenAI API key

## Installation

- Clone the repository:

- Install the required packages:
pip install -r requirements.txt

- Set up your OpenAI API key:
OPENAI_API_KEY='your-api-key-here'

- Ensure you have your property investment data file ready at the specified path.

- Run the main script:
python main.py

- Interact with the model by typing your property investment questions. Type 'exit' to quit.

## Code Overview
- setup_rag():  Sets up the Retrieval-Augmented Generation by loading documents, splitting them, and creating embeddings.

- rag_query():  Queries the RAG setup to retrieve relevant documents.

- AutoGen Agent Configuration:  Configures different agents for specific roles.

- Group Chat Setup:  Sets up a group chat for interaction between the user and the agents.

- main():  The main function that initializes the RAG setup and handles user input for property investment questions.
