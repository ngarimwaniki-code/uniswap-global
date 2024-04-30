from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Country, School, Student, Exchange, Interest, Message, Review, Document, Event, Announcement, Gallery, GalleryImage, FAQ, Poll, Vote, Scholarship, Resource, News, Feedback, Profile, Application,  BlogPost, Comment
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit, Field, Div, HTML
from crispy_forms.bootstrap import FormActions
from taggit.forms import TagField



class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'country', 'school', 'interests']
    
    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Div(
                Field('bio', css_class='form-control'),
                css_class='form-group'
            ),
            Div(
                Field('country', css_class='form-control'),
                css_class='form-group'
            ),
            Div(
                Field('school', css_class='form-control'),
                css_class='form-group'
            ),
            Div(
                Field('interests', css_class='form-control'),
                css_class='form-group'
            ),
            FormActions(
                HTML('<button type="submit" class="btn btn-primary">Save</button>')
            )
        )
class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['user', 'exchange', 'status']
    
    helper = FormHelper()
    helper.form_method = 'POST'
    helper.add_input(Submit('submit', 'Apply'))


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ("email",)

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Fieldset(
                'Sign Up',
                'username',
                'password1',
                'password2',
                'email',
                css_class='form-group'
            ),
            FormActions(
                Submit('save', 'Register', css_class='btn-primary')
            )
        )

        self.helper['email'].wrap(Field, css_class='email-input-class')
        self.helper.attrs = {'novalidate': '', 'style': 'background-color: white;'}

class CountryForm(forms.ModelForm):
    class Meta:
        model = Country
        fields = ['name']
    
    helper = FormHelper()
    helper.form_method = 'POST'
    helper.add_input(Submit('submit', 'Save'))

class SchoolForm(forms.ModelForm):
    class Meta:
        model = School
        fields = ['name', 'country', 'website', 'address']
    
    helper = FormHelper()
    helper.form_method = 'POST'
    helper.add_input(Submit('submit', 'Save'))

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['user', 'school', 'bio', 'interests']
    
    helper = FormHelper()
    helper.form_method = 'POST'
    helper.add_input(Submit('submit', 'Save'))

class ExchangeForm(forms.ModelForm):
    class Meta:
        model = Exchange
        fields = ['title', 'description', 'host_school', 'participating_schools', 'start_date', 'end_date', 'is_active']
    
    helper = FormHelper()
    helper.form_method = 'POST'
    helper.add_input(Submit('submit', 'Save'))

class InterestForm(forms.ModelForm):
    class Meta:
        model = Interest
        fields = ['name']
    
    helper = FormHelper()
    helper.form_method = 'POST'
    helper.add_input(Submit('submit', 'Save'))

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['sender', 'receiver', 'exchange', 'subject', 'content', 'is_read']
    
    helper = FormHelper()
    helper.form_method = 'POST'
    helper.add_input(Submit('submit', 'Send'))

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['exchange', 'student', 'rating', 'comment']
    
    helper = FormHelper()
    helper.form_method = 'POST'
    helper.add_input(Submit('submit', 'Save'))

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ['exchange', 'uploaded_by', 'title', 'file']
    
    helper = FormHelper()
    helper.form_method = 'POST'
    helper.add_input(Submit('submit', 'Upload'))

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['name', 'description', 'location', 'start_datetime', 'end_datetime', 'organizer', 'attendees']
    
    helper = FormHelper()
    helper.form_method = 'POST'
    helper.add_input(Submit('submit', 'Save'))

class AnnouncementForm(forms.ModelForm):
    class Meta:
        model = Announcement
        fields = ['title', 'content', 'date', 'author']
    
    helper = FormHelper()
    helper.form_method = 'POST'
    helper.add_input(Submit('submit', 'Publish'))

class GalleryForm(forms.ModelForm):
    class Meta:
        model = Gallery
        fields = ['title', 'description', 'cover_image']
    
    helper = FormHelper()
    helper.form_method = 'POST'
    helper.add_input(Submit('submit', 'Save'))

class GalleryImageForm(forms.ModelForm):
    class Meta:
        model = GalleryImage
        fields = ['gallery', 'image', 'description']
    
    helper = FormHelper()
    helper.form_method = 'POST'
    helper.add_input(Submit('submit', 'Upload'))

class FAQForm(forms.ModelForm):
    class Meta:
        model = FAQ
        fields = ['question', 'answer']
    
    helper = FormHelper()
    helper.form_method = 'POST'
    helper.add_input(Submit('submit', 'Save'))

class PollForm(forms.ModelForm):
    class Meta:
        model = Poll
        fields = ['question', 'options', 'created_by']
    
    helper = FormHelper()
    helper.form_method = 'POST'
    helper.add_input(Submit('submit', 'Create Poll'))

class VoteForm(forms.ModelForm):
    class Meta:
        model = Vote
        fields = ['poll', 'voter', 'selected_option']
    
    helper = FormHelper()
    helper.form_method = 'POST'
    helper.add_input(Submit('submit', 'Vote'))

class ScholarshipForm(forms.ModelForm):
    class Meta:
        model = Scholarship
        fields = ['name', 'description', 'provider', 'amount', 'deadline']
    
    helper = FormHelper()
    helper.form_method = 'POST'
    helper.add_input(Submit('submit', 'Apply'))

class ResourceForm(forms.ModelForm):
    class Meta:
        model = Resource
        fields = ['title', 'description', 'file']
    
    helper = FormHelper()
    helper.form_method = 'POST'
    helper.add_input(Submit('submit', 'Upload'))

class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['title', 'content']
    
    helper = FormHelper()
    helper.form_method = 'POST'
    helper.add_input(Submit('submit', 'Publish'))


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['user', 'subject', 'message']
    
    helper = FormHelper()
    helper.form_method = 'POST'
    helper.add_input(Submit('submit', 'Submit'))

