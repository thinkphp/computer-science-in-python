# Introduction to Django Framework (Python 3)

Welcome to the introduction coursework for Django Framework using Python 3. This guide is designed for Stanford students and focuses on key concepts, each accompanied by at least three examples.

## 1. Django Project Structure

Django follows a specific project structure to organize your web application.

### Examples:

a. Creating a new Django project:
```
django-admin startproject mysite
```

b. Project directory structure:
```
mysite/
    manage.py
    mysite/
        __init__.py
        settings.py
        urls.py
        asgi.py
        wsgi.py
```

c. Creating a new app within the project:
```
python manage.py startapp blog
```

## 2. Models

Models in Django represent database tables and define the structure of your data.

### Examples:

a. Basic model for a blog post:
```python
from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    pub_date = models.DateTimeField('date published')
```

b. Model with foreign key relationship:
```python
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.CharField(max_length=100)
    text = models.TextField()
```

c. Model with many-to-many relationship:
```python
class Tag(models.Model):
    name = models.CharField(max_length=50)

class Post(models.Model):
    # ... other fields ...
    tags = models.ManyToManyField(Tag)
```

## 3. Views

Views handle the logic of your application and return responses to user requests.

### Examples:

a. Function-based view:
```python
from django.http import HttpResponse

def hello_world(request):
    return HttpResponse("Hello, World!")
```

b. Class-based view:
```python
from django.views import View
from django.http import HttpResponse

class HelloWorldView(View):
    def get(self, request):
        return HttpResponse("Hello, World!")
```

c. Generic list view:
```python
from django.views.generic import ListView
from .models import Post

class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
```

## 4. URLs

URL configuration maps URLs to views in your Django application.

### Examples:

a. Basic URL pattern:
```python
from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.hello_world, name='hello_world'),
]
```

b. URL pattern with parameters:
```python
urlpatterns = [
    path('posts/<int:year>/<int:month>/', views.monthly_archive, name='monthly_archive'),
]
```

c. Including app URLs in the main project:
```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),
]
```

## 5. Templates

Templates are used to generate HTML dynamically and separate the presentation logic from Python code.

### Examples:

a. Basic template:
```html
<!DOCTYPE html>
<html>
<head>
    <title>{% block title %}My Site{% endblock %}</title>
</head>
<body>
    {% block content %}
    {% endblock %}
</body>
</html>
```

b. Template inheritance:
```html
{% extends "base.html" %}

{% block title %}Blog Posts{% endblock %}

{% block content %}
    <h1>Latest Posts</h1>
    <ul>
    {% for post in posts %}
        <li>{{ post.title }}</li>
    {% endfor %}
    </ul>
{% endblock %}
```

c. Template with forms:
```html
<form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Submit</button>
</form>
```

## 6. Forms

Django provides a powerful form library to handle HTML forms and data validation.

### Examples:

a. Basic form:
```python
from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)
```

b. Model form:
```python
from django.forms import ModelForm
from .models import Post

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'pub_date']
```

c. Form handling in a view:
```python
from django.shortcuts import render, redirect
from .forms import ContactForm

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Process the data
            return redirect('success')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})
```

## 7. Authentication

Django provides a built-in authentication system to manage users and permissions.

### Examples:

a. User registration:
```python
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})
```

b. Login view:
```python
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
    return render(request, 'login.html')
```

c. Requiring login for a view:
```python
from django.contrib.auth.decorators import login_required

@login_required
def profile_view(request):
    return render(request, 'profile.html')
```

This introduction covers the fundamental concepts of Django with multiple examples for each. As you progress through the course, you'll delve deeper into these concepts and learn how to build complex web applications using Django.



I've created an introductory coursework for Django Framework using Python 3, focusing on key concepts with at least three examples for each. The content is structured as a markdown document, which makes it easy to read and potentially convert to other formats if needed.

The coursework covers seven fundamental concepts:
1. Django Project Structure
2. Models
3. Views
4. URLs
5. Templates
6. Forms
7. Authentication

Each section includes a brief explanation of the concept followed by at least three practical examples. This structure should help students understand both the theory and practical application of Django concepts.

Would you like me to explain or elaborate on any specific part of this coursework? Or perhaps you'd like to see how we could expand on a particular concept?
