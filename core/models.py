from django.db import models

class Hackathon(models.Model):
    name = models.CharField(max_length=128, verbose_name="Name")
    desc = models.CharField(max_length=128, verbose_name="Description", blank=True)
    def __str__(self):
        return self.name
    
class JudgeRole(models.Model):
    name = models.CharField(max_length=64, verbose_name="Role Name")
    def __str__(self):
        return self.name
    
class Judge(models.Model):
    name = models.CharField(max_length=128, verbose_name="Name")
    role = models.ForeignKey(JudgeRole, on_delete=models.CASCADE, default=1)
    email = models.EmailField(blank=True)
    hackathon = models.ForeignKey(Hackathon, on_delete=models.CASCADE)
    def __str__(self):
        return self.name #"(id:" + str(self.pk) + "; name:" + self.name + ")"

class Team(models.Model):
    name = models.CharField(max_length=128, verbose_name="Team Name")
    participants = models.CharField(max_length=512, verbose_name="Participants: comma-separated", blank=True)
    hackathon = models.ForeignKey(Hackathon, on_delete=models.CASCADE)
    def __str__(self):
        return self.name# "(id:" + str(self.pk) + "; name:" + self.name + ")"

class Scale(models.Model):
    name = models.CharField(max_length=64, verbose_name="Scale Name", unique=True)
    def __str__(self):
        return self.name

            
class ScaleEntry(models.Model):
    entry = models.CharField(max_length=64, verbose_name="Entry")
    weight = models.IntegerField(verbose_name="Weight")
    scale = models.ForeignKey(Scale, on_delete=models.CASCADE)
    def __str__(self):
        return  self.entry # + " (" + self.scale.name + ")"
    class Meta:
        unique_together = (('scale', 'entry'))    

class JudgingRound(models.Model):
    
    hackathon = models.ForeignKey(Hackathon, on_delete=models.CASCADE)
    number = models.IntegerField(default=1, verbose_name="Round")

    def __str__(self):
        return "round " + str(self.number)
    
class Criteria(models.Model):
    name = models.CharField(max_length=255, verbose_name="Criteria Name")
    scale = models.ForeignKey(Scale, on_delete=models.CASCADE)
    judging_round = models.ForeignKey(JudgingRound, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    
    class Meta:
        unique_together = (('name', 'judging_round'))    
    
        

    
class JudgeResponse(models.Model):
    round = models.ForeignKey(JudgingRound, on_delete=models.CASCADE)
    #should be subset of JudgingRound.judges
    judge = models.ForeignKey(Judge, on_delete=models.CASCADE, limit_choices_to={})
    #should be subset of JudgingRound.teams
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    #should be subset of JudgingRound.criteria
    criterion = models.ForeignKey(Criteria, on_delete=models.CASCADE)
    mark = models.ForeignKey(ScaleEntry, on_delete=models.CASCADE)

    def __str__(self):
        return "round " + str(self.round.number) + " response"
    
    class Meta:
        unique_together = (('round', 'judge', 'team', 'criterion'))
    

class Responses(models.Model):
    hack_id = models.IntegerField(verbose_name="Hack")
    round_no = models.IntegerField(verbose_name="Round")
    round_id = models.IntegerField(verbose_name="RID")
    judge_id = models.IntegerField(verbose_name="Judge")
    team_name = models.CharField(max_length=128, verbose_name="Team Name")
    judge_name = models.CharField(max_length=128, verbose_name="Judge Name")
    team_id = models.IntegerField(verbose_name="Team Id")
    criteria = models.CharField(max_length=256, verbose_name="Criteria Name")
    mark_weight = models.IntegerField(verbose_name="Weight")
    mark = models.CharField(max_length=256, verbose_name="Mark")
    class Meta:
        managed = False
        db_table = 'core_resonses_vw'
