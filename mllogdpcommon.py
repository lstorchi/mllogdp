import numpy as np

def to_descriptor (orderedset, atomtypes):

    desc = np.zeros(len(orderedset))

    for at in atomtypes:
        idx = orderedset.index(at)

        desc[idx] += 1

    return desc

def import_descriptor (filename):
    fp = open(filename, "r")

    fp.readline()

    smilelogd = {}
    smilesetid = {}
    descriptors = []
    yval = []
    for l in fp:
        sline = l.split(",")
        smile = sline[1]
        logd = np.float64(sline[-1])
        vid = sline[2]

        descv = ' '.join(sline[3].split()).split(" ")

        descriptors.append([ np.int(v) for v in descv])

        smilelogd[smile] = logd
        smilesetid[smile] = vid
        yval.append(np.float(sline[-1]))
    
    fp.close()

    return smilelogd, \
            np.asarray(descriptors), \
            np.asarray(yval), smilesetid
