import csv

csv_file = "Bestseller - Sheet1.csv"
best_selling = "none"
max_sold = 0

with open(csv_file, 'r', encoding='utf-8') as file:
    csv_reader = csv.reader(file)

    next(csv_reader)  # Skip the header row

    for row in csv_reader:
        current_sales = float(row[4])
        if current_sales > max_sold:
            max_sold = current_sales
            best_selling = row[0]

output_file = "Bestseller_info.csv"
with open(output_file, 'w', newline='', encoding='utf-8') as output_file:
    csv_writer = csv.writer(output_file)
    csv_writer.writerow(["Best Selling Book", "Sales"])
    csv_writer.writerow([best_selling, max_sold])

print(f"The best selling book is '{best_selling}' with sales of {max_sold}.")
