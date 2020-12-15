from django.shortcuts import render
from .models import Article
from .documents import ArticleDocument

# Create your views here.
def home(request):
	# let's extract the url parameter
	query = request.GET.get('q')
	
	if query:
		# let's pass a query to our Elasticsearch index
        s = ArticleDocument.search()
		results = s.query('multi_match', query=query, fields=['title', 'text'])
		# let's convert the results into a Django queryset
        articles = s.to_queryset()
    else:
		# if there is no query, just return all articles
        articles = Article.events.all()
	
	context = {
		'articles': articles,
	}
	
	return render(request, 'home.html', context)