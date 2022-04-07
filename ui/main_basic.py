# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_basic.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1131, 733)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/pic/fig/cbeis.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.mdiArea = QtWidgets.QMdiArea(self.centralwidget)
        self.mdiArea.setObjectName("mdiArea")
        self.gridLayout.addWidget(self.mdiArea, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1131, 22))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        self.menu_3 = QtWidgets.QMenu(self.menubar)
        self.menu_3.setObjectName("menu_3")
        self.menu_new_win = QtWidgets.QMenu(self.menu_3)
        self.menu_new_win.setObjectName("menu_new_win")
        self.help = QtWidgets.QMenu(self.menubar)
        self.help.setObjectName("help")
        self.menu_5 = QtWidgets.QMenu(self.menubar)
        self.menu_5.setObjectName("menu_5")
        self.menu_kernel = QtWidgets.QMenu(self.menu_5)
        self.menu_kernel.setObjectName("menu_kernel")
        self.menu_anova_ttest = QtWidgets.QMenu(self.menu_5)
        self.menu_anova_ttest.setObjectName("menu_anova_ttest")
        self.menu_bayesian = QtWidgets.QMenu(self.menu_5)
        self.menu_bayesian.setObjectName("menu_bayesian")
        self.menu_circular = QtWidgets.QMenu(self.menu_5)
        self.menu_circular.setObjectName("menu_circular")
        self.menu_correlation_regression = QtWidgets.QMenu(self.menu_5)
        self.menu_correlation_regression.setObjectName("menu_correlation_regression")
        self.menu_contingency = QtWidgets.QMenu(self.menu_5)
        self.menu_contingency.setObjectName("menu_contingency")
        self.menu_distribution = QtWidgets.QMenu(self.menu_5)
        self.menu_distribution.setObjectName("menu_distribution")
        self.menu_effect_size = QtWidgets.QMenu(self.menu_5)
        self.menu_effect_size.setObjectName("menu_effect_size")
        self.menu_4 = QtWidgets.QMenu(self.menu_5)
        self.menu_4.setObjectName("menu_4")
        self.menu_multivariate_tests = QtWidgets.QMenu(self.menu_5)
        self.menu_multivariate_tests.setObjectName("menu_multivariate_tests")
        self.menu_others = QtWidgets.QMenu(self.menu_5)
        self.menu_others.setObjectName("menu_others")
        self.menu_reliablility_consistency = QtWidgets.QMenu(self.menu_5)
        self.menu_reliablility_consistency.setObjectName("menu_reliablility_consistency")
        self.menu_non_parametric = QtWidgets.QMenu(self.menu_5)
        self.menu_non_parametric.setObjectName("menu_non_parametric")
        self.menu_plotting = QtWidgets.QMenu(self.menu_5)
        self.menu_plotting.setObjectName("menu_plotting")
        self.menu_power_analysis = QtWidgets.QMenu(self.menu_5)
        self.menu_power_analysis.setObjectName("menu_power_analysis")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action_open = QtWidgets.QAction(MainWindow)
        self.action_open.setObjectName("action_open")
        self.action_author = QtWidgets.QAction(MainWindow)
        self.action_author.setObjectName("action_author")
        self.action_logs = QtWidgets.QAction(MainWindow)
        self.action_logs.setObjectName("action_logs")
        self.action_tileSubWin = QtWidgets.QAction(MainWindow)
        self.action_tileSubWin.setObjectName("action_tileSubWin")
        self.action_cascadeSubWin = QtWidgets.QAction(MainWindow)
        self.action_cascadeSubWin.setObjectName("action_cascadeSubWin")
        self.action_draw = QtWidgets.QAction(MainWindow)
        self.action_draw.setObjectName("action_draw")
        self.action_win_data = QtWidgets.QAction(MainWindow)
        self.action_win_data.setObjectName("action_win_data")
        self.action_win_plot_q = QtWidgets.QAction(MainWindow)
        self.action_win_plot_q.setObjectName("action_win_plot_q")
        self.action_win_plot_m = QtWidgets.QAction(MainWindow)
        self.action_win_plot_m.setObjectName("action_win_plot_m")
        self.action_win_log = QtWidgets.QAction(MainWindow)
        self.action_win_log.setObjectName("action_win_log")
        self.action_win_result = QtWidgets.QAction(MainWindow)
        self.action_win_result.setObjectName("action_win_result")
        self.action_kerner_scipy_stats = QtWidgets.QAction(MainWindow)
        self.action_kerner_scipy_stats.setObjectName("action_kerner_scipy_stats")
        self.action_kerner_statsmodels = QtWidgets.QAction(MainWindow)
        self.action_kerner_statsmodels.setObjectName("action_kerner_statsmodels")
        self.action_kerner_pingouin = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/pic/resource/fig/pingouin.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.action_kerner_pingouin.setIcon(icon1)
        self.action_kerner_pingouin.setObjectName("action_kerner_pingouin")
        self.action_anova = QtWidgets.QAction(MainWindow)
        self.action_anova.setObjectName("action_anova")
        self.action_ancova = QtWidgets.QAction(MainWindow)
        self.action_ancova.setObjectName("action_ancova")
        self.action_rm_anova = QtWidgets.QAction(MainWindow)
        self.action_rm_anova.setObjectName("action_rm_anova")
        self.action_epsilon = QtWidgets.QAction(MainWindow)
        self.action_epsilon.setObjectName("action_epsilon")
        self.action_mixed_anova = QtWidgets.QAction(MainWindow)
        self.action_mixed_anova.setObjectName("action_mixed_anova")
        self.action_welch_anova = QtWidgets.QAction(MainWindow)
        self.action_welch_anova.setObjectName("action_welch_anova")
        self.action_tost = QtWidgets.QAction(MainWindow)
        self.action_tost.setObjectName("action_tost")
        self.action_ttest = QtWidgets.QAction(MainWindow)
        self.action_ttest.setObjectName("action_ttest")
        self.action_bayesfactor_binom = QtWidgets.QAction(MainWindow)
        self.action_bayesfactor_binom.setObjectName("action_bayesfactor_binom")
        self.action_bayesfactor_ttest = QtWidgets.QAction(MainWindow)
        self.action_bayesfactor_ttest.setObjectName("action_bayesfactor_ttest")
        self.action_bayesfactor_pearson = QtWidgets.QAction(MainWindow)
        self.action_bayesfactor_pearson.setObjectName("action_bayesfactor_pearson")
        self.action_convert_angles = QtWidgets.QAction(MainWindow)
        self.action_convert_angles.setObjectName("action_convert_angles")
        self.action_circ_axial = QtWidgets.QAction(MainWindow)
        self.action_circ_axial.setObjectName("action_circ_axial")
        self.action_circ_corrcc = QtWidgets.QAction(MainWindow)
        self.action_circ_corrcc.setObjectName("action_circ_corrcc")
        self.action_circ_corrcl = QtWidgets.QAction(MainWindow)
        self.action_circ_corrcl.setObjectName("action_circ_corrcl")
        self.action_circ_mean = QtWidgets.QAction(MainWindow)
        self.action_circ_mean.setObjectName("action_circ_mean")
        self.action_circ_r = QtWidgets.QAction(MainWindow)
        self.action_circ_r.setObjectName("action_circ_r")
        self.action_circ_rayleigh = QtWidgets.QAction(MainWindow)
        self.action_circ_rayleigh.setObjectName("action_circ_rayleigh")
        self.action_circ_vtest = QtWidgets.QAction(MainWindow)
        self.action_circ_vtest.setObjectName("action_circ_vtest")
        self.action_chi2_independence = QtWidgets.QAction(MainWindow)
        self.action_chi2_independence.setObjectName("action_chi2_independence")
        self.action_chi2_mcnemar = QtWidgets.QAction(MainWindow)
        self.action_chi2_mcnemar.setObjectName("action_chi2_mcnemar")
        self.action_dichotomous_crosstab = QtWidgets.QAction(MainWindow)
        self.action_dichotomous_crosstab.setObjectName("action_dichotomous_crosstab")
        self.action_corr = QtWidgets.QAction(MainWindow)
        self.action_corr.setObjectName("action_corr")
        self.action_pairwise_corr = QtWidgets.QAction(MainWindow)
        self.action_pairwise_corr.setObjectName("action_pairwise_corr")
        self.action_partial_corr = QtWidgets.QAction(MainWindow)
        self.action_partial_corr.setObjectName("action_partial_corr")
        self.action_pcorr = QtWidgets.QAction(MainWindow)
        self.action_pcorr.setObjectName("action_pcorr")
        self.action_rcorr = QtWidgets.QAction(MainWindow)
        self.action_rcorr.setObjectName("action_rcorr")
        self.action_distance_corr = QtWidgets.QAction(MainWindow)
        self.action_distance_corr.setObjectName("action_distance_corr")
        self.action_rm_corr = QtWidgets.QAction(MainWindow)
        self.action_rm_corr.setObjectName("action_rm_corr")
        self.action_linear_regression = QtWidgets.QAction(MainWindow)
        self.action_linear_regression.setObjectName("action_linear_regression")
        self.action_logistic_regression = QtWidgets.QAction(MainWindow)
        self.action_logistic_regression.setObjectName("action_logistic_regression")
        self.action_mediation_analysis = QtWidgets.QAction(MainWindow)
        self.action_mediation_analysis.setObjectName("action_mediation_analysis")
        self.action_anderson = QtWidgets.QAction(MainWindow)
        self.action_anderson.setObjectName("action_anderson")
        self.action_gzscore = QtWidgets.QAction(MainWindow)
        self.action_gzscore.setObjectName("action_gzscore")
        self.action_homoscedasticity = QtWidgets.QAction(MainWindow)
        self.action_homoscedasticity.setObjectName("action_homoscedasticity")
        self.action_normality = QtWidgets.QAction(MainWindow)
        self.action_normality.setObjectName("action_normality")
        self.action_sphericity = QtWidgets.QAction(MainWindow)
        self.action_sphericity.setObjectName("action_sphericity")
        self.action_compute_effsize = QtWidgets.QAction(MainWindow)
        self.action_compute_effsize.setObjectName("action_compute_effsize")
        self.action_compute_effsize_from_t = QtWidgets.QAction(MainWindow)
        self.action_compute_effsize_from_t.setObjectName("action_compute_effsize_from_t")
        self.action_convert_effsize = QtWidgets.QAction(MainWindow)
        self.action_convert_effsize.setObjectName("action_convert_effsize")
        self.action_compute_esci = QtWidgets.QAction(MainWindow)
        self.action_compute_esci.setObjectName("action_compute_esci")
        self.action_compute_bootci = QtWidgets.QAction(MainWindow)
        self.action_compute_bootci.setObjectName("action_compute_bootci")
        self.action_pairwise_corr_2 = QtWidgets.QAction(MainWindow)
        self.action_pairwise_corr_2.setObjectName("action_pairwise_corr_2")
        self.action_pairwise_ttests = QtWidgets.QAction(MainWindow)
        self.action_pairwise_ttests.setObjectName("action_pairwise_ttests")
        self.action_pairwise_tukey = QtWidgets.QAction(MainWindow)
        self.action_pairwise_tukey.setObjectName("action_pairwise_tukey")
        self.action_pairwise_gameshowell = QtWidgets.QAction(MainWindow)
        self.action_pairwise_gameshowell.setObjectName("action_pairwise_gameshowell")
        self.action_multicomp = QtWidgets.QAction(MainWindow)
        self.action_multicomp.setObjectName("action_multicomp")
        self.action_box_m = QtWidgets.QAction(MainWindow)
        self.action_box_m.setObjectName("action_box_m")
        self.action_multivariate_normality = QtWidgets.QAction(MainWindow)
        self.action_multivariate_normality.setObjectName("action_multivariate_normality")
        self.action_multivariate_ttest = QtWidgets.QAction(MainWindow)
        self.action_multivariate_ttest.setObjectName("action_multivariate_ttest")
        self.action_set_default_options = QtWidgets.QAction(MainWindow)
        self.action_set_default_options.setObjectName("action_set_default_options")
        self.action_cronbach_alpha = QtWidgets.QAction(MainWindow)
        self.action_cronbach_alpha.setObjectName("action_cronbach_alpha")
        self.action_intraclass_corr = QtWidgets.QAction(MainWindow)
        self.action_intraclass_corr.setObjectName("action_intraclass_corr")
        self.action_cochran = QtWidgets.QAction(MainWindow)
        self.action_cochran.setObjectName("action_cochran")
        self.action_friedman = QtWidgets.QAction(MainWindow)
        self.action_friedman.setObjectName("action_friedman")
        self.action_kruskal = QtWidgets.QAction(MainWindow)
        self.action_kruskal.setObjectName("action_kruskal")
        self.action_mad = QtWidgets.QAction(MainWindow)
        self.action_mad.setObjectName("action_mad")
        self.action_madmedianrule = QtWidgets.QAction(MainWindow)
        self.action_madmedianrule.setObjectName("action_madmedianrule")
        self.action_mwu = QtWidgets.QAction(MainWindow)
        self.action_mwu.setObjectName("action_mwu")
        self.action_wilcoxon = QtWidgets.QAction(MainWindow)
        self.action_wilcoxon.setObjectName("action_wilcoxon")
        self.action_harrelldavis = QtWidgets.QAction(MainWindow)
        self.action_harrelldavis.setObjectName("action_harrelldavis")
        self.action_plot_blandaltman = QtWidgets.QAction(MainWindow)
        self.action_plot_blandaltman.setObjectName("action_plot_blandaltman")
        self.action_plot_circmean = QtWidgets.QAction(MainWindow)
        self.action_plot_circmean.setObjectName("action_plot_circmean")
        self.action_plot_paired = QtWidgets.QAction(MainWindow)
        self.action_plot_paired.setObjectName("action_plot_paired")
        self.action_plot_shift = QtWidgets.QAction(MainWindow)
        self.action_plot_shift.setObjectName("action_plot_shift")
        self.action_plot_rm_corr = QtWidgets.QAction(MainWindow)
        self.action_plot_rm_corr.setObjectName("action_plot_rm_corr")
        self.action_qqplot = QtWidgets.QAction(MainWindow)
        self.action_qqplot.setObjectName("action_qqplot")
        self.action_power_anova = QtWidgets.QAction(MainWindow)
        self.action_power_anova.setObjectName("action_power_anova")
        self.action_power_rm_anova = QtWidgets.QAction(MainWindow)
        self.action_power_rm_anova.setObjectName("action_power_rm_anova")
        self.action_power_chi2 = QtWidgets.QAction(MainWindow)
        self.action_power_chi2.setObjectName("action_power_chi2")
        self.action_power_corr = QtWidgets.QAction(MainWindow)
        self.action_power_corr.setObjectName("action_power_corr")
        self.action_power_ttest = QtWidgets.QAction(MainWindow)
        self.action_power_ttest.setObjectName("action_power_ttest")
        self.action_power_ttest2n = QtWidgets.QAction(MainWindow)
        self.action_power_ttest2n.setObjectName("action_power_ttest2n")
        self.menu.addAction(self.action_open)
        self.menu_2.addAction(self.action_draw)
        self.menu_new_win.addAction(self.action_win_data)
        self.menu_new_win.addAction(self.action_win_plot_q)
        self.menu_new_win.addAction(self.action_win_plot_m)
        self.menu_new_win.addAction(self.action_win_log)
        self.menu_new_win.addAction(self.action_win_result)
        self.menu_3.addAction(self.menu_new_win.menuAction())
        self.menu_3.addAction(self.action_tileSubWin)
        self.menu_3.addAction(self.action_cascadeSubWin)
        self.help.addAction(self.action_author)
        self.help.addAction(self.action_logs)
        self.menu_kernel.addAction(self.action_kerner_scipy_stats)
        self.menu_kernel.addAction(self.action_kerner_statsmodels)
        self.menu_kernel.addAction(self.action_kerner_pingouin)
        self.menu_anova_ttest.addAction(self.action_anova)
        self.menu_anova_ttest.addAction(self.action_ancova)
        self.menu_anova_ttest.addAction(self.action_rm_anova)
        self.menu_anova_ttest.addAction(self.action_epsilon)
        self.menu_anova_ttest.addAction(self.action_mixed_anova)
        self.menu_anova_ttest.addAction(self.action_welch_anova)
        self.menu_anova_ttest.addAction(self.action_tost)
        self.menu_anova_ttest.addAction(self.action_ttest)
        self.menu_bayesian.addAction(self.action_bayesfactor_binom)
        self.menu_bayesian.addAction(self.action_bayesfactor_ttest)
        self.menu_bayesian.addAction(self.action_bayesfactor_pearson)
        self.menu_circular.addAction(self.action_convert_angles)
        self.menu_circular.addAction(self.action_circ_axial)
        self.menu_circular.addAction(self.action_circ_corrcc)
        self.menu_circular.addAction(self.action_circ_corrcl)
        self.menu_circular.addAction(self.action_circ_mean)
        self.menu_circular.addAction(self.action_circ_r)
        self.menu_circular.addAction(self.action_circ_rayleigh)
        self.menu_circular.addAction(self.action_circ_vtest)
        self.menu_correlation_regression.addAction(self.action_corr)
        self.menu_correlation_regression.addAction(self.action_pairwise_corr)
        self.menu_correlation_regression.addAction(self.action_partial_corr)
        self.menu_correlation_regression.addAction(self.action_distance_corr)
        self.menu_correlation_regression.addAction(self.action_rm_corr)
        self.menu_correlation_regression.addAction(self.action_linear_regression)
        self.menu_correlation_regression.addAction(self.action_logistic_regression)
        self.menu_correlation_regression.addAction(self.action_mediation_analysis)
        self.menu_contingency.addAction(self.action_chi2_independence)
        self.menu_contingency.addAction(self.action_chi2_mcnemar)
        self.menu_contingency.addAction(self.action_dichotomous_crosstab)
        self.menu_distribution.addAction(self.action_anderson)
        self.menu_distribution.addAction(self.action_gzscore)
        self.menu_distribution.addAction(self.action_homoscedasticity)
        self.menu_distribution.addAction(self.action_normality)
        self.menu_distribution.addAction(self.action_sphericity)
        self.menu_effect_size.addAction(self.action_compute_effsize)
        self.menu_effect_size.addAction(self.action_compute_effsize_from_t)
        self.menu_effect_size.addAction(self.action_convert_effsize)
        self.menu_effect_size.addAction(self.action_compute_esci)
        self.menu_effect_size.addAction(self.action_compute_bootci)
        self.menu_4.addAction(self.action_pairwise_corr_2)
        self.menu_4.addAction(self.action_pairwise_ttests)
        self.menu_4.addAction(self.action_pairwise_tukey)
        self.menu_4.addAction(self.action_pairwise_gameshowell)
        self.menu_4.addAction(self.action_multicomp)
        self.menu_multivariate_tests.addAction(self.action_box_m)
        self.menu_multivariate_tests.addAction(self.action_multivariate_normality)
        self.menu_multivariate_tests.addAction(self.action_multivariate_ttest)
        self.menu_others.addAction(self.action_set_default_options)
        self.menu_reliablility_consistency.addAction(self.action_cronbach_alpha)
        self.menu_reliablility_consistency.addAction(self.action_intraclass_corr)
        self.menu_non_parametric.addAction(self.action_cochran)
        self.menu_non_parametric.addAction(self.action_friedman)
        self.menu_non_parametric.addAction(self.action_kruskal)
        self.menu_non_parametric.addAction(self.action_mad)
        self.menu_non_parametric.addAction(self.action_madmedianrule)
        self.menu_non_parametric.addAction(self.action_mwu)
        self.menu_non_parametric.addAction(self.action_wilcoxon)
        self.menu_non_parametric.addAction(self.action_harrelldavis)
        self.menu_plotting.addAction(self.action_plot_blandaltman)
        self.menu_plotting.addAction(self.action_plot_circmean)
        self.menu_plotting.addAction(self.action_plot_paired)
        self.menu_plotting.addAction(self.action_plot_shift)
        self.menu_plotting.addAction(self.action_plot_rm_corr)
        self.menu_plotting.addAction(self.action_qqplot)
        self.menu_power_analysis.addAction(self.action_power_anova)
        self.menu_power_analysis.addAction(self.action_power_rm_anova)
        self.menu_power_analysis.addAction(self.action_power_chi2)
        self.menu_power_analysis.addAction(self.action_power_corr)
        self.menu_power_analysis.addAction(self.action_power_ttest)
        self.menu_power_analysis.addAction(self.action_power_ttest2n)
        self.menu_5.addAction(self.menu_kernel.menuAction())
        self.menu_5.addAction(self.menu_anova_ttest.menuAction())
        self.menu_5.addAction(self.menu_bayesian.menuAction())
        self.menu_5.addAction(self.menu_circular.menuAction())
        self.menu_5.addAction(self.menu_contingency.menuAction())
        self.menu_5.addAction(self.menu_correlation_regression.menuAction())
        self.menu_5.addAction(self.menu_distribution.menuAction())
        self.menu_5.addAction(self.menu_effect_size.menuAction())
        self.menu_5.addAction(self.menu_4.menuAction())
        self.menu_5.addAction(self.menu_multivariate_tests.menuAction())
        self.menu_5.addAction(self.menu_non_parametric.menuAction())
        self.menu_5.addAction(self.menu_power_analysis.menuAction())
        self.menu_5.addAction(self.menu_reliablility_consistency.menuAction())
        self.menu_5.addAction(self.menu_plotting.menuAction())
        self.menu_5.addAction(self.menu_others.menuAction())
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menu_5.menuAction())
        self.menubar.addAction(self.help.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menu.setTitle(_translate("MainWindow", "文件"))
        self.menu_2.setTitle(_translate("MainWindow", "绘图"))
        self.menu_3.setTitle(_translate("MainWindow", "窗口"))
        self.menu_new_win.setTitle(_translate("MainWindow", "新建"))
        self.help.setTitle(_translate("MainWindow", "关于"))
        self.menu_5.setTitle(_translate("MainWindow", "数据分析"))
        self.menu_kernel.setTitle(_translate("MainWindow", "分析内核选择"))
        self.menu_anova_ttest.setTitle(_translate("MainWindow", "方差分析与T检验"))
        self.menu_bayesian.setTitle(_translate("MainWindow", "贝叶斯"))
        self.menu_circular.setTitle(_translate("MainWindow", "圆弧处理"))
        self.menu_correlation_regression.setTitle(_translate("MainWindow", "相关性与回归"))
        self.menu_contingency.setTitle(_translate("MainWindow", "偶然性"))
        self.menu_distribution.setTitle(_translate("MainWindow", "分布"))
        self.menu_effect_size.setTitle(_translate("MainWindow", "影响因子"))
        self.menu_4.setTitle(_translate("MainWindow", "多重比较和事后检验"))
        self.menu_multivariate_tests.setTitle(_translate("MainWindow", "多元检验"))
        self.menu_others.setTitle(_translate("MainWindow", "其他"))
        self.menu_reliablility_consistency.setTitle(_translate("MainWindow", "可靠性与一致性"))
        self.menu_non_parametric.setTitle(_translate("MainWindow", "非参数检验"))
        self.menu_plotting.setTitle(_translate("MainWindow", "绘图"))
        self.menu_power_analysis.setTitle(_translate("MainWindow", "功率分析"))
        self.action_open.setText(_translate("MainWindow", "打开"))
        self.action_open.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.action_author.setText(_translate("MainWindow", "作者"))
        self.action_author.setShortcut(_translate("MainWindow", "F1"))
        self.action_logs.setText(_translate("MainWindow", "更新日志"))
        self.action_logs.setShortcut(_translate("MainWindow", "Ctrl+L"))
        self.action_tileSubWin.setText(_translate("MainWindow", "平铺显示"))
        self.action_cascadeSubWin.setText(_translate("MainWindow", "级联显示"))
        self.action_draw.setText(_translate("MainWindow", "绘制"))
        self.action_draw.setShortcut(_translate("MainWindow", "Ctrl+D"))
        self.action_win_data.setText(_translate("MainWindow", "数据窗口"))
        self.action_win_data.setShortcut(_translate("MainWindow", "Ctrl+1"))
        self.action_win_plot_q.setText(_translate("MainWindow", "绘图窗口(Qcustomplot)"))
        self.action_win_plot_q.setShortcut(_translate("MainWindow", "Ctrl+2"))
        self.action_win_plot_m.setText(_translate("MainWindow", "绘图窗口(Matplot)"))
        self.action_win_plot_m.setShortcut(_translate("MainWindow", "Ctrl+3"))
        self.action_win_log.setText(_translate("MainWindow", "日志窗口"))
        self.action_win_log.setShortcut(_translate("MainWindow", "Ctrl+4"))
        self.action_win_result.setText(_translate("MainWindow", "输出窗口"))
        self.action_win_result.setShortcut(_translate("MainWindow", "Ctrl+5"))
        self.action_kerner_scipy_stats.setText(_translate("MainWindow", "Scipy.stats"))
        self.action_kerner_statsmodels.setText(_translate("MainWindow", "Statsmodels"))
        self.action_kerner_pingouin.setText(_translate("MainWindow", "Pingouin"))
        self.action_anova.setText(_translate("MainWindow", "方差分析"))
        self.action_anova.setToolTip(_translate("MainWindow", "One-way and N-way ANOVA"))
        self.action_ancova.setText(_translate("MainWindow", "协方差分析"))
        self.action_ancova.setToolTip(_translate("MainWindow", "ANCOVA with one or more covariate(s)"))
        self.action_rm_anova.setText(_translate("MainWindow", "重复测量方差分析"))
        self.action_rm_anova.setToolTip(_translate("MainWindow", "One-way and two-way repeated measures ANOVA"))
        self.action_epsilon.setText(_translate("MainWindow", "Epsilon adjustement factor for repeated measures"))
        self.action_mixed_anova.setText(_translate("MainWindow", "Mixed-design (split-plot) ANOVA"))
        self.action_welch_anova.setText(_translate("MainWindow", "One-way Welch ANOVA"))
        self.action_tost.setText(_translate("MainWindow", "Two One-Sided Test (TOST) for equivalence"))
        self.action_ttest.setText(_translate("MainWindow", "T-test"))
        self.action_bayesfactor_binom.setText(_translate("MainWindow", "Bayes factor of a binomial test with k successes, n trials and base probability"))
        self.action_bayesfactor_ttest.setText(_translate("MainWindow", "Bayes Factor of a T-test"))
        self.action_bayesfactor_pearson.setText(_translate("MainWindow", "Bayes Factor of a Pearson correlation"))
        self.action_convert_angles.setText(_translate("MainWindow", "Element-wise conversion of arbitrary-unit circular quantities to radians"))
        self.action_circ_axial.setText(_translate("MainWindow", "Transforms n-axial data to a common scale"))
        self.action_circ_corrcc.setText(_translate("MainWindow", "Correlation coefficient between two circular variables"))
        self.action_circ_corrcl.setText(_translate("MainWindow", "Correlation coefficient between one circular and one linear variable random variables"))
        self.action_circ_mean.setText(_translate("MainWindow", "Mean direction for (binned) circular data"))
        self.action_circ_r.setText(_translate("MainWindow", "Mean resultant vector length for circular data"))
        self.action_circ_rayleigh.setText(_translate("MainWindow", "Rayleigh test for non-uniformity of circular data"))
        self.action_circ_vtest.setText(_translate("MainWindow", "V test for non-uniformity of circular data with a specified mean direction"))
        self.action_chi2_independence.setText(_translate("MainWindow", "Chi-squared independence tests between two categorical variables"))
        self.action_chi2_mcnemar.setText(_translate("MainWindow", "Performs the exact and approximated versions of McNemar’s test"))
        self.action_dichotomous_crosstab.setText(_translate("MainWindow", "Generates a 2x2 contingency table from a pandas.DataFrame that contains only dichotomous entries, which are converted to 0 or 1"))
        self.action_corr.setText(_translate("MainWindow", "(Robust) correlation between two variables"))
        self.action_pairwise_corr.setText(_translate("MainWindow", "Pairwise (partial) correlations between columns of a pandas dataframe"))
        self.action_partial_corr.setText(_translate("MainWindow", "Partial and semi-partial correlation"))
        self.action_pcorr.setText(_translate("MainWindow", "Partial correlation matrix (pandas.DataFrame method)."))
        self.action_rcorr.setText(_translate("MainWindow", "Correlation matrix of a dataframe with p-values and/or sample size on the upper triangle (pandas.DataFrame method)."))
        self.action_distance_corr.setText(_translate("MainWindow", "Distance correlation between two arrays"))
        self.action_rm_corr.setText(_translate("MainWindow", "Repeated measures correlation"))
        self.action_linear_regression.setText(_translate("MainWindow", "(Multiple) Linear regression"))
        self.action_logistic_regression.setText(_translate("MainWindow", "(Multiple) Binary logistic regression"))
        self.action_mediation_analysis.setText(_translate("MainWindow", "Mediation analysis using a bias-correct non-parametric bootstrap method"))
        self.action_anderson.setText(_translate("MainWindow", "Anderson-Darling test of distribution"))
        self.action_gzscore.setText(_translate("MainWindow", "Geometric standard (Z) score"))
        self.action_homoscedasticity.setText(_translate("MainWindow", "Test equality of variance"))
        self.action_normality.setText(_translate("MainWindow", "Univariate normality test"))
        self.action_sphericity.setText(_translate("MainWindow", "Mauchly and JNS test for sphericity"))
        self.action_compute_effsize.setText(_translate("MainWindow", "Calculate effect size between two set of observations"))
        self.action_compute_effsize_from_t.setText(_translate("MainWindow", "Compute effect size from a T-value"))
        self.action_convert_effsize.setText(_translate("MainWindow", "Conversion between effect sizes"))
        self.action_compute_esci.setText(_translate("MainWindow", "Parametric confidence intervals around a Cohen d or a correlation coefficient"))
        self.action_compute_bootci.setText(_translate("MainWindow", "Bootstrapped confidence intervals of univariate and bivariate functions"))
        self.action_pairwise_corr_2.setText(_translate("MainWindow", "Pairwise (partial) correlations between columns of a pandas dataframe"))
        self.action_pairwise_ttests.setText(_translate("MainWindow", "Pairwise T-tests"))
        self.action_pairwise_tukey.setText(_translate("MainWindow", "Pairwise Tukey-HSD post-hoc test"))
        self.action_pairwise_gameshowell.setText(_translate("MainWindow", "Pairwise Games-Howell post-hoc test"))
        self.action_multicomp.setText(_translate("MainWindow", "P-values correction for multiple comparisons"))
        self.action_box_m.setText(_translate("MainWindow", "Test equality of covariance matrices using the Box’s M test"))
        self.action_multivariate_normality.setText(_translate("MainWindow", "Henze-Zirkler multivariate normality test"))
        self.action_multivariate_ttest.setText(_translate("MainWindow", "Hotelling T-squared test (= multivariate T-test)"))
        self.action_set_default_options.setText(_translate("MainWindow", "Reset Pingouin’s default global options"))
        self.action_cronbach_alpha.setText(_translate("MainWindow", "Cronbach’s alpha reliability measure"))
        self.action_intraclass_corr.setText(_translate("MainWindow", "Intraclass correlation"))
        self.action_cochran.setText(_translate("MainWindow", "Cochran Q test"))
        self.action_friedman.setText(_translate("MainWindow", "Friedman test for repeated measurements"))
        self.action_kruskal.setText(_translate("MainWindow", "Kruskal-Wallis H-test for independent samples"))
        self.action_mad.setText(_translate("MainWindow", "Median Absolute Deviation (MAD) along given axis of an array"))
        self.action_madmedianrule.setText(_translate("MainWindow", "Robust outlier detection based on the MAD-median rule"))
        self.action_mwu.setText(_translate("MainWindow", "Mann-Whitney U Test (= Wilcoxon rank-sum test)"))
        self.action_wilcoxon.setText(_translate("MainWindow", "Wilcoxon signed-rank test"))
        self.action_harrelldavis.setText(_translate("MainWindow", "Harrell-Davis robust estimate of the qth quantile(s) of the data"))
        self.action_plot_blandaltman.setText(_translate("MainWindow", "Generate a Bland-Altman plot to compare two sets of measurements"))
        self.action_plot_circmean.setText(_translate("MainWindow", "Plot the circular mean and vector length of a set of angles on the unit circle"))
        self.action_plot_paired.setText(_translate("MainWindow", "Paired plot"))
        self.action_plot_shift.setText(_translate("MainWindow", "Shift plot"))
        self.action_plot_rm_corr.setText(_translate("MainWindow", "Plot a repeated measures correlation"))
        self.action_qqplot.setText(_translate("MainWindow", "Quantile-Quantile plot"))
        self.action_power_anova.setText(_translate("MainWindow", "Evaluate power, sample size, effect size or significance level of a one-way balanced ANOVA."))
        self.action_power_rm_anova.setText(_translate("MainWindow", "Evaluate power, sample size, effect size or significance level of a balanced one-way repeated measures ANOVA"))
        self.action_power_chi2.setText(_translate("MainWindow", "Evaluate power, sample size, effect size or significance level of chi-squared tests"))
        self.action_power_corr.setText(_translate("MainWindow", "Evaluate power, sample size, correlation coefficient or significance level of a correlation test"))
        self.action_power_ttest.setText(_translate("MainWindow", "Evaluate power, sample size, effect size or significance level of a one-sample T-test, a paired T-test or an independent two-samples T-test with equal sample sizes"))
        self.action_power_ttest2n.setText(_translate("MainWindow", "Evaluate power, effect size or significance level of an independent two-samples T-test with unequal sample sizes"))
import resource.label_rc
