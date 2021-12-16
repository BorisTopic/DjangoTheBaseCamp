from django.shortcuts import render, redirect
from .models import Post, Contact, Newsletter
from django.core.paginator import Paginator

# Create your views here.


def home(request):
    return render(request, 'finalproject/home.html')


def thecampfire(request):
    thecampfire_posts = Post.objects.all()
    context = {
        'thecampfire_posts': thecampfire_posts
    }
    return render(request, 'finalproject/thecampfire.html', context)


def thecampfire_detail(request, post_id):
    thecampfire_posts = Post.objects.get(pk=post_id)
    context = {
        'thecampfire_posts': thecampfire_posts
    }
    return render(request, 'finalproject/thecampfire_detail.html', context)


def thecampfire_post(request):
    if request.method == 'POST':
        post_title = request.POST.get('post_title', '')
        post_summary = request.POST.get('post_summary', '')
        post_image = request.POST.get('post_image', '')
        post = Post(post_title=post_title, post_summary=post_summary, post_image=post_image)
        post.save()
        return redirect('finalproject:thecampfire')

    return render(request, 'finalproject/thecampfire_post.html')


def newsletter(request):
    newsletter_articles = Newsletter.objects.all()
    article_name = request.GET.get('article_name')
    if article_name != '' and article_name is not None:
        newsletter_articles = newsletter_articles.filter(title__icontains=article_name)
    paginator = Paginator(newsletter_articles, 3)
    page = request.GET.get('page')
    newsletter_articles = paginator.get_page(page)
    context = {
        'newsletter_articles': newsletter_articles
    }
    return render(request, 'finalproject/newsletter.html', context)


def contact(request):
    if request.method == 'POST':
        contact_name = request.POST.get('contact_name', '')
        contact_email = request.POST.get('contact_email', '')
        contact_summary = request.POST.get('contact_summary', '')
        contact = Contact(contact_name=contact_name, contact_email=contact_email, contact_summary=contact_summary)
        contact.save()
        return redirect('finalproject:home')

    return render(request, 'finalproject/contact.html')