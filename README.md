# Tool Lending Webserver

## Introduction

This project is a demonstration of a simple tool lending webserver built with Python, Flask, and SQLite. It was created as a learning exercise with the help of OpenAI's ChatGPT (specifically the o1-mini model). NO MANUAL CODING has been used!!! Using the tool itself, the initial database has been extended with fake names and addresses and additional tools. While the project contains some elements specific to the Hungarian language, AI translation tools can be used to understand and adapt the code.

## Project Goal

This application is not intended for production use and should not be relied upon for managing real-world tool lending scenarios.

The main goal of this project was to explore the capabilities of readily available tools and libraries for web development in Python. It simulates a tool lending service with basic functionalities like adding tools, lending them out to customers, and tracking their return dates.

This code is for demonstration purposes only. It does not handle user permissions or concurrency. Issues could arise if multiple users interact with the application simultaneously. For example:
* **Overlapping tool assignments:**  Multiple users could potentially "borrow" the last available tool, leading to inconsistencies in the inventory.
* **Inventory discrepancies:** The inventory display may not update in real-time to reflect changes made by other users, potentially showing incorrect availability.

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

MIT License

Hungarian description, not translated from the English part

# Szerszámkölcsönző - Demo Verzió

## Leírás

A **Szerszámkölcsönző** egy egyszerű webalkalmazás, amely lehetővé teszi a szerszámok kölcsönzését és kezelését. Ez a projekt egy demó eszköz, amelyet egyetlen felhasználó számára terveztem felhasználói élmény bemutatására. Az alkalmazás néhány funkciót egyszerűsít, hogy könnyen érthető és kezelhető legyen.

## Funkciók

- **Szerszámok Megtekintése**: Lista a rendelkezésre álló szerszámokról és azok mennyiségéről.
- **Személyek Kezelése**: Személyek hozzáadása és keresése név vagy cím alapján.
- **Kölcsönzések Nyilvántartása**: Szerszámok kölcsönzése és visszahozatala, valamint a kölcsönzési adatok megtekintése.
- **Paginálás**: Adatok oldalakra bontása a jobb kezelhetőség érdekében.
- **Modal Ablakok**: Részletes személyi adatok megjelenítése felugró ablakban.

## Telepítési Útmutató

### Előfeltételek

- Python 3.12 vagy újabb
- Pip csomagkezelő

### Lépések

1. **Klónozd a repót:**
    ```bash
    git clone https://github.com/felhasznalonev/szerszamkolcsonzo.git
    cd szerszamkolcsonzo
    ```

2. **Hozz létre virtuális környezetet és aktiváld:**
    ```bash
    python -m venv venv
    # Windows
    venv\Scripts\activate
    # macOS/Linux
    source venv/bin/activate
    ```

3. **Telepítsd a függőségeket:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Inicializáld az adatbázist:**
    ```bash
    python init_db.py
    ```

5. **Futtasd az alkalmazást:**
    ```bash
    python app.py
    ```

6. **Nyisd meg a böngészőt és navigálj a következő címre:**
    ```
    http://127.0.0.1:5000/
    ```

## Használati Útmutató

### Szerszámok

- Az alkalmazás főoldalán megtekintheted a rendelkezésre álló szerszámokat és azok mennyiségét.
- Szerszámot hozzáadhatsz a "Szerszám Hozzáadása" gombra kattintva.

### Személyek

- A "Személyek" oldalon kereshetsz név vagy cím alapján.
- Új személyt adhatsz hozzá a "Új Személy Hozzáadása" gombra kattintva.

### Kölcsönzések

- A "Kölcsönzések" oldalon megtekintheted az aktuális kölcsönzéseket.
- Szerszámot kölcsönözhetsz a "Kölcsönzés" gombra kattintva.
- Kölcsönzött szerszámot visszahozhatsz a "Visszahozva" gombra kattintva.
- Személy részleteit megtekintheted a nevek linkjére kattintva, ami felugró ablakban jeleníti meg az adatokat.

## Technológiák

- **Backend**: Flask (Python)
- **Adatbázis**: SQLite (Fejlesztéshez), PostgreSQL (Többfelhasználós környezethez ajánlott)
- **Frontend**: Bootstrap, jQuery
- **Deployment**: Gunicorn (Termelési szerverhez)

## Fejlesztési Állapot

Ez az alkalmazás egy demó verzió, amelyet egyetlen felhasználó számára terveztem. Néhány funkció egyszerűsítve van a könnyebb használhatóság érdekében. A jövőbeni fejlesztések között szerepel a többfelhasználós támogatás, biztonsági intézkedések, és egy robusztusabb adatbázis-rendszer bevezetése.

## Konfigurációk

- **DATABASE_URI**: Az adatbázis kapcsolati URI-ja a `app.py` fájlban konfigurálható.
- **WSGI Server**: A termelési környezetben Gunicorn vagy más WSGI szerver használata ajánlott.

## Hozzájárulás

Ez egy demó projekt, ha szeretnéd, fejleszd tovább!

## Licenc

Ez a projekt MIT licenc szerint használható.
