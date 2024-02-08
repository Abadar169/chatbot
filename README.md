# SQL Query Generator Chatbot

This project introduces a chatbot designed to interpret natural language queries and translate them into SQL queries, allowing users to interact with databases without needing to know SQL syntax. Built with Python, leveraging OpenAI's GPT models through the LangChain library, and providing a user-friendly interface with Streamlit, this chatbot aims to make database interactions more accessible and intuitive.

## Features

- **Natural Language Processing**: Uses OpenAI's GPT models to understand and process natural language queries.
- **Dynamic SQL Query Generation**: Automatically generates SQL queries based on the user's natural language input.
- **Interactive Web Interface**: A Streamlit-based web interface that allows users to easily input questions and view the corresponding SQL queries and results.
- **Support for MySQL Database**: Configured to interact with MySQL databases, with potential to extend support to other database systems.
- **Secure Query Execution**: Implements basic security measures to prevent harmful queries from being executed.

## Installation

### Prerequisites

- Python 3.6+
- MySQL Database
- An OpenAI API key

### Setup

1. **Clone the repository**

    git clone https://github.com/<your-username>/sql-query-generator-chatbot.git
    cd sql-query-generator-chatbot


2. **Create and activate a virtual environment (optional)**

    python -m venv venv
    source venv/bin/activate # For Windows use .\venv\Scripts\activate


3. **Install dependencies**

    pip install -r requirements.txt


4. **Environment Configuration**

    Rename `.env.example` to `.env` and update it with your database credentials and OpenAI API key.

    cp .env.example .env

   
## Usage

To launch the chatbot interface, run: streamlit run app.py


Navigate to the URL provided in the output to start interacting with the chatbot through the web UI.

## Contributing

Contributions to enhance the chatbot's functionality, improve security, or extend database compatibility are welcome. To contribute:

1. Fork the project.
2. Create your feature branch (`git checkout -b feature/AmazingFeature`).
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`).
4. Push to the branch (`git push origin feature/AmazingFeature`).
5. Open a pull request.


## Acknowledgments

- Thanks to OpenAI for the GPT models, enabling advanced natural language processing capabilities.
- Gratitude to the developers of LangChain for facilitating the integration of language models with SQL databases.
- Appreciation for the Streamlit team for creating an intuitive way to build interactive web apps in Python.


