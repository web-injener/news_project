from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404
from django.urls import reverse
from django.views.generic import TemplateView, ListView
from .models import News,Category,Fotografiya
from .forms import ContactForm

def news_detail(request, news):
    idnews = get_object_or_404(News,slug=news,status=News.Status.published)
    context = {
        "idnews": idnews
    }
    return render(request,'news/news_detail.html',context=context)
class HomePage(ListView):
    model = News
    template_name = 'news/home.html'
    context_object_name = 'news' # =>News.objects.all() News modeldagi obektlar toplami 'news':news

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)

        context['categories'] = Category.objects.all()
        context['news'] = self.model.published.all().order_by('-publish_time')
        context['latest_news'] =self.model.published.all().order_by('-publish_time')[:5]
        context['uz_news'] = self.model.published.all().filter(category__name="o'zbekiston")[:6]
        context['tech_news'] = self.model.published.all().filter(category__name="texnologiya").order_by("-publish_time")
        context['sport_news'] = self.model.published.all().filter(category__name="sport").order_by('-publish_time')[:5]
        context['fotografiya'] = Fotografiya.objects.all()[:10]

        return context

class ContactPageView(TemplateView):
    template_name = 'news/contact.html'

    def get(self,request,*args,**kwargs):
        form = ContactForm()
        context ={
            "form":form
        }
        return render(request,'news/contact.html',context)

    def post(self,request,*args,**kwargs):
        form = ContactForm(request.POST)
        if request.method == 'POST' and form.is_valid():
            form.save()
            return HttpResponse("<p>Ma'lumotlar yuborildi</p>")
        context = {
            "form": form
        }
        return render(request,'news/contact.html',context)


class UzbekistonNewsView(ListView):
    model = News
    template_name = 'news/uzbekiston.html'
    context_object_name = 'uzb_news'

    def get_queryset(self):
        uzb_news = News.published.all().filter(category__name="o'zbekiston").order_by('-publish_time')
        return uzb_news


class SportNewsView(ListView):
    model = News
    template_name = 'news/sport.html'
    context_object_name = 'sport_news'

    def get_queryset(self):
        sport_news = News.published.all().filter(category__name="sport").order_by('-publish_time')
        return sport_news

class TexnologiyaNewsView(ListView):
    model = News
    template_name = 'news/texnologiya.html'
    context_object_name = 'tech_news'

    def get_queryset(self):
        tech_news = News.published.all().filter(category__name="texnologiya").order_by('-publish_time')
        return tech_news

class DunyoNewsView(ListView):
    model = News
    template_name = 'news/dunyo.html'
    context_object_name = 'dunyo_news'

    def get_queryset(self):
        dunyo_news = News.published.all().filter(category__name="dunyo").order_by('-publish_time')
        return dunyo_news

class SiyosatNewsView(ListView):
    model = News
    template_name = 'news/siyosat.html'
    context_object_name = 'siyosat_news'

    def get_queryset(self):
        siyosat_news = News.published.all().filter(category__name="siyosat").order_by('-publish_time')
        return siyosat_news


class TalimNewsView(ListView):
    model = News
    template_name = 'news/talim.html'
    context_object_name = 'talim_news'

    def get_queryset(self):
        talim_news = News.published.all().filter(category__name="ta'lim").order_by('-publish_time')
        return talim_news
