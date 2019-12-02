import re
import os
priority = { "TopSecret":1,"Secret":2,"Classified":3,"Unclassified":4 }
prefix = "/home/saran/Desktop/sem7//security_lab/new/Bell-la-Padula/"

def get_access_list():
	file = open("users.txt")
	d={}
	for line in file.readlines():
		line = re.sub("\s","",line)
		l = re.split(":|,",line)

		d[l[0]]=[]
		for i in range(1,len(l)):
			d[l[0]].append(l[i])
	file.close()
	return d

def get_level(user_access,name):
	for l in user_access:
		if name in user_access[l]:
			return l
	return None
 
def get_order(level):
	return priority[level]

def file_list(folder):
	files = os.listdir(prefix+folder)
	l1 = []
	l2 = []
	for f in files:
		l1.append(f)
		l2.append(folder+"/"+f)
	return l1,l2

def read_access(level):
	l=[]
	order = get_order(level)
	for i in priority:
		if priority[i]>=order:
			l.append(i)
	return l

def print_file(path):
	file = open(path)
	str = file.read()
	print(str)

def read_file(level):
	c=0
	l=[]
	for i in read_access(level):
		files,path=file_list(i)
		for f in files:
			print(c,f)
			c+=1
			l.append((c,f,i+"/"+f))
	print ("file no?")
	n = int(input())
	#n = int(n)
	print(l[n][2])
	print_file(l[n][2])

def write_file(level):
	print("filename ?")
	filename = input()
	print("content ?")
	content = input()
	
	file = open(level+"/"+filename,"w")
	file.write(content)
	file.close()			

def write_access(level):
	l=[]
	order = get_order(level)
	for i in priority:
		if priority[i]==order:
			l.append(i)
	return l

def print_access(level):
	print ("\n\nRead Permissions")
	for i in read_access(level):
		print ("\n"+i.upper())
		files,path = file_list(i)
		for f in files:
			print(f)
			
	print ("\n\nWrite Permissions")
	for i in write_access(level):
		print ("\n"+i.upper())
		files,path = file_list(i)
		for i in files:
			print(i)
 
def access_files(name,level):
	print_access(level)
	choice = input("Read r or Write w\n")

	if choice == "r":
		read_file(level)
	if choice == "w":
		write_file(level)	


if __name__ == "__main__":
	user_access = get_access_list()
	name = "sw1"
	level = get_level(user_access,name)

	if level == None:
		print ("User Not Found")
	else:
		access_files(name,level)
