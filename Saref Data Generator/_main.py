import device
import constants
import weatherStation

devices = {}

devices['T1T'] = device.Thermometer("T1T", (14,30,0), "Terrace",  25.5)
devices['T1B'] = device.Thermometer("T1B", (14,31,0), "Bedroom",  30.0)
devices['T1L'] = device.Thermometer("T1L", (14,30,0), "LivingRoom",  25.5)
devices['T1E'] = device.Thermometer("T1E", (14,31,0), "Entrance",  30.0)
devices['T1K'] = device.Thermometer("T1K", (14,30,0), "Kitchen",  25.5)

devices['W1L'] = device.DoorSwitch("W1L", (14,30,0), "LivingRoom", "CloseState")
devices['W2L'] = device.DoorSwitch("W2L", (14,30,0), "LivingRoom", "CloseState")
devices['D1L'] = device.DoorSwitch("D1L", (14,30,0), "LivingRoom", "CloseState")
devices['W1B'] = device.DoorSwitch("W1B", (14,30,0), "Bedroom", "CloseState")
devices['D1B'] = device.DoorSwitch("D1B", (14,30,0), "Bedroom", "CloseState")
devices['D1E'] = device.DoorSwitch("D1E", (14,30,0), "Entrance", "CloseState")
devices['W1K'] = device.DoorSwitch("W1K", (14,30,0), "Kitchen", "CloseState")
devices['D1K'] = device.DoorSwitch("D1K", (14,30,0), "Kitchen", "CloseState")
devices['D1U'] = device.DoorSwitch("D1U", (14,30,0), "UtilityRoom", "CloseState")

devices['L1T'] = device.LightSwitch("L1T", (14,30,0), "Terrace", "OffState")
devices['L1B'] = device.LightSwitch("L1B", (14,30,0), "Bedroom", "OffState")
devices['L1U'] = device.LightSwitch("L1U", (14,30,0), "UtilityRoom", "OffState")
devices['L1L'] = device.LightSwitch("L1L", (14,30,0), "LivingRoom", "OffState")
devices['L1E'] = device.LightSwitch("L1E", (14,30,0), "Entrance", "OffState")
devices['L1K'] = device.LightSwitch("L1K", (14,30,0), "Kitchen", "OffState")

devices['P1T'] = device.SmartPresence("P1T", (14,30,0), "Terrace", "OffState")
devices['P1B'] = device.SmartPresence("P1B", (14,30,0), "Bedroom", "OffState")
devices['P1U'] = device.SmartPresence("P1U", (14,30,0), "UtilityRoom", "OffState")
devices['P1L'] = device.SmartPresence("P1L", (14,30,0), "LivingRoom", "OffState")
devices['P1E'] = device.SmartPresence("P1E", (14,30,0), "Entrance", "OffState")
devices['P2E'] = device.SmartPresence("P2E", (14,30,0), "Entrance", "OffState")
devices['P1K'] = device.SmartPresence("P1K", (14,30,0), "Kitchen", "OffState")

devices['B1E'] = device.Button("B1E", (14,30,0), "Entrance", "OffState")

devices['WS1'] = weatherStation.WeatherStation("WS1", (14,30,0))



# print RDF content in a file
with open('measurements.ttl', 'w') as output_file:
  output_file.write(constants.PREAMBLE)
  for dev in devices.values():
    output_file.write(dev.getRDF())

