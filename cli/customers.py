from cli.utils import get_db

def add_customer(args):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO customers (customer_id, first_name, last_name, phone_number, email, registration_date) VALUES (?, ?, ?, ?, ?, DATE('now'))",
        (args.id, args.first, args.last, args.phone, args.email)
    )
    conn.commit()
    conn.close()
    print(f"Customer {args.first} {args.last} added successfully!")

def list_customers(_):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT customer_id, first_name, last_name, phone_number, email, registration_date FROM customers")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    conn.close()
