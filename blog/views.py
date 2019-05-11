from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Blog
# Create your views here.

def home(request):
    blogs = Blog.objects.all()
    return render(request, 'index.html',{'blog':blogs})

def detail(request, blog_id):
    blog_detail = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'detail.html',{'detail':blog_detail})

def new(request):
    return render(request, 'new.html')

def create(request):
    blog = Blog() # 이렇게하면 class의 틀이 들어간다
    blog.title = request.GET['title'] # class 틀에 데이터를 넣는다
    blog.body = request.GET['body'] # class 틀에 데이터를 넣는다
    blog.pub_date = timezone.datetime.now() # 현재 시간을 넣는다.
    blog.save() # DB에 저장
    return redirect('/detail/' + str(blog.id)) # 바로 출력

def delete(request, blog_id):
    #get_object_or_404(Blog, pk=blog_id).delete()
    memo = Blog.objects.get(pk = blog_id)
    memo.delete()

    return redirect('/')

def edit(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)

    return render(request, 'edit.html', {'blog':blog})

def update(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.save()

    return redirect('/detail/'+str(blog.id))

def about(request):
    text = request.GET['fulltext']
    text_len = text.split()
    text_dic = {}

    for word in text_len :
        if word in text_dic :
            text_dic[word] += 1
        else :
            text_dic[word] = 1

    return render(request, 'about.html', {'text':text, 'text_list':len(text_len), 'text_dic':text_dic.items()})
 