# MonitorML


This project is for monitoring ML systems, including managing dataset, supervising training and evaluating processes, and deployment of the ML system.


## How to run?

1. Initialize the proto file: 

    `python -m grpc_tools.protoc -I . --python_out=. --pyi_out=. --grpc_python_out=. ml_monitor.proto`

2. Run the server:
    `python server.py`

    
3. Then the server will be hosted on the specified port, we can call each api upon the server connecting to the specified port. Or run simple client for demo purposes:

    `python client.py`

