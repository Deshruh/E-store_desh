from django.shortcuts import render


def articles(request):
    return render(request, 'articles/articles.html')


def article_details(request):
    return render(request, 'articles/article_details.html')
