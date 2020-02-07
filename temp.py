import pickle
file = open("data\\nastr",'wb')
pickle.dump({}, file)
file.close()