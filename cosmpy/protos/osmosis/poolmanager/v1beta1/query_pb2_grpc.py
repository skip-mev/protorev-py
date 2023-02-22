"""Client and server classes corresponding to protobuf-defined services."""
import grpc
from ....osmosis.poolmanager.v1beta1 import query_pb2 as osmosis_dot_poolmanager_dot_v1beta1_dot_query__pb2

class QueryStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Params = channel.unary_unary('/osmosis.poolmanager.v1beta1.Query/Params', request_serializer=osmosis_dot_poolmanager_dot_v1beta1_dot_query__pb2.ParamsRequest.SerializeToString, response_deserializer=osmosis_dot_poolmanager_dot_v1beta1_dot_query__pb2.ParamsResponse.FromString)
        self.EstimateSwapExactAmountIn = channel.unary_unary('/osmosis.poolmanager.v1beta1.Query/EstimateSwapExactAmountIn', request_serializer=osmosis_dot_poolmanager_dot_v1beta1_dot_query__pb2.EstimateSwapExactAmountInRequest.SerializeToString, response_deserializer=osmosis_dot_poolmanager_dot_v1beta1_dot_query__pb2.EstimateSwapExactAmountInResponse.FromString)
        self.EstimateSwapExactAmountOut = channel.unary_unary('/osmosis.poolmanager.v1beta1.Query/EstimateSwapExactAmountOut', request_serializer=osmosis_dot_poolmanager_dot_v1beta1_dot_query__pb2.EstimateSwapExactAmountOutRequest.SerializeToString, response_deserializer=osmosis_dot_poolmanager_dot_v1beta1_dot_query__pb2.EstimateSwapExactAmountOutResponse.FromString)
        self.NumPools = channel.unary_unary('/osmosis.poolmanager.v1beta1.Query/NumPools', request_serializer=osmosis_dot_poolmanager_dot_v1beta1_dot_query__pb2.NumPoolsRequest.SerializeToString, response_deserializer=osmosis_dot_poolmanager_dot_v1beta1_dot_query__pb2.NumPoolsResponse.FromString)

class QueryServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Params(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def EstimateSwapExactAmountIn(self, request, context):
        """Estimates swap amount out given in.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def EstimateSwapExactAmountOut(self, request, context):
        """Estimates swap amount in given out.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def NumPools(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

def add_QueryServicer_to_server(servicer, server):
    rpc_method_handlers = {'Params': grpc.unary_unary_rpc_method_handler(servicer.Params, request_deserializer=osmosis_dot_poolmanager_dot_v1beta1_dot_query__pb2.ParamsRequest.FromString, response_serializer=osmosis_dot_poolmanager_dot_v1beta1_dot_query__pb2.ParamsResponse.SerializeToString), 'EstimateSwapExactAmountIn': grpc.unary_unary_rpc_method_handler(servicer.EstimateSwapExactAmountIn, request_deserializer=osmosis_dot_poolmanager_dot_v1beta1_dot_query__pb2.EstimateSwapExactAmountInRequest.FromString, response_serializer=osmosis_dot_poolmanager_dot_v1beta1_dot_query__pb2.EstimateSwapExactAmountInResponse.SerializeToString), 'EstimateSwapExactAmountOut': grpc.unary_unary_rpc_method_handler(servicer.EstimateSwapExactAmountOut, request_deserializer=osmosis_dot_poolmanager_dot_v1beta1_dot_query__pb2.EstimateSwapExactAmountOutRequest.FromString, response_serializer=osmosis_dot_poolmanager_dot_v1beta1_dot_query__pb2.EstimateSwapExactAmountOutResponse.SerializeToString), 'NumPools': grpc.unary_unary_rpc_method_handler(servicer.NumPools, request_deserializer=osmosis_dot_poolmanager_dot_v1beta1_dot_query__pb2.NumPoolsRequest.FromString, response_serializer=osmosis_dot_poolmanager_dot_v1beta1_dot_query__pb2.NumPoolsResponse.SerializeToString)}
    generic_handler = grpc.method_handlers_generic_handler('osmosis.poolmanager.v1beta1.Query', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))

class Query(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Params(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/osmosis.poolmanager.v1beta1.Query/Params', osmosis_dot_poolmanager_dot_v1beta1_dot_query__pb2.ParamsRequest.SerializeToString, osmosis_dot_poolmanager_dot_v1beta1_dot_query__pb2.ParamsResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def EstimateSwapExactAmountIn(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/osmosis.poolmanager.v1beta1.Query/EstimateSwapExactAmountIn', osmosis_dot_poolmanager_dot_v1beta1_dot_query__pb2.EstimateSwapExactAmountInRequest.SerializeToString, osmosis_dot_poolmanager_dot_v1beta1_dot_query__pb2.EstimateSwapExactAmountInResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def EstimateSwapExactAmountOut(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/osmosis.poolmanager.v1beta1.Query/EstimateSwapExactAmountOut', osmosis_dot_poolmanager_dot_v1beta1_dot_query__pb2.EstimateSwapExactAmountOutRequest.SerializeToString, osmosis_dot_poolmanager_dot_v1beta1_dot_query__pb2.EstimateSwapExactAmountOutResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def NumPools(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/osmosis.poolmanager.v1beta1.Query/NumPools', osmosis_dot_poolmanager_dot_v1beta1_dot_query__pb2.NumPoolsRequest.SerializeToString, osmosis_dot_poolmanager_dot_v1beta1_dot_query__pb2.NumPoolsResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)