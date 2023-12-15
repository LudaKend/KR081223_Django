from django.core.management import BaseCommand
from mailing.models import Mailing
from django.core.mail import send_mail

class Command(BaseCommand):
    def handle(self, *args, **options):
        '''формирует список отправлений'''
        send_list = Mailing.objects.all()
        print(send_list) # для отладки

        # for item in send_list:
        #     if item.
        #     print(item)
        #     Category.objects.create(**item)
        # category_for_create = []
        # for item in list_category:
        #     category_for_create.append(Category(**item['fields']))
        #
        # print(category_for_create)  #для отладки
        # Category.objects.bulk_create(category_for_create)