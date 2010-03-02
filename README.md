# GeoIP Server

A Python script to instantiate a simple XML-RPC server for remote geolocation lookups of IPs and hostnames.

Relies on [`pygeoip`](http://code.google.com/p/pygeoip/) and a [MaxMind GeoLite City database](http://www.maxmind.com/app/geolitecity) for the actual location lookups.

## Usage

    $ python geoip_server.py /path/to/GeoIP.dat PORT

Once the server is up and running, you can make requests to it using any XML-RPC client interface. For example, using Python's `xmlrpclib`:

    >>> import xmlrpclib
    
    >>> server = xmlrpclib.Server("http://ip:port")
    >>> print server.record_by_name("github.com")
    {'city': 'San Antonio', 'region_name': 'TX', 'area_code': 210, 'longitude': -98.574799999999996, 'country_code3': 'USA', 'country_name': 'United States', 'postal_code': '78229', 'dma_code': 641, 'country_code': 'US', 'latitude': 29.507200000000012}

The `pygeoip` functions `record_by_name` and `record_by_addr`, `region_by_name`, and `region_by_addr` are exposed for remote execution.
