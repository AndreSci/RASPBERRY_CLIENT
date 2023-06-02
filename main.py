""" For start, you need enter in terminal:
uvicorn main:app --port 8090 --reload
"""

from fastapi import FastAPI, status, HTTPException

import uvicorn

from routes.events import event_router
from routes.database import db_router
from misc.settings import SettingsIni

from misc.consts import GlobalConstsControl, LOGGER

load_settings = SettingsIni()
load_settings.create_settings()
GlobalConstsControl.create_logger()

# Объявляем главного главаря
app = FastAPI()

# Register routes
app.include_router(event_router, prefix="/event")
app.include_router(db_router, prefix="/db")


if __name__ == "__main__":
    # Напоминание для запуска через терминал
    # uvicorn main:app --port 8080 --reload
    from misc.consts import CLIENT_PORT, CLIENT_HOST

    def main():
        LOGGER.event("Был создан сервер из файла main.py")
    main()

    uvicorn.run("main:app", host=CLIENT_HOST, port=CLIENT_PORT, reload=False)
