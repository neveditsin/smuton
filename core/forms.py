from django import forms
from .models import Judge, Team, Scale, ScaleEntry, Criteria, Hackathon, JudgingRound, JudgeResponse
from _mysql import NULL


class JudgeForm(forms.ModelForm):

    class Meta:
        model = Judge
        fields = ['name', 'email', 'role', 'hackathon']
        exclude = ['hackathon']
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}

    def __init__(self, *args, **kwargs):
        return super(JudgeForm, self).__init__(*args, **kwargs)

    def is_valid(self):
        return super(JudgeForm, self).is_valid()

    def full_clean(self):
        return super(JudgeForm, self).full_clean()

    def clean_name(self):
        first_name = self.cleaned_data.get("name", None)
        return first_name

    def clean_email(self):
        email = self.cleaned_data.get("email", None)
        return email
    
    def clean_role(self):
        email = self.cleaned_data.get("role", None)
        return email

    def clean(self):
        return super(JudgeForm, self).clean()

    def validate_unique(self):
        return super(JudgeForm, self).validate_unique()

    def save(self, commit=True):
        return super(JudgeForm, self).save(commit)


class TeamForm(forms.ModelForm):

    class Meta:
        model = Team
        fields = ['name', 'participants', 'hackathon']
        exclude = ['hackathon']
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}

    def __init__(self, *args, **kwargs):
        return super(TeamForm, self).__init__(*args, **kwargs)

    def is_valid(self):
        return super(TeamForm, self).is_valid()

    def full_clean(self):
        return super(TeamForm, self).full_clean()

    def clean_name(self):
        name = self.cleaned_data.get("name", None)
        return name

    def clean_participants(self):
        participants = self.cleaned_data.get("participants", None)
        return participants

    def clean_hackathon(self):
        participants = self.cleaned_data.get("hackathon", None)
        return participants

    def clean(self):
        return super(TeamForm, self).clean()

    def validate_unique(self):
        return super(TeamForm, self).validate_unique()

    def save(self, commit=True):
        return super(TeamForm, self).save(commit)


class ScaleForm(forms.ModelForm):

    class Meta:
        model = Scale
        fields = ['name']
        exclude = []
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}

    def __init__(self, *args, **kwargs):
        return super(ScaleForm, self).__init__(*args, **kwargs)

    def is_valid(self):
        return super(ScaleForm, self).is_valid()

    def full_clean(self):
        return super(ScaleForm, self).full_clean()

    def clean_name(self):
        name = self.cleaned_data.get("name", None)
        return name

    def clean(self):
        return super(ScaleForm, self).clean()

    def validate_unique(self):
        return super(ScaleForm, self).validate_unique()

    def save(self, commit=True):
        return super(ScaleForm, self).save(commit)


class ScaleEntryForm(forms.ModelForm):

    class Meta:
        model = ScaleEntry
        fields = ['entry', 'weight']
        exclude = ['scale']
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}

    def __init__(self, *args, **kwargs):
        return super(ScaleEntryForm, self).__init__(*args, **kwargs)

    def is_valid(self):
        return super(ScaleEntryForm, self).is_valid()

    def full_clean(self):
        return super(ScaleEntryForm, self).full_clean()

    def clean_entry(self):
        entry = self.cleaned_data.get("entry", None)
        return entry

    def clean_weight(self):
        weight = self.cleaned_data.get("weight", None)
        return weight

    def clean(self):
        return super(ScaleEntryForm, self).clean()

    def validate_unique(self):
        return super(ScaleEntryForm, self).validate_unique()

    def save(self, commit=True):
        return super(ScaleEntryForm, self).save(commit)


class CriteriaForm(forms.ModelForm):

    class Meta:
        model = Criteria
        fields = ['name', 'scale']
        exclude = []
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}

    def __init__(self, *args, **kwargs):
        return super(CriteriaForm, self).__init__(*args, **kwargs)

    def is_valid(self):
        return super(CriteriaForm, self).is_valid()

    def full_clean(self):
        return super(CriteriaForm, self).full_clean()

    def clean_name(self):
        name = self.cleaned_data.get("name", None)
        return name

    def clean_scale(self):
        scale = self.cleaned_data.get("scale", None)
        return scale

    def clean(self):
        return super(CriteriaForm, self).clean()

    def validate_unique(self):
        return super(CriteriaForm, self).validate_unique()

    def save(self, commit=True):
        return super(CriteriaForm, self).save(commit)


class HackathonForm(forms.ModelForm):

    class Meta:
        model = Hackathon
        fields = ['name', 'desc']
        exclude = []
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}

    def __init__(self, *args, **kwargs):
        return super(HackathonForm, self).__init__(*args, **kwargs)

    def is_valid(self):
        return super(HackathonForm, self).is_valid()

    def full_clean(self):
        return super(HackathonForm, self).full_clean()

    def clean_name(self):
        name = self.cleaned_data.get("name", None)
        return name

    def clean_desc(self):
        desc = self.cleaned_data.get("desc", None)
        return desc

    def clean(self):
        return super(HackathonForm, self).clean()

    def validate_unique(self):
        return super(HackathonForm, self).validate_unique()

    def save(self, commit=True):
        return super(HackathonForm, self).save(commit)


class JudgingRoundForm(forms.ModelForm):

    class Meta:
        model = JudgingRound
        fields = ['hackathon', 'number']
        exclude = ['hackathon', 'number']
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}

    def __init__(self, *args, **kwargs):
        return super(JudgingRoundForm, self).__init__(*args, **kwargs)

    def is_valid(self):
        return super(JudgingRoundForm, self).is_valid()

    def full_clean(self):
        return super(JudgingRoundForm, self).full_clean()

    def clean_hackathon(self):
        hackathon = self.cleaned_data.get("hackathon", None)
        return hackathon

    def clean_number(self):
        number = self.cleaned_data.get("number", None)
        return number

    def clean(self):
        return super(JudgingRoundForm, self).clean()

    def validate_unique(self):
        return super(JudgingRoundForm, self).validate_unique()

    def save(self, commit=True):
        return super(JudgingRoundForm, self).save(commit)


class JudgeResponseFormHead(forms.Form):
    def __init__(self, jround, *args, **kwargs):
        super(JudgeResponseFormHead, self).__init__(*args, **kwargs)
        self.jround = jround
        self.fields['judge'] = forms.ModelChoiceField(queryset=Judge.objects.filter(hackathon = self.jround.hackathon), \
                                                         widget=forms.RadioSelect(), label = "Judge", \
                                                         required=True, empty_label = None)
        self.fields['team'] = forms.ModelChoiceField(queryset=Team.objects.filter(hackathon = self.jround.hackathon), \
                                                         widget=forms.RadioSelect(), label = "Team", \
                                                         required=True, empty_label = None) 

class JudgeResponseForm(forms.Form):
    def __init__(self, criteria, *args, **kwargs):
        super(JudgeResponseForm, self).__init__(*args, **kwargs)
        self.criteria = criteria
        self.fields['mark'] = forms.ModelChoiceField(queryset=ScaleEntry.objects.filter(scale = self.criteria.scale), \
                                                     widget=forms.RadioSelect(), label = criteria.name, \
                                                     required=True, empty_label = None)  

class UploadFileForm(forms.Form):
    file = forms.FileField()
    
    
class UploadMultiFileForm(forms.Form):
    file_field = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))