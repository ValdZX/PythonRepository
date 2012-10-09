def readSimb(mass):
	gl_index = 0
	flag = False
	assert len(mass)>=2
		
	
	while True:
		if flag == False:
			while gl_index < len(mass):
				if gl_index==len(mass)-1:
					break
				if mass[gl_index] > mass[gl_index+1]:
					tmp=mass[gl_index]
					mass[gl_index]=mass[gl_index+1]
					mass[gl_index+1]=tmp
					if gl_index > 0:
						gl_index-=1
					flag = True
				else:
					if gl_index < len(mass):
						gl_index+=1
		else:
			while gl_index > 0:
				if gl_index==len(mass)-1:
					break
				if mass[gl_index] > mass[gl_index+1]:
					tmp=mass[gl_index]
					mass[gl_index]=mass[gl_index+1]
					mass[gl_index+1]=tmp
					if gl_index > 0:
						gl_index-=1
				else:
					if gl_index < len(mass):
						gl_index+=1
					flag = False
					
		if gl_index==len(mass)-1:
			break
	return mass
def test_readSimb():
	assert readSimb([8,1,3,4,1,8,2,5])==[1, 1, 2, 3, 4, 5, 8, 8]
	assert readSimb([1,2,3])==[1,2,3]
	assert readSimb([-1,-2,-3])==[-3,-2,-1]
	assert readSimb([12,5])==[5,12]
	#assert readSimb([])==[] #Error
	assert readSimb([0,0])==[0,0]
	assert readSimb(["b","a"])==["a","b"]
	assert readSimb(["cba","abc"])==["abc","cba"]
	assert readSimb(["abd","abc"])==["abc","abd"]
	assert readSimb(["abd",4])==[4,"abd"]
	assert readSimb(["",4])==[4,""]
	assert readSimb([4,False])==[False,4]
	assert readSimb([True,False,True])==[False,True,True]
	
	print "Test passed ok!"
	
def main():
	test_readSimb()
main()