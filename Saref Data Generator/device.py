import datetime

class Device():
  def __init__(self, deviceName, HHMMSS, room):
    self.deviceName = deviceName
    self.timestamp = None
    timeParams = [2020,12,2] + list(HHMMSS) + [0]
    self.timestamp = datetime.datetime(*timeParams).isoformat() 
    self.unixTimestamp = int(datetime.datetime(*timeParams).timestamp())
    self.room = room;
  
  def setState(self):
    pass
  
  def getRDF(self):
    pass

class Button(Device):
  def __init__(self, deviceName, HHMMSS, room, state="OffState"):
    super().__init__(deviceName, HHMMSS, room)
    self.setState(state)
  
  def setState(self, state):
    if state not in ["OnState", "OffState"]:
      raise Exception("State not allowed.")
    else:
      self.state = state

  def getRDF(self):
    PREFIX = "ex:"
    DEVICE_URI = PREFIX + self.deviceName
    STATE = self.state
    ROOM = self.room
    TIMESTAMP = self.timestamp
    UNIX_TIMESTAMP = self.unixTimestamp
    
    return f"""
{DEVICE_URI} rdf:type saref:Device ;
            rdf:type smart:SmartButton ;
      saref:hasState ex:{STATE} ;			
      smart:isLocatedIn ex:{ROOM} ;
      saref:hasTimestamp "{TIMESTAMP}"^^xsd:dateTime  ;
      smart:hasUnixTimestamp "{UNIX_TIMESTAMP}"^^xsd:integer  ;
.
"""

class Thermometer(Device):
  def __init__(self, deviceName, HHMMSS, room, temperature):
    super().__init__(deviceName, HHMMSS, room)
    self.temperature = temperature

  def getRDF(self):
    PREFIX = "ex:"
    DEVICE_URI = PREFIX + self.deviceName
    URI_M = PREFIX + self.deviceName + "_m1"
    VALUE = self.temperature
    TIMESTAMP = self.timestamp
    UNIX_TIMESTAMP = self.unixTimestamp
    ROOM = self.room;
    
    return f"""
{DEVICE_URI} rdf:type saref:TemperatureSensor ;
      saref:makesMeasurement {URI_M} ;
      smart:isLocatedIn ex:{ROOM} ;			
.

{URI_M} rdf:type saref:Measurement;
			saref:hasValue "{VALUE}"^^xsd:float ;
      saref:isMeasuredIn om:degree_Celsius ;
      saref:hasTimestamp "{TIMESTAMP}"^^xsd:dateTime  ;
      smart:hasUnixTimestamp "{UNIX_TIMESTAMP}"^^xsd:integer  ;
.
"""

class CO2sensor(Device):
  def __init__(self, deviceName, HHMMSS, room, ppm):
    super().__init__(deviceName, HHMMSS, room)
    self.ppm = ppm

  def getRDF(self):
    PREFIX = "ex:"
    DEVICE_URI = PREFIX + self.deviceName
    URI_M = PREFIX + self.deviceName + "_m1"
    VALUE = self.ppm
    TIMESTAMP = self.timestamp
    UNIX_TIMESTAMP = self.unixTimestamp
    ROOM = self.room;
    
    return f"""
{DEVICE_URI} rdf:type smart:CO2 ;
      saref:makesMeasurement {URI_M} ;
      smart:isLocatedIn ex:{ROOM} ;			
.

{URI_M} rdf:type saref:Measurement;
			saref:hasValue "{VALUE}"^^xsd:float ;
      saref:isMeasuredIn om:partsPerMillion ;
      saref:hasTimestamp "{TIMESTAMP}"^^xsd:dateTime  ;
      smart:hasUnixTimestamp "{UNIX_TIMESTAMP}"^^xsd:integer  ;
.
"""



class LightSwitch(Device):
  def __init__(self, deviceName, HHMMSS, room, state="OffState"):
    super().__init__(deviceName, HHMMSS, room)
    self.setState(state)
  
  def setState(self, state):
    if state not in ["OnState", "OffState"]:
      raise Exception("State not allowed.")
    else:
      self.state = state

  def getRDF(self):
    PREFIX = "ex:"
    DEVICE_URI = PREFIX + self.deviceName
    STATE = self.state
    ROOM = self.room
    #TIMESTAMP = self.timestamp
    
    return f"""
{DEVICE_URI} rdf:type saref:LightSwitch ;
      saref:hasState ex:{STATE} ;			
      smart:isLocatedIn ex:{ROOM} ;
.
"""

class SmartPresence(Device):
  def __init__(self, deviceName, HHMMSS, room, state="OffState"):
    super().__init__(deviceName, HHMMSS, room)
    self.setState(state)
  
  def setState(self, state):
    if state not in ["OnState", "OffState"]:
      raise Exception("State not allowed.")
    else:
      self.state = state

  def getRDF(self):
    PREFIX = "ex:"
    DEVICE_URI = PREFIX + self.deviceName
    STATE = self.state
    ROOM = self.room
    #TIMESTAMP = self.timestamp
    
    return f"""
{DEVICE_URI} rdf:type smart:SmartPresence ;
      saref:hasState ex:{STATE} ;			
      smart:isLocatedIn ex:{ROOM} ;
.
"""

class DoorSwitch(Device):
  def __init__(self, deviceName, HHMMSS, room, state="OffState"):
    super().__init__(deviceName, HHMMSS, room)
    self.setState(state)
  
  def setState(self, state):
    if state not in ["OpenState", "CloseState"]:
      raise Exception("State not allowed.")
    else:
      self.state = state

  def getRDF(self):
    if(self.deviceName.startswith('W')): 
      TYPE = 'smart:Window'
    else:
      TYPE = 'smart:Door'
    PREFIX = "ex:"
    DEVICE_URI = PREFIX + self.deviceName
    STATE = self.state
    #TIMESTAMP = self.timestamp
    ROOM = self.room

    
    return f"""
{DEVICE_URI} rdf:type saref:DoorSwitch ;
            rdf:type {TYPE} ;
      saref:hasState ex:{STATE} ;
      smart:isLocatedIn ex:{ROOM} ;
.
""" 