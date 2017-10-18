from scipy import stats
import numpy as np

def get_slope_t_statistic(slope, residuals, independents):
  '''gets the t statistic for a slope'''
  n = len(residuals)
  res_2 = [r**2 for r in residuals]
  sum_res_2 = np.sum(res_2)
  x_bar = np.mean(independents)
  diffs_2 = [(x - x_bar)**2 for x in independents]
  sum_diffs_2 = np.sum(diffs_2)
  se = np.sqrt((sum_res_2/(n-2))/sum_diffs_2)
  tt = slope/se
  return tt

def get_two_sided_p_value(tt, df):
  '''returns a two sided p value'''
  pval = stats.t.sf(np.abs(tt), df)*2  # two-sided pvalue = Prob(abs(t)>tt)
  return pval