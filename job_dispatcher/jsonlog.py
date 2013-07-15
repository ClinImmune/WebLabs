import json
from datetime import datetime
from collections import OrderedDict

class LogManager(object):
	 
	 def __init__(self, *args, **kwargs):
	 	self.fileHandle = open("log.json", "r+a")
	 
	 def print_log(self):
	 	print self.fileHandle.read()
	 
	 def close(self):
	 	self.fileHandle.close()
	 	
	 def appendMessage(self, **kwargs):
	 	log_message = {} 
	 	log_message["code"] = kwargs.get("code")
	 	log_message["message"] = kwargs.get("message")
	 	log_message["time"] = str(datetime.now())
	 	
	 	if not log_message["message"]:
	 		raise ValueError("""
	 			You must specify a message to be logged, the more explicit, the
	 			better.
	 		""")
	 	
	 	self.fileHandle.write(
	 		"".join([
	 			json.dumps(log_message, indent=4),
	 			",\n"
	 		])
	 	)
	 	
if __name__ == "__main__":
	log = LogManager()
	log.appendMessage(code=1234, message="test message was appended")
	log.print_log()
	log.close()
