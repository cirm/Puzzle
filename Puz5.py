import pickle

file = pickle.load(open("banner.p", "rb"))

x = (len(file))

for item in file:
    print(''.join(item[z][0]*item[z][1] for z in range(len(item))))
