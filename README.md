# VlxControl
VlxControl is a lightweight service that uses [PyVLX](https://github.com/Julius2342/pyvlx) to control io-Homecontrol devices with a Velux KLF 200. Once started, it can be used to control windows, rollershutters, ... from any arbitrary home control software that can execute the curl command.

Installation
------------
Install dependencies and make it executable:

```bash
pip3 install -r requirements.txt
chmod +x vlxcontrol.py
```

Configuration
-------------
Please enter your KLF 200 connection information into the ./pyvlx.yaml configuration file.

Usage
----
```bash
usage: vlxcontrol.py [-h] [-c CONFIG] host port

positional arguments:
  host
  port

optional arguments:
  -h, --help            show this help message and exit
  -c CONFIG, --config CONFIG
                        specify the path to a pyvlx.yaml configuration file
```

Start the service running
```bash
./vlxcontrol.py <listen_address> <port>
```

and make calls using cURL. To close a window, for example, run

```bash
curl -X POST --data "{\"node\":\"windowNameInKlf\", \"position\":100}" --header "Content-Type: application/json" http://<your-server>:<port>/set
```
