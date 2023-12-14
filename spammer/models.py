from django.db import models

NULLABLE = {'null': True, 'blank': True}


class Client(models.Model):
    '''класс-модель для получателей рассылок'''
    client_name = models.CharField(max_length=100, verbose_name='Имя клиента')
    email = models.EmailField(verbose_name='email клиента', **NULLABLE)
    spammer = models.ForeignKey('spammer.Spammer', on_delete=models.CASCADE, verbose_name='ФИО менеджера', **NULLABLE)
    is_active = models.BooleanField(verbose_name='действителен', default=True)


    def __str__(self):
        '''строковое отображение обьекта'''
        return f'{self.client_name}, {self.is_active}'

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'


class Spammer(models.Model):
    '''класс-модель для пользователей-менеджеров, формирующих рассылки'''
    spammer_name = models.CharField(max_length=100, verbose_name='ФИО менеджера')
    company = models.TextField(verbose_name='Компания', **NULLABLE)
    email = models.EmailField(verbose_name='email менеджера', **NULLABLE)
    is_active = models.BooleanField(verbose_name='действителен', default=True)


    def __str__(self):
        '''строковое отображение обьекта'''
        return f'{self.spammer_name}, {self.company}, {self.is_active}'

    class Meta:
        verbose_name = 'Менеджер'
        verbose_name_plural = 'Менеджеры'

