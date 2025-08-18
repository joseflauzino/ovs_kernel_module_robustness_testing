import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import os

# Kernel versions and the full set of families
kernel_versions = ['v3.19.8', 'v4.20.9', 'v5.19.9', 'v6.14.6']
families = ['ovs_datapath', 'ovs_vport', 'ovs_flow', 'ovs_packet', 'ovs_meter', 'ovs_ct_limit']

# Build data dict with fixed keys and equal-length lists
data = {fam: [] for fam in families}

for version in kernel_versions:
    filename = f"../processed/results_kernel_{version}.csv"
    if not os.path.exists(filename):
        print(f"File not found: {filename}. Filling zeros for this version.")
        for fam in families:
            data[fam].append(0)
        continue

    dfv = pd.read_csv(filename)

    if 'Family' not in dfv.columns:
        raise KeyError(f"'Family' column not found in {filename}")

    # Normalize and count
    counts = (dfv['Family']
              .astype(str)
              .str.strip()
              .value_counts())

    # Append a value for *every* family, using 0 if missing
    for fam in families:
        data[fam].append(int(counts.get(fam, 0)))

# Sanity check: all series must match the number of versions
assert all(len(vals) == len(kernel_versions) for vals in data.values()), "Length mismatch building data."

# Create DataFrame (rows: versions, cols: families)
df = pd.DataFrame(data, index=kernel_versions)

# Plot with reversed axes
plt.figure(figsize=(10, 6))
sns.set_theme(font_scale=1.2)
ax = sns.heatmap(df.T, annot=True, cmap='Greys', cbar_kws={'label': 'Total Number of Failures'})

# Set axis labels with increased font size
ax.set_xlabel('Kernel Version', fontsize=18)
ax.set_ylabel('Generic Netlink Family', fontsize=18)
ax.figure.axes[-1].yaxis.label.set_size(18)  # Colorbar label size

# Export to PDF
plt.tight_layout()
output_file = "PDF/heatmap_failures_across_kernels.pdf"
plt.savefig(output_file, format="pdf", bbox_inches='tight')
plt.close()
print(f"Saved as {output_file}")