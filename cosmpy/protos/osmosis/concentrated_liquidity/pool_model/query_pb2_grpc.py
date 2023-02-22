"""Client and server classes corresponding to protobuf-defined services."""
import grpc
from ....osmosis.concentrated_liquidity.pool_model import query_pb2 as osmosis_dot_concentrated__liquidity_dot_pool__model_dot_query__pb2

class QueryStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Pools = channel.unary_unary('/osmosis.concentratedliquidity.v1beta1.Query/Pools', request_serializer=osmosis_dot_concentrated__liquidity_dot_pool__model_dot_query__pb2.QueryPoolsRequest.SerializeToString, response_deserializer=osmosis_dot_concentrated__liquidity_dot_pool__model_dot_query__pb2.QueryPoolsResponse.FromString)
        self.Pool = channel.unary_unary('/osmosis.concentratedliquidity.v1beta1.Query/Pool', request_serializer=osmosis_dot_concentrated__liquidity_dot_pool__model_dot_query__pb2.QueryPoolRequest.SerializeToString, response_deserializer=osmosis_dot_concentrated__liquidity_dot_pool__model_dot_query__pb2.QueryPoolResponse.FromString)
        self.Params = channel.unary_unary('/osmosis.concentratedliquidity.v1beta1.Query/Params', request_serializer=osmosis_dot_concentrated__liquidity_dot_pool__model_dot_query__pb2.QueryParamsRequest.SerializeToString, response_deserializer=osmosis_dot_concentrated__liquidity_dot_pool__model_dot_query__pb2.QueryParamsResponse.FromString)
        self.LiquidityDepthsForRange = channel.unary_unary('/osmosis.concentratedliquidity.v1beta1.Query/LiquidityDepthsForRange', request_serializer=osmosis_dot_concentrated__liquidity_dot_pool__model_dot_query__pb2.QueryLiquidityDepthsForRangeRequest.SerializeToString, response_deserializer=osmosis_dot_concentrated__liquidity_dot_pool__model_dot_query__pb2.QueryLiquidityDepthsForRangeResponse.FromString)
        self.UserPositions = channel.unary_unary('/osmosis.concentratedliquidity.v1beta1.Query/UserPositions', request_serializer=osmosis_dot_concentrated__liquidity_dot_pool__model_dot_query__pb2.QueryUserPositionsRequest.SerializeToString, response_deserializer=osmosis_dot_concentrated__liquidity_dot_pool__model_dot_query__pb2.QueryUserPositionsResponse.FromString)

class QueryServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Pools(self, request, context):
        """Pools returns all concentrated liquidity pools
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Pool(self, request, context):
        """Pool returns the Pool specified by the pool id
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Params(self, request, context):
        """Params returns concentrated liquidity module params.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def LiquidityDepthsForRange(self, request, context):
        """LiquidityDepthsForRange returns Liqiudity Depths for given range
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UserPositions(self, request, context):
        """UserPositions returns all concentrated postitions of some address.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

def add_QueryServicer_to_server(servicer, server):
    rpc_method_handlers = {'Pools': grpc.unary_unary_rpc_method_handler(servicer.Pools, request_deserializer=osmosis_dot_concentrated__liquidity_dot_pool__model_dot_query__pb2.QueryPoolsRequest.FromString, response_serializer=osmosis_dot_concentrated__liquidity_dot_pool__model_dot_query__pb2.QueryPoolsResponse.SerializeToString), 'Pool': grpc.unary_unary_rpc_method_handler(servicer.Pool, request_deserializer=osmosis_dot_concentrated__liquidity_dot_pool__model_dot_query__pb2.QueryPoolRequest.FromString, response_serializer=osmosis_dot_concentrated__liquidity_dot_pool__model_dot_query__pb2.QueryPoolResponse.SerializeToString), 'Params': grpc.unary_unary_rpc_method_handler(servicer.Params, request_deserializer=osmosis_dot_concentrated__liquidity_dot_pool__model_dot_query__pb2.QueryParamsRequest.FromString, response_serializer=osmosis_dot_concentrated__liquidity_dot_pool__model_dot_query__pb2.QueryParamsResponse.SerializeToString), 'LiquidityDepthsForRange': grpc.unary_unary_rpc_method_handler(servicer.LiquidityDepthsForRange, request_deserializer=osmosis_dot_concentrated__liquidity_dot_pool__model_dot_query__pb2.QueryLiquidityDepthsForRangeRequest.FromString, response_serializer=osmosis_dot_concentrated__liquidity_dot_pool__model_dot_query__pb2.QueryLiquidityDepthsForRangeResponse.SerializeToString), 'UserPositions': grpc.unary_unary_rpc_method_handler(servicer.UserPositions, request_deserializer=osmosis_dot_concentrated__liquidity_dot_pool__model_dot_query__pb2.QueryUserPositionsRequest.FromString, response_serializer=osmosis_dot_concentrated__liquidity_dot_pool__model_dot_query__pb2.QueryUserPositionsResponse.SerializeToString)}
    generic_handler = grpc.method_handlers_generic_handler('osmosis.concentratedliquidity.v1beta1.Query', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))

class Query(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Pools(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/osmosis.concentratedliquidity.v1beta1.Query/Pools', osmosis_dot_concentrated__liquidity_dot_pool__model_dot_query__pb2.QueryPoolsRequest.SerializeToString, osmosis_dot_concentrated__liquidity_dot_pool__model_dot_query__pb2.QueryPoolsResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Pool(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/osmosis.concentratedliquidity.v1beta1.Query/Pool', osmosis_dot_concentrated__liquidity_dot_pool__model_dot_query__pb2.QueryPoolRequest.SerializeToString, osmosis_dot_concentrated__liquidity_dot_pool__model_dot_query__pb2.QueryPoolResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Params(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/osmosis.concentratedliquidity.v1beta1.Query/Params', osmosis_dot_concentrated__liquidity_dot_pool__model_dot_query__pb2.QueryParamsRequest.SerializeToString, osmosis_dot_concentrated__liquidity_dot_pool__model_dot_query__pb2.QueryParamsResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def LiquidityDepthsForRange(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/osmosis.concentratedliquidity.v1beta1.Query/LiquidityDepthsForRange', osmosis_dot_concentrated__liquidity_dot_pool__model_dot_query__pb2.QueryLiquidityDepthsForRangeRequest.SerializeToString, osmosis_dot_concentrated__liquidity_dot_pool__model_dot_query__pb2.QueryLiquidityDepthsForRangeResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UserPositions(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/osmosis.concentratedliquidity.v1beta1.Query/UserPositions', osmosis_dot_concentrated__liquidity_dot_pool__model_dot_query__pb2.QueryUserPositionsRequest.SerializeToString, osmosis_dot_concentrated__liquidity_dot_pool__model_dot_query__pb2.QueryUserPositionsResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)