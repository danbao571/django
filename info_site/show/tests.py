import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'info_site.settings')
django.setup()

# from show.models import Test
#
#
# e = Test()
# e.blog = {
#     'name': [
#         {'name': 'django', 'type': 2},
#         {'name': 'python', 'type': 1},
#         {'name': 'java', 'type': 1}
#                ]
#           }
#
# e.headline = 'again a test'
# # e.save()
# dict = {'pic': 'sadsadasd'}
# print(dict['pic'])

