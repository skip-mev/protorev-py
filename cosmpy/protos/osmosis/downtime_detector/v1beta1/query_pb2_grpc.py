"""Client and server classes corresponding to protobuf-defined services."""
import grpc
from ....osmosis.downtime_detector.v1beta1 import query_pb2 as osmosis_dot_downtime__detector_dot_v1beta1_dot_query__pb2

class QueryStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.RecoveredSinceDowntimeOfLength = channel.unary_unary('/osmosis.downtimedetector.v1beta1.Query/RecoveredSinceDowntimeOfLength', request_serializer=osmosis_dot_downtime__detector_dot_v1beta1_dot_query__pb2.RecoveredSinceDowntimeOfLengthRequest.SerializeToString, response_deserializer=osmosis_dot_downtime__detector_dot_v1beta1_dot_query__pb2.RecoveredSinceDowntimeOfLengthResponse.FromString)

class QueryServicer(object):
    """Missing associated documentation comment in .proto file."""

    def RecoveredSinceDowntimeOfLength(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

def add_QueryServicer_to_server(servicer, server):
    rpc_method_handlers = {'RecoveredSinceDowntimeOfLength': grpc.unary_unary_rpc_method_handler(servicer.RecoveredSinceDowntimeOfLength, request_deserializer=osmosis_dot_downtime__detector_dot_v1beta1_dot_query__pb2.RecoveredSinceDowntimeOfLengthRequest.FromString, response_serializer=osmosis_dot_downtime__detector_dot_v1beta1_dot_query__pb2.RecoveredSinceDowntimeOfLengthResponse.SerializeToString)}
    generic_handler = grpc.method_handlers_generic_handler('osmosis.downtimedetector.v1beta1.Query', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))

class Query(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def RecoveredSinceDowntimeOfLength(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/osmosis.downtimedetector.v1beta1.Query/RecoveredSinceDowntimeOfLength', osmosis_dot_downtime__detector_dot_v1beta1_dot_query__pb2.RecoveredSinceDowntimeOfLengthRequest.SerializeToString, osmosis_dot_downtime__detector_dot_v1beta1_dot_query__pb2.RecoveredSinceDowntimeOfLengthResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)