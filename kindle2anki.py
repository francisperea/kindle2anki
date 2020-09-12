import csv

with open('countdown.tsv') as csv_file:
	csv_reader = csv.reader(csv_file, delimiter=',')
	line_count = 0
	for row in csv_reader:
		print(f'Inglés: \t{row[0]} \t Uso: {row[1]} ')
		line_count += 1
	print(f'Processed {line_count} lines.')