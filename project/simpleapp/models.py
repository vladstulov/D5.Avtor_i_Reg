from django.db import models
from django.core.validators import MinValueValidator

# Создаём модель новости
class News(models.Model):
    title = models.CharField(
        max_length=50,
        unique=True,
    )
    text = models.TextField()

    dateCreation = models.DateTimeField(auto_now_add=True)

    author = models.CharField(
        max_length=50,
    )

    # category = models.ForeignKey(
    #     to='Category',
    #     on_delete=models.CASCADE,
    #     related_name='news',  # все продукты в категории будут доступны через поле products
    # )

    def __str__(self):
        return f'{self.title.title()}. Дата публикации: {self.dateCreation.strftime("%d %B, %Y")}. {self.text[:50]}...'

    def get_absolute_url(self):  # добавим абсолютный путь, чтобы после создания нас перебрасывало на страницу с товаром
        return f'/news/{self.id}'
