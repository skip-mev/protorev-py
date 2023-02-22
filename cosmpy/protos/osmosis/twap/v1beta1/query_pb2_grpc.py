"""Client and server classes corresponding to protobuf-defined services."""
import grpc
from ....osmosis.twap.v1beta1 import query_pb2 as osmosis_dot_twap_dot_v1beta1_dot_query__pb2

class QueryStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Params = channel.unary_unary('/osmosis.twap.v1beta1.Query/Params', request_serializer=osmosis_dot_twap_dot_v1beta1_dot_query__pb2.ParamsRequest.SerializeToString, response_deserializer=osmosis_dot_twap_dot_v1beta1_dot_query__pb2.ParamsResponse.FromString)
        self.ArithmeticTwap = channel.unary_unary('/osmosis.twap.v1beta1.Query/ArithmeticTwap', request_serializer=osmosis_dot_twap_dot_v1beta1_dot_query__pb2.ArithmeticTwapRequest.SerializeToString, response_deserializer=osmosis_dot_twap_dot_v1beta1_dot_query__pb2.ArithmeticTwapResponse.FromString)
        self.ArithmeticTwapToNow = channel.unary_unary('/osmosis.twap.v1beta1.Query/ArithmeticTwapToNow', request_serializer=osmosis_dot_twap_dot_v1beta1_dot_query__pb2.ArithmeticTwapToNowRequest.SerializeToString, response_deserializer=osmosis_dot_twap_dot_v1beta1_dot_query__pb2.ArithmeticTwapToNowResponse.FromString)
        self.GeometricTwap = channel.unary_unary('/osmosis.twap.v1beta1.Query/GeometricTwap', request_serializer=osmosis_dot_twap_dot_v1beta1_dot_query__pb2.GeometricTwapRequest.SerializeToString, response_deserializer=osmosis_dot_twap_dot_v1beta1_dot_query__pb2.GeometricTwapResponse.FromString)
        self.GeometricTwapToNow = channel.unary_unary('/osmosis.twap.v1beta1.Query/GeometricTwapToNow', request_serializer=osmosis_dot_twap_dot_v1beta1_dot_query__pb2.GeometricTwapToNowRequest.SerializeToString, response_deserializer=osmosis_dot_twap_dot_v1beta1_dot_query__pb2.GeometricTwapToNowResponse.FromString)

class QueryServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Params(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ArithmeticTwap(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ArithmeticTwapToNow(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GeometricTwap(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GeometricTwapToNow(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

def add_QueryServicer_to_server(servicer, server):
    rpc_method_handlers = {'Params': grpc.unary_unary_rpc_method_handler(servicer.Params, request_deserializer=osmosis_dot_twap_dot_v1beta1_dot_query__pb2.ParamsRequest.FromString, response_serializer=osmosis_dot_twap_dot_v1beta1_dot_query__pb2.ParamsResponse.SerializeToString), 'ArithmeticTwap': grpc.unary_unary_rpc_method_handler(servicer.ArithmeticTwap, request_deserializer=osmosis_dot_twap_dot_v1beta1_dot_query__pb2.ArithmeticTwapRequest.FromString, response_serializer=osmosis_dot_twap_dot_v1beta1_dot_query__pb2.ArithmeticTwapResponse.SerializeToString), 'ArithmeticTwapToNow': grpc.unary_unary_rpc_method_handler(servicer.ArithmeticTwapToNow, request_deserializer=osmosis_dot_twap_dot_v1beta1_dot_query__pb2.ArithmeticTwapToNowRequest.FromString, response_serializer=osmosis_dot_twap_dot_v1beta1_dot_query__pb2.ArithmeticTwapToNowResponse.SerializeToString), 'GeometricTwap': grpc.unary_unary_rpc_method_handler(servicer.GeometricTwap, request_deserializer=osmosis_dot_twap_dot_v1beta1_dot_query__pb2.GeometricTwapRequest.FromString, response_serializer=osmosis_dot_twap_dot_v1beta1_dot_query__pb2.GeometricTwapResponse.SerializeToString), 'GeometricTwapToNow': grpc.unary_unary_rpc_method_handler(servicer.GeometricTwapToNow, request_deserializer=osmosis_dot_twap_dot_v1beta1_dot_query__pb2.GeometricTwapToNowRequest.FromString, response_serializer=osmosis_dot_twap_dot_v1beta1_dot_query__pb2.GeometricTwapToNowResponse.SerializeToString)}
    generic_handler = grpc.method_handlers_generic_handler('osmosis.twap.v1beta1.Query', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))

class Query(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Params(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/osmosis.twap.v1beta1.Query/Params', osmosis_dot_twap_dot_v1beta1_dot_query__pb2.ParamsRequest.SerializeToString, osmosis_dot_twap_dot_v1beta1_dot_query__pb2.ParamsResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ArithmeticTwap(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/osmosis.twap.v1beta1.Query/ArithmeticTwap', osmosis_dot_twap_dot_v1beta1_dot_query__pb2.ArithmeticTwapRequest.SerializeToString, osmosis_dot_twap_dot_v1beta1_dot_query__pb2.ArithmeticTwapResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ArithmeticTwapToNow(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/osmosis.twap.v1beta1.Query/ArithmeticTwapToNow', osmosis_dot_twap_dot_v1beta1_dot_query__pb2.ArithmeticTwapToNowRequest.SerializeToString, osmosis_dot_twap_dot_v1beta1_dot_query__pb2.ArithmeticTwapToNowResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GeometricTwap(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/osmosis.twap.v1beta1.Query/GeometricTwap', osmosis_dot_twap_dot_v1beta1_dot_query__pb2.GeometricTwapRequest.SerializeToString, osmosis_dot_twap_dot_v1beta1_dot_query__pb2.GeometricTwapResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GeometricTwapToNow(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/osmosis.twap.v1beta1.Query/GeometricTwapToNow', osmosis_dot_twap_dot_v1beta1_dot_query__pb2.GeometricTwapToNowRequest.SerializeToString, osmosis_dot_twap_dot_v1beta1_dot_query__pb2.GeometricTwapToNowResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)