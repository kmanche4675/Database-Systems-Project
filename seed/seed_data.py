import sqlite3
import os

# Define the database path relative to the script's root
# Assumes this script is run from the project root (Database-Systems-Project)
DB_PATH = os.path.join('db', 'burgerplus.db')

def populate_database():
    """Connects to the database and inserts synthetic data into all tables."""
    print("--- Connecting to Database and Inserting Data ---")
    
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        
        # SQLITE Tweak: Temporarily disable foreign key checks for bulk inserts
        cursor.execute("PRAGMA foreign_keys = OFF;") 

        # 1. EMPLOYEES (Required for creating orders)
        employees_data = [
            (1255, 'Alice', 'Smith', 'alice@burgerplus.com', '555-1001', '2023-08-15', 'Manager', 65000.00),
            (6292, 'Bob', 'Jones', 'bob@burgerplus.com', '555-1002', '2024-01-20', 'Cashier', 35000.00),
            (5433, 'Charlie', 'Brown', 'charlie@burgerplus.com', '555-1003', '2024-05-10', 'Cook', 40000.00)
        ]
        cursor.executemany("""
            INSERT INTO employees (employee_id, first_name, last_name, email, phone_number, hire_date, job_role, salary) 
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, employees_data)

        # 2. CUSTOMERS (Required for testing customer orders)
        customers_data = [
            (1, 'John', 'Doe', '1234567890', 'john@example.com', '2024-10-24'),
            (2, 'Eve', 'Martinez', '555-2002', 'eve@example.com', '2024-11-14'),
            (3, 'Frank', 'Harris', '555-2003', 'frank@example.com', '2024-11-19')
        ]
        cursor.executemany("""
            INSERT INTO customers (customer_id, first_name, last_name, phone_number, email, registration_date) 
            VALUES (?, ?, ?, ?, ?, ?)
        """, customers_data)
        
        # 3. MENU_ITEMS (Required for orders)
        menu_items_data = [
            (10, 'Spicy Burger', 'Burger', 10.99, 'Hot and Juicy', 1),
            (1, 'Classic Cheeseburger', 'Burger', 8.99, 'Beef patty with cheddar.', 1),
            (2, 'Veggie Delight', 'Burger', 9.99, 'Black bean patty.', 1),
            (3, 'Fries (Large)', 'Side', 3.50, 'Crispy large-cut fries.', 1),
            (4, 'Cola (Medium)', 'Drink', 2.00, 'Fountain dispensed cola.', 1)
        ]
        cursor.executemany("""
            INSERT INTO menu_items (item_id, name, category, price, description, is_available) 
            VALUES (?, ?, ?, ?, ?, ?)
        """, menu_items_data)

        # 4. INVENTORY
        inventory_data = [
            (201, 'Beef Patties', 'unit', 500, 100),
            (202, 'Buns (Sesame)', 'unit', 300, 50),
            (203, 'Lettuce', 'kg', 10, 3),
            (204, 'Spicy Sauce', 'liter', 20, 5)
        ]
        cursor.executemany("""
            INSERT INTO inventory (inventory_id, ingredient_name, unit_of_measure, current_stock, reorder_point) 
            VALUES (?, ?, ?, ?, ?)
        """, inventory_data)
        
        # 5. ORDERS 
        orders_data = [
    # Order 1000: Handled by Bob (6292)
    (1000, 2, 6292, '2024-11-23', '09:30:00', 18.99, 'Complete'), 
    # Order 1001: Handled by Alice (1255)
    (1001, 1, 1255, '2024-11-23', '12:00:00', 39.96, 'Pending'), 
    # Order 1002: Handled by Bob (6292)
    (1002, None, 6292, '2024-11-23', '13:15:00', 15.49, 'Complete') 
    ]
        cursor.executemany("""
            INSERT INTO orders (order_id, customer_id, employee_id, order_date, order_time, total_amount, order_status) 
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, orders_data)

        # 6. ORDER_DETAILS
        order_details_data = [
            # Details for Order 1000 (1x 8.99 + 2x 3.50 = 15.99)
            (1000, 1, 1, 8.99), 
            (1000, 3, 2, 3.50), 
            # Details for Order 1001 (1x 10.99 + 2x 9.99 + 1x 8.99 = 39.96)
            (1001, 10, 1, 10.99), 
            (1001, 2, 2, 9.99),   
            (1001, 1, 1, 8.99),   
            # Details for Order 1002 (1x 9.99 + 1x 2.00 + 1x 3.50 = 15.49)
            (1002, 2, 1, 9.99), 
            (1002, 4, 1, 2.00), 
            (1002, 3, 1, 3.50) 
        ]
        cursor.executemany("""
            INSERT INTO order_details (order_id, item_id, quantity, unit_price) 
            VALUES (?, ?, ?, ?)
        """, order_details_data)

        # Commit changes and enable foreign keys again
        conn.commit()
        cursor.execute("PRAGMA foreign_keys = ON;") 
        conn.close()
        
        print("Successfully populated all tables with synthetic data.")

    except sqlite3.IntegrityError as e:
        print(f"ERROR: Integrity constraint failed. Data not inserted. Details: {e}")
    except sqlite3.OperationalError as e:
        print(f"ERROR: Operational error (Table missing? Run schema first). Details: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == '__main__':
    populate_database()