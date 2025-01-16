import uvicorn
from fastapi import FastAPI, WebSocket
from api.routers import data_router  # Adjust import path as needed
from fastapi.middleware.cors import CORSMiddleware
from services.db_service import connect_db, disconnect_db
from services.redis_service import connect_redis, disconnect_redis, load_data_to_redis

app = FastAPI()
app.include_router(data_router.router)

# CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Replace with frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def startup_event():
    connect_db("dbname.db")  
    connect_redis()
    load_data_to_redis()  #populate redis from sqlite

@app.on_event("shutdown")
async def shutdown_event():
    disconnect_db()
    disconnect_redis()

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
   uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)

