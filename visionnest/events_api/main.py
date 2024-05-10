from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse
import shutil
from pathlib import Path

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

@app.post("/upload_images/")
async def upload_images(files: list[UploadFile] = File(...)):
    save_folder = Path("uploaded_images")
    save_folder.mkdir(exist_ok=True)
    if not files:
        return JSONResponse(content={"message": "No files included in the request"}, status_code=400)
    
    saved_files = []
    for file in files:
        try:
            file_path = save_folder / file.filename
            with file_path.open("wb") as buffer:
                shutil.copyfileobj(file.file, buffer)
            saved_files.append(file.filename)
        except Exception as e:
            return JSONResponse(content={"message": f"Failed to save {file.filename}. Error: {str(e)}"}, status_code=500)
        finally:
            await file.close()
    return JSONResponse(content={"message": f"{len(saved_files)} files uploaded successfully", "files": saved_files}, status_code=200)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Adjust the allowed origins as needed
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

