from django.urls import path
from .views import NewsList, NewsDetail, NewsSearchList, NewsAddList, NewsEditView, NewsDeleteView  # импортируем наше представление

urlpatterns = [
    # path — означает путь. В данном случае путь ко всем товарам у нас останется пустым, позже станет ясно, почему
    path('', NewsList.as_view()),
    path('search', NewsSearchList.as_view()),
    path('add', NewsAddList.as_view()),
    path('<int:pk>', NewsDetail.as_view(), name = 'note'),  # pk — это первичный ключ товара, который будет выводиться у нас в шаблон
    path('<int:pk>/edit', NewsEditView.as_view(), name = 'newsEdit'),
    path('<int:pk>/delete', NewsDeleteView.as_view(), name = 'newsDelete'),
]
