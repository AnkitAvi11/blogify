from django.shortcuts import render, redirect

from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import Blog
from django.utils.text import slugify
import string
from django.contrib import messages

#   function to generate random string of a given length
def random_string_generator(size = 10, chars = string.ascii_lowercase + string.digits): 
    return ''.join(random.choice(chars) for _ in range(size))

#   view function to handle the 
@login_required(login_url='/account/login/')
def add_blog(request) : 
    context = {}

    if request.method == 'POST' : 
        try : 
            title = request.POST.get('title')
            slug = slugify(title)
            description = request.POST.get('title')
            thumbnail = request.FILES.get('thumbnail')
            body = request.POST.get('body')

            context['title'] = title
            context['description'] = description
            context['body'] = body

            while Blog.objects.filter(slug=slug).exists() : 
                randstr = random_string_generator(size=10)
                slug = "{}-{}".format(slug, randstr)

            Blog.objects.create(user=request.user, title=title, description=description, thumbnail=thumbnail, body=body, slug=slug)

            messages.success(request, 'Blog has been sucessfully published')
            return redirect('/blog/add/')
            
        except Exception : 
            messages.error(request, Exception)
            return render(request, 'blog/addblog.html', context)    
    else : 
        return render(request, 'blog/addblog.html', context)


#   view function to view all the blogs
def viewallblogs(request) : 
    blogs = Blog.objects.exclude().order_by('-pub_date')
    print(blogs)
    return render(request, 'blog/blogs.html', {"blogs" : blogs})
