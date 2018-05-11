# -*- coding:utf-8 -*-



import os.path

class PinYinMixin:
    '''中文处理'''


    def __init__(self, dict_file='word.data'):
        self.word_dict = {}
        self.dict_file = dict_file

    def load_word(self):
        if not os.path.exists(self.dict_file):
            raise IOError("NotFoundFile")

        with file(self.dict_file) as f_obj:
            for f_line in f_obj.readlines():
                try:
                    line = f_line.split('    ')
                    self.word_dict[line[0]] = line[1]
                except:
                    line = f_line.split('   ')
                    self.word_dict[line[0]] = line[1]

    def cn2pinyin(self, string=""):
        result = []
        if not isinstance(string, unicode):
            string = string.decode("utf-8")

        for char in string:
            key = '%X' % ord(char)
            if not self.word_dict.get(key):    #加一条判断，当碰到非汉字的时候原字符保留
                result.append(char)
            else:
                result.append(self.word_dict.get(key, char).split()[0][:-1].lower())
        return result


    def get_cn_first_letter(self, str, codec="unicode"):
        if codec != "GBK":
            if codec != "unicode":
                str = str.decode(codec)
            str = str.encode("GBK")

        if str < "\xb0\xa1" or str > "\xd7\xf9":
            return ""
        if str < "\xb0\xc4":
            return "a"
        if str < "\xb2\xc0":
            return "b"
        if str < "\xb4\xed":
            return "c"
        if str < "\xb6\xe9":
            return "d"
        if str < "\xb7\xa1":
            return "e"
        if str < "\xb8\xc0":
            return "f"
        if str < "\xb9\xfd":
            return "g"
        if str < "\xbb\xf6":
            return "h"
        if str < "\xbf\xa5":
            return "j"
        if str < "\xc0\xab":
            return "k"
        if str < "\xc2\xe7":
            return "l"
        if str < "\xc4\xc2":
            return "m"
        if str < "\xc5\xb5":
            return "n"
        if str < "\xc5\xbd":
            return "o"
        if str < "\xc6\xd9":
            return "p"
        if str < "\xc8\xba":
            return "q"
        if str < "\xc8\xf5":
            return "r"
        if str < "\xcb\xf9":
            return "s"
        if str < "\xcd\xd9":
            return "t"
        if str < "\xce\xf3":
            return "w"
        if str < "\xd1\x88":
            return "x"
        if str < "\xd4\xd0":
            return "y"
        if str < "\xd7\xf9":
            return "z"


    def get_cn_first_letters(self, cn_str):
        #cn_str = cn_str.decode('utf8')

        S = ''
        for s in cn_str:
            S += self.get_cn_first_letter(s)
        return S

if __name__ == '__main__':
    cn = PinYinMixin()
    print cn.get_cn_first_letters('柯发通'.decode('UTF8'))