data = open('excel/miseq01.txt', "rb").read()
newdata = data.replace("\r", "\n")
if newdata != data:
	f = open('excel/miseq01.txt', "wb")
	f.write(newdata)
	f.close()
