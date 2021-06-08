fh=open("FileExample.txt")

strcontents=fh.read()
fh.close()

print("File content:",strcontents)
print("type of strcontents:",type(strcontents))