# ER Diagram Generator for Restaurant Database

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import matplotlib.lines as mlines

# modern color palette
fig, ax = plt.subplots(figsize=(24, 18))
ax.set_xlim(0, 100)
ax.set_ylim(0, 100)
ax.axis('off')
fig.patch.set_facecolor('white')

# modern colors with better contrast
entity_color = '#D6EAF8'  # soft blue
weak_entity_color = '#FADBD8'  # soft coral
relationship_color = '#D5F4E6'  # soft mint

def draw_entity(ax, x, y, width, height, name, attributes, pk, is_weak=False):
    linewidth = 2.5 if is_weak else 2
    edge_color = '#2C3E50' if not is_weak else '#E74C3C'
    
    # shadow effect
    shadow = FancyBboxPatch((x+0.3, y-0.3), width, height,
                           boxstyle="round,pad=0.15",
                           edgecolor='none',
                           facecolor='#BDC3C7',
                           alpha=0.3,
                           linewidth=0)
    ax.add_patch(shadow)
    
    # main entity box
    entity = FancyBboxPatch((x, y), width, height,
                           boxstyle="round,pad=0.15",
                           edgecolor=edge_color,
                           facecolor=weak_entity_color if is_weak else entity_color,
                           linewidth=linewidth)
    ax.add_patch(entity)
    
    # entity name with background
    name_bg = FancyBboxPatch((x+1, y+height-4.5), width-2, 3,
                            boxstyle="round,pad=0.05",
                            edgecolor='none',
                            facecolor='#34495E',
                            alpha=0.1)
    ax.add_patch(name_bg)
    
    ax.text(x + width/2, y + height - 2.5, name,
            ha='center', va='center', fontsize=14, fontweight='bold', color='#2C3E50')
    
    # attributes
    y_offset = y + height - 7
    for attr in attributes:
        is_pk = attr in pk
        is_fk = 'FK:' in attr
        
        if is_pk:
            attr_text = f"🔑 {attr}"
            color = '#E74C3C'
            weight = 'bold'
        elif is_fk:
            attr_text = f"→ {attr}"
            color = '#3498DB'
            weight = 'normal'
        else:
            attr_text = f"  • {attr}"
            color = '#2C3E50'
            weight = 'normal'
        
        ax.text(x + 2, y_offset, attr_text,
                ha='left', va='top', fontsize=8.5,
                fontweight=weight, color=color)
        y_offset -= 2.1

def draw_relationship(ax, x, y, size, name):
    points = [(x, y + size), (x + size, y), (x, y - size), (x - size, y)]
    
    # shadow
    shadow_points = [(p[0]+0.3, p[1]-0.3) for p in points]
    shadow = mpatches.Polygon(shadow_points, closed=True,
                             edgecolor='none',
                             facecolor='#BDC3C7',
                             alpha=0.3)
    ax.add_patch(shadow)
    
    # main diamond
    diamond = mpatches.Polygon(points, closed=True,
                              edgecolor='#27AE60',
                              facecolor=relationship_color,
                              linewidth=2.5)
    ax.add_patch(diamond)
    
    ax.text(x, y, name, ha='center', va='center',
            fontsize=11, fontweight='bold', color='#27AE60')

def draw_connection(ax, x1, y1, x2, y2, card1, card2, participation1='partial', participation2='partial'):
    line = mlines.Line2D([x1, x2], [y1, y2],
                        color='#34495E', linewidth=2, alpha=0.8)
    ax.add_line(line)
    
    # calculate perpendicular offset for label placement
    dx = x2 - x1
    dy = y2 - y1
    length = (dx**2 + dy**2)**0.5
    if length > 0:
        perp_x = -dy / length * 2.5  # perpendicular offset
        perp_y = dx / length * 2.5
    else:
        perp_x, perp_y = 0, 2.5
    
    # place card1 near first point (15% along the line)
    if card1:
        label_x1 = x1 + dx * 0.15
        label_y1 = y1 + dy * 0.15
        ax.text(label_x1 + perp_x, label_y1 + perp_y, card1, fontsize=11, fontweight='bold', 
                color='white', ha='center', va='center',
                bbox=dict(boxstyle='round,pad=0.35', facecolor='#3498DB', edgecolor='none', alpha=0.95))
    
    # place card2 near second point (85% along the line)
    if card2:
        label_x2 = x1 + dx * 0.85
        label_y2 = y1 + dy * 0.85
        ax.text(label_x2 + perp_x, label_y2 + perp_y, card2, fontsize=11, fontweight='bold',
                color='white', ha='center', va='center',
                bbox=dict(boxstyle='round,pad=0.35', facecolor='#3498DB', edgecolor='none', alpha=0.95))
    
    # total participation markers
    if participation1 == 'total':
        ax.plot([x1-1.5, x1+1.5], [y1, y1], color='#E74C3C', linewidth=6, solid_capstyle='round')
    if participation2 == 'total':
        ax.plot([x2-1.5, x2+1.5], [y2, y2], color='#E74C3C', linewidth=6, solid_capstyle='round')

print("Generating E-R Diagram...")

# employees entity
draw_entity(ax, 3, 70, 24, 24, 'EMPLOYEES',
            ['employee_id', 'first_name', 'last_name', 'email (UNIQUE)',
             'hire_date', 'job_role', 'salary'],
            ['employee_id'])

# customers entity
draw_entity(ax, 73, 70, 24, 24, 'CUSTOMERS',
            ['customer_id', 'first_name', 'last_name',
             'phone_number (UNIQUE)', 'email', 'registration_date'],
            ['customer_id'])

# orders entity
draw_entity(ax, 33, 44, 34, 22, 'ORDERS',
            ['order_id', 'FK: customer_id (nullable)',
             'FK: employee_id', 'order_date', 'order_time',
             'total_amount', 'order_status'],
            ['order_id'])

# order details (weak entity)
draw_entity(ax, 37, 16, 26, 17, 'ORDER_DETAILS',
            ['order_id (PK1)', 'item_id (PK2)',
             'quantity', 'unit_price'],
            ['order_id (PK1)', 'item_id (PK2)'],
            is_weak=True)

# menu items entity
draw_entity(ax, 73, 16, 24, 22, 'MENU_ITEMS',
            ['item_id', 'name (UNIQUE)', 'category',
             'price', 'description', 'is_available'],
            ['item_id'])

# inventory entity
draw_entity(ax, 3, 16, 27, 18, 'INVENTORY',
            ['inventory_id', 'ingredient_name (UNIQUE)',
             'unit_of_measure', 'current_stock', 'reorder_point'],
            ['inventory_id'])

# relationships
draw_relationship(ax, 30, 72, 3.5, 'takes')
draw_connection(ax, 27, 80, 30, 75.5, '1', 'N', participation1='partial', participation2='total')
draw_connection(ax, 30, 68.5, 33, 62, '', '', participation2='total')

draw_relationship(ax, 70, 72, 3.5, 'places')
draw_connection(ax, 73, 80, 70, 75.5, '1', 'N', participation1='partial', participation2='partial')
draw_connection(ax, 70, 68.5, 67, 62, '', '', participation2='partial')

draw_relationship(ax, 50, 38, 3.5, 'contains')
draw_connection(ax, 50, 44, 50, 41.5, '1', 'N', participation1='total', participation2='total')
draw_connection(ax, 50, 34.5, 50, 33, '', '', participation1='total', participation2='total')

draw_relationship(ax, 68, 26, 3.5, 'is_in')
draw_connection(ax, 73, 26, 71.5, 26, '1', 'N', participation1='partial', participation2='total')
draw_connection(ax, 64.5, 26, 63, 26, '', '', participation2='total')

# title with modern styling
ax.text(50, 97, 'E-R Diagram: Restaurant Ordering System',
        ha='center', va='top', fontsize=20, fontweight='bold', color='#2C3E50',
        bbox=dict(boxstyle='round,pad=0.8', facecolor='#ECF0F1', edgecolor='#34495E', linewidth=2))

# modern legend
legend_elements = [
    mpatches.Patch(facecolor=entity_color, edgecolor='#2C3E50', linewidth=2, label='Regular Entity'),
    mpatches.Patch(facecolor=weak_entity_color, edgecolor='#E74C3C', linewidth=2.5, label='Weak/Junction Entity'),
    mpatches.Patch(facecolor=relationship_color, edgecolor='#27AE60', linewidth=2.5, label='Relationship'),
    mlines.Line2D([0], [0], color='#E74C3C', linewidth=6, solid_capstyle='round', label='Total Participation'),
]

ax.legend(handles=legend_elements, loc='lower left', fontsize=11, frameon=True, 
         fancybox=True, shadow=True, framealpha=0.95)

# cleaner cardinality box
notes = """RELATIONSHIPS & CARDINALITIES:

  CUSTOMERS (0,N) ── places ── (0,1) ORDERS
    1:N relationship, both partial

  EMPLOYEES (0,N) ── takes ── (1,1) ORDERS
    1:N relationship, ORDERS must have employee

  ORDERS (1,N) ── contains ── (1,1) ORDER_DETAILS
    1:N relationship, both total

  MENU_ITEMS (0,N) ── is_in ── (1,1) ORDER_DETAILS
    1:N relationship, ORDER_DETAILS must have item

  INVENTORY: No relationships (standalone)"""

ax.text(2, 8, notes, ha='left', va='top', fontsize=10,
        family='sans-serif', color='#2C3E50',
        bbox=dict(boxstyle='round,pad=1', facecolor='#ECF0F1', 
                 edgecolor='#34495E', linewidth=2, alpha=0.95))

plt.tight_layout()
# Save with same DPI as screen for consistency
plt.savefig('er_diagram.png', dpi=100, bbox_inches='tight', facecolor='white', edgecolor='none')
print("E-R Diagram saved as 'er_diagram.png'")
plt.show()
