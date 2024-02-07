# from langchain import OpenAI, SQLDatabase, SQLDatabaseChain
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

def execute_chain():
    print("Type 'exit' to quit")
    while True:
        feed = input("Enter your question: ")
        if feed.lower() == 'exit':
            break
        else:
            try:
                # Directly inject the question into the QUERY template
                question = QUERY.format(question=feed)
                response = db_chain.run(question)
                
                # Assuming direct validation of the AI-generated SQL query
                # This part needs careful handling based on the actual format of `response`
                # Here's a simplified, hypothetical validation assuming `response` includes the SQL query text
                if "select" not in response.lower().split("sqlquery:")[1].strip().split()[0].lower():
                    raise ValueError("Generated query is not a SELECT query. Operation not allowed.")
                
                print(response)
            except Exception as e:
                print(f"Error: {e}")

# Execute the optimized chain
execute_chain()



# def validate_query(sql_query):
#     """
#     Checks if the given SQL query is a SELECT query. This function assumes that
#     the SQL query string is already formatted correctly by the AI.
#     """
#     # Convert the query to lower case and strip leading/trailing whitespace for simpler checking
#     query_lower = sql_query.strip().lower()

#     # Check if query starts with 'select'
#     if not query_lower.startswith('select'):
#         raise ValueError("Only SELECT queries are allowed. UPDATE and DELETE operations are restricted.")

# def execute_chain():
#     print("Type 'exit' to quit")

#     while True:
#         feed = input("Enter your question: ")

#         if feed.lower() == 'exit':
#             print('Exiting...')
#             break
#         else:
#             try:
#                 question = QUERY.format(question=feed)
#                 response = db_chain.run(question)
                
#                 # Extract the SQLQuery part from the response for validation
#                 # Assuming the response format is a string that includes "SQLQuery: <query>"
#                 # This extraction method may need adjustment based on the actual response format
#                 sql_query = response.split("SQLQuery: ")[1].split("\n")[0]  # Simplified extraction logic
                
#                 # Validate the extracted SQL query
#                 validate_query(sql_query)
                
#                 # If the query passes validation, you can then proceed to display the response
#                 # or execute the query against the database as needed
#                 print(response)
                
#             except Exception as e:
#                 print(e)


# def execute_chain():
#     print("Type 'exit' to quit")

#     while True:
#         feed = input("Enter your question: ")

#         if feed.lower() == 'exit':
#             print('Exiting...')
#             break
#         else:
#             try:
#                 question = QUERY.format(question=feed)
#                 print(db_chain.run(question))
#             except Exception as e:
#                 print(e)

# execute the chain
execute_chain()