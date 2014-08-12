m = '/Users/gricelab/Documents/Joseph/mapping_file_conversion/Final/MiSeq_19.txt'

mapfi = open(m, "rb").read()
updated = mapfi.replace("		", "")
if updated != mapfi:
	f = open(m, "wb")
	f.write(updated)
	f.close()

	
