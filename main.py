import argparse
from cli import customers
from cli import orders
from cli import menu

parser = argparse.ArgumentParser(description="BurgerPlus CLI")

subparsers = parser.add_subparsers(title="Commands")

# Add customer
add_cust = subparsers.add_parser("add_customer")
add_cust.add_argument("--id", type=int, required=True)
add_cust.add_argument("--first", type=str, required=True)
add_cust.add_argument("--last", type=str, required=True)
add_cust.add_argument("--phone", type=str, required=True)
add_cust.add_argument("--email", type=str, required=True)
add_cust.set_defaults(func=customers.add_customer)

# Orders
add_order = subparsers.add_parser("create_order")
add_order.add_argument("--order_id", type=int, required=True)
add_order.add_argument("--customer_id", type=int, required=True)
add_order.add_argument("--employee_id", type=int, required=True)
add_order.add_argument("--item", dest="items", nargs=2, type=int, metavar=("item_id", "qty"), action="append", required=True, help="Add an item to the order as a pair: item_id qty. Repeat --item for multiple line items.")
add_order.set_defaults(func=orders.list_orders)

# Menu items
add_menu = subparsers.add_parser("add_menu_item")
add_menu.add_argument("--item_id", type=int, required=True)
add_menu.add_argument("--name", required=True)
add_menu.add_argument("--category", choices=["Burger", "Side", "Drink", "Dessert"] , required=True)
add_menu.add_argument("--price", type=float, required=True)
add_menu.add_argument("--description", default="")
add_menu.add_argument("--is_available", action="store_true")
add_menu.set_defaults(func=menu.add_menu_item)

# List customers
list_cust = subparsers.add_parser("list_customers")
list_cust.set_defaults(func=customers.list_customers)

# List menu items
list_menu = subparsers.add_parser("list_menu_items")
list_menu.set_defaults(func=menu.list_menu_items)

args = parser.parse_args()
args.func(args)