from fastapi import FastAPI

from caller.caller import router as caller_router

app = FastAPI(title="CallerApp", version="0.0.1")

app.include_router(caller_router.router)
