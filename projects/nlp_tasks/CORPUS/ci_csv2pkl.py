with open('ci.csv', 'r') as fp:
    lines = fp.readlines()
fp.close()

ci = []
for line in lines:
    if ',' not in line:
        continue
    line = line.split(',')[0]
    ci.append(line)
import pickle
with open('ci.pkl', 'wb') as fp:
    pickle.dump(ci, fp)
fp.close()

