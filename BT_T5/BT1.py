# from itertools import groupby

import numpy as np
import pandas as pd

#thư viện tính ANOVA
import statsmodels.formula.api as smf
import statsmodels.stats.multicomp as multi

df= pd.read_csv('../heart_failure_clinical_records_dataset.csv')
print(df)

'''
Liệu người hút thuốc có ảnh hưởng đến khả năng tử vong trong thời gian điều trị không
'''
sub1=df.copy()
sub1=df[(df['smoking']==1)]
# print(sub1)

df['time']=pd.to_numeric(df['time'], errors='coerce')

ct1=sub1.groupby('time').size()
ct2=sub1.groupby('DEATH_EVENT').size()
print(ct1)
print(ct2)

#tính ANOVA
print()
print('Liệu người hút thuốc có ảnh hưởng đến khả năng tử vong trong thời gian điều trị không')
model1=smf.ols(formula='time ~ C(DEATH_EVENT)',data=sub1)
results1=model1.fit()
print(results1.summary())

print()
print()

'''
Mối liên hệ sự sống giữa phần trăm máu co bóp tim mỗi lần co bóp và thời gian bị bệnh
'''

sub2=df.copy()

sub3=sub2[['ejection_fraction','time']]

sub2=df[(df['DEATH_EVENT']==0)]

sub3['ejection_fraction']=pd.to_numeric(sub3['ejection_fraction'], errors='coerce')
sub3['time']=pd.to_numeric(sub3['time'], errors='coerce')

# print(df['platelets'].value_counts())

sub3['ejection_fraction']=pd.qcut(sub2['ejection_fraction'],3,labels=['1','2','3'])
c6=sub1['ejection_fraction'].value_counts().sort_index()
print(sub2.groupby('ejection_fraction').size())

model2 = smf.ols(formula='time ~ C(ejection_fraction)', data=sub3)
results2=model2.fit()
print(results2.summary())

print()

print('Tính trung bình cho ejection_fraction')
m2=sub3.groupby('ejection_fraction').mean()
print(m2)


print('Tính độ lệch chuẩn cho ejection_fraction')
sd2=sub3.groupby('ejection_fraction').std()
print(sd2)

print()

'''
phân tích sâu
'''
mc1=multi.MultiComparison(sub2['time'],sub2['ejection_fraction'])
res1=mc1.tukeyhsd()
print(res1.summary())