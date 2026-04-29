from fastapi import FastAPI
from app.api.router import api_router

app = FastAPI(
    title="Vibe-Driven Agent API",
    description="从感性意图到理性工程的自动化架构 Agent",
    version="0.1.0"
)

# 挂载路由
app.include_router(api_router)

@app.get("/")
async def root():
    return {
        "status": "online",
        "mode": "Vibe-Driven",
        "docs": "/docs"
    }