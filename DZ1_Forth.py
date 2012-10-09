#!/usr/bin/env python
# -*- coding:utf8 -*-
"example of homework solution"
import os

def eval_forth(file_path):
	file_forth = open(file_path,"r")
	massPrint = []
	stack = []
	while True:
		strCom = file_forth.readline()
		strCom=strCom[0:-1]
		if strCom=="":
			break
		massCom = strCom.split(' ')
		if len(massCom)==2:
			if massCom[0]=="put":
				stack.append(massCom[1])
			else:
				massPrint.append("Unknown command \""+massCom[0]+"\"")
		elif len(massCom)==1:
			if massCom[0]=="pop":
				if len(stack)>0:
					stack=stack[0:-1]
				else:
					massPrint.append("Not enough operands.")
			elif massCom[0]=="print":
				if len(stack)>0:
					massPrint.append(stack[-1])
					stack=stack[0:-1]
				else:
					massPrint.append("Not enough operands.")
			elif massCom[0]=="add":
				if  len(stack)>=2:
					if stack[-1][0]=="\"" and stack[-2][0]=="\"":						
						tmpSt = "\""+stack[-1][1:-1] + stack[-2][1:-1]+"\""						
						stack=stack[0:-2]
						stack.append(tmpSt)
					elif stack[-1][0]=="\"":						
						tmpSt = "\""+stack[-1][1:-1] + str(stack[-2])+ "\""						
						stack=stack[0:-2]
						stack.append(tmpSt)
					elif stack[-2][0]=="\"":						
						tmpSt ="\""+str(stack[-1]) +stack[-2][1:-1]+ "\""					
						stack=stack[0:-2]
						stack.append(tmpSt)						
					else:
						tmpInt = int(stack[-1]) + int(stack[-2])						
						stack=stack[0:-2]
						stack.append(str(tmpInt))
				else:
					massPrint.append("Not enough operands.")
			elif massCom[0]=="sub":
				if  len(stack)>=2:
					if stack[-1][0]!="\"" and stack[-2][0]!="\"":
						tmpInt = int(stack[-1]) - int(stack[-2])						
						stack=stack[0:-2]
						stack.append(str(tmpInt))
					else:
						massPrint.append("Can't subtract 'str' and 'int' objects")
				else:
					massPrint.append("Not enough operands.")
			else:
				massPrint.append("Unknown command \""+massCom[0]+"\"")
	return 	massPrint
	
def testForth():	
	strNameFile = "C:\\test.frt"
	
	input_file = open(strNameFile,"w")
	input_file.write("put 1\nput 3\nadd\nprint\n")	
	input_file.close()
	assert eval_forth(strNameFile)==["4"]
	
	input_file = open(strNameFile,"w")
	input_file.write("put 7\nput 15\nsub\nprint\n")
	input_file.close()
	assert eval_forth(strNameFile)==["8"]
	
	input_file = open(strNameFile,"w")
	input_file.write("put \"Kadabra\"\nput \"Abra\"\nadd\nprint\n")
	input_file.close()
	assert eval_forth(strNameFile)==["\"AbraKadabra\""]
	
	
	input_file = open(strNameFile,"w")
	input_file.write("put \"Abra\"\nput \"Kadabra\"\nsub\nprint\n")
	input_file.close()
	assert eval_forth(strNameFile)==["Can't subtract 'str' and 'int' objects","\"Kadabra\""]	
	
	input_file = open(strNameFile,"w")
	input_file.write("put \"12\"\nput 20\nadd\nprint\n")
	input_file.close()
	assert eval_forth(strNameFile)==["\"2012\""]
	
	input_file = open(strNameFile,"w")
	input_file.write("put 1\nput 2\nput 3\nput 4\nput 5\nput 6\nadd\nadd\nsub\nadd\nadd\nprint\n")
	input_file.close()	
	assert eval_forth(strNameFile)==["15"]
	
	input_file = open(strNameFile,"w")
	input_file.write("mov 1\nmov 1\nadd\nprint\n")
	input_file.close()
	assert eval_forth(strNameFile)==["Unknown command \"mov\"","Unknown command \"mov\"","Not enough operands.","Not enough operands."]
	
	os.remove("C:\input.txt")
	print "Tests Forth passed ok!"
def main():
	"main"
	testForth()
	return 0

if __name__ == "__main__":
	exit(main())
    

