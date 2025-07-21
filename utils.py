"""
Este archivo es parte del ejemplo para sentar bases de git.
Este módulo contiene utilidades comunes que pueden ser utilizadas en diferentes partes del proyecto.
"""

def time_to_minutes(time : str) -> int:
  """
  Converts a time string in the format HH:mm:ss to the total number of minutes.

  Args:
    time (str): A string representing time in the format HH:mm:ss where:
                - HH is the number of hours.
                - mm is the number of minutes.
                - ss is the number of seconds.

  Returns:
    int: The total number of minutes. If the input string is not in the correct format, or contains invalid values, the function returns 0.
  """
  try:
    hours, minutes, seconds = map(int, time.split(":"))
    total_minutes = hours * 60 + minutes + seconds / 60
    return round(total_minutes)
  except ValueError:
    return 0