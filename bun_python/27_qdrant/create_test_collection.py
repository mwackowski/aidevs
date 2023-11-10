from qdrant_client import QdrantClient
from qdrant_client.http import models

client = QdrantClient("localhost", port=6333)

client.create_collection(
    collection_name="first_test_collection",
    vectors_config=models.VectorParams(size=100, distance=models.Distance.COSINE),
)
