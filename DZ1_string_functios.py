#!/usr/bin/env python
# -*- coding:utf8 -*-
"DZ1_Part1"

def xfind(str1, str2):
	"find"
	result=-1
	if len(str1)==0:
		return result
	if len(str2)==0:
		return 0
	
	i=0
	while i<len(str1):
		if str1[i]==str2[0]:
			isEquals=True
			j=1
			while j<len(str2):
				if i+j<len(str1):
					if str2[j]==str1[i+j]:
						isEquals=True
					else:
						isEquals=False
						break
					j+=1
				else:
					return result
			if isEquals==True:
				result = i
				break
		i+=1
	return result

def xreplace(str1, str2, str3):
	"replace"
	if len(str2)==0:
		rezStr=str3
		i=0
		while i<len(str1):
			rezStr+=str1[i]+str3
			i+=1
		return rezStr
	
	ListSubs=[]
	reStr1=str1
	while True:
		fId = xfind(reStr1, str2)
		if fId !=-1:				
			subStr1=reStr1[:(fId)]
			reStr1=reStr1[(fId+len(str2)):]
			ListSubs.append(subStr1+str3)
			
		else:
			ListSubs.append(reStr1)
			resultStr=""
			for str in ListSubs:
				resultStr+=str
			return resultStr	
	return str1

def xsplit(str1, str2):
	ListSubs=[]
	reStr1=str1
	if len(str2)==0:
		for sym in str1:
			ListSubs.append(sym)
		return ListSubs
	
	while True:
		fId = xfind(reStr1, str2)
		if fId !=-1:				
			subStr1=reStr1[:(fId)]
			reStr1=reStr1[(fId+len(str2)):]
			ListSubs.append(subStr1)			
		else:
			ListSubs.append(reStr1)
			break
	return ListSubs

def xjoin(s, array):
	rezStr=str(array[0])
	i=1
	while i<len(array):
		rezStr+=(s+str(array[i]))
		i+=1
	return rezStr
	
def test_xfind():
	"unit test for xfind function"  
	s1="abcd"	
	s2="bc"
	assert xfind(s1, s2) == s1.find(s2)
	s1="abcb"	
	s2="b"
	assert xfind(s1, s2) == s1.find(s2)
	s1="abcd"	
	s2="cc"
	assert xfind(s1, s2) == s1.find(s2)
	s1="abcd"	
	s2="bcdsg"
	assert xfind(s1, s2) == s1.find(s2)
	s1="abcd"	
	s2=""
	assert xfind(s1, s2) == s1.find(s2)
	s1=""
	s2="abcd"	
	assert xfind(s1, s2) == s1.find(s2)
	s1="abcd"	
	s2="abcd"
	assert xfind(s1, s2) == s1.find(s2)
	s1="abcd"	
	s2="+"
	assert xfind(s1, s2) == s1.find(s2)
	s1="ab cd"	
	s2="bc"
	assert xfind(s1, s2) == s1.find(s2)
	print "Tests xfind ok!"

def test_xreplace():
	"unit test for xreplace function"  
	s1="abcd"	
	s2="bc"
	s3="bc2"
	assert xreplace(s1, s2, s3) == s1.replace(s2,s3)
	s1="abcdaf"	
	s2="a"
	s3="7"
	assert xreplace(s1, s2, s3) == s1.replace(s2,s3)	
	s1="abcdaf"	
	s2="x"
	s3="!"
	assert xreplace(s1, s2, s3) == s1.replace(s2,s3)
	s1="abcdaf"	
	s2="123"
	s3="!"
	assert xreplace(s1, s2, s3) == s1.replace(s2,s3)
	s1="abcaffca"	
	s2="ca"
	s3="55"
	assert xreplace(s1, s2, s3) == s1.replace(s2,s3)
	s1="afcaffca"	
	s2="fca"
	s3=","
	assert xreplace(s1, s2, s3) == s1.replace(s2,s3)
	s1="afcaffca"	
	s2="f"
	s3="FAUST"
	assert xreplace(s1, s2, s3) == s1.replace(s2,s3)
	s1="aOcaOOca"	
	s2="O"
	s3="O"
	assert xreplace(s1, s2, s3) == s1.replace(s2,s3)
	s1="direct"	
	s2="directory"
	s3="dir"
	assert xreplace(s1, s2, s3) == s1.replace(s2,s3)
	s1="1234"	
	s2=""
	s3="dir"
	assert xreplace(s1, s2, s3) == s1.replace(s2,s3)
	s1="direct"	
	s2="dir"
	s3=""
	assert xreplace(s1, s2, s3) == s1.replace(s2,s3)
	s1=""	
	s2="dir"
	s3="direct"
	assert xreplace(s1, s2, s3) == s1.replace(s2,s3)
	print "Tests xreplace ok!"

def test_xsplit():
	s1="ab as df gx"
	s2=" "
	assert xsplit(s1,s2)==s1.split(s2)
	s1="b as df gx"
	s2="a"
	assert xsplit(s1,s2)==s1.split(s2)
	s1="ab as df gx"
	s2="as1993 and as1992"
	assert xsplit(s1,s2)==s1.split(s2)
	s1="eax999ebx999ecx999edx999"
	s2="999"
	assert xsplit(s1,s2)==s1.split(s2)
	s1="comand"
	s2="C"
	assert xsplit(s1,s2)==s1.split(s2)
	s1="qwszdfzgpqwszdfzgyqwszdfzgtqwszdfzghqwszdfzgoqwszdfzgnqwszdfzg"
	s2="qwszdfzg"
	print xsplit(s1,s2)
	assert xsplit(s1,s2)==s1.split(s2)
	s1=""
	s2="comand"
	assert xsplit(s1,s2)==s1.split(s2)
	s1="ab as df gx"
	s2=""
	print xsplit(s1,s2)
	#print s1.split(s2)
	#assert xsplit(s1,s2)==s1.split(s2)  # Unfortunately, the default function split don't work with splitter ""
	print "Tests xsplit ok!"

def test_xjoin():	
	s=","
	array=["1","2","3","4","5","6","7","8"]
	assert xjoin(s,array)==s.join(array)
	s=""
	array=["1","2","3","4","5","6","7","8"]
	assert xjoin(s,array)==s.join(array)
	s="Julia"
	array=["1","2","3","4","5","6","7","8"]
	assert xjoin(s,array)==s.join(array)
	s=" & "
	array=["Julia","Vlad"]	
	assert xjoin(s,array)==s.join(array)
	s=","
	array=[" ",""," "]
	assert xjoin(s,array)==s.join(array)
	s="b"
	array=["a"]
	assert xjoin(s,array)==s.join(array)
	print "Tests xjoin ok!"
	
def main():
    "main"
    test_xfind()
    test_xreplace()
    test_xsplit()
    test_xjoin()	
    return 0

if __name__ == "__main__":
    exit(main())
    

