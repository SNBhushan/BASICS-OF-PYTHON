# kwargs==>dict
def player(**kwargs):
    print("type:",type(kwargs))
    print("KKwargs:",kwargs)
    print("players: name:{],class:{},stream:{}".format(kwargs["name"],kwargs["class"],kwargs["stream"]))

    
player("name":"bhushan",class:10,stream:"mech")