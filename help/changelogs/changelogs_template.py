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

    latest_version = "0.03"

    latest_date = "2022.03.30"

    def __init__(self):
        self.res = ""

    def get(self):
        tab = ""

        f = ""
        f += Template.feature % dict(feature="MDI的子窗口类型增加至4种（数据图表、绘图、日志及输出）")
        f += Template.feature % dict(feature="完善MDI多窗口管理的逻辑")
        f += Template.feature % dict(feature="增加对QCustomPlot（2.01）的绘图支持，增加图形的所发、拖拽等控制功能")
        f += Template.feature % dict(feature="部分API调整")
        f += Template.feature % dict(feature="Bug修复")
        tab += Template.version % dict(num=0.03, date="2022.03.30", features=f)

        f = ""
        f += Template.feature % dict(feature="增加MDI设计")
        f +=Template.feature % dict(feature = "增加对qtpandas（1.04）的支持")
        f += Template.feature % dict(feature="增加数据读取与数据绘制接口")
        tab += Template.version % dict(num = 0.02, date = "2022.03.28", features = f)

        f = ""
        f +=Template.feature % dict(feature = "确定基本程序框架")
        f += Template.feature % dict(feature="逻辑与页面分离")
        tab += Template.version % dict(num = 0.01, date = "2022.03.27", features = f)
        self.res = Template.tmp % dict(versions = tab)
        # print(self.res)
        return self.res


if __name__ == "__main__":
    t= Template()
    t.get()







