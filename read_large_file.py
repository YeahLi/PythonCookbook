filepath = "README.md"
newFilepath = "copy_test.txt"
try:
	with open(filepath, "r") as large_file:
		with open(newFilepath, "w") as new_file:
			#Read data from a large file and write it into a new file
			while True :
				content = large_file.read(1024)
				if len(content)==0:
					break
				new_file.write(content)
except Exception as e:
	raise e