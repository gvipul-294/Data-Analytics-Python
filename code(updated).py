import math
import operator

score=[]
Max_score=[]

concept_list= df1['concept id']
concept_list=list(concept_list)
score=[]
for i in range(10):
    score.append(0)
ConceptScoreDataSet = dict(zip(concept_list,score))
conceptTest1=['ST1', 'ST2', 'ST3', 'ST4', 'ST5']
conceptTest2=['ST6', 'ST7', 'ST8', 'ST9', 'ST10']
conceptTest_names=['Concept1 ', 'Concept2 ', 'Concept3 ', 'Concept4 ', 'Concept5 ']
MisConceptTest_names=['Conpcet1 ', 'Conpcet2 ', 'Concept3 ', 'Concept4 ', 'Concept5 ']

ConceptTest1_heads = dict(zip(conceptTest1,conceptTest_names))
ConceptTest2_heads = dict(zip(conceptTest2,conceptTest_names))

MisConceptTest1_heads = dict(zip(conceptTest1,MisConceptTest_names))
MisConceptTest2_heads = dict(zip(conceptTest2,MisConceptTest_names))


for j in range(3):
    tempScore=0
    tempMaxScore=0
    for key in ConceptScoreDataSet:
        ConceptScoreDataSet[key]=0
    for i in Ques:
        res=df3_set[''.join(i)][j]
        a=''.join(i)
        b='.1'
        c='.2'
        d='.3'
        if(df3['testid'][j]=='test-0001'):
            ans=correct_ans_set[a+b][0]
            marks=marks_set[a+c][0]
            concept=concept_set[a+d][0]
        elif (df3['testid'][j]=='test-0002'):
            ans=correct_ans_set[a+b][1]
            marks=marks_set[a+c][1]
            concept=concept_set[a+d][1]
        
        #ConceptScoreDataSet = dict(zip(concept,score))
        
        tempMaxScore=tempMaxScore+marks
        
        if(res=='Nan'):
            df4[''.join(i)][j]=0
        else:
            if(ans==res):
                df4[''.join(i)][j]=marks
                tempScore=tempScore+marks
                ConceptScoreDataSet[''.join(concept)] = ConceptScoreDataSet[''.join(concept)]+marks 
                if(df3['testid'][j]=='test-0001'):
                    df4['' + MisConceptTest1_heads[''.join(concept)] + 'score'][j]= ConceptScoreDataSet[''.join(concept)]
                elif (df3['testid'][j]=='test-0002'):
                    df4['' + MisConceptTest2_heads[''.join(concept)] + 'score'][j]= ConceptScoreDataSet[''.join(concept)]
                
            else:
                df4[''.join(i)][j]=0
            
    score.append(tempScore)
    Max_score.append(tempMaxScore)
    print('Marks according to concept', end='\n')
    print(ConceptScoreDataSet, end='\n')
    #x = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
    sorted_set = dict(sorted(ConceptScoreDataSet.items(), key=operator.itemgetter(1), reverse=True))
    sorted_setList=list(sorted_set.keys())
    if(df3['testid'][j]=='test-0001'):
        value=5
        for i in conceptTest1:
            if(sorted_setList.index(''.join(i))>5):
                df4['' + ConceptTest1_heads[''.join(i)] + 'rank'][j] = value
                value=value-1
            
            else:
                 df4['' + ConceptTest1_heads[''.join(i)] + 'rank'][j] = sorted_setList.index(''.join(i)) + 1
    
    elif (df3['testid'][j]=='test-0002'):
        value=5
        for i in conceptTest2:
            #print(sorted_setList.index(''.join(i)), end='\n')
            if(sorted_setList.index(''.join(i))>5):
                df4['' + ConceptTest2_heads[''.join(i)] + 'rank'][j] = value
                value=value-1
            
            else:
                 df4['' + ConceptTest2_heads[''.join(i)] + 'rank'][j] = sorted_setList.index(''.join(i)) + 1
            
    
    print('Ranked upon data according to set', end='\n')
    print(sorted_set, end='\n')

    
print('marks with respect to each question', end='\n')

for i in Ques:
    """a=''.join(i)
    b='.1'
"""    
    print(df4[i][0])


