from django_filters import FilterSet  # импортируем filterset, чем-то напоминающий знакомые дженерики
from .models import News


# создаём фильтр
class NewsFilter(FilterSet):
    # Здесь в мета классе надо предоставить модель и указать поля, по которым будет фильтроваться (т. е. подбираться) информация о товарах
    class Meta:
        model = News
        fields = {
            'title': ['icontains'],
            'dateCreation': ['lt'],
            'author': ['icontains'],
        }  # поля, которые мы будем фильтровать (т. е. отбирать по каким-то критериям, имена берутся из моделей)
