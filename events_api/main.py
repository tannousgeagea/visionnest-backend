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
    for file in files:
        try:
            file_path = save_folder / file.filename
            with file_path.open("wb") as buffer:
                shutil.copyfileobj(file.file, buffer)
        finally:
            await file.close()
    return JSONResponse(content={"message": f"{len(files)} files uploaded successfully"}, status_code=200)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Adjust the allowed origins as needed
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)