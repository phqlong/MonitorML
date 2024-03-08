import grpc
import logging
from concurrent import futures

from ml_monitor_pb2 import (
    StatusRequest,
    StatusResponse,
    DataUploadRequest,
    DataUploadResponse,
    InferenceRequest,
    InferenceResponse,
)
from ml_monitor_pb2_grpc import MLServiceServicer, add_MLServiceServicer_to_server

import utils

logging.basicConfig(level=logging.INFO)


class MLMonitorServicer(MLServiceServicer):
    def __init__(self):
        pass

    def GetStatus(self, request: StatusRequest, context):
        data = utils.get_ml_monitor_data(token=request.token)
        if data:
            return StatusResponse(status=data["status"])
        else:
            context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
            context.set_details('Not found token in database!')
            return StatusResponse()
        

    def UploadData(self, request: DataUploadRequest, context) -> DataUploadResponse:
        data = utils.get_ml_monitor_data(token=request.token)

        if data:
            try:
                messages = utils.save_raw_data_to_file(
                    files_iterator=request.files,
                    data_path=data["data_path"]
                )
                return DataUploadResponse(messages=messages)
            except Exception as e:
                return DataUploadResponse(messages=["Failed! Details: " + str(e)])
        else:
            context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
            context.set_details('Not found token in database!')
            return DataUploadResponse()


    def Inference(self, request: InferenceRequest, context) -> InferenceResponse:
        
        return super().Inference(request, context)
    
        
  
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=4))
    add_MLServiceServicer_to_server(
        MLMonitorServicer(), server
    )
    server.add_insecure_port("[::]:50051")
    logging.info("Starting server on [::]:50051")

    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
