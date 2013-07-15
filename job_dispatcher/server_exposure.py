import zmq
import msgpack
import psycopg2 as pg
import pymongo
from jsonlog import LogManager
from datetime import datetime
from collections import OrderedDict

"""
This module defines two methods which are used for parsing information
"""
class SendJobToDispatch(object):
	"""
	Helper class for sending messages over to dispatch.
	"""

	def __init__(self, *args, **kwargs):
		self.log = LogManager()
		
		self._mongo_fields = [
			("MONGO_DATABASE",),
			("MONGO_USERNAME",),
			("MONGO_PASSWORD",),
			("MONGO_HOST","localhost"),
			("MONGO_PORT","27017")
		]
		self._sql_fields = [
			("SQL_TYPE",),
			("SQL_DATABASE",),
			("SQL_HOST","localhost"),
			("SQL_PORT","5432")
		]
		self._zmq_fields = [
			("PROTOCOL", "tcp"),
			("HOST", "localhost"),
			("PORT", "2222")
		]
		## Validate mongo information


	def logMessage(self, **kwargs):
		self.log.appendMessage

	def _testMongoConnection(self, **kwargs):
		pass

	def _testPostgresConnection(self, **kwargs):
		pass


	def _generateDBMessage(**kwargs):
		"""
		TODO:
		---- Test connections to ensure message passing safety
	
		Defines a method which compiles all database information into an 
		OrderedDict.
		"""
		msg = OrderedDict()
	
		for field in _fields:
			if kwargs.get(field[0]):
				pass # all dandy
			try:
				field[1]
			except Exception as e:
				raise ValueError("""Fail""") 
		
			
	
	## Test connection settings
	## TODO add in postgres, and mongo. If needed, people can add other
	## database types as private methods
	
	
	def _generateRequestMessage(**kwargs):
		"""
		Generates a messagepack message which takes in parameters about the
		Mongo and SQL databases, and information about where the job
		information could be found.
		"""
		## Required Mongo Parameters
		msg = OrderedDict()
	
		## Job ID information
		## First value in fields is the kwarg nae
		## Second value is the default value
		_message_fields = [
			"MONGO_JOB_ID",  # Document ID field for job
			"SQL_JOB_TABLE", # SQL jobs table name
			"SQL_JOB_ID"     # SQL job id in jobs table
		]
		for field in _message_fields:
			if kwargs.get(field):
				msg[field] = kwargs.get(field)	
			else:
				raise ValueError("""
					There was an error parsing the key-word arguments for the
					generateRequestMessage function. Please correct your
					program and try again.
						Error: %s
				""" % (e,))

		try:
			return msgpack.packb(msg)
		except Exception as e:
			raise ValueError("""
				There was an error parsing your message into the messagepack
				binary format. Please refer to the following error for more
				information:
					%s
			""" % (str(e),))
		
	def _generateZMQRequest(**kwargs):
		"""
		Generates a ZeroMQ push socket which binds to the following defaults
			Protocol : tcp
			Host     : localhost
			Port     : 2222
		Topologically speaking, this function serves as the gateway between the
		web server and the job dispatchers. When called, it returns a 
		connection object which will be used for passing in
		"""
	
		PROTOCOL = kwargs.get("PROTOCOL", "tcp")
		HOST     = kwargs.get("HOST",     "localhost")
		PORT     = kwargs.get("PORT",     "2222")
		
		zmq_connection = "".join([
			PROTOCOL,
			"://",
			HOST,
			":",
			PORT
		]) 
	
		try:
			## Initialize ZeroMQ socket
			context = zmq.Context()
			sock = context.socket(zmq.PUSH)
			sock.bind(zmq_connection)
			return sock
	
		except Exception as e:
			raise ValueError("""
				There was an error processing your request. You bound a ZMQ 
				push socket to the following address: %s.
					Error: %s
			""" % (zmq_connection,e,))

	def sendMessage(**kwargs):
		"""
		Public function which parses three kwargs: database, message, and 
		connection.
		"""
		pass
		
if __name__ == "__main__":
	dispatcher = SendJobToDispatch()
	print "fuuuuu-"
	
