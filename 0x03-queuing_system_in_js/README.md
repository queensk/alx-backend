# 0x03. Queuing System in JS

This project is about implementing a queuing system in JavaScript using Node.js and Redis.

## What is a queuing system?

A queuing system is a way of processing tasks asynchronously and in order. A queue is a data structure that holds a collection of items, where the first item added is the first item removed (FIFO). A queuing system allows any process to send (enqueue) a task to the queue, and any process to receive (dequeue) the task from the front of the queue and execute it.

## Why use a queuing system?

A queuing system can be useful for handling long-running or resource-intensive tasks that do not need to be completed immediately or synchronously. For example, sending email newsletters, resizing images, processing payments, etc. A queuing system can also help with load balancing, fault tolerance, scalability and performance.

## How to use this project?

This project uses **BullMQ**¹, a Node.js library that implements robust queue systems based on Redis², a fast and reliable in-memory data store. To use this project, you need to have Node.js and Redis installed on your machine.

To install the dependencies, run:

```bash
npm install
```

To start the Redis server, run:

```bash
redis-server
```

To start the Node.js server, run:

```bash
node index.js
```

The Node.js server will create two queues: **emailQueue** and **imageQueue**. You can send tasks to these queues by making POST requests to the following endpoints:

- `/email` : This endpoint expects a JSON body with an `email` property containing a valid email address. It will enqueue a task to send a welcome email to that address.
- `/image` : This endpoint expects a JSON body with an `url` property containing a valid image URL. It will enqueue a task to download and resize the image to 200x200 pixels.

You can also monitor the status of the queues by making GET requests to the following endpoints:

- `/stats` : This endpoint will return a JSON object with the number of active, completed, failed and delayed tasks in each queue.
- `/logs` : This endpoint will return a JSON array with the logs of each task execution, including the queue name, task id, data and result.

## How to test this project?

This project uses **Mocha**³ and **Chai**⁴ for testing. To run the tests, run:

```bash
npm test
```

The tests will check the following scenarios:

- The server responds with status code 200 and a JSON object with a message property when receiving valid POST requests to `/email` and `/image`.
- The server responds with status code 400 and a JSON object with an error property when receiving invalid POST requests to `/email` and `/image`.
- The server responds with status code 200 and a JSON object with the queue statistics when receiving GET requests to `/stats`.
- The server responds with status code 200 and a JSON array with the task logs when receiving GET requests to `/logs`.
- The emailQueue and imageQueue are created and have workers assigned to them.
- The tasks are enqueued and executed correctly according to their data and result.
