import openai
import os
import json
from llama_index.core import Settings
from llama_index.llms.openai import OpenAI
from llama_index.embeddings.openai import OpenAIEmbedding
from llama_index.core import VectorStoreIndex
from llama_index.core import SimpleDirectoryReader
from llama_index.core import StorageContext
from llama_index.core import load_index_from_storage
import logging
import sys

def check_directory(directory):
    """
    Check if the specified directory exists.
    """
    if not os.path.exists(directory):
        print(f"Directory '{directory}' does not exist.")
        return False
    return True

def load_documents_from_directory(directory):
    """
    Load documents from a directory using SimpleDirectoryReader.
    """
    reader = SimpleDirectoryReader(directory)
    documents = reader.load_data()
    return documents

def create_vector_index(documents):
    """
    Create a vector index from a list of documents using VectorStoreIndex.
    """
    index = VectorStoreIndex.from_documents(documents)
    return index

def save_vector_index(index, index_dir, filename):
    index.storage_context.persist(os.path.join(index_dir, filename))
    print(f"Vector index saved to '{os.path.join(index_dir, filename)}'.")
    
