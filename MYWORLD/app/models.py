from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from taggit.managers import TaggableManager

class BlogPost(models.Model):
    STATUS_CHOICES = [
        ('Draft', 'Draft'),
        ('Published', 'Published'),
        ('Archived', 'Archived'),
    ]

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()
    published_date = models.DateTimeField(default=timezone.now)
    featured_image = models.ImageField(upload_to='blog_images/', null=True, blank=True)
    likes = models.ManyToManyField(User, related_name='liked_posts', blank=True)
    shares = models.PositiveIntegerField(default=0)
    views = models.PositiveIntegerField(default=0)
    tags = TaggableManager(blank=True)  # Using Taggit for tags
    is_featured = models.BooleanField(default=False)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Draft')
    slug = models.SlugField(max_length=255, unique=True)  # Slug field for SEO-friendly URLs

    def __str__(self):
        return self.title

    def total_likes(self):
        return self.likes.count()

    def total_comments(self):
        return self.comments.count()

    def get_absolute_url(self):
        return reverse('blog:post_detail', args=[self.slug])  # Define appropriate URL name

    class Meta:
        ordering = ['-published_date']  # Order posts by published date

class Comment(models.Model):
    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    likes = models.ManyToManyField(User, related_name='liked_comments', blank=True)

    def __str__(self):
        return f"Comment by {self.user.username} on {self.post.title}"

    def total_likes(self):
        return self.likes.count()

class UserActivity(models.Model):
    ACTIVITY_CHOICES = [
        ('View', 'View'),
        ('Like', 'Like'),
        ('Share', 'Share'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    activity_type = models.CharField(max_length=20, choices=ACTIVITY_CHOICES)
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.user.username} {self.activity_type} {self.post.title}"




class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    country = models.ForeignKey('Country', on_delete=models.SET_NULL, null=True)
    school = models.ForeignKey('School', on_delete=models.SET_NULL, null=True)
    interests = models.ManyToManyField('Interest', blank=True)

    def __str__(self):
        return self.user.get_full_name()

class Application(models.Model):
    STATUS_CHOICES = (
        ('Applied', 'Applied'),
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    exchange = models.ForeignKey('Exchange', on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Applied')

    def __str__(self):
        return f"{self.user.get_full_name()} - {self.exchange.title}"

class Country(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class School(models.Model):
    name = models.CharField(max_length=200)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    website = models.URLField()
    address = models.TextField()

    def __str__(self):
        return self.name

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    interests = models.ManyToManyField('Interest')

    def __str__(self):
        return self.user.get_full_name()

class Exchange(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    host_school = models.ForeignKey(School, related_name='exchanges_hosted', on_delete=models.CASCADE)
    participating_schools = models.ManyToManyField(School, related_name='exchanges_participated')
    start_date = models.DateField()
    end_date = models.DateField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Interest(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Message(models.Model):
    sender = models.ForeignKey(User, related_name='sent_messages', on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, related_name='received_messages', on_delete=models.CASCADE)
    exchange = models.ForeignKey(Exchange, on_delete=models.CASCADE)
    subject = models.CharField(max_length=255)
    content = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.sender} -> {self.receiver}: {self.subject}"

class Review(models.Model):
    exchange = models.ForeignKey(Exchange, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(default=5)
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student} - {self.exchange}"

class Document(models.Model):
    exchange = models.ForeignKey(Exchange, on_delete=models.CASCADE)
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Event(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    location = models.CharField(max_length=255)
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()
    organizer = models.ForeignKey(User, on_delete=models.CASCADE)
    attendees = models.ManyToManyField(User, related_name='events_attending')

    def __str__(self):
        return self.name

class Announcement(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date = models.DateField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Gallery(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    cover_image = models.ImageField(upload_to='gallery_covers/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class GalleryImage(models.Model):
    gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='gallery_images/')
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.gallery.title} - Image {self.id}"

class FAQ(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField()

    def __str__(self):
        return self.question

class Poll(models.Model):
    question = models.CharField(max_length=255)
    options = models.TextField(help_text="Enter options separated by comma")
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question

class Vote(models.Model):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    voter = models.ForeignKey(User, on_delete=models.CASCADE)
    selected_option = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.voter} voted for {self.selected_option} in {self.poll}"

class Scholarship(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    provider = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    deadline = models.DateField()

    def __str__(self):
        return self.name

class Resource(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    file = models.FileField(upload_to='resources/')

    def __str__(self):
        return self.title

class News(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    published_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name



class Feedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=255)
    message = models.TextField()
    submitted_on = models.DateTimeField(default=now)

    def __str__(self):
        return f"Feedback from {self.user.username} - {self.subject}"

    

class Program(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    duration = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)  # Price field for program
    enrollment_open = models.BooleanField(default=True)  # Enrollment status field

    def __str__(self):
        return self.title

class StudentStory(models.Model):
    student_name = models.CharField(max_length=100)
    program = models.ForeignKey(Program, on_delete=models.CASCADE)
    story = models.TextField()
    date_posted = models.DateField()

    def __str__(self):
        return f"{self.student_name} - {self.program.title}"

class PartnerUniversity(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class CareerOpportunity(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    company = models.CharField(max_length=200)
    location = models.CharField(max_length=100)
    salary = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    posted_date = models.DateField()

    def __str__(self):
        return self.title

class CulturalImmersionProgram(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    duration = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    enrollment_open = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class LanguageLearningExperience(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    language = models.CharField(max_length=50)
    duration = models.CharField(max_length=100)
    level = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    enrollment_open = models.BooleanField(default=True)

    def __str__(self):
        return self.title
