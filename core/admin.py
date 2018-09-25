from django.contrib import admin

from .models import Criteria, Hackathon, Judge, JudgingRound, Scale, ScaleEntry, Team, JudgeResponse

admin.site.register(Judge)
admin.site.register(Team)


admin.site.register(Scale)
admin.site.register(ScaleEntry)
admin.site.register(Criteria)

admin.site.register(Hackathon)
admin.site.register(JudgingRound)
admin.site.register(JudgeResponse)