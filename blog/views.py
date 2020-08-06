from django.shortcuts import render, get_object_or_404
from django.utils import timezone
import datetime
from django.contrib.auth.models import User
from .models import Post

#def post_list(request):
    # Tao post mau trog DB
    #user = User.objects.get(username='thaotran')
    #post_mau = Post.objects.get_or_create(
        #author = user,
        #title = "Post so 1",
        #text = "Day la post so 1",
        #created_date = datetime.datetime.now().date(),
        #published_date = datetime.datetime.now().date()
    #)
    # Lay tat ca posts ra
    #posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')

    # Gui response

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts':posts})
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})
