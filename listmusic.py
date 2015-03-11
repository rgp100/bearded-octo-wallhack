from os import walk

f = []
for (dirpath, dirnames, filenames) in walk('./Music'):
    f.extend(filenames)
    break

#delete after troubleshoot
print f
