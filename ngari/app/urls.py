from django.urls import path
from . import views
from .views import search

urlpatterns = [
    path('register/', views.register_request, name='register'),
    path('login/', views.login_request, name='login'),
    path('logout/', views.logout_request, name='logout'),
    
    path('exchanges/', views.list_exchanges, name='exchange_list'),  # Changed name to 'exchange_list'
    path('exchange/<int:exchange_id>/', views.exchange_details, name='exchange_details'),
    path('exchange/<int:exchange_id>/apply/', views.apply_for_exchange, name='apply_for_exchange'),
    
    path('profile/', views.view_profile, name= 'view_profile'),
    path('edit-profile/', views.edit_profile, name='edit_profile'),
    path('upload-document/', views.upload_document, name='upload_document'),
    path('view-documents/', views.view_documents, name='view_documents'),
    
    path('admin/', views.admin_dashboard, name='admin_dashboard'),
    path('admin/approve/<int:application_id>/', views.approve_application, name='approve_application'),
    
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('faq/', views.faq, name='faq'),
    
    path('events/', views.EventListView.as_view(), name='events_list'),
    path('events/<int:pk>/', views.EventDetailView.as_view(), name='event_detail'),
    path('events/create/', views.EventCreateView.as_view(), name='event_create'),
    
    
    
    path('submit-feedback/', views.submit_feedback, name='submit_feedback'),
    path('feedback-thankyou/', views.feedback_thankyou, name='feedback_thankyou'),

    path('programs/', views.programs, name='programs'),
    path('enroll/<int:program_id>/', views.enroll_program, name='enroll_program'),
    path('stories/', views.stories, name='stories'),
    path('partners/', views.partners, name='partners'),

    path('search/', search, name='search'),

    path('career-opportunities/', views.career_opportunities, name='career_opportunities'),
    path('cultural-immersion/', views.cultural_immersion, name='cultural_immersion'),
    path('language-learning/', views.language_learning, name='language_learning'),
]
