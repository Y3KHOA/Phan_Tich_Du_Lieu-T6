import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from numpy import size

data=pd.read_csv('../heart_failure_clinical_records_dataset.csv')

print(data)

#đếm biến quan tâm
print('đếm cho biến: chết do suy tim')
c1=data['DEATH_EVENT'].value_counts()
print(c1)

#tính phần trăm
print('tính phần trăm chết')
p1=data['DEATH_EVENT'].value_counts(normalize= True)
print(p1)

#quan tâm đến độ tử vong từ tuổi 40 - 50 trở lên
print('chết do suy tim từ 40-50')
sub=data[(data['age']>=70)&(data['DEATH_EVENT']==1)]
sub2=sub.copy()
print(sub2)

#đếm cho tuổi
print('đếm cho biến age')
c2=sub2['age'].value_counts()
print(c2)

#tính phần trăm
print('tính phần trăm biến age')
p2=sub2['age'].value_counts(normalize=True).sort_index()
print(p2)

#biểu đồ chết do bệnh
dead=data['creatinine_phosphokinase']

true_x=[]
true_y=[]
false_x=[]
false_y=[]

print(data.values)
for item in data.values:
    if item[12]==0:
        true_x.append(item[0])
        true_y.append(item[2])
    else:
        false_x.append(item[0])
        false_y.append(item[2])
plt.scatter(true_x, true_y, marker='o', c='g')
plt.scatter(false_x,false_y,marker='s',c='y')
plt.bar(true_x,true_y,color='b')
plt.bar(false_x,false_y,color='r')
plt.legend(['sống', 'chết','sống','chết'])
plt.xlabel('tuổi')
plt.ylabel('mức độ của enzym CPK trong máu (mcg / L)')
plt.title('tỉ lệ sống')
plt.show()
