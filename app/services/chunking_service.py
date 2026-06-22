class ChunkingService:
    def __init__(self,chunking_size = 1000, overlap_size = 200):
        self.chunking_size = chunking_size
        self.overlap_size = overlap_size
    
    def chunk_text(self,text:str):
        chunks = []
        start = 0
        while start < len(text):
            end = min(start + self.chunking_size, len(text))
            chunk = text[start:end]
            chunks.append(chunk)
            start += self.chunking_size - self.overlap_size
        return chunks