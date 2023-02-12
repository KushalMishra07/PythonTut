# Manipulate string value into a required format using python

class txtfunc():
    def __init__(self, woi):
        self.woi = woi

    def eval(woi):

        try:
            if woi is None:
                return None
            else:
                return parsed(woi)
        except:
            return None


def parsed(woi):
    ls = ['MRA', 'MCA', 'FCA']
    spacepos = int(woi.find(" "))
    hyphenpos = int(woi.find("-"))
    woilen = len(woi)
    print(hyphenpos)
    print(spacepos)
    if woi[0:3] in ls:
        return woi
    elif (spacepos != -1):
        if (hyphenpos != -1):
            print(woi[spacepos + 1:hyphenpos])
        elif (hyphenpos == -1):
            print(woi[0:spacepos])
    elif (spacepos == -1):
        if (hyphenpos != -1):
            print(woi[0:hyphenpos])
        elif woilen > 23:
            print(woi.rstrip(woi[-14:-1]))
        elif 14 < woilen < 18:
            print(woi.rstrip(woi[-6:-1]))
        elif woilen > 9 and woilen > 13:
            print(woi.rstrip(woi[:-1]))
    else:
        return None


og = txtfunc.eval("BCAKSHALIAKLHJBHB")
