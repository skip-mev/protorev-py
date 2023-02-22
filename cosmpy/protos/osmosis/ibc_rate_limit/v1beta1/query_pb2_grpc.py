"""Client and server classes corresponding to protobuf-defined services."""
import grpc
from ....osmosis.ibc_rate_limit.v1beta1 import query_pb2 as osmosis_dot_ibc__rate__limit_dot_v1beta1_dot_query__pb2

class QueryStub(object):
    """Query defines the gRPC querier service.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Params = channel.unary_unary('/osmosis.ibcratelimit.v1beta1.Query/Params', request_serializer=osmosis_dot_ibc__rate__limit_dot_v1beta1_dot_query__pb2.QueryParamsRequest.SerializeToString, response_deserializer=osmosis_dot_ibc__rate__limit_dot_v1beta1_dot_query__pb2.QueryParamsResponse.FromString)

class QueryServicer(object):
    """Query defines the gRPC querier service.
    """

    def Params(self, request, context):
        """Params defines a gRPC query method that returns the ibc-rate-limit module's
        parameters.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

def add_QueryServicer_to_server(servicer, server):
    rpc_method_handlers = {'Params': grpc.unary_unary_rpc_method_handler(servicer.Params, request_deserializer=osmosis_dot_ibc__rate__limit_dot_v1beta1_dot_query__pb2.QueryParamsRequest.FromString, response_serializer=osmosis_dot_ibc__rate__limit_dot_v1beta1_dot_query__pb2.QueryParamsResponse.SerializeToString)}
    generic_handler = grpc.method_handlers_generic_handler('osmosis.ibcratelimit.v1beta1.Query', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))

class Query(object):
    """Query defines the gRPC querier service.
    """

    @staticmethod
    def Params(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/osmosis.ibcratelimit.v1beta1.Query/Params', osmosis_dot_ibc__rate__limit_dot_v1beta1_dot_query__pb2.QueryParamsRequest.SerializeToString, osmosis_dot_ibc__rate__limit_dot_v1beta1_dot_query__pb2.QueryParamsResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)