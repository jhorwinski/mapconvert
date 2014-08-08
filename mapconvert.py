#author: Joseph Horwinski
#start date: 8/5/2014
#Reorganizes the excel format Miseq V4 (runs 1-16) mapping files to be inline with the
#semi-standardized github format. The excel data had to have spaces removed from various
#fields, such as "Surface Swab" to "SurfaceSwab" for the column headers to line up.
#Description placed in the last column. There is a discrepancy between the description 
#in the excel file (ex. "sample"#SampleID) and the github mapping files (ex. "GLS000002")
#for Miseq 1-12.


mapfi = open('excel/miseq01.txt')
desfi = open('generated/miseq01gen.txt', 'w')



for line in mapfi:
	line=line.rstrip()
	line=line.split()
	first=line[0:3]
	first.append(line[17])
	first.append(line[7])
	first.append(line[6])
	first.append(line[12])
	first.append(line[9])
	first.append(line[18])
	first.append(line[3])
	first.append(line[4])
	first.append(line[13])
	first.append(line[10])
	first.append(line[5])
	first.append(line[14])
	first.append(line[11])
	first.append(line[8])
	first.append(line[15])
	first.append(line[16])
	first.extend(line[20:])
	first.append(line[19])
	x='	'.join(first)
	desfi.write(x)
	desfi.write('\n')
desfi.close()
	
