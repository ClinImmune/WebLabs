#ifndef __DISPATCHER
#define __DISPATCHER

#define DISPATCH_SUCCESSFUL 100
#define DISPATCH_PENDING    101
#define DISPATCH_FAILED     102

#define SERVER_ADDRESS      "127.0.0.1"
#define SERVER_PORT         9876

// Defines the struct for a FIFO queue
typedef struct job_queue {
	void *job;
	struct job_queue *next;
} job_queue;

// Initializes a new queue
job_queue *init_queue();

// Sends a message with the job id to the job manager
int push_job();
// Provides an interface
int create_job();

int connect_to_server();

#endif
