import zmq
import msgpack

context = zmq.Context()

class _ZMQSessionMeta(type):
	"""
Defines a metaclass which keeps tracks of all addresses the sessions bind to. 
If a session is declared on the same address as another.
	"""
	pass
	
class _ZMQBaseSession(object):
	"""
	Creates a zmq session for any ZMQ socket type. Instead of using this class
	directly, it would generally be more helpful to use one of the subclasses
	because they 
	"""
	
	def __init__(self, **kwargs):
	 	if None in (kwargs.get("session_type"), kwargs.get("address")):
	 		raise Exception(""" 
	You must specify both a zmq socket type and address. Please call 	
	ZMQSession in the following fashion: 

		PullSession = ZMQSession(type="PULL", address="tcp://127.0.0.1:9000")

		You are seeing this error because you probably forgot to set one of the
		parameters. You gave the following attributes:
			session_type = %s
			name         = %s
	 		""" % (str(kwargs.get("type")), str(kwargs.get("address"))))
	 	
	 	self.session_type = kwargs.get("session_type")
	 	self.address = kwargs.get("address")
	 	if "://" not in self.address:
	 		"".join(["tcp://", self.address])
	 	try:
	 		self.socket = context.socket(getattr(zmq, str(self.session_type)))
	 		self.socket.connect(self.address)
	 	except Exception as e:
	 		raise Exception("""
You have attempted to create a zmq socket with the following attributes:
	session_type : %s
	address      : %s
Please use only one of the following types:
	REQ, REP, PUB, SUB, PAIR, DEALER, ROUTER, PULL, PUSH, XSUB, XPUB.
And use an open address. Please refer to the following error for more 
information:
	Error: %s
	 		""" % (str(self.session_type), str(self.address), str(e)) )
	 
	def close(self):
		self.socket.close()
		 	
class _ZMQRecvSession(_ZMQBaseSession):
	
	def receive(self):
		try:
			print self.address
			print self.session_type
			return self.socket.recv() 
			#return self.unpack(self.socket.recv())
		except Exception:
			try:
				return self.socket.recv()
			except Exception as e:
				raise Exception("""
	There was an error receiving a message.
	Error: %s
				""" % (str(e),))
	
	def unpack(self, message):
		try:
			return msgpack.unpackb(message)
		except Exception as e:
			raise Exception("""
	The data passed, was unable to be parsed by messagpack, probably because
	it is not in a binary format.
	
		Message: %s

		Error: %s
			
			""" % (str(message), str(e)))

class _ZMQSendSession(_ZMQBaseSession):
	
	def send(self, message):
		try:
			self.socket.send(self.pack(message))
		except Exception as e:
			print e
	def pack(self, message):
		try:
			return msgpack.packb(message)
		except Exception as e:
			return Exception(""" 
	The data passed was unable to be parsed into the messagepack binary format.
	Please only pack dicts, lists, and tuples in messagepack.
	
		Message: %s
	
		Error: %s
	
			""" % (str(message), str(e)))

class _ZMQSession(_ZMQSendSession, _ZMQRecvSession):
	pass
	
class ZMQPullSession(_ZMQRecvSession):
	"""
	Creates a new pull session with zmq
	"""
	def __init__(self, address):
		super(ZMQPullSession, self).__init__(
			session_type="PULL", address=str(address)
		)
		
class ZMQPushSession(_ZMQSendSession):
	"""
	Creates a new pull session with zmq
	"""
	def __init__(self, address):
		super(ZMQPushSession, self).__init__(
			session_type="PUSH", address=str(address)
		)
		
class ZMQReqSession(_ZMQSession):
	"""
	Creates a new pull session with zmq
	"""
	def __init__(self, address):
		super(ZMQReqSession, self).__init__(
			session_type="REQ", address=str(address)
		)

class ZMQRepSession(_ZMQSession):
	"""
	Creates a new pull session with zmq
	"""
	def __init__(self, address):
		super(ZMQRepSession, self).__init__(
			session_type="REP", address=str(address)
		)
		
