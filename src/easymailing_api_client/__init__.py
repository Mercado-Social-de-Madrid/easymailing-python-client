"""
A client library for accessing Easymailing API
"""
from .client import AuthenticatedClient, Client

__version__ = "0.2.dev0"

__all__ = (
    "AuthenticatedClient",
    "Client",
)
