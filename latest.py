# latest.py

import os
from langchain.agents import create_sql_agent
from langchain.llms import OpenAI
from langchain.sql_database import SQLDatabase
from langchain.agents.agent_toolkits import SQLDatabaseToolkit
from langchain.chat_models import ChatOpenAI
import openai

# Set up OpenAI API key
openai.api_key = "sk-proj-qSRWqGrxyJbfp3L0PSq2T3BlbkFJmhUPTUwNDQlXFTswfgWx"

# Assuming your database file is named 'basic_examples.db' in the current directory
database_path = 'basic_examples.db'

# Create an instance of SQLDatabase
db = SQLDatabase.from_uri(f'sqlite:///{database_path}')

# Create an instance of ChatOpenAI
llm = ChatOpenAI(model_name="gpt-4", openai_api_key=openai.api_key)

# Create an instance of SQLDatabaseToolkit by combining the SQL database instance (db) and the language model (llm)
toolkit = SQLDatabaseToolkit(db=db, llm=llm)

# Create an agent executor
agent_executor = create_sql_agent(
    llm=llm,
    toolkit=toolkit,
    verbose=True
)

def execute_query(query):
    return agent_executor.run(query)
