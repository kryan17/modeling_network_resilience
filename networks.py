from geopy.distance import geodesic

# class Port:

class Server:
  def __init__(self, id, num_service_port):
    self.id = id
    self.num_service_port = num_service_port
    self.ports = []
    for x in self.num_service_port:
      self.ports.append([x, 'Open'])

  def check_open_ports(self, Server):
    self.server = Server


class Router:
  def __init__(self, id):
    self.id = id
    self.type = "Router"
    self.server = None

  def connect_to_server(self, Server):
    self.server = Server

class Tower:
  def __init__(self, id, lat, lon , range):
    self.id = id
    self.lat = lat
    self.lon = lon
    self.type = "Cell Tower"
    self.range = range #the range in km
    self.router = None

  def print_location(self):
    print("Cell tower", self.id, "exists at point (%f, %f)" %(self.lon, self.lat))

  def connect_to_server(self, Router):
    self.router = Router



class DataCenter:
  def __init__(self, id, lat, lon ):
    self.id = id
    self.lat = lat
    self.lon = lon
    self.type = "Data Center"

  def print_location(self):
    print("Data Center", self.id, "exists at point (%f, %f)" %(self.lon, self.lat))

class Device:
  def __init__(self, id, type:None, lat:None, lon:None):
    self.id = id
    self.type = type
    self.lat = lat
    self.lon = lon

  def check_tower_connection(self, tower):
    coords_1 = (self.lat, self.lon)
    coords_2 = (tower.lat, tower.lon)
    dist = geodesic(coords_1, coords_2).km
    print(dist)
    if dist < tower.range:
      # print("Can Connect")
      return True
    else:
      # print("Fails to Connect")
      return False


  def check_connection(self, tower):
    coords_1 = (self.lat, self.lon)
    coords_2 = (tower.lat, tower.lon)
    dist = geodesic(coords_1, coords_2).km
    print(dist)
    if dist < tower.range:
      # print("Can Connect")
      return True
    else:
      # print("Fails to Connect")
      return False

class User:
  def __init__(self, id, name, device=None):
    self.id = id
    self.name = name
    self.device = device

  def print_name(self):
    print("User", self.id, "is named %s" %(self.name))

  def give_device(self, device):
    self.device = device



