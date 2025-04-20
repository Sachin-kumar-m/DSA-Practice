import csv

# Input and output file names
input_csv = "/Users/sacmahes/Downloads/apac (1).csv"  # CSV file containing values
output_file = "apac.txt"  # File to save the formatted output

# Open CSV file and output file
with open(input_csv, "r") as csvfile, open(output_file, "w") as outfile:
    reader = csv.reader(csvfile)
    
    for row in reader:
        if row:  # Ensure the row is not empty
            value = row[0]  # Assuming values are in the first column
            
            # Prefixing with a single quote to avoid Excel #NAME? issue
            formatted_line = f"python3 /srv/www/iridize/manage.py run_custom_script -folder='/tmp' -file='test_script' -params='{{\"domain\": \"{value}\"}}\n"
            
            outfile.write(formatted_line)

print(f"Formatted output saved to {output_file}")
