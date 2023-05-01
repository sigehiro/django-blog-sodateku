from django import forms
from .models import Comment


class CommentCreateForm(forms.ModelForm):
    
    class Meta:
        model = Comment
        fields = ('text',)
        labels = {'text':'コメント', }
        widgets = {
            'text':forms.Textarea(
            attrs={
                'class':'form-control',
                'placeholder':'内容',
                'row':5,
            }),
        }