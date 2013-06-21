http://www.swig.org/Doc1.3/Python.html

#include <malloc.h>
#include <zmq.h>

#include "mongo.h"
#include "dispatch.h"

/* Notes:

Create methods so that python can update the server address if needed, so that 
the program does not need to be recompiled.

Have every job on the queue be handled  by the second thread, independent of
python. If a job fails, put it into the failure queue, and report all failures
into a text document of some kind
*/

// Program level variables
char *server_address;
int server_port;
job_queue *job_q;


job_queue *init_queue() {
	return_q = (job_queue *)malloc(sizeof(job_queue));
	if (!return_q) {
		printf("There has been a fatal error, no memory exists!\n");
	}
	
}

int push_job();
int create_job() {
	if (!job_q) {
		job_q = init_queue();
	}
}

int connect_to_server() {

}

