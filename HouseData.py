import matplotlib.pyplot as plt
from matplotlib.patches import Patch
from collections import defaultdict

color_counts = {
    '#880D1E': 0,  # Rep Unopposed
    '#D00000': 30,  # Rep Blowout
    '#CE4257': 38,  # Rep Solid
    '#E37696': 17,  # Rep Close
    '#03045E': 17,  # Dem Unopposed
    '#0077B6': 5,  # Dem Blowout
    '#53A2BE': 4,  # Dem Solid 
    '#90E0EF': 9,  # Dem Close
}

rep_unopposed = color_counts['#880D1E']
rep_blowout = color_counts['#D00000']
rep_solid = color_counts['#CE4257']
rep_close = color_counts['#E37696']
dem_unopposed = color_counts['#03045E']
dem_blowout = color_counts['#0077B6']
dem_solid = color_counts['#53A2BE']
dem_close = color_counts['#90E0EF']

rep_stacked_vals_ordered = [rep_unopposed, rep_blowout, rep_solid, rep_close]
dem_stacked_vals_ordered = [dem_unopposed, dem_blowout, dem_solid, dem_close]
rep_stacked_colors_ordered = ['#880D1E', '#D00000', '#CE4257', "#E37696"]
dem_stacked_colors_ordered = ['#03045E', '#0077B6', '#53A2BE', '#90E0EF']
labelsRep = ['Unopposed', 'Blowout', 'Solid', 'Close']
labelsDem = ['Unopposed', 'Blowout', 'Solid', 'Close']

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
ax.set_title("Florida House seats up for election in 2026: Seat Breakdown by Previous Election Results")

legend_elements_ordered = [
    Patch(facecolor='#880D1E', label='Unopposed (Rep)'),
    Patch(facecolor='#D00000', label='Blowout (Rep)'),
    Patch(facecolor='#CE4257', label='Solid (Rep)'),
    Patch(facecolor='#E37696', label='Close (Rep)'),
    Patch(facecolor='#03045E', label='Unopposed (Dem)'),
    Patch(facecolor='#0077B6', label='Blowout (Dem)'),
    Patch(facecolor='#53A2BE', label='Solid (Dem)'),
    Patch(facecolor='#90E0EF', label='Close (Dem)'),
]
plt.tight_layout()
plt.show()
