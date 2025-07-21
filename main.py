"""
This is the main file empty point for the application.
"""

from typing import Optional

def hello_world(name: str = None) -> Optional[str]:
  """
  Prints a hello world message.
  """
  if not name:
    return None
  return f"Hello, {name}"
