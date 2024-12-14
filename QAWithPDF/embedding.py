from llama_index.core import Settings
from llama_index.embeddings.gemini import GeminiEmbedding
from llama_index.core import VectorStoreIndex
from llama_index.core.node_parser import SentenceSplitter

import sys
from exception import CustomException
from logger import logging


def download_gemini_embedding(model, document):
    """
    Downloads and initializes a Gemini Embedding model for vector embeddings.

    Returns:
    - VectorStoreIndex: An index of vector embeddings for efficient similarity queries.
    """
    try:
        logging.info("Initializing Gemini Embedding model")
        gemini_embed_model = GeminiEmbedding(
            model="models/gemini-1.5-flash-latest"
        )  # Check model name format

        # Ensure the Settings class is available
        Settings.llm = model
        Settings.embed_model = gemini_embed_model
        Settings.node_parser = SentenceSplitter(chunk_size=800, chunk_overlap=20)

        logging.info("Creating VectorStoreIndex")
        index = VectorStoreIndex.from_documents(
            document, embed_model=gemini_embed_model, llm=model
        )
        index.storage_context.persist()

        logging.info("Index and query engine initialized")
        query_engine = index.as_query_engine()
        return query_engine
    except Exception as e:
        raise CustomException(e, sys)
