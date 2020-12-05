#!/usr/bin/python3
# geektechstuff bluetooth
# https://geektechstuff.com/2020/06/01/python-and-bluetooth-part-1-scanning-for-devices-and-services-python/
import bluetooth

def scan_services():
   print("Scanning for bluetooth devices: ")
   devices = bluetooth.discover_devices(lookup_names = True)
   number_of_devices = len(devices)
   print(number_of_devices, "devices found")
   for addr,name in devices:
      print("\n")
      print("Device Name: %s" % (name))
      print("Device MAC Address: %s" % (addr))
      print("Services Found:")
      services = bluetooth.find_service(address=addr)
      if len(services) <=0:
          print("zero services found on", addr)
      else:
          for serv in services:
              print(serv['name'])
      print("\n")
   return()

scan_services()