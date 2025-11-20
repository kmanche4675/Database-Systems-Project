CREATE TABLE employees (
 employee_id INT PRIMARY KEY,
 first_name VARCHAR(50) NOT NULL,
 last_name VARCHAR(50) NOT NULL,
 email VARCHAR(100) UNIQUE,
 hire_date DATE NOT NULL,
 job_role VARCHAR(50) NOT NULL,
 salary DECIMAL(10, 2)
);

CREATE TABLE ORDERS(
    order_id INT PRIMARY KEY,
    customer_id INT, -- FK to customers. NULL if the order is a walk-in/anonymous customer
    employee_id INT NOT NULL, -- FK to employees (who took the order)
    order_date DATE NOT NULL,
    order_time TIME NOT NULL,
    total_amount DECIMAL(10, 2) NOT NULL CHECK (total_amount >= 0),
    order_status VARCHAR(20) NOT NULL, -- e.g., 'Pending', 'Complete', 'Cancelled'

    FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
    FOREIGN KEY (employee_id) REFERENCES employees(employee_id)
);

CREATE TABLE ORDER_DETAILS(
    order_id INT NOT NULL,
    item_id INT NOT NULL,
    quantity INT NOT NULL CHECK (quantity > 0), -- Must order at least 1 item
    unit_price DECIMAL(5, 2) NOT NULL, -- Price at the time of sale (for historical data)
    
    PRIMARY KEY (order_id, item_id), -- Composite PK
    
    FOREIGN KEY (order_id) REFERENCES orders(order_id),
    FOREIGN KEY (item_id) REFERENCES menu_items(item_id)
);

CREATE TABLE INVENTORY(
    inventory_id INT PRIMARY KEY,
    ingredient_name VARCHAR(100) NOT NULL UNIQUE,
    unit_of_measure VARCHAR(10) NOT NULL, -- e.g., 'kg', 'lb', 'item'
    current_stock INT NOT NULL CHECK (current_stock >= 0), -- Cannot be negative
    reorder_point INT NOT NULL
);

CREATE TABLE MENU_ITEMS(
        item_id INT PRIMARY KEY,
    name VARCHAR(100) NOT NULL UNIQUE, -- Item name must be unique
    category VARCHAR(50) NOT NULL,     -- e.g., 'Burger', 'Side', 'Drink'
    price DECIMAL(5, 2) NOT NULL CHECK (price >= 0), -- Price must be non-negative
    description VARCHAR(255),
    is_available BOOLEAN DEFAULT TRUE
);

CREATE TABLE CUSTOMERS(
        customer_id INT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    phone_number VARCHAR(15) UNIQUE, -- Useful for quickly identifying customers
    email VARCHAR(100),
    registration_date DATE
);


