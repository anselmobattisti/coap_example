from coapthon.resources.resource import Resource
from coapthon.server.coap import CoAP
from threading import Thread
import sys

class Sensor(Resource):
  def __init__(self,name="Sensor",coap_server=None):
    super(Sensor,self).__init__(name,coap_server,visible=True,observable=True,allow_children=True)
    self.payload = ""
    self.resource_type = "rt1"
    self.content_type = "application/json"
    self.interface_type = "if1"

  def render_GET(self,request):    
    return self

  def render_POST(self, request):
    seres = self.init_resource(request, Sensor())
    return seres

class CoAPServer(CoAP):
  def __init__(self, host, port, multicast=False):
    CoAP.__init__(self,(host,port),multicast)
    self.add_resource('s1/',Sensor())
    print "CoAP server started on {}:{}".format(str(host),str(port))
    print self.root.dump()

def pollUserInput(server):
  while 1:
    user_input = raw_input("Add New Sensor: ")
    print user_input
    server.add_resource(user_input, Sensor())

def main():
  ip = sys.argv[1] #localhost
  port = int(sys.argv[2]) #5683
  multicast=False

  server = CoAPServer(ip,port,multicast)
  thread = Thread(target = pollUserInput, args=(server,))
  thread.setDaemon(True)
  thread.start()

  try:
    server.listen(10)
    print "executed after listen"
  except KeyboardInterrupt:
    print server.root.dump()
    server.close()
    sys.exit()

if __name__=="__main__":
  main()