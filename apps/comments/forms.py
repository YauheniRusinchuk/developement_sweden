from django import forms


class FormComment(forms.Form):
    ''' Form comments  '''
    text = forms.CharField(label="",)
    text.widget.attrs.update({'class': 'form_input', 'placeholder': 'comments ...'})
