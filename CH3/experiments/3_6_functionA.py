# This program is an experiment from section 3.6
# It iterates the given function 200 times and displays the result in a table in a PDF file
# Date: May 14, 2025
# Author: Miguel Ángel Vargas

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

# Define the function
def F(x):
    return x**2 - 2

# Get comma-separated seeds from the user
seed_input = input("Enter seeds (comma-separated, in (-2, 2)): ")
seeds = [float(s.strip()) for s in seed_input.split(",")]

# Validate seeds
for s in seeds:
    if not (-2 < s < 2):
        raise ValueError(f"Invalid seed {s}. Each seed must be in the interval (-2, 2)")

# Start writing the PDF
with PdfPages("orbit_tables.pdf") as pdf:
    for seed in seeds:
        # Compute the orbit
        orbit = [seed]
        for _ in range(199):
            orbit.append(F(orbit[-1]))
        
        # Reshape into 4 columns of 50 rows (column-wise)
        data = np.array(orbit).reshape(4, 50).T
        df = pd.DataFrame(data, columns=["x_0–49", "x_50–99", "x_100–149", "x_150–199"])
        df = df.round(5) # Round to 5 decimal places

        # Create and style the figure
        fig, ax = plt.subplots(figsize=(8.5, 11))
        ax.axis('off')
        table = ax.table(cellText=df.values, colLabels=df.columns, loc='center')
        table.auto_set_font_size(False)
        table.set_fontsize(8)
        table.scale(1.2, 1.2)
        pdf.savefig(fig, bbox_inches='tight')
        plt.close()

print("PDF saved as orbit_tables.pdf")
