from collections import OrderedDict

def PresentI(adjective : str, positive : bool):
    return adjective if positive else adjective[:-1] + "くない"

def PastI(adjective : str, positive : bool):
    return PresentI(adjective, positive)[:-1] + "かった"

def Conjugate(adjective : OrderedDict, past : bool, positive : bool):
    if (adjective['type'] == 'i'):
        if (adjective['japanese'] == 'いい'):
            return PastI("良い", positive) if past else "良くない" if not positive else adjective['japanese']
        else:
            return (PastI(adjective['japanese'], positive) if past else PresentI(adjective['japanese'], positive)) + "です"
    else:
        return adjective['japanese'][:-1] + ("です" if positive else "ではありません") + ("でした" if past else "")