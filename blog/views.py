from django.shortcuts import render
from .models import Post
# Create your views here.



from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
def posts(request):
    post_list = Post.objects.all()
    paginator = Paginator(post_list, 2)
    if request.GET.get('page'):
        # Grab the current page from query parameter
        page = int(request.GET.get('page'))
    else:
        page = None
       
    try:
        # Create a page object for the current page. 
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If the query parameter is empty then grab the first page.
        posts = paginator.page(1)
        page = 1
    except EmptyPage:
        # If the query parameter is greater than num_pages then grab the last page.
        posts = paginator.page(paginator.num_pages)
        page = paginator.num_pages
    
    return render(request, 'blog_listing_page.html', {
                      'posts':posts, 
                      'page_range': paginator.page_range, 
                      'num_pages': paginator.num_pages,
                      'current_page': page})