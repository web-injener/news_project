from django.urls import path
from .views import news_detail,HomePage,ContactPageView,UzbekistonNewsView,DunyoNewsView,TalimNewsView,TexnologiyaNewsView,SportNewsView,SiyosatNewsView
urlpatterns = [
    path('', HomePage.as_view(),name="home_page"),
    path('contact/',ContactPageView.as_view(),name="contact_page"),
    path('yangliklar/uzbekiston/',UzbekistonNewsView.as_view(),name="uzbekiston_page"),
    path('yangliklar/siyosat/',SiyosatNewsView.as_view(),name="siyosat_page"),
    path('yangliklar/texnologiya/',TexnologiyaNewsView.as_view(),name="texnologiya_page"),
    path('yangliklar/sport/',SportNewsView.as_view(),name="sport_page"),
    path('yangliklar/dunyo/',DunyoNewsView.as_view(),name="dunyo_page"),
    path('yangliklar/talim/',TalimNewsView.as_view(),name="talim_page"),
    path('yangliklar/<slug:news>/', news_detail, name="news_detail"),
]