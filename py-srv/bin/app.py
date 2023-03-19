from elasticsearch import Elasticsearch
from elasticsearch.client import IndicesClient
import os

from settings import configurations
# from data import INDEX_NAME

INDEX_NAME=os.environ["INDEX_NAME"]

es = Elasticsearch(
        "elasticsearch:9200",
        http_auth=["elastic", "changeme"],
    )

client = IndicesClient(es)

client.create(index=INDEX_NAME, body=configurations)
