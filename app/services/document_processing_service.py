from app.services.chunking_service import ChunkingService
from app.services.embedding_service import EmbeddingService
from app.services.vector_store_service import VectorStoreService


class DocumentProcessingService:
    def __init__(self, chunking_service: ChunkingService
                 , embedding_service: EmbeddingService
                 , vector_store_service: VectorStoreService):
        self.chunking_service = chunking_service
        self.embedding_service = embedding_service
        self.vector_store_service = vector_store_service

    async def process_document(self, text: str):

        chunks = self.chunking_service.chunk_text(text)
        embeddings = self.embedding_service.generate_embedding(chunks)
        self.vector_store_service.store_embeddings(chunks,embeddings) 


        # Here you can add any additional processing logic if needed
        