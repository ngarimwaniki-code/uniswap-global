from django.shortcuts import render, redirect,  get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from .models import Exchange, BlogPost, Comment, UserActivity, Application, Profile, Document, Event, Feedback, Program, StudentStory, PartnerUniversity, CareerOpportunity, CulturalImmersionProgram, LanguageLearningExperience
from .forms import CustomUserCreationForm, ApplicationForm, ProfileForm, DocumentForm, EventForm,  FeedbackForm
from django.views.generic import ListView, DetailView, CreateView
from .models import *

@login_required
def programs(request):
    programs = Program.objects.all()
    return render(request, 'app/programs.html', {'programs': programs})

@login_required
def enroll_program(request, program_id):
    # Add your enrollment logic here
    return HttpResponse("Enrolled in program with ID: {}".format(program_id))

@login_required
def stories(request):
    stories = StudentStory.objects.all()
    return render(request, 'stories.html', {'stories': stories})

@login_required
def partners(request):
    partners = PartnerUniversity.objects.all()
    return render(request, 'partners.html', {'partners': partners})

def home(request):
    programs = Program.objects.all()  
    return render(request, 'app/home.html', {'programs': programs})

def register_request(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            Profile.objects.create(user=user)  # Create a profile for the new user
            login(request, user)
            return redirect("home")
    else:
        form = CustomUserCreationForm()
    return render(request, 'app/register.html', {'form': form})

def login_request(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            return render(request, 'app/login.html', {'error': "Invalid username or password"})
    return render(request, 'app/login.html')

def logout_request(request):
    logout(request)
    return redirect("home")

@login_required
def list_exchanges(request):
    exchanges = Exchange.objects.all()
    return render(request, 'app/exchange_list.html', {'exchanges': exchanges})

@login_required
def exchange_details(request, exchange_id):
    exchange = Exchange.objects.get(id=exchange_id)
    return render(request, 'app/exchange_details.html', {'exchange': exchange})

@login_required
def apply_for_exchange(request, exchange_id):
    exchange = Exchange.objects.get(id=exchange_id)
    application, created = Application.objects.get_or_create(user=request.user, exchange=exchange)
    if created:
        application.status = 'Applied'
        application.save()
        return redirect('exchange_details', exchange_id=exchange_id)
    else:
        return render(request, 'app/exchange_details.html', {'exchange': exchange, 'error': 'You have already applied to this program.'})

@login_required
def view_profile(request):
    try:
        profile = request.user.profile
    except Profile.DoesNotExist:
        profile = None
    
    return render(request, 'app/view_profile.html', {'profile': profile})


@login_required
def edit_profile(request):
    # Check if the user has a profile
    if hasattr(request.user, 'profile'):
        profile = request.user.profile
    else:
        # If the user does not have a profile, create one
        profile = Profile.objects.create(user=request.user)

    if request.method == "POST":
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('view_profile')
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'app/edit_profile.html', {'form': form})

@login_required
def upload_document(request):
    if request.method == "POST":
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            document = form.save(commit=False)
            document.user = request.user
            document.save()
            return redirect('view_documents')
    else:
        form = DocumentForm()
    return render(request, 'app/upload_document.html', {'form': form})

@login_required
def view_documents(request):
    documents = Document.objects.filter(user=request.user)
    return render(request, 'app/view_documents.html', {'documents': documents})

@login_required
@staff_member_required
def admin_dashboard(request):
    applications = Application.objects.filter(status='Applied')
    return render(request, 'app/admin_dashboard.html', {'applications': applications})

@login_required
@staff_member_required
def approve_application(request, application_id):
    application = Application.objects.get(id=application_id)
    application.status = 'Approved'
    application.save()
    return redirect('admin_dashboard')

def about(request):
    return render(request, 'app/about.html')

def contact(request):
    return render(request, 'app/contact.html')

def faq(request):
    return render(request, 'app/faq.html')

class EventListView(ListView):
    model = Event
    template_name = 'app/event_list.html'
    context_object_name = 'events'

class EventDetailView(DetailView):
    model = Event
    template_name = 'app/event_detail.html'


class EventCreateView(CreateView):
    model = Event
    form_class = EventForm
    template_name = 'app/event_create.html'
    success_url = '/events/'


@login_required
def submit_feedback(request):
    if request.method == "POST":
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.user = request.user
            feedback.save()
            return redirect('feedback_thankyou')
    else:
        form = FeedbackForm()
    return render(request, 'app/submit_feedback.html', {'form': form})

def feedback_thankyou(request):
    return render(request, 'app/feedback_thankyou.html')



def search(request):
    query = request.GET.get('q')
    results = []

    if query:
        profiles = Profile.objects.filter(user__username__icontains=query)
        applications = Application.objects.filter(user__username__icontains=query)
        countries = Country.objects.filter(name__icontains=query)
        schools = School.objects.filter(name__icontains=query)
        students = Student.objects.filter(user__username__icontains=query)
        exchanges = Exchange.objects.filter(title__icontains=query)
        interests = Interest.objects.filter(name__icontains=query)
        messages = Message.objects.filter(subject__icontains=query)
        reviews = Review.objects.filter(comment__icontains=query)
        documents = Document.objects.filter(title__icontains=query)
        events = Event.objects.filter(name__icontains=query)
        announcements = Announcement.objects.filter(title__icontains=query)

        results = {
            'profiles': profiles,
            'applications': applications,
            'countries': countries,
            'schools': schools,
            'students': students,
            'exchanges': exchanges,
            'interests': interests,
            'messages': messages,
            'reviews': reviews,
            'documents': documents,
            'events': events,
            'announcements': announcements,
        }

    return render(request, 'app/search_results.html', {'query': query, 'results': results})

@login_required
def career_opportunities(request):
    opportunities = CareerOpportunity.objects.all()
    return render(request, 'app/career_opportunities.html', {'opportunities': opportunities})

@login_required
def cultural_immersion(request):
    programs = CulturalImmersionProgram.objects.all()
    return render(request, 'app/cultural_immersion.html', {'programs': programs})

@login_required
def language_learning(request):
    experiences = LanguageLearningExperience.objects.all()
    return render(request, 'app/language_learning.html', {'experiences': experiences})