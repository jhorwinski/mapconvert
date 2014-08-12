#author: Joseph Horwinski
#start date: 8/11/2014
#Reorganizes the old GitHub format Miseq V1V3 (runs 9-12) mapping files to be inline with the
#now standardized 17 column github format. Replaces "1" wtih "001" and "10" with "010" in study ID. Must be manually overridden for miseg9 which requires an additional "0"

miseq=raw_input('Enter MiSeqV1V3 Number (ex. 01):')
sd=raw_input('Enter sequencing date (ex. 2014-01-27):')

git = '/Users/gricelab/Documents/Joseph/mapping_file_conversion/Github/MiSeqV1V3-'
gen = '/Users/gricelab/Documents/Joseph/mapping_file_conversion/Generated/MiSeqV1V3_'
tsv = '-NO-REG-NUM.tsv'
txt = '.txt'
run = 'MiSeqV1V3_'
colhds = '#SampleID	BarcodeSequence	LinkerPrimerSequence	BarcodeName	ProjectID	StudyID	DateSequenced	RunName	HostSpecies	SampleType	Control	RCBarcodeSequence	ReversePrimerSequence	WellPosition	PCRcycles	DNAconc(ng/ul)	Description'
tab = '	'
oo = '0'

m = git+miseq+tsv
d = gen+miseq+txt
rn = run+miseq
rnno0 = str(int(miseq))
rntab = tab+rnno0+tab
rnw0s = tab+oo+rnno0+tab

mapfi = open(m, "rb").read()
updated = mapfi.replace('	1	', '	001	')
updated = updated.replace(rntab, rnw0s)
if updated != mapfi:
	f = open(m, "wb")
	f.write(updated)
	f.close()

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
		line=line.replace('Surface swab', 'SurfaeSwab')
		line=line.split()
		first=line[0:3]
		first.append('NA')
		first.append(line[7])
		first.append(line[12])
		first.append(sd)
		first.append(rn)
		first.append(line[5])
		first.append(line[10])
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
		first.append(line[9])
		first.append(line[18])
		first.append('35')
		first.append('NA')
		first.append(line[24])
		x='	'.join(first)
		desfi.write(x)
		desfi.write('\n')
desfi.close()
	
