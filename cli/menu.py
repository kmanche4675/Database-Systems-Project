from cli.utils import get_db

def add_menu_item(args):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO menu_items (item_id, name, category, price, description, is_available)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (args.item_id, args.name, args.category, args.price, args.description, 1 if args.is_available else 0))
    conn.commit()
    print(f"Menu item {args.name} added.")

def list_menu_items(_):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT item_id, name, category, price, is_available FROM menu_items")
    for row in cursor.fetchall():
        print(row)