
![Logo](https://static.wixstatic.com/media/b2dfda_1c51fe6397954d13a39841c7f66f4a7d~mv2.png/v1/fill/w_480,h_300,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/b2dfda_1c51fe6397954d13a39841c7f66f4a7d~mv2.png)


<div align="center" ><a href="https://git.io/typing-svg"><img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=30&pause=1000&color=93ACF7&width=435&lines=FlaskDataMateX" alt="Typing SVG" /></a></div>

## <img src="https://user-images.githubusercontent.com/74038190/216122003-1c7d9078-357a-47f5-81c7-1c4f2552e143.png" style="width: 50px; height: 50px;" alt=""> Introduction

FlaskDataMateX is a Python Flask-based web application designed to manage customers, items, and transactions. This project provides RESTful endpoints for performing CRUD operations on customers, items, and transactions.

## <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Travel%20and%20places/High%20Voltage.png" style="width: 50px; height: 50px;" alt=""> Features

- Manage Customers: Add, update, and delete customer records.
- Manage Items: Add, update, and delete item details.
- Manage Transactions: Record and modify transactions between customers and items.
- Simple, modular structure using Flask Blueprints for better scalability and code organization.
- MySQL database integration for data persistence.


## <img src="https://user-images.githubusercontent.com/74038190/216122028-c05b52fb-983e-4ee8-8811-6f30cd9ea5d5.png" style="width: 50px; height: 50px;" alt=""> Project Structure

- **app.py**: The main entry point for the application. Registers all blueprints (customers, items, transactions) and handles CORS configuration.
- **customers.py**: Defines routes and logic for managing customer-related operations.
- **items.py**: Contains endpoints for managing item details.
- **transactions.py**: Handles transaction operations like adding, updating, and deleting transaction records.
- **config.py**: Manages the database connection configuration.

## <img src="https://user-images.githubusercontent.com/74038190/216122041-518ac897-8d92-4c6b-9b3f-ca01dcaf38ee.png" style="width: 50px; height: 50px;" alt=""> Prerequisites

Before running the FlaskDataMateX project, ensure you have the following installed on your system:

1. **Python 3.x**: FlaskDataMateX requires Python 3 or higher.
   - You can download Python from the official website: [https://www.python.org/downloads/](https://www.python.org/downloads/)

2. **MySQL**: The application uses MySQL as the database. Ensure that MySQL is installed and running.
   

3. **Pip**: Make sure `pip` is installed to manage Python packages.
   - If pip is not installed, you can install it using:
     ```bash
     python -m ensurepip --upgrade
     ```

4. **MySQL Connector**: The application uses MySQL Connector to connect to the database.
   - Install the MySQL Connector with the following command:
     ```bash
     pip install mysql-connector-python
     ```

5. **Flask**: Flask is required to run the web application.
   - You can install Flask using pip:
     ```bash
     pip install Flask
     ```

6. **Flask-CORS**: Flask-CORS is needed to handle Cross-Origin Resource Sharing (CORS) for frontend-backend communication.
   - Install Flask-CORS using pip:
     ```bash
     pip install Flask-CORS
     ```

7. **MySQL Database Setup**: Ensure you have a MySQL database set up and running, with a database named `FlaskDataMateX` as required by the app.
   - You can create the database using the following SQL command:
     ```sql
     CREATE DATABASE FlaskDataMateX;
     ```

Once you have these prerequisites installed and configured, you're ready to proceed with setting up and running FlaskDataMateX.


## <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Objects/Keyboard.png" style="width: 50px; height: 50px;" alt=""> Clone the repository:


```bash
  git clone https://github.com/sasmithx/FlaskDataMateX.git
```


## <img src="https://user-images.githubusercontent.com/74038190/216122069-5b8169d7-1d8e-4a13-b245-a8e4176c99f8.png" style="width: 50px; height: 50px;" alt=""> License

This project is licensed under the MIT License - see the [MIT License](LICENSE) file for details.

<div align="center" style="display: flex; align-items: flex-start;">
    <img src="https://techstack-generator.vercel.app/python-icon.svg" alt="icon" width="65" height="65" />
    <img src="https://techstack-generator.vercel.app/mysql-icon.svg" alt="icon" width="65" height="65" />
    <img src="https://techstack-generator.vercel.app/restapi-icon.svg" alt="icon" width="65" height="65" />
</div>

<p align="center">
  &copy; 2024 Sasmith Manawadu
</p>
