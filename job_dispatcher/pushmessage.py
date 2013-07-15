import zmq
import msgpack
import threading
from datetime import datetime
from collections import OrderedDict

"""
class ThreadedSocket(type):
	
	def __init__(cls, name, bases, dct):
		super(ThreadedSocket, cls).__init__(name, bases, dct)
		cls.instance = None
		
	def __call__(cls, *args, **kwargs):
		if cls.instance is None:
			cls.instance = super(ThreadedSocket, cls). \
				__call__(*args, **kwargs)
		return cls.instance
"""

class ZMQSocket(object):
	#__metaclass__ = ThreadedSocket

	def __init__(self, *args, **kwargs):
		self.socket = self._generateSocket(**kwargs)
		
	def _generateSocket(self, **kwargs):
		PROTOCOL = kwargs.get("PROTOCOL", "tcp")
		HOST = kwargs.get("HOST", "127.0.0.1")
		PORT = kwargs.get("PORT", "2222")
		self.address = "".join([
			PROTOCOL,
			"://",
			HOST,
			":",
			PORT,
		])
		try:
			context = zmq.Context()
			sock = context.socket(zmq.PUSH)
			sock.bind(self.address)
			return sock
		except Exception as e:
			raise ValueError("""
There was an error processing your request. You bound a ZMQ 
push socket to the following address: %s.
	Error: %s
			""" % (self.address,e,))

	def push(self, **kwargs):
		msg = msgpack.packb(kwargs.get("message", None))
		self.socket.send(msg)
		

def sendMessage(**kwargs):
	msg = {}
	msg["message"] = "Hello"
	sock = ZMQSocket()
	sock.push(message=msg)
	print "##################################################################"
	
def printNum(*args):
	for arg in args:
		print str(arg)
	
if __name__ == "__main__":

	for i in range(0,100000):
		if i is 10000:
			thread = threading.Thread(target=sendMessage) 
		else:
			thread = threading.Thread(target=printNum, args=(i,))
		thread.start()
