from fastapi import APIRouter, UploadFile, File
from app.util.file_validator import validate_file
from app.services.document_service import DocumentService
from app.services.chunking_service import ChunkingService
import os

router = APIRouter()
document_service = DocumentService()

Upload_Directory = "uploads"

@router.post("/documents/upload")
async def upload_document(file: UploadFile = File(...)):
    content = await file.read()
    try:
        await validate_file(file,content)
    except ValueError as e:
        return {"error": str(e)}

    file_path = os.path.join(Upload_Directory, file.filename)

    with open(file_path, "wb") as buffer:
        buffer.write(content)

    extracted_text = document_service.extract_text(file_path)


    return {"message": "File uploaded successfully",
            "text": extracted_text,
            "filename": file.filename}