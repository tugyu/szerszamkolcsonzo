# Tool Lending Webserver

## Introduction

This project is a demonstration of a simple tool lending webserver built with Python, Flask, and SQLite. It was created as a learning exercise with the help of OpenAI's ChatGPT (specifically the o1-mini model). NO MANUAL CODING has been used!!! Using the tool itself, the initial database has been extended with fake names and addresses and additional tools. While the project contains some elements specific to the Hungarian language, AI translation tools can be used to understand and adapt the code.

## Project Goal

The main goal of this project was to explore the capabilities of readily available tools and libraries for web development in Python. It simulates a tool lending service with basic functionalities like adding tools, lending them out to customers, and tracking their return dates.

## Development Process

The project was developed through a series of prompts to ChatGPT o1-mini, gradually adding features and addressing issues. Here's a summary of the prompts and the challenges they presented:

1. **Basic Setup:** Setting up the project with Flask, SQLite, and Jinja, and implementing core functionalities like adding tools, customers, and loans.
2. **Search and Filtering:** Adding search and filter options to the customers page and sorting functionality to the loans page.
3. **Pagination and Modals:** Implementing pagination for the customers and loans pages, and adding modal windows to display customer details when clicking on their names in the loans page.
4. **Debugging:** Troubleshooting a 500 error on the loans page and understanding the debugging information provided by Flask.
5. **Further Debugging:** Addressing a deprecation warning related to date handling and fixing an issue with the modal window not displaying customer details.
6. **JavaScript Issue:** Resolving a JavaScript error related to the jQuery library and ensuring the modal window displays data correctly.

## Features

* **Tool Management:** Add, edit, and delete tools.
* **Customer Management:** Add, edit, and delete customers.
* **Loan Management:** Lend out tools to customers, track loan dates, and mark returns.
* **Search and Filter:** Search and filter customers by name and address.
* **Sorting:** Sort loans by due date.
* **Pagination:** Paginate lists of customers and loans for better readability.
* **Modal Windows:** Display customer details in a modal window when clicking on their names in the loans page.

## Technologies Used

* Python
* Flask
* SQLite
* Jinja
* HTML
* CSS
* JavaScript
* DB Browser for SQLite - utility to check, modify database


## Installation

1. Clone the repository: `git clone https://github.com/tugyu/szerszamkolcsonzo.git`
2. Create a virtual environment: `python -m venv venv`
3. Activate the virtual environment: `source venv/bin/activate` (Linux/macOS) or `venv\Scripts\activate` (Windows)
4. Install the dependencies: `pip install -r requirements.txt`
5. Run once `python init_db.py`
6. Run the application: `python app.py`

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

## License

[Choose a license and add it here, e.g., MIT License]