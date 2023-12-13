from django.db import models

NULLABLE = {'null': True, 'blank': True}

class Spammer(models.Model):
    '''класс-модель для пользователей-менеджеров, формирующих рассылки'''
    spammer_name = models.CharField(max_length=100, verbose_name='ФИО менеджера')
    company = models.TextField(verbose_name='Компания', **NULLABLE)
    is_active = models.BooleanField(verbose_name='действителен', default=True)


    def __str__(self):
        '''строковое отображение обьекта'''
        return f'{self.name}, {self.company}, {self.is_active}'

    class Meta:
        verbose_name = 'Менеджер'
        verbose_name_plural = 'Менеджеры'
