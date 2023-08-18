from django import forms

from todo.models import Task, Tag


class TaskForm(forms.ModelForm):
    tag = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )
    deadline = forms.DateField(
        required=False,
        widget=forms.DateTimeInput(attrs={'type': 'date'}),
    )

    class Meta:
        model = Task
        fields = [
            "content",
            "deadline",
            "is_completed",
            "tag",
        ]


class TagForm(forms.ModelForm):

    class Meta:
        model = Tag
        fields = "__all__"
