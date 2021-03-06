#author: Joseph Horwinski
#start date: 8/5/2014
#Reorganizes the excel format Miseq V1V3 (runs 1-8) mapping files to be inline with the
#now standardized 17 column github format. Also converts tab delimited text file source 
#from CR to LF line breaks. 

miseq=raw_input('Enter MiSeqV1V3 Number (ex. 01):')
sd=raw_input('Enter sequencing date (ex. 2014-01-27):')

excel = '/Users/gricelab/Documents/Joseph/mapping_file_conversion/Excel/MiSeqV1V3_'
gen = '/Users/gricelab/Documents/Joseph/mapping_file_conversion/Generated/MiSeqV1V3_'
txt = '.txt'
run = 'MiSeqV1V3_'
colhds = '#SampleID	BarcodeSequence	LinkerPrimerSequence	BarcodeName	ProjectID	StudyID	DateSequenced	RunName	HostSpecies	SampleType	Control	RCBarcodeSequence	ReversePrimerSequence	WellPosition	PCRcycles	DNAconc(ng/ul)	Description'

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
		first.append('NA')
		first.append(line[13])
		first.append(line[14])
		first.append(sd)
		first.append(rn)
		first.append(line[10])
		first.append(line[8])
		control=line[16]
		if control == 'water':
			first.append('Water')
		elif control == 'mock':
			first.append('Mock')
		elif control == 'Control':
			first.append('Study')
		else:
			first.append('No')
		#first.append('control?_No_Sequencing_Water_Mock')
		first.append('NA')
		first.append(line[3])
		first.append(line[12])
		first.append('35')
		first.append('NA')
		first.append(line[23])
		x='	'.join(first)
		desfi.write(x)
		desfi.write('\n')
desfi.close()
	
