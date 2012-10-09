def simpleDel(num):
	if num<=0:
		print "Not positive number can not be decomposed into factors. (num="+str(num)+")"
		return []
	mass=[]
	i=2
	tmp=num
	while i<=num/2:
		if tmp%i == 0:
			while True:
				if tmp%i==0:
					tmp=tmp/i
					mass.append(i)
				else:
					break
		i+=1
	if len(mass)==0:
		mass.append(num)
	print mass
	return mass

def test_simpleDel():
	assert simpleDel(100) == [2,2,5,5]
	assert simpleDel(8) == [2,2,2]
	assert simpleDel(27) == [3,3,3]
	assert simpleDel(113) == [113]
	assert simpleDel(121) == [11,11]
	assert simpleDel(4) == [2,2]
	assert simpleDel(3*11*179)==[3,11,179]
	assert simpleDel(-99) == []
	assert simpleDel(0) == []
	print "Test passed simpleDel OK!"

def main():
	#simpleDel(100)
	test_simpleDel()

main()