#!/usr/bin/python3
"""
Creates a unique FileStorage instance for the application.
Then, reload the stored instance.
"""

from models.engine import file_storage

storage = file_storage.FileStorage()
storage.reload()
