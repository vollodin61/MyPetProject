import uvicorn

from src.database.api.config.api_config import app

if __name__ == "__main__":
    uvicorn.run(app="api_main:app", reload=True)
