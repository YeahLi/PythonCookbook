large_file = open(filepath, "r")
new_file = open(newFilepath, "w+")

#Read data from a large file and write it into a new file
while True:
    content = large_file.read(1024)
 
    if len(content)==0:
        break
 
    new_file.write(content)

large_file.close()
new_file.close()