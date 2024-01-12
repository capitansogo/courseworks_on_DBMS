from django.db import models


class League(models.Model):
    name = models.CharField('Название лиги', max_length=50, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Лига'
        verbose_name_plural = 'Лиги'


class Teams(models.Model):
    name = models.CharField('Название команды', max_length=50)
    country = models.CharField('Страна', max_length=50)
    logo = models.ImageField('Логотип Команды', max_length=50, upload_to='media/')
    league = models.ForeignKey(League, on_delete=models.CASCADE, blank=True, null=True)
    goals = models.IntegerField('Голы', blank=True, null=True)
    goals_conceded = models.IntegerField('Пропущенные голы', blank=True, null=True)
    possession = models.FloatField('Владение мячом', blank=True, null=True)
    passings_accuracy = models.FloatField('Точность передач', blank=True, null=True)
    balls_recovered = models.IntegerField('Отборы', blank=True, null=True)
    tackles_won = models.IntegerField('Взятия мяча', blank=True, null=True)
    clean_sheets = models.IntegerField('Сухие матчи', blank=True, null=True)
    saves = models.IntegerField('Сэйвы', blank=True, null=True)
    distance_covered = models.FloatField('Пройденное расстояние', blank=True, null=True)
    yellow_cards = models.IntegerField('Желтые карточки', blank=True, null=True)
    red_cards = models.IntegerField('Красные карточки', blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Информация о команде'
        verbose_name_plural = 'Информация о командах'


class Players(models.Model):
    name = models.CharField('Имя', max_length=50)
    age = models.IntegerField('Возраст', blank=True, null=True)
    nationality = models.CharField('Национальность', max_length=50, blank=True, null=True)
    photo = models.ImageField('Фото', upload_to='images/')
    team = models.ForeignKey(Teams, on_delete=models.CASCADE)
    matches_played = models.CharField('Сыгранные матчи', blank=True, null=True, max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Информация о футболисте'
        verbose_name_plural = 'Информация о футболистах'


class Coach(models.Model):
    name = models.CharField('Имя', max_length=50)
    photo = models.ImageField('Фото', upload_to='images/')
    team = models.ForeignKey(Teams, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Информация о тренере'
        verbose_name_plural = 'Информация о тренерах'


class Matches(models.Model):
    name1 = models.ForeignKey(Teams, on_delete=models.CASCADE, related_name='name1')
    name2 = models.ForeignKey(Teams, on_delete=models.CASCADE, related_name='name2')
    date = models.DateField('Дата проведения матча')
    stage = models.CharField('Этап', max_length=50)
    goals1 = models.IntegerField('Голы', blank=True, null=True)
    goals2 = models.IntegerField('Голы', blank=True, null=True)
    possession1 = models.IntegerField('Владение мячом', blank=True, null=True)
    possession2 = models.IntegerField('Владение мячом', blank=True, null=True)
    league = models.ForeignKey(League, on_delete=models.CASCADE)
    total_attempts1 = models.IntegerField('Всего ударов', blank=True, null=True)
    total_attempts2 = models.IntegerField('Всего ударов', blank=True, null=True)
    attack1 = models.IntegerField('Атаки', blank=True, null=True)
    attack2 = models.IntegerField('Атаки', blank=True, null=True)
    corners1 = models.IntegerField('Угловые', blank=True, null=True)
    corners2 = models.IntegerField('Угловые', blank=True, null=True)
    passings_accuracy1 = models.IntegerField('Точность передач', blank=True, null=True)
    passings_accuracy2 = models.IntegerField('Точность передач', blank=True, null=True)
    passes_completed1 = models.IntegerField('Точные передачи', blank=True, null=True)
    passes_completed2 = models.IntegerField('Точные передачи', blank=True, null=True)
    offsides1 = models.IntegerField('Офсайды', blank=True, null=True)
    offsides2 = models.IntegerField('Офсайды', blank=True, null=True)
    yellow_cards1 = models.IntegerField('Желтые карточки', blank=True, null=True)
    yellow_cards2 = models.IntegerField('Желтые карточки', blank=True, null=True)
    red_cards1 = models.IntegerField('Красные карточки', blank=True, null=True)
    red_cards2 = models.IntegerField('Красные карточки', blank=True, null=True)

    def __str__(self):
        return f"{self.name1} {self.name2}"

    class Meta:
        verbose_name = 'Информация о матче'
        verbose_name_plural = 'Информация о матчах'


class WinnersEurope(models.Model):
    command = models.ForeignKey(Teams, on_delete=models.CASCADE)
    date = models.DateField('Дата', blank=True, null=True)
    total_wins = models.IntegerField('Всего побед', blank=True, null=True)

    def __str__(self):
        return f"{self.command}"

    class Meta:
        verbose_name = 'Победители Лиги Европы'
        verbose_name_plural = 'Победители Лиги Европы'


class WinnersChampions(models.Model):
    command = models.ForeignKey(Teams, on_delete=models.CASCADE)
    date = models.DateField('Дата', blank=True, null=True)
    total_wins = models.IntegerField('Всего побед', blank=True, null=True)

    def __str__(self):
        return f"{self.command}"

    class Meta:
        verbose_name = 'Победители Лиги Чемпионов'
        verbose_name_plural = 'Победители Лиги Чемпионов'
