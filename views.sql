CREATE OR REPLACE VIEW core_resonses_vw AS 
    SELECT 
	core_judginground.id as round_id,
	core_judginground.hackathon_id as hack_id,
	core_judginground.number as round_no,	
	core_judgeresponse.judge_id as judge_id,
	core_team.name as team_name,
	core_team.id as team_id,
	core_criteria.name as critera,
	core_scaleentry.weight as mark_weight,	
	core_scaleentry.name as mark,
	core_judge.name as judge_name
    FROM core_judgeresponse, core_scaleentry, core_judginground, core_criteria, core_judge, core_team
    WHERE 
	core_judgeresponse.mark_id = core_scaleentry.id
	AND
	core_judgeresponse.round_id = core_judginground.id
	AND
	core_judgeresponse.criterion_id = core_criteria.id
	AND
	core_judgeresponse.judge_id = core_judge.id
	AND
	core_judgeresponse.team_id = core_team.id
	ORDER BY hack_id, round_no, judge_id, team_name, critera