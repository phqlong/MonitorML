import logging

import grpc
import ml_monitor_pb2
import ml_monitor_pb2_grpc


def run():
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = ml_monitor_pb2_grpc.MLServiceStub(channel)

        print("-------------- GetStatus --------------")
        for token in ["12345678", "12345679", "12345680", "0"]:
            print("Token: " + token)
            try:
                request = ml_monitor_pb2.StatusRequest(token=token)
                response = stub.GetStatus(request)
                print(response)
            except Exception as e:
                print("Error: " + str(e.details()))

        print("\n-------------- Upload Files --------------")
        token = "12345678"
        print("Token: " + token)
        try:
            files = [
                ml_monitor_pb2.FileUpload(filename='file1.txt', content=b'File 1 content'),
                ml_monitor_pb2.FileUpload(filename='file2.txt', content=b'File 2 content'),
            ]
            request = ml_monitor_pb2.DataUploadRequest(token=token, files=files)
            response = stub.UploadData(request)
            print(response)
        except Exception as e:
            print("Error: " + str(e.details()))


if __name__ == "__main__":
    logging.basicConfig()
    run()
