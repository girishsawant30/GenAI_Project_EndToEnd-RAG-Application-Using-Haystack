from haystack.utils import Secret
from haystack.components.embedders import SentenceTransformersTextEmbedder
from haystack.components.builders import PromptBuilder
from haystack_integrations.components.retrievers.pinecone import PineconeEmbeddingRetriever
from haystack.components.generators import HuggingFaceTGIGenerator
from haystack import Pipeline
from QASystem.ingestion import ingest
from QASystem.utils import pinecone_config
import os
from dotenv import load_dotenv

def get_result(query):
    pass

if __name__ == '__main__':
    get_result()

    