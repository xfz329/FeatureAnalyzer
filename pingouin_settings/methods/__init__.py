#   -*- coding:utf-8 -*-
#   The __init__.py.py in FeatureAnalyzer
#   created by Jiang Feng(silencejiang@zju.edu.cn)
#   created at 19:01 on 2022/4/2

# anova and test
from pingouin_settings.methods.anova_ttest.anova import *
from pingouin_settings.methods.anova_ttest.ancova import *
from pingouin_settings.methods.anova_ttest.rm_anova import *
from pingouin_settings.methods.anova_ttest.epsilon import *
from pingouin_settings.methods.anova_ttest.mixed_anova import *
from pingouin_settings.methods.anova_ttest.welch_anova import *
from pingouin_settings.methods.anova_ttest.tost import *
from pingouin_settings.methods.anova_ttest.ttest import *

# bayesian
from pingouin_settings.methods.bayesian.bayesfactor_binom import *
from pingouin_settings.methods.bayesian.bayesfactor_ttest import *
from pingouin_settings.methods.bayesian.bayesfactor_pearson import *

# circular
# TODO

# contingency
from pingouin_settings.methods.contingency.chi2_independence import *
from pingouin_settings.methods.contingency.chi2_mcnemar import *
from pingouin_settings.methods.contingency.dichotomous_crosstab import *

# correlation_regression
from pingouin_settings.methods.correlation_regression.corr import *
from pingouin_settings.methods.correlation_regression.pairwise_corr import *
from pingouin_settings.methods.correlation_regression.partial_corr import *
from pingouin_settings.methods.correlation_regression.distance_corr import *
from pingouin_settings.methods.correlation_regression.rm_corr import *


# plotting
from pingouin_settings.methods.plotting.plot_blandaltman import *