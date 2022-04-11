#   -*- coding:utf-8 -*-
#   The output_template.py in FeatureAnalyzer
#   created by Jiang Feng(silencejiang@zju.edu.cn)
#   created at 19:39 on 2022/4/10

tmp = \
"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Title</title>
<style type=text/css>
    dt {text-align: left;font-family:Times New Roman;font-size: 30px}
    dd.normal {text-align: left;font-family:Times New Roman;font-size: 14px;font-style:normal;}
    dd.italic {text-align: left;font-family:Times New Roman;font-size: 14px;font-style:italic;}
</style>
</head>
<body>
%(static)s
</body>
</html>
"""
static = \
""" <h1> %(head)s </h1>
    <p>  %(desc)s </p>
    <p>  命令开始时间 %(s_time)s </p>
    <p>  命令结束时间 %(e_time)s </p>
    <p>  %(duration)s </p>
    <dt> 入口参数  </dt>
    <dd>
    <dl>
    %(parameters)s
    </dl>
    </dd>
    <dt> 运算结果  </dt>
    <dd>
    <dl>
    %(result)s
    </dl>
    </dd>
"""

paras = \
"""     <dt> %(key)s </dt>    
        <dd> %(value)s </dd>
"""

result = \
"""     <dt> %(key)s </dt>    
        <dd> %(value)s </dd>
"""

fig = \
"""
    <img src = %(path)s>
"""
import pandas as pd
import numpy
class Template:

    def __init__(self):
        self.out = ""
        self.stat = ""
        self.keys ={}

    def get(self):
        # with open("test.html","w",encoding="utf-8") as outfile:
        #     outfile.write(self.out)
        return self.out

    def add(self, desc, para, ans = None):
        self.keys.clear()
        self.keys.setdefault("head",desc["detail"])
        self.keys.setdefault("desc",desc["brief"])
        self.keys.setdefault("s_time",desc["start_time"])
        self.keys.setdefault("e_time",desc["finish_time"])
        self.keys.setdefault("duration","未计算")
        self.keys.setdefault("parameters", self.update_para(para))
        self.keys.setdefault("result", self.update_ans(desc,ans))

        self.stat += static %self.keys
        self.out = tmp % dict(static = self.stat)

    def update_para(self,para):
        p = ""
        for k in para:
            if type(para[k]) == pd.core.frame.DataFrame:
                temp = paras % dict(key = k, value = "type(DataFrame)")
            else:
                temp = paras % dict(key=k, value=para[k])
            p += temp
        return p

    def update_ans(self, desc, ans):
        if ans is None:
            return fig % dict(path = desc["path"])
        elif type(ans) is pd.core.frame.DataFrame:
            from tabulate import tabulate
            return tabulate(ans, headers="keys", showindex=False, floatfmt=".3f",tablefmt="html")
        elif type(ans) is float or type(ans) is numpy.float64:
            return str(ans)



if __name__ == "__main__":
    t= Template()
    t.get()