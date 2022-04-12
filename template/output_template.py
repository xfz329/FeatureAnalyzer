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
    h1 {text-align: left;font-family:Times New Roman;font-size: 30px}
    p   {text-align: left;font-family:Times New Roman;font-size: 20px}
    dt {text-align: left;font-family:Times New Roman;font-size: 20px}
    dd.normal {text-align: left;font-family:Times New Roman;font-size: 18px;font-style:normal;}
    dd.italic {text-align: left;font-family:Times New Roman;font-size: 18px;font-style:italic;}
    table, th, td {border: 1px solid black;}
    table {border-collapse: collapse;}
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
    <dt><strong> 运行时间 </strong></dt>
    <dd class = italic>  命令开始时间 %(s_time)s </dd>
    <dd class = italic>  命令结束时间 %(e_time)s </dd>
    <dd class = italic>  命令运行时间 %(duration)s </dd>
    <dt><strong> 入口参数 </strong></dt>
    <dd>
    <dl>
    %(parameters)s
    </dl>
    </dd>
    <dt><strong> 运算结果 </strong></dt>
    <dd>
    <dl>
    %(result)s
    </dl>
    </dd>
"""

paras = \
"""     <dt><strong> %(key)s </strong></dt>    
        <dd class = normal> %(value)s </dd>
"""

result = \
"""     <dt> %(key)s </dt>    
        <dd class = normal> %(value)s </dd>
"""

fig = \
"""
    <dd class = normal>图片已存储为 %(path)s </dd>
    <dd class = normal><img src = "%(path)s" alt = %(path)s width = 600 height = 450></dd>
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
        self.keys.setdefault("s_time",desc["start_time"].toString("HH:mm:ss.zzz"))
        self.keys.setdefault("e_time",desc["finish_time"].toString("HH:mm:ss.zzz"))

        self.keys.setdefault("duration",self.get_duration(desc["start_time"],desc["finish_time"]))
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
            return str(round(ans,3))
        else:
            # 多个dataframe 如何处理 ch2——independent

            return str(ans)

    def get_duration(self,s,e):
        duration = s.msecsTo(e)
        h = int(duration/(3600 *1000))
        m = int((duration - h*3600*1000)/(60*1000))
        s = int((duration - h*3600*1000 - m*60*1000)/1000)
        ms = int(duration%1000)
        duration = "%s:%s:%s.%s" %(str(h).zfill(2),str(m).zfill(2),str(s).zfill(2),str(ms).zfill(3))
        return duration



if __name__ == "__main__":
    t= Template()
    t.get()