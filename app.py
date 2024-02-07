import streamlit as st
from langchain_community.llms import OpenAI
from langchain_community.utilities import SQLDatabase
from langchain_experimental.sql import SQLDatabaseChain
from dotenv import load_dotenv, find_dotenv
import os

_ = load_dotenv(find_dotenv())  # read local env file for the secrets
openai_key = os.getenv('OPENAI_KEY')
db_user = os.getenv('DB_USER')
db_password = os.getenv('DB_PASSWORD')
database = os.getenv('DATABASE')

db = SQLDatabase.from_uri(
    f"mysql+pymysql://{db_user}:{db_password}@localhost:3306/{database}",
)

llm = OpenAI(temperature=0, openai_api_key=openai_key)

QUERY = """
Given: "{question}"
Generate a SELECT SQL query to fetch data without altering the database. 
Format:
- SQLQuery: The query
- SQLResult: Query result
- Answer: Summary of the result
"""


# set up the llm chain
db_chain = SQLDatabaseChain(llm=llm, database=db, verbose=True)




def execute_chain_streamlit():
    user_question = st.text_input("Enter your question:", "")

    if st.button('Send'):
        if user_question:
            try:
                question = QUERY.format(question=user_question)
                response = db_chain.run(question)
                
                # Directly display the response as it is a descriptive text
                st.write(response)
                
            except Exception as e:
                st.error(f"Error: {e}")

if __name__ == "__main__":
    st.title("SQL Query Generator Chatbot")
    execute_chain_streamlit()