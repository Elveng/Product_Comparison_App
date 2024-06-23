# Product Comparison Application

A PyQt5-based desktop application that allows users to compare products from a MySQL database, manage a list of favorite products, and handle user authentication.

## Table of Contents
- [Introduction](#introduction)
- [Project Purpose](#project-purpose)
- [Problem Statement](#problem-statement)
- [Methodology](#methodology)
- [Features](#features)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)
- [Contact](#contact)

## Introduction
The Product Comparison Application is a PyQt5 desktop application that connects to a MySQL database to fetch, display, and manage a list of products. Users can compare products, add them to a favorites list, and handle user authentication for secure access.

## Project Purpose
This project was developed for a database lecture to demonstrate practical applications of database management and integration with a user interface. The main objectives include:
- Understanding database connectivity and operations using MySQL.
- Implementing a graphical user interface (GUI) with PyQt5 to interact with the database.
- Managing user authentication and authorization within the application.
- Performing CRUD (Create, Read, Update, Delete) operations on product data and user favorites.

## Problem Statement
In our fast-paced, consumer-driven world, the large quantity of available products often overwhelms consumers, making it difficult to make well-informed decisions. The lack of a convenient and comprehensive comparison tool can leave us feeling uncertain about our choices. This project aims to address this issue by providing a platform that allows you to access detailed product information and perform side-by-side comparisons.

**Why Did I Choose This Topic?**
I chose this topic because, in today's challenging economic climate, selecting products with the right price-performance balance is critical. I personally consider these factors before every purchase, and I know many others do the same. This project is a response to a pressing need in our current economic environment. I wanted to create a tool that would empower users to make informed decisions and, at the same time, assist businesses in effectively displaying their products.

## Methodology
**Technologies:**
- **Front-End Development:** PyQt5 is used to create a user-friendly desktop application.
- **Back-End Development:** Python is used for the back-end logic and database interactions.
- **Database Management:** MySQL is used to store and manage product information.

**How Technologies Are Used:**
- **PyQt5:** Used to design the user interface of the application. Users interact with the system through a natural, responsive, and visually pleasing graphical user interface.
- **Python:** Serves as the back-end scripting language, facilitating database interaction and business logic. It retrieves and presents product data to the front-end, handles user requests, and performs necessary data processing.

**Database Table Structure:**
- The database consists of tables designed to efficiently store product information. Each product has attributes such as ID, name, price, description, and image, which are organized into tables.

## Features
- **Product Comparison:** Compare two products side-by-side.
- **Favorite Management:** Add or remove products from the favorites list.
- **User Authentication:** Login and sign-up functionalities.
- **Database Interaction:** Connects to a MySQL database to fetch product information.

**User Capabilities:**
- **Search for Products:** Users can search for products by name, category, or price range.
- **View Specifications:** Access detailed product specifications to compare features and attributes.
- **Compare Different Items:** Select multiple products and compare them side-by-side to highlight differences and similarities.

### Code-Specific Details:
- The main UI elements are defined in `main_ui.py`, including text fields for username and password, buttons for login and sign-up, and a table to display products.
- The application logic, including database connection, product comparison, and favorite management, is implemented in `Project_main1.py`.
- The application connects to a MySQL database using the `mysql-connector-python` package.
- The database connection details, such as host, user, password, and database name, are specified in `Project_main1.py`.

## Contributing
We welcome contributions to improve this project. Please follow these steps to contribute:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Commit your changes (`git commit -am 'Add some feature'`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Create a new Pull Request.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements
This project was developed as part of a database lecture. Special thanks to the course instructors and peers for their support and feedback.

## Contact
For any inquiries, please contact:
- Name: Tahsin Berk ÖZTEKİN
- Email: tahsinberkoztekin@gmail.com
