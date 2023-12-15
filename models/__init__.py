#!/usr/bin/python3
"""
    This file makes this folder a package because of
    __init__ magic file.
"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
