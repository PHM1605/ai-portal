from fastapi import FastAPI, File
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
import io, base64, cv2
import numpy as np

app = FastAPI()

origins = ["http://localhost:3000"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"])

@app.post("/uploadImage")
async def uploadImage(image: bytes = File(...)):
    img_stream = io.BytesIO(image)
    img = cv2.imdecode(np.frombuffer(img_stream.read(), np.uint8), 1)
    outp_img_path = 'test.png'
    cv2.imwrite(outp_img_path, img)
    with open(outp_img_path, 'rb') as f:
        base64img = base64.b64encode(f.read())
    return base64img