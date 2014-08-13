#author: Joseph Horwinski
#start date: 8/13/2014
#Removes 'RCBarcode' and 'BarcodeName' columns and changes column header 'DNAconc(ng/ul)' 
#to 'DNAconc'. Adds column 'LibraryPreparer' and fills in column info. Changes 'NA's in #
#'HostSpecies' column to 'Control'.


#miseq=raw_input('Enter MiSeqV1V3 Number (ex. 01):')
#v='MiSeqV1V3_'


miseq=raw_input('Enter MiSeq Number (ex. 01):')

v='MiSeq_'

txt = '.txt'

#doc = '/Users/gricelab/Documents/Club_Grice/mapping_files/'
doc = '/Users/gricelab/Documents/Joseph/mapping_file_conversion/Generated/'

m = doc+v+miseq+txt

colhds = '#SampleID	BarcodeSequence	LinkerPrimerSequence	ProjectID	StudyID	DateSequenced	RunName	HostSpecies	SampleType	Control	ReversePrimerSequence	WellPosition	PCRcycles	DNAconc	Description'

#mapfi = open(m, "rb").read()
#updated = mapfi.replace("\r", "\n")
#if updated != mapfi:
#	f = open(m, "wb")
#	f.write(updated)
#	f.close()

mapfi = open(m, 'r')

file = open("newfile.txt", "w")

for line in mapfi:
	line=line.rstrip()
	if line.startswith('#SampleID'):
		file.write(colhds)
		file.write('\n')
		continue
	else:
		line=line.split()
		first=line[0:3]
		first.append(line[4:8])
		species = (line[8])
		if species == 'NA':
			first.append('Control')
		else:
			first.append(line[8])
		first.append(line[9:11])
		first.append(line[12:])
		x='	'.join(first)
		file.write(x)
		file.write('\n')
file.close()
mapfi.close()


