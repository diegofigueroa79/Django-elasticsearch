# Django-elasticsearch
Implementation of django-elasticsearch-dsl to create a full-text search feature.

The core process of integrating Elasticsearch came down to our documents.py script.

https://github.com/diegofigueroa79/Django-elasticsearch/blob/main/django_es_proj/articles/documents.py

From this script, we can tell Elasticsearch how we want it to index our Django models:

```python
@registry.register_document
class ArticleDocument(Document):
    class Index:
        # Name of the index
        name = 'articles'

        settings = {
            'number_of_shards': 1,
            'number_of_replicas': 0
        }
    # the fields that we want indexed
    title = fields.TextField(
        analyzer = my_analyzer,
        fields={'raw': fields.KeywordField()}
    )
    text = fields.TextField(
        analyzer = my_analyzer,
        fields={'raw': fields.KeywordField()}
    )
	
	# in this class we put all the fields
	# that we want indexed into elasticsearch
	# except the fields that we want to apply
	# our custom analyzer
    class Django:
        model = Article # the model associated with this Document
        fields = [
        ]
```
Everything will be setup under our ArticleDocument class. From this class you can make Elasticsearch queries so I think it's best practice to name it <You're model> + Document. 
Under our ArticleDocument class we are creating a Django class that will specify from which model Elasticsearch will be creating the indexed fields from.

Before you can start making queries with Elasticsearch, you must build your index. This can be done in the command line under the same directory where you have your
manage.py file.
```bash
python manage.py search_index --rebuild
```

After building your index and saving some example data you can now begin making queries with Elasticsearch with Django.
```python
result = ArticleDocument.search().query('match', title='example')
for hit in result:
  print(hit.title)
```
