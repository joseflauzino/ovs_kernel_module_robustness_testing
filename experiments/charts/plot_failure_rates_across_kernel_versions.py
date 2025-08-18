import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Kernel versions and the full set of families
kernel_versions = ['v3.19.8', 'v4.20.9', 'v5.19.9', 'v6.14.6']
families = ['ovs_datapath', 'ovs_vport', 'ovs_flow', 'ovs_packet', 'ovs_meter', 'ovs_ct_limit']

# Paths
test_cases_dir = "../../src/input/test_cases"
processed_dir = "../processed"

# Count total test cases per family
total_cases = {}
for fam in families:
    fam_dir = os.path.join(test_cases_dir, fam)
    if os.path.exists(fam_dir):
        total_cases[fam] = len([f for f in os.listdir(fam_dir) if os.path.isfile(os.path.join(fam_dir, f))])
    else:
        print(f"Warning: test case directory not found for {fam}")
        total_cases[fam] = 0

# Build failure rates array
failure_rates = np.full((len(families), len(kernel_versions)), 0.0)
for j, version in enumerate(kernel_versions):
    filename = os.path.join(processed_dir, f"results_kernel_{version}.csv")
    if not os.path.exists(filename):
        print(f"File not found: {filename}, skipping...")
        continue

    df = pd.read_csv(filename)
    counts = df['Family'].value_counts()

    for i, fam in enumerate(families):
        failures = counts.get(fam, 0)
        total = total_cases[fam]
        rate = (failures / total * 100)
        if rate > 0:
            failure_rates[i, j] = round(rate, 2)

# Plot grouped bar chart
n_families = len(families)
n_versions = len(kernel_versions)
bar_width = 0.2
x = np.arange(n_families)

# Grayscale shades
grayscale = ['0.9', '0.7', '0.4', '0.1']
plt.rcParams.update({'font.size': 18})

# Plot
fig, ax = plt.subplots(figsize=(10, 6))
for j in range(n_versions):
    ax.bar(x + j * bar_width, failure_rates[:, j], width=bar_width,
           label=kernel_versions[j], color=grayscale[j], edgecolor='black')

ax.set_xticks(x + bar_width * (n_versions - 1) / 2)
ax.set_xticklabels(families, rotation=45, ha='right')
ax.set_ylabel('Failure Rate (%)')
ax.set_ylim(0, 100)
ax.legend(title='Kernel Version', loc='upper right', fontsize=16)
plt.grid(axis='y', linestyle='--', alpha=0.5)

# Export to PDF
output_file = "PDF/failure_rates_by_family.pdf"
plt.savefig(output_file, format="pdf", bbox_inches='tight')
plt.close()
print(f"Saved as {output_file}")