from .models import Category,News
def latest_news(request):
    categories = Category.objects.all()
    latest_news = News.published.all().order_by('-publish_time')[:10]
    context = {
        'latest_news':latest_news,
        'categories':categories
    }
    return context