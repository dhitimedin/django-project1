from django import forms
from books.models import Publisher, Author, Book
#from django.forms import modelform_factory

#PublisherForm = modelform_factory(Publisher)

TOPIC_CHOICES = (
    ('general', 'General enquiry'),
    ('bug', 'Bug report'),
    ('suggestion', 'Suggestion'),
)

class ContactForm(forms.Form):
    topic = forms.ChoiceField(choices=TOPIC_CHOICES)
    message = forms.CharField(widget=forms.Textarea())
    sender = forms.EmailField(required=False)

    def clean_message(self):
        message = self.cleaned_data.get('message', '')
        num_words = len(message.split())
        if num_words < 4:
            raise forms.ValidationError("Not enough words!")
        return message

class PublisherForm(forms.ModelForm):
    class Meta:
        model = Publisher
        fields = '__all__'  # Or specify individual fields if needed

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = '__all__'

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Enter book title'}),
            'publication_date': forms.DateInput(attrs={'type': 'date'}),
        }