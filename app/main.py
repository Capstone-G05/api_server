import uvicorn
from fastapi import FastAPI, WebSocket
from api.routers import data_router  # Adjust import path as needed
from fastapi.middleware.cors import CORSMiddleware
from services.db_service import connect_db, disconnect_db
from services.redis_service import connect_redis, disconnect_redis, load_data_to_redis

app = FastAPI()
app.include_router(data_router.router)

<<<<<<< HEAD
origins = [
    "http://localhost",        # For same machine
    "http://127.0.0.1",        # For same machine
    "http://192.168.100.135:8080",    # frontend machine
    "http://192.168.100.161:3000",
    "http://10.5.0.2:8080",
    "http://localhost:5173" # simulation frontend 
]

# CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Replace with frontend URL
=======
# CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Replace with frontend URL
>>>>>>> 86732a364e0ca8d66b28fc00b1af1eb51d6fbcf0
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
<<<<<<< HEAD
   uvicorn.run("main:app", host="127.0.0.1", port=8020, reload=True)
=======
   uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
>>>>>>> 86732a364e0ca8d66b28fc00b1af1eb51d6fbcf0

