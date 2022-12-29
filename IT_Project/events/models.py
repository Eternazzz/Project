from django.db import models


class Positions(models.Model):
    Position = models.CharField('Должность', max_length=30, null=False)
    Salary = models.IntegerField('Зарплата', null=False)

    def __str__(self):
        return f"{self.Position}"

    class Meta:
        verbose_name = "Должности"
        verbose_name_plural = "Должности"


class TypeofTour(models.Model):
    Title = models.CharField('Тип тура', max_length=30, null=False)
    Number_of_persons = models.IntegerField('Количество человек', null=True)

    def __str__(self):
        return f"{self.Title}"

    class Meta:
        verbose_name = "Виды туров"
        verbose_name_plural = "Виды туров"


class Events(models.Model):
    Name = models.CharField('Название мероприятия', max_length=60, null=False)
    Event_date = models.DateTimeField('Время проведения', null=False)
    Event_place = models.CharField('Местро проведения', max_length=50, null=False)

    def __str__(self):
        return f"{self.Name}"

    class Meta:
        verbose_name = "Мероприятия"
        verbose_name_plural = "Мероприятия"


class Hotels(models.Model):
    Name = models.CharField('Название отеля', max_length=30, null=False)
    Class = models.CharField('Класс отеля', max_length=30, null=False)

    def __str__(self):
        return f"{self.Name}"

    class Meta:
        verbose_name = "Отели"
        verbose_name_plural = "Отели"


class Employees(models.Model):
    Surname = models.CharField('Фамилия', max_length=25, null=False)
    Name = models.CharField('Имя', max_length=25, null=False)
    Patronymic = models.CharField('Отчество', max_length=25, null=False)
    Position = models.ForeignKey(Positions, on_delete=models.PROTECT, related_name='Positions')

    def __str__(self):
        return f"{self.Surname} {self.Name}"

    class Meta:
        verbose_name = "Работники"
        verbose_name_plural = "Работники"


class Clients(models.Model):
    Surname = models.CharField('Фамилия', max_length=25, null=False)
    Name = models.CharField('Имя', max_length=25, null=False)
    Patronymic = models.CharField('Отчество', max_length=25, null=False)
    Passport = models.CharField('Серия и номер пасспорта', max_length=11, null=False)
    Date_of_Birth = models.DateField('Дата рождения', null=False)
    Telephone = models.CharField('Номер телефона', max_length=16, null=True)

    def __str__(self):
        return f"{self.Surname} {self.Name}"

    class Meta:
        verbose_name = "Клиенты"
        verbose_name_plural = "Клиенты"


class Tours(models.Model):
    Name = models.CharField('Название тура', max_length=30, null=False)
    Departure = models.DateField('Отправление', null=False)
    Arrival = models.DateField('Прибытие', null=False)
    Type = models.ForeignKey(TypeofTour, on_delete=models.PROTECT)
    T_Events = models.ManyToManyField(Events, 'Мероприятия')
    T_Hotels = models.ManyToManyField(Hotels, 'Отели')

    def __str__(self):
        return f"{self.Name}"

    class Meta:
        verbose_name = "Туры"
        verbose_name_plural = "Туры"


class Sales(models.Model):
    Employee = models.ForeignKey(Employees, on_delete=models.PROTECT, related_name='Employees')
    Client = models.ForeignKey(Clients, on_delete=models.PROTECT, related_name='Clients')
    Tours = models.ForeignKey(Tours, on_delete=models.PROTECT, related_name='Tours')
    Date_of_sale = models.DateField('Дата продажи билета', null=False, auto_now=True)
    Price_of_sale = models.IntegerField('Цена билета', null=False)

    def __str__(self):
        return f'Продажа {self.Employee}'

    class Meta:
        verbose_name = "Продажи"
        verbose_name_plural = "Продажи"
