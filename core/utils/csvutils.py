from core import models
import pandas as pd


def import_csv_simple(file, j_round, override):
    #round,jid,tid,crit,mark
    df = unpivot(pd.read_csv(file))    
    load_into_model(j_round, override, df.iterrows())    
    return
    
    
def load_into_model(j_round, override_flag, dataset):
    print(j_round)
    print(dataset)
    for index, row in dataset:
        r_round = models.JudgingRound.objects.get(id=j_round)
        #try:
        r_judge=models.Judge.objects.get(id=int(row['judge']))    
        #except models.Judge.DoesNotExist:
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
    



        

