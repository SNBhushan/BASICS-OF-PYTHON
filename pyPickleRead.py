import pickle

fh=open("teamlist","rb")
contents=pickle.load(fh)
fh.close()
print("contenst",contents)
print("type",type(contents))
