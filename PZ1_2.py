def readSimb(str):
	strResult = ""
	tmpSym = ""
	flag = False
	for sym in str:
		if tmpSym != sym:
			tmpSym = sym
			flag = True
		elif flag == True:
			flag = False
			if sym == '#':
				assert len(strResult) != 0
				strResult = strResult + strResult[-1]
			else:
				strResult += sym
	print strResult
	return strResult

def main():
	readSimb("##")
	readSimb("1")
	readSimb("11")
	readSimb("11111")
	readSimb("11#")
	readSimb("11##")
	readSimb("11122234###55")

main()