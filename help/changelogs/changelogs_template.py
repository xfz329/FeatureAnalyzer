#   -*- coding:utf-8 -*-
#   The author_template.py in FeatureAnalyzer
#   created by Jiang Feng(silencejiang@zju.edu.cn)
#   created at 14:08 on 2022/3/27

class Template:
    tmp = \
        """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <title>Title</title>
            <style type=text/css>
                h1 {text-align: left;font-family:Times New Roman;font-size: 30px}
                p.normal {text-align: left;font-family:Times New Roman;font-size: 14px;font-style:normal;}
                p.italic {text-align: left;font-family:Times New Roman;font-size: 14px;font-style:italic;}
            </style>
        </head>
        <body>
            %(versions)s
        </body>
        </html>
        """
    version = \
        """
        <h1>&emsp;%(num)s</h1>
        <p class= italic>&emsp;Released on %(date)s</p>
        %(features)s
        """

    feature = \
        """
        <p class= normal>&emsp;&emsp;%(feature)s</p>
        """

    def __init__(self):
        self.res = ""

    def get(self):
        f = ""
        f +=Template.feature % dict(feature = "确定基本程序框架")
        f += Template.feature % dict(feature="逻辑与页面分离")
        tab = ""
        tab += Template.version % dict(num = 0.01, date = "2022.03.27", features = f)
        self.res = Template.tmp % dict(versions = tab)
        # print(self.res)
        return self.res


if __name__ == "__main__":
    t= Template()
    t.get()







