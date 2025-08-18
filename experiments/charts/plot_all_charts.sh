if [ -z "$VIRTUAL_ENV" ]; then
  virtualenv ovs-env
  source ovs-env/bin/activate
  pip install -r requirements.txt
fi

echo "Plotting..."
python3 plot_heatmap_failures_across_kernels.py      # plot Figure 4
python3 plot_failure_rates_across_kernel_versions.py # plot Figure 5
python3 plot_failure_count_by_rule_and_family.py     # plot Figure 6