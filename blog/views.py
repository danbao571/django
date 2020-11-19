from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from blog.models import Blog, BlogType


def blog_detail(request, blog_pk):
    blog = get_object_or_404(Blog, pk=blog_pk)
    return render(request, 'blog/blog_detail.html', locals())


def blog_list(request):
    # 取出表中所有信息
    blog_list = Blog.objects.all()
    blog_types = BlogType.objects.all()
    # 实例化Paginator对象，按每页20条数据分页
    paginator = Paginator(blog_list, 5)
    # 获取前端传过来的p参数， 默认为1，
    page_num = request.GET.get('p', 1)
    # 返回p对应页数的数据
    page_of_blogs = paginator.get_page(page_num)
    # 获取当前页码
    cut_page = page_of_blogs.number
    # 返回的页码数
    num_list = [i for i in range(max(1, cut_page-2), cut_page)] + \
               [i for i in range(cut_page, min(cut_page+2, paginator.num_pages)+1)]
    return render(request, 'blog/blog_list.html', locals())


def get_blog_type(request, blog_type_pk):
    blog_types = BlogType.objects.all()
    blog_type = get_object_or_404(BlogType, pk=blog_type_pk)
    blog_list = Blog.objects.filter(blog_type=blog_type)
    paginator = Paginator(blog_list, 5)
    # 获取前端传过来的p参数， 默认为1，
    page_num = request.GET.get('p', 1)
    # 返回p对应页数的数据
    page_of_blogs = paginator.get_page(page_num)
    # 获取当前页码
    cut_page = page_of_blogs.number
    # 返回的页码数
    num_list = [i for i in range(max(1, cut_page - 2), cut_page)] + \
               [i for i in range(cut_page, min(cut_page + 2, paginator.num_pages) + 1)]
    return render(request, 'blog/blog_type.html', locals())
