from datetime import datetime
from cli.utils import get_db

def create_order(args):
    conn = get_db()
    cursor = conn.cursor()

    now = datetime.now()
    order_date = now.date()
    order_time = now.time().strftime('%H:%M:%S')

    cursor.execute("""
        INSERT INTO orders (order_id, customer_id, employee_id, order_date, order_time, total_amount, order_status)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (args.order_id, args.customer_id, args.employee_id, order_date, order_time, 0.0, 'Pending'))

    total = 0
    for item_id, quantity in args.items:
        cursor.execute("SELECT price FROM menu_items WHERE item_id = ?", (item_id,))
        row = cursor.fetchone()
        if not row:
            print(f"Item {item_id} not found.")
            conn.rollback()
            return
        price = row[0]
        total += price * quantity

        cursor.execute("""
            INSERT INTO order_details (order_id, item_id, quantity, unit_price)
            VALUES (?, ?, ?, ?)
        """, (args.order_id, item_id, quantity, price))

    cursor.execute(
        "UPDATE orders SET total_amount = ?, order_status = 'Complete' WHERE order_id = ?",
        (total, args.order_id)
    )
    conn.commit()
    conn.close()
    print(f"Order {args.order_id} created successfully with total amount ${total:.2f}.")

def list_orders(_):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT order_id, order_date, order_time, total_amount, order_status FROM orders")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    conn.close()
