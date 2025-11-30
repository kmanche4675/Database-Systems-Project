from cli.utils import get_db

def add_menu_item(args):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO menu_items (item_id, name, category, price, description, is_available) VALUES (?, ?, ?, ?, ?, ?)",
        (args.item_id, args.name, args.category, args.price, args.description, int(args.is_available))
    )
    conn.commit()
    conn.close()
    print(f"Menu item {args.name} added successfully!")

def list_menu_items(_):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT item_id, name, category, price, description, is_available FROM menu_items")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    conn.close()
