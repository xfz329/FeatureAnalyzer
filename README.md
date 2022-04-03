# FeatureAnalyzer

##  手动安装qtpandas 最新版本
* 从[qtpandas](https://github.com/draperjames/qtpandas)主页Code处下载zip文件，手动编译安装1.0.4版本
* 解压缩，启动终端，切换到解压后的文件夹，注意如果使用python的虚拟环境要灵活切换
* 输入代码，先编译再安装
~~~python
python setup.py build
python setup.py install
~~~
## 修改代码
由于qtpandas 使用的pandas版本太低，部分api 已经进行了调整，需要我们手动修改代码才能正确运行，参考[博文](https://www.cnblogs.com/i-am-sailing/p/13739815.html)具体而言包括：
1. ModuleNotFoundError: No module named 'pandas.tslib'
* 出错位置 qtpandas\views\EditDialogs.py
* 语句 from pandas.tslib import NaTType
* 修改成 from pandas._libs.lib import *
* line 17 in File  EditDialogs.py

2. ImportError: Missing optional dependency 'openpyxl'.  Use pip or conda to install openpyxl.
* 出错位置 pandas\compat\_optional.py", line 141, in import_optional_dependency raise ImportError(msg)
* 修改 安装openpyxl

3. AttributeError: 'DataFrame' object has no attribute 'ix'
* 出错位置 qtpandas\models\DataFrameModel.py", line 396, in data  result = convertValue(row, col, columnDtype)
* 修改 DataFrameModel.py 凡在对DataFrame的操作中使用了“.ix[row_index, column_index]”或类似操作的，多处，将.ix 改成.loc
* line 366,368,376,380,394,408 in File DataFrameModel.py

4. 此时双击表格会出现 AttributeError: 'QDrag' object has no attribute 'start'
* 出错位置 qtpandas\views\DataTableView.py", line 70, in mouseMoveEvent self.startDrag(self.indexAt(event.pos()))
* 'start' was renamed to 'exec_' in Qt 4.3.
* 修改 start为exec_
* line 66 in File DataTableView.py

5. 双击编辑表格出出现 AttributeError: 'DataFrame' object has no attribute 'set_value'
* 出错位置qtpandas\models\DataFrameModel.py", line 497, in setData self._dataFrame.set_value(row, col, value)
* 修改 self._dataFrame.set_value(row, col, value)  为 self._dataFrame.at[row, col] = value
* line 397 in File DataFrameModel.py

6.   name 'NaTType' is not defined
* 出错位置 qtpandas\views
* 修改 if isinstance(defaultValue, NaTType): 为  if isinstance(defaultValue, type(pandas.NaT)):  同时在顶部导入包 import pandas
* line 177 in File  EditDialogs.py
