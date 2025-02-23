import os
import time

import uvicorn
from fastapi import FastAPI, WebSocket
from fastapi.middleware.cors import CORSMiddleware

from services.redis_service import RedisService
from services.sqlite_service import SQLiteService
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


# TODO: replace with lifespan event handler
@app.on_event("startup")
async def startup_event():
    datastore = RedisService()
    database = SQLiteService()
    database.initialize()
    datastore.load_data(database)
    database.close()
    datastore.close()


@app.get("/")
async def root():
    """
    Preform test of _Redis_ `datastore` and _SQLite_ `database`
    """
    datastore = RedisService()
    database = SQLiteService()

    # Test Redis
    datastore.set("TEST", 0)
    redis_start = time.time_ns()
    datastore.set("TEST", 1)
    redis_result = int(datastore.get("TEST")) == 1
    redis_end = time.time_ns()

    # Test SQLite
    database.execute("DELETE FROM redis_keys WHERE key = 'TEST'")
    sqlite_start = time.time_ns()
    database.execute("INSERT INTO redis_keys (key, value) VALUES ('TEST', 1)")
    cursor = database.execute("SELECT value FROM redis_keys WHERE key = 'TEST'")
    sqlite_result = int(cursor.fetchone()[0]) == 1
    sqlite_end = time.time_ns()

    datastore.close()
    database.close()

    return {
        "redis": {
            "status": "ONLINE" if redis_result else "OFFLINE",
            "delay": f"{(redis_end - redis_start) / 1000000} ms",
        },
        "sqlite": {
            "status": "ONLINE" if sqlite_result else "OFFLINE",
            "delay": f"{(sqlite_end - sqlite_start) / 1000000} ms",
        }
    }


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
