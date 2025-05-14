# Doubling function

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

# Define the function
def F(x):
    if not (0 <= x < 1):
        raise ValueError("x must be in [0, 1)")
    return (2 * x) % 1 # 2x mod 1

# Get comma-separated seeds from the user
seed_input = input("Enter seeds (comma-separated, in (-2, 2)): ")
seeds = [float(s.strip()) for s in seed_input.split(",")]

# Validate seeds
for s in seeds:
    if not (-2 < s < 2):
        raise ValueError(f"Invalid seed {s}. Each seed must be in the interval (-2, 2)")

# Start writing the PDF
with PdfPages("orbits_functionC.pdf") as pdf:
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

print("PDF saved as orbits_functionC.pdf")
