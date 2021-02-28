from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.template.response import TemplateResponse
from django.urls import reverse
from rest_framework.views import APIView
from rest_framework.response import Response
from blog.models import Blog, BlogType
from django.http import JsonResponse
from djpjax import PJAXResponseMixin


def blog_detail(request, blog_pk):
    blog = get_object_or_404(Blog, pk=blog_pk)
    return render(request, 'blog/blog_detail.html', locals())


class BlogListView(PJAXResponseMixin, APIView):

    def get(slef, request, *args, **kwargs):
        data = slef.get_blog_list(request)

        if request.is_ajax():
            return render(request, 'blog/blog_list.html', locals())
        return render(request, 'blog/blog_list.html', locals())

    def get_blog_list(slef, request, *args, **kwargs):
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
        return locals()


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


class BlogTypeView(PJAXResponseMixin, APIView):

    def get(self, request):
        blog_type = request.GET.get('type')
        data = self.get_blog_list(request, blog_type)
        if request.is_ajax():
            return render(request, 'blog/blog_type.html', locals())
        return render(request, 'blog/blog_list.html', locals())

    def get_blog_list(slef, request, blog_type):
        # 取出表中所有信息
        blog_types = BlogType.objects.all()
        blog_type = get_object_or_404(BlogType, type_name=blog_type)
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
        return locals()


class TestView(APIView):

    def get(self, request):
        result = request.data
        result_1 = request.query_params
        print(request.GET)
        print(result_1)
        print(result)
        return JsonResponse(data=result)
