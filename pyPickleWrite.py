

import pickle

team = {
    "groupA" : ["India","Newzealand","England"],
    "groupB" : ["Aus","WI","SA"]
}
fh = open("teamlist","wb")
pickle.dump(team,fh)

fh.close()
