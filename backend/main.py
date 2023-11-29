from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["http://localhost:3000"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"])

@app.post("/uploadImages")
async def uploadImages(images: list[UploadFile]):
    ret = []
    for img_upload in images:
        ret.append(img_upload.filename)
        data = await img_upload.read()
        outp_img_path = img_upload.filename
        with open(outp_img_path, 'wb') as f:
            f.write(data)
    return {'images': ret}
