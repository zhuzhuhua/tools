# -*- coding: UTF-8 -*-
import os,sys

_init=\
"""# -*- coding: UTF-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf8')

##########
if __name__ == '__main__':
    print "初始化成功"
"""
class Tools:
    def __init__(self):
        self.new()

    def new(self):
        if len(sys.argv)>1:
            newfile = sys.argv[1]
        else:
            newfile = "init2.py"
        with open(newfile, "w") as file:
            #file.seek(0)  游标从0开始
            #last_site = file.tell()  更新游标位置
            file.write(_init)
            file.close()


# cmd = "python /Users/zhuyun/PycharmProjects/tools/init2.py"
# print os.system(cmd)



if __name__ == '__main__':
    t = Tools()