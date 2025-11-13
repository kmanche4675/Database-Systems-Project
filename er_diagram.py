# ER Diagram Generator for Restaurant Database

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch
import matplotlib.lines as mlines

fig, ax = plt.subplots(figsize=(22, 16))
ax.set_xlim(0, 100)
ax.set_ylim(0, 100)
ax.axis('off')

entity_color = '#E8F4F8'
weak_entity_color = '#FFF4E6'
relationship_color = '#E8F5E9'

def draw_entity(ax, x, y, width, height, name, attributes, pk, is_weak=False):
    linewidth = 3 if is_weak else 2
    
    entity = FancyBboxPatch((x, y), width, height,
                           boxstyle="round,pad=0.1",
                           edgecolor='black',
                           facecolor=weak_entity_color if is_weak else entity_color,
                           linewidth=linewidth)
    ax.add_patch(entity)
    
    ax.text(x + width/2, y + height - 2, name,
            ha='center', va='top', fontsize=13, fontweight='bold')
    
    y_offset = y + height - 6
    for attr in attributes:
        is_pk = attr in pk
        is_fk = 'FK:' in attr
        
        if is_pk:
            attr_text = f"[PK] {attr}"
            style = 'italic'
            weight = 'bold'
        elif is_fk:
            attr_text = attr
            style = 'normal'
            weight = 'normal'
        else:
            attr_text = f"     {attr}"
            style = 'normal'
            weight = 'normal'
        
        ax.text(x + 2, y_offset, attr_text,
                ha='left', va='top', fontsize=9,
                fontstyle=style, fontweight=weight)
        y_offset -= 2.5

def draw_relationship(ax, x, y, size, name):
    points = [(x, y + size), (x + size, y), (x, y - size), (x - size, y)]
    diamond = mpatches.Polygon(points, closed=True,
                              edgecolor='black',
                              facecolor=relationship_color,
                              linewidth=2)
    ax.add_patch(diamond)
    
    ax.text(x, y, name, ha='center', va='center',
            fontsize=11, fontweight='bold')

def draw_connection(ax, x1, y1, x2, y2, card1, card2, participation1='partial', participation2='partial'):
    line = mlines.Line2D([x1, x2], [y1, y2],
                        color='black', linewidth=2.5)
    ax.add_line(line)
    
    offset = 4
    if x1 < x2:
        ax.text(x1 + offset, y1 + 2, card1, fontsize=11, fontweight='bold', color='darkblue')
        ax.text(x2 - offset, y2 + 2, card2, fontsize=11, fontweight='bold', color='darkblue')
    else:
        ax.text(x1 - offset, y1 + 2, card1, fontsize=11, fontweight='bold', color='darkblue')
        ax.text(x2 + offset, y2 + 2, card2, fontsize=11, fontweight='bold', color='darkblue')
    
    if participation1 == 'total':
        ax.plot([x1-1.5, x1+1.5], [y1, y1], 'k-', linewidth=5)
    if participation2 == 'total':
        ax.plot([x2-1.5, x2+1.5], [y2, y2], 'k-', linewidth=5)

print("Generating E-R Diagram...")

# employees entity
draw_entity(ax, 5, 72, 20, 22, 'EMPLOYEES',
            ['employee_id', 'first_name', 'last_name', 'email (UNIQUE)',
             'hire_date', 'job_role', 'salary'],
            ['employee_id'])

# customers entity
draw_entity(ax, 75, 72, 20, 22, 'CUSTOMERS',
            ['customer_id', 'first_name', 'last_name',
             'phone_number (UNIQUE)', 'email', 'registration_date'],
            ['customer_id'])

# orders entity
draw_entity(ax, 38, 46, 24, 20, 'ORDERS',
            ['order_id', 'FK: customer_id (nullable)',
             'FK: employee_id', 'order_date', 'order_time',
             'total_amount', 'order_status'],
            ['order_id'])

# order details (weak entity)
draw_entity(ax, 38, 18, 24, 16, 'ORDER_DETAILS',
            ['order_id (PK1)', 'item_id (PK2)',
             'quantity', 'unit_price'],
            ['order_id (PK1)', 'item_id (PK2)'],
            is_weak=True)

# menu items entity
draw_entity(ax, 75, 18, 20, 20, 'MENU_ITEMS',
            ['item_id', 'name (UNIQUE)', 'category',
             'price', 'description', 'is_available'],
            ['item_id'])

# inventory entity
draw_entity(ax, 5, 18, 20, 16, 'INVENTORY',
            ['inventory_id', 'ingredient_name (UNIQUE)',
             'unit_of_measure', 'current_stock', 'reorder_point'],
            ['inventory_id'])

# relationships
draw_relationship(ax, 30, 72, 3.5, 'takes')
draw_connection(ax, 25, 80, 30, 75.5, '1', 'N', participation1='partial', participation2='total')
draw_connection(ax, 30, 68.5, 38, 62, '', '', participation2='total')

draw_relationship(ax, 70, 72, 3.5, 'places')
draw_connection(ax, 75, 80, 70, 75.5, '1', 'N', participation1='partial', participation2='partial')
draw_connection(ax, 70, 68.5, 62, 62, '', '', participation2='partial')

draw_relationship(ax, 50, 40, 3.5, 'contains')
draw_connection(ax, 50, 46, 50, 43.5, '1', 'N', participation1='total', participation2='total')
draw_connection(ax, 50, 36.5, 50, 34, '', '', participation1='total', participation2='total')

draw_relationship(ax, 68, 28, 3.5, 'is_in')
draw_connection(ax, 75, 28, 71.5, 28, '1', 'N', participation1='partial', participation2='total')
draw_connection(ax, 64.5, 28, 62, 28, '', '', participation2='total')

# title
ax.text(50, 97, 'E-R Diagram: Restaurant Ordering System',
        ha='center', va='top', fontsize=17, fontweight='bold')

# legend
legend_elements = [
    mpatches.Patch(facecolor=entity_color, edgecolor='black', label='Regular Entity'),
    mpatches.Patch(facecolor=weak_entity_color, edgecolor='black', linewidth=3, label='Weak/Junction Entity'),
    mpatches.Patch(facecolor=relationship_color, edgecolor='black', label='Relationship'),
    mlines.Line2D([0], [0], color='black', linewidth=5, label='Total Participation (required)'),
]

ax.legend(handles=legend_elements, loc='lower left', fontsize=10)

# cardinalities
notes = """
RELATIONSHIPS & CARDINALITIES:

• CUSTOMERS (0,N) - places - (0,1) ORDERS
  1:N relationship, both partial
  
• EMPLOYEES (0,N) - takes - (1,1) ORDERS
  1:N relationship, ORDERS must have employee
  
• ORDERS (1,N) - contains - (1,1) ORDER_DETAILS
  1:N relationship, both total
  
• MENU_ITEMS (0,N) - is_in - (1,1) ORDER_DETAILS
  1:N relationship, ORDER_DETAILS must have item
  
• INVENTORY: No relationships (standalone)
"""

ax.text(2, 8, notes, ha='left', va='top', fontsize=9,
        family='monospace', bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.4))

plt.tight_layout()
plt.savefig('er_diagram.png', dpi=300, bbox_inches='tight', facecolor='white')
print("E-R Diagram saved as 'er_diagram.png'")
plt.show()
