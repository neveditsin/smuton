from core import models
from core.utils.multiteams import MultientryPaperFormPage
import pandas as pd
from warnings import catch_warnings


def fs_csv_parse(path, jround):
 
    data = pd.read_csv(path, sep = ';', header = None)
    df = data
    
    #print(dt)
    filename = df[0][1]
    df = df.drop([0], axis=1)
    print(filename)
    
    df = df.T
    
    
    criteria_team_marks = []
    for _, row in df.iterrows():     
        if(row[0] == MultientryPaperFormPage.QR_FIELD + ".id"):
            qr_data = row[1:]
        else:
            cr_team = row[0].split(MultientryPaperFormPage.DATA_SEPARATOR)
            cr = cr_team[0]
            team = cr_team[1].replace(".sources", "")
            marks = row[1:]        
            criteria_team_marks.append((cr, team, marks))
            
            
    
    jtcm_db = []
    i = 1 #marks are enumerated from 1
    for jid in qr_data:
        #get judge
        r_judge = models.Judge.objects.filter(pk = jid).get()
        for ctm in criteria_team_marks:
            if str(ctm[2][i]) == 'nan':
                continue
            r_team = models.Team.objects.filter(name = ctm[1]).get()
            r_crit = models.Criteria.objects.filter(judging_round = jround).get(name=ctm[0])
            r_mark = models.ScaleEntry.objects.filter(scale=r_crit.scale.id).get(entry=ctm[2][i])
            jtcm_db.append((r_judge, r_team, r_crit, r_mark))
        i+=1     

        
    return jtcm_db


def import_csv_simple(file, j_round, override):
    #round,jid,tid,crit,mark
    df = unpivot(pd.read_csv(file))    
    load_into_model(j_round, override, df.iterrows())    
    return

def import_csv_evaluators(file, hack_id, override):
    #round,jid,tid,crit,mark
    df = pd.read_csv(file, header=None)   
    hack = models.Hackathon.objects.get(id=hack_id)
    for _, row in df.iterrows():        
        ev_name = row[0]
        if override == False:                
            models.Judge.objects.create(
                name=ev_name,
                hackathon=hack
                )
        else:
            models.Judge.objects.update_or_create(
                name=ev_name,
                hackathon=hack
                )   

def import_csv_teams(file, hack_id, override):
    #round,jid,tid,crit,mark
    df = pd.read_csv(file, header=None)   
    hack = models.Hackathon.objects.get(id=hack_id)
    for _, row in df.iterrows():
        team_name = row[0]
        team_members = ""
        if(len(row) > 1):
            team_members = row[1]
        if override == False:                
            models.Team.objects.create(
                name=team_name,
                participants=team_members,
                hackathon=hack
                )
        else:
            models.Team.objects.update_or_create(
                name=team_name,
                participants=team_members,
                hackathon=hack
                )   

    
def load_into_model(j_round, override_flag, dataset):
    print(j_round)
    print(dataset)
    for _, row in dataset:
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
    



        

