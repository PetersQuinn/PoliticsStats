import matplotlib.pyplot as plt
from matplotlib.patches import Patch
from collections import defaultdict

color_counts = {
    '#880D1E': 3,  # Rep Unopposed
    '#D00000': 2,  # Rep Blowout
    '#CE4257': 3,  # Rep Solid
    '#E37696': 4,  # Rep Close
    '#FFB5C2': 3,  # Rep Term-Limited
    '#03045E': 3,  # Dem Unopposed
    '#0077B6': 0,  # Dem Blowout
    '#53A2BE': 1,  # Dem Solid 
    '#90E0EF': 1,  # Dem Close
    '#CAF0F8': 2,  # Dem Term-Limited
    '#828282': 5,  # Dem not up for election
    '#787276': 13,  # Rep not up for election

}

rep_safe = color_counts['#787276']
rep_unopposed = color_counts['#880D1E']
rep_blowout = color_counts['#D00000']
rep_solid = color_counts['#CE4257']
rep_close = color_counts['#E37696']
rep_term = color_counts['#FFB5C2']
dem_safe = color_counts['#828282']
dem_unopposed = color_counts['#03045E']
dem_blowout = color_counts['#0077B6']
dem_solid = color_counts['#53A2BE']
dem_close = color_counts['#90E0EF']
dem_term = color_counts['#CAF0F8']

rep_stacked_vals_ordered = [rep_safe, rep_unopposed, rep_blowout, rep_solid, rep_close, rep_term]
dem_stacked_vals_ordered = [dem_safe, dem_unopposed, dem_blowout, dem_solid, dem_close, dem_term]
rep_stacked_colors_ordered = ['#787276', '#880D1E', '#D00000', '#CE4257', "#E37696", '#FFB5C2']
dem_stacked_colors_ordered = ['#828282', '#03045E', '#0077B6', '#53A2BE', '#90E0EF', '#CAF0F8']
labelsRep = ['Not up for Election in 2026', 'Unopposed', 'Blowout', 'Solid', 'Close', 'Term-Limited']
labelsDem = ['Not up for Election in 2026', 'Unopposed', 'Blowout', 'Solid', 'Close', 'Term-Limited']

fig, ax = plt.subplots(figsize=(8, 6))

bottom = 0
for value, color, label in zip(rep_stacked_vals_ordered, rep_stacked_colors_ordered, labelsRep):
    if value > 0:
        ax.bar("Republicans", value, bottom=bottom, color=color)
        ax.text("Republicans", bottom + value / 2, f"{label}", ha='center', va='center', fontsize=9, color='white')
    bottom += value

bottom = 0
for value, color, label in zip(dem_stacked_vals_ordered, dem_stacked_colors_ordered, labelsDem):
    if value > 0:
        ax.bar("Democrats", value, bottom=bottom, color=color)
        ax.text("Democrats", bottom + value / 2, f"{label}", ha='center', va='center', fontsize=9, color='white')
    bottom += value

ax.set_ylabel("Number of Seats")
ax.set_title("Florida Senate seats up for election in 2026: Seat Breakdown by Previous Election Results")

legend_elements_ordered = [
    Patch(facecolor='#880D1E', label='Unopposed (Rep)'),
    Patch(facecolor='#D00000', label='Blowout (Rep)'),
    Patch(facecolor='#CE4257', label='Solid (Rep)'),
    Patch(facecolor='#E37696', label='Close (Rep)'),
    Patch(facecolor='#FFB5C2', label='Term-Limited (Rep)'),
    Patch(facecolor='#03045E', label='Unopposed (Dem)'),
    Patch(facecolor='#0077B6', label='Blowout (Dem)'),
    Patch(facecolor='#53A2BE', label='Solid (Dem)'),
    Patch(facecolor='#90E0EF', label='Close (Dem)'),
    Patch(facecolor='#CAF0F8', label='Term-Limited (Dem)')
]
plt.tight_layout()
plt.show()
