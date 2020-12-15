from django_elasticsearch_dsl import Document, fields
from django_elasticsearch_dsl.registries import registry
from elasticsearch_dsl import analyzer, tokenizer
from .models import Article

# this is our analyzer
# it describes how our fields will be indexed
my_analyzer = analyzer(
    'my_analyzer',
    tokenizer="standard",
    filter=["lowercase", "stop", "snowball"],
    char_filter=["html_strip"]
)

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