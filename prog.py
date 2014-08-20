#x=raw_input("enter thing: ")
#y=open(x)
#lst=list()
#counts=dict()
#for line in y:
#    line=line.rstrip()
    #if you use 'From' rather than 'From:' you get a duplicate of every address
    #with a total of 54 addresses
#    if not line.startswith('From:'): continue
#    line = line.split()
#    word=line[1]
#    lst.append(word)

#for name in lst:
#    counts[name]=counts.get(name,0)+1

#bigc = None
#bigw = None
#for w,c in counts.items():
#    if bigc is None or c>bigc:
#        bigw=w
#        bigc=c
        
#print bigw,bigc

#x=raw_input("enter thing: ")
#y=open(x)
#lst=list()
#for line in y:
#    line=line.rstrip()
    #if you use 'From' rather than 'From:' you get a duplicate of every address
    #with a total of 54 addresses
#    if not line.startswith('From:'): continue
#    line = line.split()
#    word=line[1]
#    print word
#    lst.append(word)
#z=len(lst)
#print "There were",z,"lines in the file with From as the first word"

file = raw_input("enter file name:")
ofile = open(file)
for line in ofile:
	line = line.rstrip()
	if line.startswith('#SampleID'):
		print line
	else:
		line = line.split()
		fstwrd = line[0]
		print fstwrd
	
	
	#hi Ciara