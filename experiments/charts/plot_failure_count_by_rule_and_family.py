import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the CSV file
file_path = "../processed/results_kernel_v6.14.6.csv"
df = pd.read_csv(file_path)

# Count occurrences of each Generic Rule per Family
rule_counts = df.groupby(['Family', 'Generic Rule']).size().reset_index(name='Failure Count')

# Set plot style to grayscale
sns.set_style("whitegrid")
gray_palette = sns.color_palette("gray", n_colors=df['Family'].nunique())

# Create the plot
plt.rcParams.update({'font.size': 20})
plt.figure(figsize=(11, 8))
sns.barplot(data=rule_counts, x='Failure Count', y='Generic Rule', hue='Family', palette=gray_palette, dodge=True)
plt.xlabel('Number of Failures', fontsize=24)
plt.ylabel('Rules', fontsize=24)
plt.yticks(rotation=45) 
plt.legend(title='Family', loc='lower right', fontsize=18)
plt.tight_layout()

# Export to PDF
output_file = "PDF/failure_count_by_rule_and_family_grayscale.pdf"
plt.savefig(output_file, format='pdf')
plt.close()
print(f"Saved as {output_file}")