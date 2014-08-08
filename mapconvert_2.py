#author: Joseph Horwinski
#start date: 8/5/2014
#Reorganizes the excel format Miseq V4 (runs 1-18) mapping files to be inline with the
#now standardized 17 column github format. Also converts tab delimited text file source 
#from CR to LF line breaks. 

miseq=raw_input('Enter MiSeq Number (ex. 01):')

excel = '/Users/gricelab/Documents/Joseph/mapping_file_conversion/Excel/MiSeq_'
gen = '/Users/gricelab/Documents/Joseph/mapping_file_conversion/Generated/MiSeq_'
txt = '.txt'
run = 'MiSeq_'
colhds = '#SampleID	BarcodeSequence	LinkerPrimerSequence	BarcodeName	ProjectID	StudyID	DateSequenced	RunName	HostSpecies	SampleType	Control RCBarcodeSequence	ReversePrimerSequence	WellPosition	PCRcycles	DNAconc(ng/ul)	Description'

m = excel+miseq+txt
d = gen+miseq+txt
rn = run+miseq

mapfi = open(m, "rb").read()
updated = mapfi.replace("\r", "\n")
if updated != mapfi:
	f = open(m, "wb")
	f.write(updated)
	f.close()

mapfi = open(m, 'r')
desfi = open(d, 'w')

for line in mapfi:
	line=line.rstrip()
	if line.startswith('#SampleID'):
		desfi.write(colhds)
		desfi.write('\n')
		continue
	else:
		line=line.split()
		first=line[0:3]
		first.append(line[17])
		first.append(line[9])
		first.append(line[10])
		first.append(line[7])
		first.append(rn)
		first.append(line[6])
		first.append(line[4])
		control=line[12]
		if control == 'water':
			first.append('Water')
		elif control == 'mock':
			first.append('Mock')
		else:
			first.append('NA')
		#first.append('control?_No_Sequencing_Water_Mock')
		first.append(line[18])
		first.append(line[3])
		first.append(line[8])
		first.append('35')
		first.append('NA')
		first.append(line[19])
		x='	'.join(first)
		desfi.write(x)
		desfi.write('\n')
desfi.close()
	
