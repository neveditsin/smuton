import csv
from core import models
import pandas as pd



def import_csv_simple(j_round, override):
    #round,jid,tid,crit,mark
    df = unpivot(pd.read_csv('C:\\\\temp\\\\responses_pivot.csv'))
    
    load_into_model(j_round, override, df.iterrows())
    
    return
    
    with open('C:\\\\temp\\\\responses.csv', newline='') as csvfile:
        resps = csv.DictReader(csvfile)
        load_into_model(j_round, override, resps)
            
    #df = pd.DataFrame.from_records(models.JudgeResponse.objects.filter(round_id=j_round).values())
def load_into_model(j_round, override_flag, dataset):
    for index, row in dataset:
        r_round = models.JudgingRound.objects.get(id=j_round)
        r_judge=models.Judge.objects.get(id=int(row['judge']))            
        r_team=models.Team.objects.get(id=int(row['team']))
        r_crit = models.Criteria.objects.filter(judging_round = r_round).get(name=row['criterion'])
        r_mark = models.ScaleEntry.objects.filter(scale=r_crit.scale.id).\
                                                get(entry=row['value'])
        if override_flag == False:                
            models.JudgeResponse.objects.create(
                round=r_round,
                judge=r_judge,
                team=r_team,
                criterion=r_crit,
                mark= r_mark,
                )
        else:
            models.JudgeResponse.objects.update_or_create(
                round=r_round,
                judge=r_judge,
                team=r_team,
                criterion=r_crit,
                mark= r_mark,
                )    



def unpivot(DataFrame):       

    print(DataFrame)
    val_vars = list(DataFrame.columns)
    val_vars.remove('judge')
    val_vars.remove('team')
    df_melted = DataFrame.melt(id_vars = ['judge', 'team'], value_vars = val_vars, var_name='criterion')
    

    
    print(df_melted)
    print(df_melted[pd.isnull(df_melted).any(axis=1)])
    return df_melted
    



        

