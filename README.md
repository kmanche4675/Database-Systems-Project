# Burger Plus -- Database Management Project

This project implements a simple relational database system for a fast food restaurant called **Burger Plus**. It includes schema creation, synthetic data generation, advanced test queries, and a command-line interface (CLI) to manage operations.

---

## Setup Instructions 

The following steps are required to initialize the database and application environment using **SQLite** and **Python 3**.
Ensure SQLite is installed and accessible from your PATH, or place sqlite3.exe in the project root.

### Clone the Repo
```bash
git clone https://github.com/kmanche4675/Database-Systems-Project.git
```
```bash
cd database-systems-project
```
2. **Install Requirements**
    - Only the built-in sqlite3 and argparse modules are used. No external libraries required.

3. **Create and Populate the Database**
    1. DELETE previous database file to ensure a clean start (CRITICAL)
    ```bash
    rm -f db/burgerplus.db
    ```
    2. CREATE the new schema
    ```bash
    sqlite3 db/burgerplus.db < db/schema.sql
     ```
    3. LOAD the synthetic data (Uses Python script)
    ```bash
    python seed/seed_data.py
    ```

## Usage: CLI Commands
Run any of the following from the Root Directory:
1. **Add a Menu Item**
    * Creates a new item for the menu
```bash
python main.py add_menu_item --item_id 999 --name "Spicy Burger" --category Burger --price 10.99 --description "Hot and Juicy"
```
***Parameter Instructions***
|  Parameter   |                        Description                       |
|--------------|----------------------------------------------------------|
|--item_id     |               Unique integer ID for the item             |
|--name        |              Name of the menu item (Unique)              |
|--category    |           Choices: Burger, Side, Drink, Dessert          |
|--price       |                   Price as a decimal                     |
|--description |                Optional text description                 |
|--available   |  Add this flag to mark the item as available/unavailable |

2. **List All Menu Items**
    * Display all menu items currently in the database
```bash
python main.py list_menu_items
```
3. **Add a Customer**
    * Register a new customer to the system
```bash
python main.py add_customer --id 1 --first John --last Doe --phone 1234567890 --email john@example.com
```
***Parameter Instructions***
| Parameter |             Description            |
|-----------|------------------------------------|
|  --id     | Unique integer ID for the customer |
|  --first  |             First Name             |
|  --last   |             Last Name              |
|  --phone  |            Phone Number            |
|  --email  |            Email Address           |

4. **Create an Order**
    * Creates a new order with one or more items (the items are passed in as pairs)
```bash
python main.py create_order --order_id 1001 --customer_id 1 --employee_id 1255 --item 1 1 --item 2 2
```
***Parameter Instructions***
|  Parameter   |                         Description                        |
|--------------|------------------------------------------------------------|
|--order_id    |               Unique integer ID for the order              |
|--customer_id |                     ID of the customer                     |
|--employee_id |           ID of the employee who took the order            |
|--items       | One or more pairs of item_id quantity: (item_id, quantity) |

5. **List Customers**
    * Display registered customers
```bash
python main.py list_customers
```

7. **Testing**
```bash
sqlite3 db/burgerplus.db < test_queries.sql
```
### Team Members
|      Name           |                                     Responsibility                                      |
|---------------------|-----------------------------------------------------------------------------------------|
|   Austin McBurney   |          Wrote CLI code, readme,  organized repository, testing & instructions          |
| Kendrick Manchester |          Managed team dynamics ensuring effective colaboration                          |
|    Dennis Garay     | Wrote the descriptive content for the relational schema and the data population process |
|    Jakobe Allen     |          Created E-R Diagram for the database. Defined entities & attributes            |
|     Dillon Davis    |            Wrote up report specificiations for entire project                           |
