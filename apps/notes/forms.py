from django import forms


class FormNote(forms.Form):
    ''' Form note '''
    body = forms.CharField(label='', widget=forms.Textarea())
    time = forms.CharField(label='',)

    body.widget.attrs.update({'placeholder': 'description ...'})
    time.widget.attrs.update({'class': 'datetime', 'placeholder': 'datetime ...'})
