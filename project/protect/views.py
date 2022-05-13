from django.shortcuts import render

#from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import PermissionRequiredMixin



from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


from .models import News
from django.shortcuts import render
from django.core.paginator import Paginator
from .filters import NewsFilter  # импортируем недавно написанный фильтр
from .forms import NewsForm  # импортируем нашу форму


class NewsList(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = News  # указываем модель, объекты которой мы будем выводить
    template_name = 'protect/news.html'  # указываем имя шаблона, в котором будет лежать HTML, в котором будут все инструкции о том, как именно пользователю должны вывестись наши объекты
    context_object_name = 'news'  # это имя списка, в котором будут лежать все объекты, его надо указать, чтобы обратиться к самому списку объектов через HTML-шаблон
    queryset = News.objects.order_by('-dateCreation')
    ordering = ['-dateCreation']
    paginate_by = 10
    permission_required = 'protect.view_news'
    # form_class = NewsForm

    def get_context_data(self, **kwargs):  # забираем отфильтрованные объекты переопределяя метод get_context_data у наследуемого класса (привет, полиморфизм, мы скучали!!!)
        context = super().get_context_data(**kwargs)
        context['form'] = NewsForm()
        context['is_not_authors'] = not self.request.user.groups.filter(name='authors').exists()
        return context

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)  # создаём новую форму, забиваем в неё данные из POST-запроса

        if form.is_valid():  # если пользователь ввёл всё правильно и нигде не ошибся, то сохраняем новый товар
            form.save()

        return super().get(request, *args, **kwargs)

class NewsSearchList(PermissionRequiredMixin, ListView):
    model = News  # указываем модель, объекты которой мы будем выводить
    template_name = 'protect/newsSearch.html'  # указываем имя шаблона, в котором будет лежать HTML, в котором будут все инструкции о том, как именно пользователю должны вывестись наши объекты
    context_object_name = 'news'  # это имя списка, в котором будут лежать все объекты, его надо указать, чтобы обратиться к самому списку объектов через HTML-шаблон
    queryset = News.objects.order_by('-dateCreation')
    ordering = ['-dateCreation']
    paginate_by = 1
    permission_required = 'protect.view_news'

    def get_context_data(self, **kwargs):  # забираем отфильтрованные объекты переопределяя метод get_context_data у наследуемого класса (привет, полиморфизм, мы скучали!!!)
        context = super().get_context_data(**kwargs)
        context['filter'] = NewsFilter(self.request.GET, queryset=self.get_queryset())  # вписываем наш фильтр в контекст
        return context


class NewsDetail(PermissionRequiredMixin, DetailView):
    model = News  # модель всё та же, но мы хотим получать детали конкретно отдельного товара
    template_name = 'protect/note.html'  # название шаблона будет product.html
    context_object_name = 'note'  # название объекта. в нём будет
    permission_required = 'protect.view_news'


class NewsAddList(PermissionRequiredMixin, CreateView):
    permission_required = 'protect.add_news'
    template_name = 'protect/newsAdd.html'
    form_class = NewsForm

class NewsEditView(PermissionRequiredMixin, UpdateView):
    permission_required = 'protect.change_news'
    template_name = 'protect/newsEdit.html'
    form_class = NewsForm
    model = News  # модель всё та же, но мы хотим получать детали конкретно отдельного товара
    context_object_name = 'note'  # название объекта. в нём будет

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return News.objects.get(pk=id)



class NewsDeleteView(PermissionRequiredMixin, DeleteView):
    template_name = 'protect/newsDelete.html'
    context_object_name = 'note'
    queryset = News.objects.all()
    success_url = '/news/'
    permission_required = 'protect.delete_news'
