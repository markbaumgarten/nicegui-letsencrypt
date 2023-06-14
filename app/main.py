#!/usr/bin/env python3
import os

from nicegui import app, ui
from pathlib import Path
from fastapi import Request
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from starlette.middleware.sessions import SessionMiddleware

static_files = StaticFiles(
    directory=(Path(__file__).parent / 'static').resolve(),
    follow_symlink=True,
)
app.mount('/static', static_files, name='static')
app.add_middleware(SessionMiddleware,
                   secret_key=os.environ.get('SECRET_KEY', 'CHANGE_THIS!'))  # use your own secret key here


@ui.page('/')
async def main_page(request: Request) -> None:
    return RedirectResponse('/info')


@ui.page('/info')
async def info(request: Request) -> None:
    with ui.header().classes('bg-transparent'), ui.column().classes('w-full max-w-3xl mx-auto my-3'):
        ui.image('/static/logo.png').classes('max-w-[20%]')
    with ui.column().classes('w-full max-w-2xl mx-auto items-stretch'):
        ui.label("""Hello world""")

ui.run(title="myapp")
