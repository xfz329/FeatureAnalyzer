#   -*- coding:utf-8 -*-
#   The main.py in FeatureAnalyzer
#   created by Jiang Feng(silencejiang@zju.edu.cn)
#   created at 19:40 on 2022/3/26

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMessageBox

import data.Globalvar as gl
import ui.pingouin_methods as pm
import ui.subwindow as sub
from process.task_open import TaskOpen
from ui.main_basic import Ui_MainWindow
from utils.logger import Logger
from template.output_template import Template


class Global_MainWindow(Ui_MainWindow):
    def __init__(self):
        super(Global_MainWindow, self).__init__()
        gl.init_()
        self.current_file = None
        self.log = Logger('fa').get_log()
        self.swm = None
        self.taskOpen = TaskOpen(self.updateWinData,"open")
        self.m2p = {}               # method_to_set_parameters
        self.s2d = {}               # subwindows to display
        temp = Template()
        gl.set_value("output", temp)
        self.set_figure_path()

    def setupUi(self,MainWindow):
        super().setupUi(MainWindow)
        self.set_m2p()
        self.set_s2d()

        self.menu_5.setToolTipsVisible(True)
        # self.mdiArea.setActivationOrder(QMdiArea.WindowOrder.ActivationHistoryOrder)
        self.swm = sub.SubwindowManager(self.mdiArea)
        self.action_author.triggered.connect(self.show_author)
        self.action_logs.triggered.connect(self.show_changelogs)
        self.action_open.triggered.connect(self.open)
        self.menu_new_win.triggered.connect(self.create_new_subwindow)
        self.menu_kernel.triggered.connect(self.choose_kernel)
        self.action_cascadeSubWin.triggered.connect(self.mdiArea.cascadeSubWindows)
        self.action_tileSubWin.triggered.connect(self.mdiArea.tileSubWindows)
        self.action_draw.triggered.connect(self.draw)
        self.create_new_subwindow(self.action_win_data)

        # connect to pingouin parameter window
        self.menu_anova_ttest.triggered.connect(self.show_para_window)
        self.menu_bayesian.triggered.connect(self.show_para_window)
        # self.menu_circular.triggered.connect(self.show_para_window)
        self.menu_contingency.triggered.connect(self.show_para_window)
        self.menu_correlation_regression.triggered.connect(self.show_para_window)

        self.menu_effect_size.triggered.connect(self.show_para_window)

        self.menu_multivariate_tests.triggered.connect(self.show_para_window)

        self.menu_non_parametric.triggered.connect(self.show_para_window)
        self.menu_plotting.triggered.connect(self.show_para_window)
        self.menu_power_analysis.triggered.connect(self.show_para_window)
        self.menu_reliablility_consistency.triggered.connect(self.show_para_window)

        self.update_statusbar("?????????????????????")

    def set_figure_path(self):
        import os
        from pathlib import Path
        BASE_DIR = Path(__file__).resolve().parent
        FIG_PATH = os.path.join(BASE_DIR, 'figures')
        if not os.path.exists(FIG_PATH):
            os.makedirs(FIG_PATH)
        gl.set_value("FIG_PATH", FIG_PATH)

    def show_author(self):
        from help.author import author
        self.about_author = author.Ui_Author_MainWindow()
        self.update_statusbar("??????????????????")
        self.about_author.show()

    def show_changelogs(self):
        from help.changelogs import  changelogs
        self.about_changelogs = changelogs.Ui_Changelogs_MainWindow()
        self.update_statusbar("??????????????????")
        self.about_changelogs.show()

    def update_statusbar(self,msg):
        self.statusbar.clearMessage()
        datetime = QtCore.QDateTime.currentDateTime()
        text = datetime.toString("HH:mm:ss")
        self.statusbar.showMessage(text+"  "+msg, 5000)

    def choose_kernel(self):
        from PyQt5.QtWidgets import QMessageBox
        QMessageBox.information(None,"??????????????????","???????????????????????????????????????Pingouin???0.5.1????????????Pingouin?????????????????????SciPy.stats????????????????????????????????????????????????????????????????????????",QMessageBox.Ok)

    def open(self):
        win = self.swm.get_sub_window("Window_Data")
        self.log.info("add data to subwindow "+ win.windowTitle())
        gl.set_value("WinToAddData",win)
        self.taskOpen.set_worker()

    def updateWinData(self):
        win = gl.get_value("WinToAddData")
        df = self.taskOpen.get_ans()
        if df is not None:
            widget = win.widget()
            widget.model().setDataFrame(df)

    def draw(self):
        winD = self.swm.get_sub_window("Window_Data")
        if not winD.isPreparedToDraw():
            return
        winP = self.swm.get_sub_window("Window_Plot")
        self.log.info("draw plot to subwindow " + winP.windowTitle()+ " using selected data in subwindow " + winD.windowTitle())

        from process.Draw import Draw
        Draw().draw(winD,winP)

    def create_new_subwindow(self, action):
        name = action.objectName()
        win_type = self.s2d.get(name)
        self.swm.add_sub_window(win_type)

    def show_para_window(self, action):
        name = action.objectName()
        method_UI = self.m2p.get(name)
        if method_UI is not None:
            self.swm.add_sub_window(sub.SubWindow_Pingouin_basic,method_UI)
        else:
            QMessageBox.warning(None, "????????????????????????", "????????????????????????"+name, QMessageBox.Ok)

    def set_s2d(self):
        self.s2d.setdefault(self.action_win_data.objectName(), sub.SubWindow_Data)
        self.s2d.setdefault(self.action_win_plot_q.objectName(), sub.SubWindow_QCustomPlot)
        self.s2d.setdefault(self.action_win_plot_m.objectName(), sub.SubWindow_Matplot)
        self.s2d.setdefault(self.action_win_result.objectName(), sub.SubWindow_Result)
        self.s2d.setdefault(self.action_win_log.objectName(), sub.SubWindow_Logs)

    def set_m2p(self):
        # anova and t_test
        self.m2p.setdefault(self.action_anova.objectName(),pm.Ui_Anova_MainWindow)
        self.m2p.setdefault(self.action_ancova.objectName(),pm.Ui_Ancova_MainWindow)
        self.m2p.setdefault(self.action_rm_anova.objectName(),pm.Ui_RM_Anova_MainWindow)
        self.m2p.setdefault(self.action_epsilon.objectName(),pm.Ui_Epsilon_MainWindow)
        self.m2p.setdefault(self.action_mixed_anova.objectName(),pm.Ui_Mixed_Anova_MainWindow)
        self.m2p.setdefault(self.action_welch_anova.objectName(),pm.Ui_Welch_MainWindow)
        self.m2p.setdefault(self.action_tost.objectName(),pm.Ui_Tost_MainWindow)
        self.m2p.setdefault(self.action_ttest.objectName(),pm.Ui_Ttest_MainWindow)

        # bayesian
        self.m2p.setdefault(self.action_bayesfactor_binom.objectName(),pm.Ui_Bayesfactor_binom_MainWindow)
        self.m2p.setdefault(self.action_bayesfactor_ttest.objectName(),pm.Ui_Bayesfactor_ttest_MainWindow)
        self.m2p.setdefault(self.action_bayesfactor_pearson.objectName(),pm.Ui_Bayesfactor_pearson_MainWindow)

        # circular

        # contingency
        self.m2p.setdefault(self.action_chi2_independence.objectName(),pm.Ui_Chi2_independence_MainWindow)
        self.m2p.setdefault(self.action_chi2_mcnemar.objectName(),pm.Ui_Chi2_mcnemar_MainWindow)
        self.m2p.setdefault(self.action_dichotomous_crosstab.objectName(),pm.Ui_Dichotomous_crosstab_MainWindow)

        # correlation_regression
        self.m2p.setdefault(self.action_corr.objectName(),pm.Ui_Corr_MainWindow)
        self.m2p.setdefault(self.action_pairwise_corr.objectName(),pm.Ui_Pairwise_corr_MainWindow)
        self.m2p.setdefault(self.action_partial_corr.objectName(),pm.Ui_Partial_corr_MainWindow)
        self.m2p.setdefault(self.action_distance_corr.objectName(),pm.Ui_Distance_corr_MainWindow)
        self.m2p.setdefault(self.action_rm_corr.objectName(),pm.Ui_Rm_corr_MainWindow)

        # effect sizes
        self.m2p.setdefault(self.action_compute_effsize.objectName(),pm.Ui_Compute_effsize_MainWindow)
        self.m2p.setdefault(self.action_compute_effsize_from_t.objectName(),pm.Ui_Compute_effsize_from_t_MainWindow)
        self.m2p.setdefault(self.action_convert_effsize.objectName(),pm.Ui_Convert_effsize_MainWindow)

        # multivariate_normality
        self.m2p.setdefault(self.action_box_m.objectName(),pm.Ui_Box_m_MainWindow)
        self.m2p.setdefault(self.action_multivariate_normality.objectName(),pm.Ui_Multivariate_normality_MainWindow)


        # non_parametric
        self.m2p.setdefault(self.action_cochran.objectName(),pm.Ui_Cochran_MainWindow)
        self.m2p.setdefault(self.action_friedman.objectName(),pm.Ui_Friedman_MainWindow)
        self.m2p.setdefault(self.action_kruskal.objectName(),pm.Ui_Kruskal_MainWindow)
        self.m2p.setdefault(self.action_mad.objectName(),pm.Ui_Mad_MainWindow)
        self.m2p.setdefault(self.action_madmedianrule.objectName(),pm.Ui_Madmedianrule_MainWindow)
        self.m2p.setdefault(self.action_mwu.objectName(),pm.Ui_Mwu_MainWindow)
        self.m2p.setdefault(self.action_wilcoxon.objectName(),pm.Ui_Wilcoxon_MainWindow)
        self.m2p.setdefault(self.action_harrelldavis.objectName(),pm.Ui_Harrelldavis_MainWindow)

        # plotting
        self.m2p.setdefault(self.action_plot_blandaltman.objectName(),pm.Ui_Plot_blandaltman_MainWindow)
        self.m2p.setdefault(self.action_plot_paired.objectName(),pm.Ui_Plot_paired_MainWindow)
        self.m2p.setdefault(self.action_plot_shift.objectName(),pm.Ui_Plot_shift_MainWindow)
        self.m2p.setdefault(self.action_plot_rm_corr.objectName(),pm.Ui_Plot_rm_corr_MainWindow)
        self.m2p.setdefault(self.action_qqplot.objectName(),pm.Ui_Qqplot_MainWindow)

        # power_analysis
        self.m2p.setdefault(self.action_power_anova.objectName(),pm.Ui_Power_anova_MainWindow)
        self.m2p.setdefault(self.action_power_rm_anova.objectName(),pm.Ui_Power_rm_anova_MainWindow)
        self.m2p.setdefault(self.action_power_chi2.objectName(),pm.Ui_Power_chi2_MainWindow)
        self.m2p.setdefault(self.action_power_corr.objectName(),pm.Ui_Power_corr_MainWindow)
        self.m2p.setdefault(self.action_power_ttest.objectName(),pm.Ui_Power_ttest_MainWindow)
        self.m2p.setdefault(self.action_power_ttest2n.objectName(),pm.Ui_Power_ttest2n_MainWindow)


        # reliability_consistency
        self.m2p.setdefault(self.action_cronbach_alpha.objectName(),pm.Ui_Cronbach_alpha_MainWindow)
        self.m2p.setdefault(self.action_intraclass_corr.objectName(),pm.Ui_Intraclass_corr_MainWindow)





if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Global_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
