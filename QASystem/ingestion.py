from haystack import Pipeline
from haystack.components.writers import DocumentWriter
from haystack.components.preprocessors import DocumentSplitter
from haystack.components.embedders import SentenceTransformersDocumentEmbedder
from haystack_integrations.document_stores.pinecone import PineconeDocumentStore
from haystack.components.converters import PyPDFToDocument
from pathlib import Path # type: ignore
import os
from dotenv import load_dotenv
from QASystem.utils import pinecone_config

def ingest():
    indexing=Pipeline(document_store)

    #adding the components in pipeline
    indexing.add_component("converter", PyPDFToDocument())
    indexing.add_component("splitter", DocumentSplitter(split_by="sentence", split_length=2))
    indexing.add_component("embedder", SentenceTransformersDocumentEmbedder())
    indexing.add_component("writer", DocumentWriter(document_store))

    indexing.connect("converter","splitter")
    indexing.connect("splitter", "embedder")
    indexing.connect("embedder", "writer")

    indexing.run({"converter": {"sources": [Path("E:\\Girish Documents\\Study\\Data Science\\DataScience_GenAI_Study\\GenAI_Project_EndToEnd-RAG-Application-Using-Haystack-Mistral-FastAPI\\Data\\Retrieval-Augmented-Generation-for-NLP.pdf")]}})


if __name__ == '__main__':
    document_store=pinecone_config()
    ingest()

