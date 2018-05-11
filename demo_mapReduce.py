# -*- coding: UTF-8 -*-
def mapper(filename):
    with open(filename, "r") as f:
        _lines = f.readlines()
        tmpData = {}
        for _line in _lines:
            _line = _line.strip()
            if _line in tmpData:
                tmpData[_line] += 1
            else:
                tmpData[_line] = 1

    return tmpData


_dict = mapper('1.txt')
_dict2 = mapper('11.txt')

_arr = [_dict,_dict2]

_all = {}
for _dict in _arr:
    for k,v in _dict.items():
        if k in _all:
            _all[k] += v
        else:
            _all[k] = v


print _all