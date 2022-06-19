from django.shortcuts import render
from .models import Post

posts = [
    {
        'author' : 'Mohammad kawsar Alom Foysal',
        'title': 'Blog Post 1',
        'content': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Mollitia, autem ea? Natus esse fuga suscipit, quia culpa quaerat',
        'date_posted': 'july 27, 2021'
    },

    {
        'author' : 'Soyad Mohiful Islam ',
        'title': 'Blog Post 2',
        'content': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Mollitia, autem ea? Natus esse fuga suscipit, quia culpa quaerat',
        'date_posted': 'july 29, 2021'
    },
    {
        'author' : 'Forhad hossen hridoy ',
        'title': 'Blog Post 10',
        'content': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Mollitia, autem ea? Natus esse fuga suscipit, quia culpa quaerat',
        'date_posted': 'july 29, 2021'
    },
     {
        'author' : 'Takdirul Islam Sishir',
        'title': 'Blog Post 3',
        'content': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Mollitia, autem ea? Natus esse fuga suscipit, quia culpa quaerat',
        'date_posted': 'july 29, 2021'
    }
]



# Create your views here.
def home(request):
    context = {'posts': Post.objects.all()}
    return render(request, 'blog/home.html', context)

def about(request):
   return render(request, 'blog/about.html', {'title': 'about'})