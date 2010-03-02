#!/usr/bin/env python
"""
<Author>
  Evan Meagher

<Start Date>
  March 1, 2010

<Description>
  Starts an XML-RPC server that allows remote clients to execute geolocation
  queries using the pygeoip library.

<Usage>
  python geoip_server.py /path/to/GeoIP.dat PORT

  Where /path/to/GeoIP.dat is the path to a legal GeoIP database. Databases can
  be downloaded at http://www.maxmind.com/app/ip-location.

  More information on pygeoip at http://code.google.com/p/pygeoip/.
"""

import sys
import urllib
from SimpleXMLRPCServer import SimpleXMLRPCServer
import pygeoip

# Handle arguments
if len(sys.argv) < 3:
    print "usage: python " + sys.argv[0] + " /path/to/GeoIP.dat PORT"
    sys.exit()

geoipdb_filename = sys.argv[1]
port = int(sys.argv[2])

# Get external IP
ip = urllib.urlopen('http://whatismyip.com/automation/n09230945.asp').read()

# Create XML-RPC server
server = SimpleXMLRPCServer(("localhost", port), allow_none=True)

# Initialize and register geoip object
geoip_obj = pygeoip.GeoIP(geoipdb_filename)
server.register_instance(geoip_obj)

# Run the server's main loop
server.serve_forever()
