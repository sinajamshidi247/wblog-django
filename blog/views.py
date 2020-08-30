from django.shortcuts import render, get_object_or_404
from .forms import AddCommentForm
from django.contrib import messages
from .models import Comment
from .models import Article



def all_articles(request):
    all_articles=Article.published.all()
    context={
        "all_articles":all_articles
    }
    return render(request,'blog/all_articles.html',context)

def article_detail(request,id,slug):
    #article=Article.objects.get(id=id,slug=slug)
    article=get_object_or_404(Article,id=id,slug=slug)
    comments=Comment.objects.filter(post=article,is_reply=False)
    if request.method == 'POST':
        form=AddCommentForm(request.POST)
       
        if form.is_valid():
            new_comment=form.save(commit=False)
            new_comment.post=article
            new_comment.user=request.user
            new_comment.save()
            messages.success(request,"done")
           
    else:
        form=AddCommentForm
           
    return render(request,'blog/article.html',{'article':article,'comments':comments,'form':form})