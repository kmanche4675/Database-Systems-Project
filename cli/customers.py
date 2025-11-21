import sqlite3
from cli.utils import get_db

def add_customer(args):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO customers (customer_id, first_name, last_name, phone_number, email, registration_date)
        VALUES (?, ?, ?, ?, ?, date('now))
    """, (args.id, args.first, args.last, args.phone, args.email))
    conn.commit()
    print(f"Customer {args.first} {args.last} added successfully.")

def list_customers(args):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM customers")
    customers = cursor.fetchall()
    for customer in customers:
        print(customer)