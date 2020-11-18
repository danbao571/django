from django.shortcuts import render
from .models import News
from django.core.paginator import Paginator
from .serializer import NewsSerializer
from rest_framework import mixins
from rest_framework.pagination import PageNumberPagination
# from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets


class NewsPagination(PageNumberPagination):
    # 默认每页显示10条数据
    page_size = 10
    # 每页显示数据量按page_size=?自己设置
    page_size_query_param = 'page_size'
    # 页数
    page_query_param = 'p'
    # 默认最大页数页100
    max_page_size = 50


class NewsListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    招标信息列表页， 分页，搜索，排序，过滤
    """
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    pagination_class = NewsPagination
    # authentication_classes = (TokenAuthentication,)
    # filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    # # filter_class = GoodsFilter
    # # 要进行搜索的字段
    # search_fields = ('name', 'goods_brief', 'goods_desc')
    # ordering_fields = ('shop_price', 'add_time')
    # # 可以重写GenericAPIView类的get_queryset方法，用于各种条件的数据过滤
    # def get_queryset(self):
    #     # 取到Goods的数据集合，是惰性取值，不会立即调用。
    #     queryset = Goods.objects.all()
    #     # 前端传一个默认值为0的price_min的参数过来
    #     price_min = self.request.query_params.get('price_min', 0)
    #     # 如果有这个参数，生成符合条件的的数据集合并返回。
    #     if price_min:
    #         queryset = queryset.filter(shop_price__gt=int(price_min))
    #     return queryset


def page_list(request):
    # 取出表中所有信息
    news_list = News.objects.all()
    # 实例化Paginator对象，按每页20条数据分页
    paginator = Paginator(news_list, 20)
    # 获取前端传过来的p参数， 默认为1，
    page_num = request.GET.get('p', 1)
    # 返回p对应页数的数据
    page_of_news = paginator.get_page(page_num)
    # 获取当前页码
    cut_page = page_of_news.number
    # 返回的页码数
    num_list = [i for i in range(max(1, cut_page-2), cut_page)] + \
               [i for i in range(cut_page, min(cut_page+2, paginator.num_pages)+1)]
    return render(request, 'page_list.html', locals())


# class EntryListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
#     """
#     test 测试
#     """
#     queryset = Test.objects.all()
#     serializer_class = EntrySerializer
#     pagination_class = NewsPagination
