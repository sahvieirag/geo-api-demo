from utils import calculate_distance

# Usamos um dicionário como um banco de dados mockado
MOCK_DB = {
    "sao_paulo_sp": {
        "address": "Praça da Sé, s/n - Sé, São Paulo - SP, 01001-000",
        "coords": (-23.5505, -46.6333)
    },
    "rio_de_janeiro_rj": {
        "address": "Cristo Redentor, Parque Nacional da Tijuca - Alto da Boa Vista, Rio de Janeiro - RJ",
        "coords": (-22.9519, -43.2105)
    },
    "salvador_ba": {
        "address": "Largo do Pelourinho - Pelourinho, Salvador - BA, 40026-280",
        "coords": (-12.9714, -38.5108)
    },
    "google_campus_sp": {
        "address": "R. Coronel Oscar Porto, 70 - Paraíso, São Paulo - SP, 04003-000",
        "coords": (-23.5743, -46.6522)
    }
}

def find_nearby_locations(origin_name, radius_km):
  """
  Encontra locais no MOCK_DB dentro de um raio a partir de um local de origem.
  Esta função é intencionalmente um pouco ineficiente para fins de demonstração.
  """
  if origin_name not in MOCK_DB:
    return None, "Local de origem não encontrado."

  origin_coords = MOCK_DB[origin_name]["coords"]
  
  nearby_places = []
  for location_name, location_data in MOCK_DB.items():
    if location_name == origin_name:
      continue
    
    distance = calculate_distance(origin_coords, location_data["coords"])
    
    if distance <= radius_km:
      nearby_places.append({
          "name": location_name,
          "address": location_data["address"],
          "distance_km": round(distance, 2)
      })
      
  return nearby_places, None