from djongo import models


class News(models.Model):
    source_url = models.CharField(verbose_name="来源url", max_length=50, default='')
    company_name = models.CharField(verbose_name="公司名称", max_length=20, default='')
    linkman = models.CharField(verbose_name="联系人", max_length=10, default='')
    phone = models.CharField(verbose_name="联系电话", max_length=20, default='')
    address = models.CharField(verbose_name="地址", max_length=100, default='')
    create_user = models.CharField(verbose_name="创建者", max_length=10, default='')
    create_date = models.CharField(verbose_name="创建时间", max_length=20, default='')
    version = models.CharField(verbose_name="版本", max_length=10, default=0)
    is_deleted = models.CharField(verbose_name="是否删除", max_length=10, default=0)
    is_repeat = models.CharField(verbose_name="是否显示", max_length=10, default=0)

    def __str__(self):
        return self.company_name

    class Meta:
        verbose_name = '信息'
        verbose_name_plural = verbose_name
        ordering = ['company_name']


# +======================================================
# class TestBlog(models.Model):
#     name = models.CharField(max_length=100)
#     tagline = models.TextField()
#
#     def __str__(self):
#         return self.name
#
#
# class TestAuthor(models.Model):
#     name = models.CharField(max_length=200)
#     email = models.EmailField()
#
#     def __str__(self):
#         return self.name
#
#
# class TestEntry(models.Model):
#     # blog = models.ForeignKey(TestBlog, on_delete=models.CASCADE)
#     blog_name = models.CharField(max_length=100)
#     # 将blog的字段加进entry里，这样查询时会比sql join快
#     blog_tagline = models.TextField()
#     headline = models.CharField(max_length=255)
#     body_text = models.TextField()
#     pub_date = models.DateField()
#     mod_date = models.DateField()
#     authors = models.ManyToManyField(TestAuthor)
#     n_comments = models.IntegerField()
#     n_pingbacks = models.IntegerField()
#     rating = models.IntegerField()
#
#     def __str__(self):
#         return self.headline


# ==========================================================
# class TestBlog(models.Model):
#     name = models.CharField(max_length=100)
#     tagline = models.TextField()
#
#     class Meta:
#         abstract = True
#
#
# class MetaData(models.Model):
#     pub_date = models.DateField()
#     mod_date = models.DateField()
#     n_pingbacks = models.IntegerField()
#     rating = models.IntegerField()
#
#     class Meta:
#         abstract = True
#
#
# class TestAuthor(models.Model):
#     name = models.CharField(max_length=200)
#     email = models.EmailField()
#
#     def __str__(self):
#         return self.name
#
#
# class TestEntry(models.Model):
#     blog = models.EmbeddedField(
#         model_container=TestBlog,
#     )
#     meta_data = models.EmbeddedField(
#         model_container=MetaData,
#     )
#
#     headline = models.CharField(max_length=255)
#     body_text = models.TextField()
#     authors = models.ManyToManyField(TestAuthor)
#     n_comments = models.IntegerField()
#
#     def __str__(self):
#         return self.headline
