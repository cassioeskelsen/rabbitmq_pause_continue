# RabbitMQ Pause and Continue

A demonstration of how to pause a queue consumer if a external condition is not satisfied. When the condition is satisfied, the consumer restart

This is especially useful when a worker need call a external API to process the data coming from a Queue.

[app](app/) Main sample app.

[broker](broker/) A library to deal with the broker. Especific implementation for each broker are decoupled. On this sample I use RabbitMQ.

[some_external_api](some_external_api/api_simulator.py) run/stop this app to simulate a external API that needs to be called after a message arrives in some queue.  

[some_external_queue_seed](some_external_queue_seed/external_producer_simulator.py) insert a message every 5 seconds on queue1

To run, open 3 terminals and: 

a) on first terminal run [some_external_api](some_external_api/api_simulator.py) with 

```
python -m some_external_api.api_simulator 
```

b) on second one run sample app  

```
source env.sh
python run.py 
```

and on the last one run [some_external_queue_seed](some_external_queue_seed/external_producer_simulator.py) to simulate a application insert messages on the queue:

```
source env.sh
python -m some_external_queue_seed.external_producer_simulator
```


After some time, stop "some_external_api" to simulate a problem.  