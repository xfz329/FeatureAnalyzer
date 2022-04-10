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
                dt {text-align: left;font-family:Times New Roman;font-size: 30px}
                dd.normal {text-align: left;font-family:Times New Roman;font-size: 14px;font-style:normal;}
                dd.italic {text-align: left;font-family:Times New Roman;font-size: 14px;font-style:italic;}
            </style>
        </head>
        <body>
            <dl>
            %(versions)s
            </dl>
        </body>
        </html>
        """
    version = \
        """
        <dt>&emsp;%(num)s</dt>
        <dd class= italic>&emsp;Released on %(date)s</dd>
        %(features)s
        """

    feature = \
        """
        <dd class= normal>&emsp;&emsp;%(feature)s</dd>
        """

    latest_version = "0.07"

    latest_date = "2022.04.10"

    def __init__(self):
        self.res = ""

    def get(self):
        tab = ""

        f = ""
        f += Template.feature % dict(feature="完成Pingouin绝大多数模块功能代码的可视化移植")
        f += Template.feature % dict(feature="调整了pingouin函数的参数设置界面")
        f += Template.feature % dict(feature="增加了一种新的图像窗口以确保pingouin的图形输出")
        f += Template.feature % dict(feature="Bug修复")
        tab += Template.version % dict(num=0.07, date="2022.04.10", features=f)

        f = ""
        f += Template.feature % dict(feature="说明文件中增加qtpandas的配置说明")
        f += Template.feature % dict(feature="增加了打包发布的nsis代码控制")
        f += Template.feature % dict(feature="增加了pingouin函数的参数设置界面")
        f += Template.feature % dict(feature="调整了线程控制任务的逻辑控制")
        f += Template.feature % dict(feature="完成Pingouin中Anova与T-test模块所有代码的可视化移植")
        f += Template.feature % dict(feature="Bug修复")
        tab += Template.version % dict(num=0.06, date="2022.04.06", features=f)

        f = ""
        f += Template.feature % dict(feature="数据统计的参数设置界面，可以自由定制")
        f += Template.feature % dict(feature="重新设计了线程控制任务的逻辑")
        f += Template.feature % dict(feature="部分API调整")
        f += Template.feature % dict(feature="Bug修复")
        tab += Template.version % dict(num=0.05, date="2022.04.02", features=f)

        f = ""
        f += Template.feature % dict(feature="资源文件更新")
        f += Template.feature % dict(feature="重新设计了MDI多窗口管理类，调整其控制逻辑")
        f += Template.feature % dict(feature="引入线程以改善耗时任务的处理导致主UI线程失去响应")
        f += Template.feature % dict(feature="增加数据统计的参数设置界面")
        f += Template.feature % dict(feature="部分API调整")
        f += Template.feature % dict(feature="Bug修复")
        tab += Template.version % dict(num=0.04, date="2022.04.01", features=f)

        f = ""
        f += Template.feature % dict(feature="MDI的子窗口类型增加至4种（数据图表、绘图、日志及输出）")
        f += Template.feature % dict(feature="完善MDI多窗口管理的逻辑")
        f += Template.feature % dict(feature="增加对QCustomPlot（2.01）的绘图支持，增加图形的缩放、拖拽等控制功能")
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







