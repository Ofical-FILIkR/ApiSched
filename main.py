import uvicorn
from fastapi import FastAPI

from src.api.routers import all_routers

app = FastAPI(
    title="api shedule"
)


for router in all_routers:
    app.include_router(router)


if __name__ == "__main__":
    uvicorn.run(app="main:app", reload=True)
