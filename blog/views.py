from .models import Post, Comment
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import (
    ListView,
)
from .forms import CommentForm


# Create your views here.


class PostListView(ListView):
    # so that we only display what has been published and not the drafts
    # no need to specify model
    queryset = Post.objects.filter(status="published").order_by("-created")
    template_name = "blog/index.html"
    paginate_by = 30
    paginate_orphans = 15
    



# im using a view function because it is handling a form so its more complex than the basic DetailView
def post_detail(request, post, pk):

    post=get_object_or_404(Post,slug=post,pk=pk,status='published')
    related_posts = post.tags.similar_objects()
    # List of active comments for this post
    comments = post.comments.filter(active=True)
    new_comment = None

    # i will get UnboundLocalError: local variable 'comment_form' referenced before assignment 
    # if i dont specify this as then comment_form will be specified only inside the loop.
    
    comment_form = CommentForm()

    if request.method == 'POST':
        # A comment was posted
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
            # redirect to same page and focus on that comment
            return redirect(post.get_absolute_url()+'#'+str(new_comment.id))
        else:
            comment_form = CommentForm()
            
    return render(
        request,
         'blog/post_detail.html',
         {'post':post,'comments': comments,'comment_form': comment_form,'related_posts': related_posts})


# handling reply, reply view
def reply_page(request):

    if request.method == "POST":

        form = CommentForm(request.POST)

        if form.is_valid():
            post_id = request.POST.get('post_id')  # from hidden input
            parent_id = request.POST.get('parent')  # from hidden input
            post_url = request.POST.get('post_url')  # from hidden input

            reply = form.save(commit=False)
    
            reply.post = Post(id=post_id)
            reply.parent = Comment(id=parent_id)
            reply.save()

            return redirect(post_url+'#'+str(reply.id))
    else:
        return redirect("/")