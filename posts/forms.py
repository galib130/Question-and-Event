from posts.models import Post,Comment
from django import forms

class CommentForm(forms.ModelForm):

    class Meta():
        model=Comment
        fields=('author','text')

        widgets={
            'author':forms.TextInput(attrs= {'class':'textinput'}),
            'text':forms.Textarea(attrs={'class':'editable medium-editor-textarea'})

        }




