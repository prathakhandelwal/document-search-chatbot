ALLOW_EXTENSION = {
    ".pdf",
    ".docx",
    ".txt",
    ".md"
}

MAX_FILE_SIZE = 10 * 1024 * 1024  # 10 MB

async def validate_file(file,content):
    extension = file.filename.split(".")[-1].lower()
    if f".{extension}" not in ALLOW_EXTENSION:
        raise ValueError("Unsupported file type")
    
    if len(content) > MAX_FILE_SIZE:
        file.file.seek(0)
        raise ValueError("File size exceeds the maximum limit")


       