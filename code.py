import pandas as pd

import math

df1=pd.read_csv('data/1.csv' ,header=1)

df2=pd.read_csv('data/2.csv' ,header=2)

df2=df2.head(2)

df1=df1.head(10)

"""for i in df1['S.No.'].values:
    i=int(i)"""

df3=pd.read_csv('data/3.csv' ,header=1)

df4=pd.read_csv('data/4.csv' ,header=1)

"""df5=pd.read_csv('data/5.csv')"""

df3=df3.head(3)

df4=df4.head(3)

correct_ans_set= df2[['Q1.1','Q2.1','Q3.1','Q4.1','Q5.1','Q6.1','Q7.1','Q8.1','Q9.1','Q10.1','Q11.1','Q12.1','Q13.1','Q14.1','Q15.1','Q16.1','Q17.1','Q18.1','Q19.1','Q20.1']]

marks_set= df2[['Q1.2','Q2.2','Q3.2','Q4.2','Q5.2','Q6.2','Q7.2','Q8.2','Q9.2','Q10.2','Q11.2','Q12.2','Q13.2','Q14.2','Q15.2','Q16.2','Q17.2','Q18.2','Q19.2','Q20.2']]

concept_set= df2[['Q1.3','Q2.3','Q3.3','Q4.3','Q5.3','Q6.3','Q7.3','Q8.3','Q9.3','Q10.3','Q11.3','Q12.3','Q13.3','Q14.3','Q15.3','Q16.3','Q17.3','Q18.3','Q19.3','Q20.3']]

df3_set= df3[['Q1','Q2','Q3','Q4','Q5','Q6','Q7','Q8','Q9','Q10','Q11','Q12','Q13','Q14','Q15','Q16','Q17','Q18','Q19','Q20']]
             

df4_set= df4[['Q1','Q2','Q3','Q4','Q5','Q6','Q7','Q8','Q9','Q10','Q11','Q12','Q13','Q14','Q15','Q16','Q17','Q18','Q19','Q20']]

Ques=['Q1','Q2','Q3','Q4','Q5','Q6','Q7','Q8','Q9','Q10','Q11','Q12','Q13','Q14','Q15','Q16','Q17','Q18','Q19','Q20']
Ans=['Q1.1','Q2.1','Q3.1','Q4.1','Q5.1','Q6.1','Q7.1','Q8.1','Q9.1','Q10.1','Q11.1','Q12.1','Q13.1','Q14.1','Q15.1','Q16.1','Q17.1','Q18.1','Q19.1','Q20.1']



score=[]
Max_score=[]
for j in range(3):
    tempScore=0
    tempMaxScore=0
    for i in Ques:
        res=df3_set[''.join(i)][j]
        a=''.join(i)
        b='.1'
        c='.2'
        ans=correct_ans_set[a+b][0]
        marks=marks_set[a+c][0]
        tempMaxScore=tempMaxScore+marks
        if(res=='Nan'):
            df4_set[''.join(i)][j]=0
        else:
            if(ans==res):
                df4_set[''.join(i)][j]=marks
                tempScore=tempScore+marks
            else:
                df4_set[''.join(i)][j]=0
            
    score.append(tempScore)
    Max_score.append(tempMaxScore)


for i in Ques:
    """a=''.join(i)
    b='.1'
"""    
    print(df4_set[i][0])



