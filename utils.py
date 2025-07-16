from geopy.distance import great_circle

def calculate_distance(coord1, coord2):
  """
  Calcula a distância em quilômetros entre duas coordenadas (lat, lon).
  """
  if not coord1 or not coord2:
    return float('inf')
  return great_circle(coord1, coord2).kilometers