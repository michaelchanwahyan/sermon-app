import os

flist = os.listdir('./JNG')
for fname in flist:
    #print(fname)
    with open(fname, 'r') as fp:
        text = fp.read()
    fp.close()
    #print(text[:10])
    if '\n'*10 in text:
        #print('!!!!!!!!!!!     BING     !!!!!!!!!')
        print(fname)
