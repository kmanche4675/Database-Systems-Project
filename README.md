# Burger Plus -- Database Management Project

This project implements a simple relational database system for a fast food restaurant called **Burger Plus**. It includes schema creation, synthetic data generation, advanced test queries, and a command-line interface (CLI) to manage operations.

---

## Setup Instructions 

The following steps are required to initialize the database and application environment using **SQLite** and **Python 3**.

### Clone the Repo
```bash
git clone https://github.com/kmanche4675/Database-Systems-Project.git
```
```bash
cd database-systems-project
```
2. **Install Requirements**
    - Only the built-in sqlite3 and argparse modules are used. No external libraries required.

3. **Create the Database**
```bash
./sqlite3 db/burgerplus.db < db/schema.sql
```

4. **Load Sample Data**
```bash
python seed/seed_data.py
```

## Usage: CLI Commands
Run any of the following from the root:
1. **Add a Menu Item**
```bash
python main.py add_menu_item --item_id 10 --name "Spicy Burger" --category Burger --price 10.99 --description "Hot and Juicy" --available
```
2. **List All Menu Items**
```bash
python main.py list_menu_items
```
3. **Add a Customer**
```bash
python main.py add_customer --id 1 --first John --last Doe --phone 1234567890 --email john@example.com
```
4. **Create an Order**
```bash
python main.py create_order --order_id 1001 --customer_id 1 --employee_id 1 --items 1 2 2 1
```
5. **List Orders**
```bash
python main.py list_orders
```
6. **Testing**
```bash
sqlite3 db/burgerplus.db < test_queries.sql
```
### Team Members
|      Name       |                            Responsibility                             |
|-----------------|-----------------------------------------------------------------------|
| Austin McBurney | Wrote CLI code, readme,  organized repository, testing & instructions |
|-----------------|-----------------------------------------------------------------------|
|    Kendrick                                                                             |
|   Manchester    | Managed team dynamics ensuring effective colaboration                 |
|-----------------|-----------------------------------------------------------------------|
|   Dennis Garay  |  Wrote the descriptive content for the relational schema and the data |    |                 |  population process                                                   |    
|-----------------|-----------------------------------------------------------------------|
|   Jakobe Allen  |  Created E-R Diagram for the database. Defninng entities, attriubtes, |    |                 |                                                                       |
|-----------------|-----------------------------------------------------------------------|
|   Dillon Davis  |  Wrote up report specificiations for entire project                   |   
|-----------------|-----------------------------------------------------------------------|
