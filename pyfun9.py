def playersdetails(name,age,team):
    print("player details:")
    print("name: {},age: {},team: {}".format(name,age,team))

playersdetails("virat",33,"rcb")


msd=("m s dhoni",33,"csk")
playersdetails(*msd)