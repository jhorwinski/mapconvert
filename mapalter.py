#author: Joseph Horwinski
#start date: 8/13/2014
#Removes 'RCBarcode' and 'BarcodeName' columns and changes column header 'DNAconc(ng/ul)' 
#to 'DNAconc'. Changes 'NA's in'HostSpecies' column to 'Control'.


miseq=raw_input('Enter MiSeqV1V3 Number (ex. 01):')
v='MiSeqV1V3_'


#miseq=raw_input('Enter MiSeq Number (ex. 01):')
#v='MiSeq_'

txt = '.txt'

'/Documents/Club_Grice/mapping_files/run_maps/MiSeq_01.txt'

doc = '/Users/gricelab/Documents/Club_Grice/mapping_files/run_maps/'
#doc = '/Users/gricelab/Documents/Joseph/mapping_file_conversion/Generated/'

m = doc+v+miseq+txt

colhds = '#SampleID	BarcodeSequence	LinkerPrimerSequence	ProjectID	StudyID	DateSequenced	RunName	HostSpecies	SampleType	Control	ReversePrimerSequence	WellPosition	PCRcycles	DNAconc	Description'

mapfi = open(m, 'r')

file = open("blank.txt", "w")

for line in mapfi:
	line=line.rstrip()
	if line.startswith('#SampleID'):
		file.write(colhds)
		file.write('\n')
		continue
	else:
		line=line.split()
		first=line[0:3]
		first.extend(line[4:8])
		species = (line[8])
		if species == 'NA':
			first.append('Control')
		else:
			first.append(line[8])
		first.extend(line[9:11])
		first.extend(line[12:])
		x='	'.join(first)
		file.write(x)
		file.write('\n')
mapfi.close()
file.close()

file2 = open("blank.txt", 'r')

mapfi2 = open(m, 'w')

for line in file2:
	line=line.rstrip()
	mapfi2.write(line)
	mapfi2.write('\n')

mapfi2.close()