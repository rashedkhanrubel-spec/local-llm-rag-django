import chromadb
from sentence_transformers import SentenceTransformer
from django.conf import settings

class RAGPipeline:
    """Retrieval-Augmented Generation pipeline."""

    def __init__(self):
        self.embedder = SentenceTransformer("all-MiniLM-L6-v2")
        self.client = chromadb.PersistentClient(path=settings.CHROMA_DB_PATH)
        self.collection = self.client.get_or_create_collection("knowledge_base")

    def ingest(self, text: str, doc_id: str, metadata: dict = {}):
        chunks = self._chunk_text(text)
        embeddings = self.embedder.encode(chunks).tolist()
        ids = [f"{doc_id}_{i}" for i in range(len(chunks))]
        self.collection.add(documents=chunks, embeddings=embeddings,
                           ids=ids, metadatas=[metadata] * len(chunks))
        return len(chunks)

    def query(self, question: str, top_k: int = 5):
        embedding = self.embedder.encode([question]).tolist()
        results = self.collection.query(query_embeddings=embedding, n_results=top_k)
        return results["documents"][0] if results["documents"] else []

    def _chunk_text(self, text: str, chunk_size: int = 500):
        words = text.split()
        return [" ".join(words[i:i+chunk_size]) for i in range(0, len(words), chunk_size)]

