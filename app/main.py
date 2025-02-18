import os

import uvicorn
from fastapi import FastAPI, WebSocket
from fastapi.middleware.cors import CORSMiddleware

from routers.data_router import router as data_router

app = FastAPI()

app.include_router(data_router)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
async def startup_event():
    pass


@app.on_event("shutdown")
async def shutdown_event():
    pass


@app.get("/")
async def read_root():
    return {"message": "Welcome GO5!"}


# WebSocket endpoint
@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        await websocket.send_text(f"Message: {data}")


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host=os.getenv("API_HOST", default="0.0.0.0"),
        port=int(os.getenv("API_PORT", default="8000")),
        reload=True
    )
