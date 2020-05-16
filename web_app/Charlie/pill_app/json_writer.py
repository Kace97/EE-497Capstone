import os
import json
from shutil import copyfile
import numpy as np

def write_to_file(pill_num, file_name, data):
	in_db = False
	file_contents = []
	code = None
	if pill_num > 1:
		file_contents = prep_file(file_name)
	
	if len(file_contents) > 0:
		for pill in file_contents:
			if pill_num == pill["Pill Number"]:
				in_db = True
				code = pill["Code"]
				print("Already in database")
	
	if not in_db:	
		b = data.tolist()
		d = {"Pill Number" : pill_num, "Code" : b}
		f = open(file_name, "a")
		if os.stat(file_name).st_size == 0:
			f.write("[\n")
		else:
			f.write(",\n")
		f.writelines(json.dumps(d, indent=2))
		f.close()
	return code

def get_data_from_file(file_name, pillID):

	data = prep_file(file_name)
	dic_code = "not found"
	num = "not found"
	
	for pill in data:
		pill_code = pill["Code"]
		if pill_code == dic_code:
			num = str(pill["Pill Number"])
			print("Is this pill " + num)
			return dic_code, num
	
	return pill_code
	
def prep_file(src):
	
	if os.stat(src).st_size == 0:
		data = None
	else:
		copyfile(src, "json/tmp.json")
		f = open("json/tmp.json", "a")
		f.write(']')
		f.close()
		with open("json/tmp.json") as jfile:
			data = json.load(jfile)
	os.remove("json/tmp.json")
	return np.array(data)
