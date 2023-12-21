import smtplib

from django.core.management import BaseCommand
from mailing.models import Mailing
from spammer.models import Spammer, Client
from django.core.mail import send_mail
from config.settings import EMAIL_HOST_USER, EMAIL_HOST_PASSWORD
from django.conf import settings

class Command(BaseCommand):
    def handle(self, *args, **options):
        '''формирует список отправлений: выбирает записи рассылок со статусом 2 - в работе,и рассылает с адреса
        менеджера, которому принадлежит рассылка, по адресам клиентов этого менеджера, каждому персонально'''
        send_list = Mailing.objects.filter(status='2')
        print(f'send_list', send_list)  # для отладки

        for item in send_list:
            spammer_email = item.spammer.email
            #for client in item.spammer.clients.all():
            for client in item.spammer.spammer_in_client.all():
                try:
                    send_mail(subject=item.subject, message=item.mailing_text, from_email=spammer_email,
                      recipient_list=[client.email,])

                except (smtplib.SMTPRecipientsRefused, smtplib.SMTPDataError) as smtp_error:
                    print(smtp_error)

                # except Exception as e:
                #     print(e)
                #     raise e

        # for item in send_list:
        #     item.spammer.email
        #     print(f'item.spammer_id:', item.spammer_id)
        #     spammer_id = item.spammer_id
        #     # spammer = Spammer.objects.filter(id=item.spammer_id)
        #     # print(f'spammer:', spammer)
        #     # print(f'spammer[0]:', spammer[0])
        #
        #     spammer_list = Spammer.objects.values('id','email')
        #     print(f'spammer_list', spammer_list)
        #
        #     for pos in spammer_list:
        #         if pos['id'] == spammer_id:
        #             spammer_email = pos['email']
        #             print(spammer_email)



            # это рабочий вариант:
            #send_mail('Test', 'Test messsage', '663610kosmo85@mail.ru', ['python-spammer@mail.ru'])#это рабочий вариант
            # этот тоже рабочий вариант:
            #send_mail(subject='тема', message='текст письма', from_email='663610kosmo85@mail.ru', recipient_list=['python-spammer@mail.ru'])
            # и этот тоже рабочий вариант:
            #send_mail(subject=item.subject, message=item.mailing_text, from_email='663610kosmo85@mail.ru',
            #          recipient_list=['python-spammer@mail.ru'])
            #пытаюсь переменные подсунуть вместо адреса
            # send_mail(subject=item.subject, message=item.mailing_text, from_email=spammer_email,
            #           recipient_list=['python-spammer@mail.ru'])


            # send_mail(subject=Mailing.subject, message=Mailing.mailing_text, from_email=Spammer.email,
            #           recipient_list=Client.email)
        #     print(item)
        #     print(item.status)
        #     print(item.spammer)

        #     Category.objects.create(**item)
        # category_for_create = []
        # for item in list_category:
        #     category_for_create.append(Category(**item['fields']))
        #
        # print(category_for_create)  #для отладки
        # Category.objects.bulk_create(category_for_create)

