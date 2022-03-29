#   -*- coding:utf-8 -*-
#   The title.py in FeatureAnalyzer
#   created by Jiang Feng(silencejiang@zju.edu.cn)
#   created at 15:42 on 2022/3/29

class Title:

    def __init__(self, win_type, prefix):
        self.type = win_type
        self.prefix = prefix
        self.count = 0

    def get_new_title(self):
        self.count += 1
        return self.prefix + "-" + str(self.count), self.prefix

    def is_winType(self,win_type):
        return self.type == win_type