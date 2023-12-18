from django.core.management import BaseCommand
from mailing.models import Mailing
from spammer.models import Spammer, Client
from django.core.mail import send_mail

class Command(BaseCommand):
    def handle(self, *args, **options):
        '''формирует список отправлений'''
        send_list = Mailing.objects.all()
        print(send_list) # для отладки

        send_list = Mailing.objects.filter(status='2')
        print(send_list)  # для отладки

        for item in send_list:
            send_mail(subject=Mailing.subject, message=Mailing.mailing_text, from_email=Spammer.email, recipient_list=Client.email)
        #     print(item)
        #     print(item.status)
        #     print(item.spammer)
        #     if item.status == 'в работе':
        #         spammer = item.spammer
        #         print(spammer)
        #         print(item.spammer)

        #     Category.objects.create(**item)
        # category_for_create = []
        # for item in list_category:
        #     category_for_create.append(Category(**item['fields']))
        #
        # print(category_for_create)  #для отладки
        # Category.objects.bulk_create(category_for_create)