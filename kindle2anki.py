#!/usr/local/bin/python3

import csv
from googletrans import Translator

translator = Translator()

filein=open('countdown.tsv')
fileout=open('deck.tsv', mode='w')

csv_reader = csv.reader(filein, delimiter='\t')
csv_writer = csv.writer(fileout, delimiter='\t')

for row in csv_reader:
	print(f'Creating card: {row[0]}')
	esword = translator.translate(row[0], src="EN", dest="ES").text
	csv_writer.writerow([row[0], esword + "<br/><br/>" + row[1]])
		
print("\nDeck created")
filein.close()
fileout.close()
