#!/usr/bin/env python
# -*- coding:utf8 -*-
"Haffman homework"
import os

def symbol_frequencies(path_file):
	"table symbol frequencies"
	"""
	Функция, подсчитывающая частоту символов в строке
	"""
	dictSumb = {}
	file = open(path_file,"r")
	strFile = file.read()
	
	i = 0
	while i < len(strFile):
		tmp = dictSumb.get(strFile[i],None)
		if tmp != None:
			dictSumb[strFile[i]] += 1
		else:
			dictSumb[strFile[i]] = 1		
		i += 1
	file.close()
	return dictSumb

def list_sort(listMass):
	"""
	Функция, сортирующая словарь по значениям
	"""
	listNewMass = []
	listValues = []
	for x in listMass:
		listValues.append(x[1])
	listValues.sort()
	for x in listValues:
		for elem in listMass:
			if x == elem[1]:
				listNewMass.append(elem)
				listMass.remove(elem)
				break
	return listNewMass
	
def make_symbol_code(dictSumb,path_file_pass):
	"""
	Функция, формирующая таблицу кодировки символов
	"""
	listKeys = dictSumb.items()
	while len(listKeys) > 1:
		listNewKeys = list_sort(listKeys)
		sum = listNewKeys[0][1] + listNewKeys[1][1]
		mass = [listNewKeys[0][0],listNewKeys[1][0]]
		listNewKeys.remove(listNewKeys[0])
		listNewKeys.remove(listNewKeys[0])
		listNewKeys.append([mass,sum])
		listKeys = listNewKeys[:]
	str = ""
	#dict_conformity={}
	listKeys_conformit = []
	Recurs(listKeys[0][0], str, listKeys_conformit)
	filePass = open(path_file_pass, "w")
	for x in listKeys_conformit:
		filePass.write(x[0] + "\n")
		filePass.write(x[1] + "\n")
	dict_conformity = dict(listKeys_conformit)
	filePass.close()
	return dict_conformity
	
def Recurs(treeTop, str, listSumb):
	"""
	Рекурсивная функция, выполняющая проход по веткам дерева
	"""
	if len(treeTop) == 2:
		str1 = str[:]
		str1 += "0"
		if len(treeTop[0]) == 2:				
			Recurs(treeTop[0], str1, listSumb)
		else:
			listSumb.append([treeTop[0], str1])
		str2 = str[:]
		str2 += "1"
		if len(treeTop[1]) == 2:
			Recurs(treeTop[1], str2, listSumb)
		else:
			listSumb.append([treeTop[1], str2])

def get_symbol_code_from_file(path_file_pass):
	"""
	Функция, формирующая таблицу кодировки символов из файла
	"""
	filePass = open(path_file_pass, "r")
	dict_pass = {}
	count_encode_bit = 0
	while True:
		str1 = filePass.readline()
		if str1 == "":
			break
		str2 = filePass.readline()
		if str2 == "":
			count_encode_bit = int(str1)
			break
		dict_pass[str1[0:-1]] = str2[0:-1]
	filePass.close()
	return dict_pass, count_encode_bit

def hf_encode(message, dict_pass):
	"""
	Кодирование входной строки(message) с исп. таблицы кодировки(dict_pass)
	"""
	byte = 0x00
	str_resul = ""
	counter = 0
	count_encode_bit=0
	flagByte = True
	for sym in message:
		for bit in dict_pass[sym]:
			flagByte = True
				
			if bit == '0':
				byte = byte << 1
				byte_mask1 = 0xFE
				byte = byte & byte_mask1
				counter += 1
				count_encode_bit += 1
			elif bit == '1':
				byte = byte << 1
				byte_mask1 = 0x01
				byte = byte | byte_mask1
				counter += 1
				count_encode_bit += 1
			if counter == 8:
				str_resul += chr(byte)
				byte = 0x00
				counter = 0
				flagByte = False
	if flagByte == True:
		str_resul += chr(byte)
		return str_resul, count_encode_bit 
		"""
		 str_resul - закодированная строка, 
		 count_encode_bit - колличество битов выходной строки
		"""


def hf_encode_file(path_file_input, path_file_output, path_file_pass):
	"""
	Кодирует файл "path_file_input" в файл "path_file_output"
	path_file_pass - таблица кодировки
	"""
	dict = make_symbol_code(symbol_frequencies(path_file_input), path_file_pass)
	file = open(path_file_input, "r")
	strFile = file.read()
	resultStr, count_encode_bit = hf_encode(strFile, dict)
	file_pass = open(path_file_pass, "a")
	file_pass.seek(0)
	file_pass.write(str(count_encode_bit) + "\n")
	
	saveFile = open(path_file_output, "w")
	saveFile.write(resultStr)

def hf_decode(dmessage, dict_pass, count_encode_bit):
	"""
	Декодирование входной строки(dmessage) с исп. таблицы кодировки(dict_pass)
	count_encode_bit - колличество закодированных битов
	"""
	byte = 0x00
	str_result = ""
	strCodeSym = ""
	dictPassList = dict_pass.items()
	j = 0
	while j < len(dmessage):		
		byte = ord(dmessage[j])
		if j != len(dmessage) - 1:
			i = 0
			while i < 8:
				byte_mask = 0x80
				rbyte = byte & byte_mask
				if rbyte == 0x00:
					strCodeSym += "0"
				elif rbyte == 0x80:
					strCodeSym += "1"
				byte = byte << 1
				for key, val in dictPassList:				
					if val == strCodeSym:
						str_result += key
						strCodeSym = ""
				i += 1
		else:
			i = 0
			byte = byte << (8 - count_encode_bit % 8)
			while i < count_encode_bit % 8:
				byte_mask = 0x80
				rbyte = byte & byte_mask
				if rbyte == 0x00:
					strCodeSym += "0"
				elif rbyte == 0x80:
					strCodeSym += "1"
				byte = byte << 1
				for key, val in dictPassList:				
					if val == strCodeSym:
						str_result += key
						strCodeSym = ""
				i += 1
		j += 1
	return str_result

def hf_decode_file(path_file_input, path_file_output, path_file_pass):
	"""
	Декодирует файл "path_file_input" в файл "path_file_output"
	path_file_pass - таблица кодировки
	"""
	dict,count_encode_bit = get_symbol_code_from_file(path_file_pass)
	file = open(path_file_input, "r")
	strFile = file.read()
	resultStr = hf_decode(strFile, dict, count_encode_bit)
	saveFile = open(path_file_output, "w")
	saveFile.write(resultStr)

def test_Haffman():
	"Testing of Haffman kripting"
	fileInput = open("C:\input1.txt", 'w')
	fileInput.write("abbccc")
	fileInput.close()
	hf_encode_file("C:\input1.txt", "C:\output1.bin", "C:\pass1.txt")
	filePass = open("C:\pass1.txt", "r") 
	assert filePass.read() == "c\n0\na\n10\nb\n11\n9\n"
	filePass.close()
	hf_decode_file("C:\output1.bin", "C:\input1_2.txt", "C:\pass1.txt")
	
	fileInput1 = open("C:\input1.txt", "r") 
	fileOutput1 = open("C:\output1.bin", "r")
	assert len(fileInput1.read()) >= len(fileOutput1.read())
	fileInput1.close()
	fileOutput1.close()
	
	fileInput1 = open("C:\input1.txt", "r") 
	fileInput1_2 = open("C:\input1_2.txt", "r") 
	assert fileInput1.read() == fileInput1_2.read()
	fileInput1.close()
	fileInput1_2.close()
	os.remove("C:\input1.txt")
	os.remove("C:\output1.bin")
	os.remove("C:\pass1.txt")
	os.remove("C:\input1_2.txt")
	
	print "Test passed ok!"
	
def main():
	"main"
	test_Haffman()
	return 0

if __name__ == "__main__":
	exit(main())