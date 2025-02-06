import sweetviz as sv
import pandas as pd

# Load the dataset
file_path = './Consultrix Data Set.csv'
data = pd.read_csv(file_path)  # Use read_csv for CSV files

# Generate the Sweetviz report
report = sv.analyze(data)

# Save the report as an HTML file for hosting
output_file = 'Consultrix_EDA_Report.html'
report.show_html(output_file)

print(f"EDA report generated successfully: {output_file}")
