import device
import constants
import random

devices = {}

ROOM_NUMBER = 150

for n in range(1, ROOM_NUMBER+1):
  ppm = random.randint(100, 5010)
  presence = random.randint(0, 2)
  devices['CO2_'+str(n)] = device.CO2sensor("CO2_"+str(n), (14,30,0), "R"+str(n),  ppm)
  devices['PRESENCE_'+str(n)] = device.SmartPresence('PRESENCE_'+str(n), (14,30,0), "R"+str(n), "OnState" if presence else "OffState")




# print RDF content in a file
with open('measurements2.ttl', 'w') as output_file:
  output_file.write(constants.PREAMBLE)
  for dev in devices.values():
    output_file.write(dev.getRDF())

