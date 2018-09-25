import pandas as pd
import math 

class Agg:
    @staticmethod
    def aggregate(resp, hid, rnd, sum_or_avg):
        df = pd.DataFrame.from_records(resp.objects.\
            filter(hack_id=hid).\
            filter(round_no=rnd).\
            values('hack_id', 'round_no', 'judge_id', 'team_name', 'team_id', 'critera', 'mark_weight'))
        

        
        jtm = df[['judge_id', 'team_id', 'mark_weight']];


        #Judges::Count (how many teams did the judge judge)
        j_Count = df[['judge_id', 'team_id']].drop_duplicates().groupby('judge_id').agg('count');
        print(j_Count) 
        
        
        #Judges::Sum (sum of all marks the jugde gave)
        j_Sum = df[['judge_id', 'mark_weight']].groupby('judge_id').agg('sum');
        print(j_Sum) 
        
        
        #J_MAIN_AGG_SUM
        judge_team_agg= jtm.groupby(['judge_id', 'team_id']).agg(sum_or_avg).add_suffix('_agg').reset_index()
        print(judge_team_agg)
        
        #Judges::Inverse_AVG
        j_Inverse_AVG = judge_team_agg[['judge_id', 'mark_weight_agg']].groupby('judge_id').agg('mean')
        j_Inverse_AVG['inv_avg'] = j_Inverse_AVG.apply(lambda row: 1/row.mark_weight_agg, axis=1)
        print("INV_AVG:") 
        print(j_Inverse_AVG) 
                
              
        #Teams::CNT (how many judges did judge the team)
        t_CNT = df[['judge_id', 'team_id']].drop_duplicates().groupby('team_id').agg('count').add_suffix('_count')
        print("t_CNT:") 
        print(t_CNT)
        

        #T_MAIN_AGG_SUM
        team_judge_agg = jtm.groupby(['team_id', 'judge_id']).agg(sum_or_avg).add_suffix('_agg').reset_index()
        print("team_judge_agg:") 
        print(team_judge_agg)
        #Teams::AVG (average mark given by each judge)
        t_AVG = team_judge_agg[['team_id', 'mark_weight_agg']][team_judge_agg.mark_weight_agg > 0]\
                .groupby('team_id')\
                .agg('mean')\
                .add_suffix('_mean')
        print("t_AVG:") 
        print(t_AVG)
        
               
     
        #AVG No
        avg_no = math.floor(t_CNT[t_CNT.judge_id_count > 0]['judge_id_count'].mean())        
        #AVG S
        avg_score = team_judge_agg['mark_weight_agg'].mean()
        #MED S
        med_score = team_judge_agg['mark_weight_agg'].median()

        print("commons:")
        print(avg_no)
        print(avg_score)        
        print(med_score)


        #Teams::W_AM (weighted average and median for teams)
        t_W_AM = pd.merge(team_judge_agg, j_Inverse_AVG[['inv_avg']], how='left', on='judge_id')
        t_W_AM['prod'] = t_W_AM.apply(lambda row: row.mark_weight_agg * row.inv_avg, axis=1)   
        t_W_AM = t_W_AM[['team_id', 'prod']].groupby('team_id').agg('sum').add_suffix('_sum').reset_index();
        t_W_AM = pd.merge(t_W_AM, t_CNT, on='team_id')
        t_W_AM['w_avg'] = t_W_AM.apply(lambda row: row.prod_sum * avg_score / row.judge_id_count, axis=1)
        t_W_AM['w_med'] = t_W_AM.apply(lambda row: row.prod_sum * med_score / row.judge_id_count, axis=1)
        t_W_AM = t_W_AM.sort_values(['w_avg'], ascending = False)
        
        print("t_W_AM:")
        print(t_W_AM)  
        
        
