from django import forms

from front.models import User, Event, Discussion

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'first_name', 'last_name']

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'description', 'start_time', 'end_time', 'registration_deadline', 'location']
        exclude = ('organizer_id',)
        widgets = {
            'start_time': forms.DateInput(attrs={'type': 'date'}),
            'end_time': forms.DateInput(attrs={'type': 'date'}),
            'registration_deadline': forms.DateInput(attrs={'type': 'date'})
        }

class DiscussionForm(forms.ModelForm):
    class Meta:
        model = Discussion
        fields = ['title', 'content', 'images', 'item_type', 'timestamp']
        exclude = ('user_id', 'parent_id', 'event_id')