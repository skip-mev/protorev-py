"""Client and server classes corresponding to protobuf-defined services."""
import grpc
from ....osmosis.gamm.v2 import query_pb2 as osmosis_dot_gamm_dot_v2_dot_query__pb2

class QueryStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.SpotPrice = channel.unary_unary('/osmosis.gamm.v2.Query/SpotPrice', request_serializer=osmosis_dot_gamm_dot_v2_dot_query__pb2.QuerySpotPriceRequest.SerializeToString, response_deserializer=osmosis_dot_gamm_dot_v2_dot_query__pb2.QuerySpotPriceResponse.FromString)

class QueryServicer(object):
    """Missing associated documentation comment in .proto file."""

    def SpotPrice(self, request, context):
        """SpotPrice defines a gRPC query handler that returns the spot price given
        a base denomination and a quote denomination.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

def add_QueryServicer_to_server(servicer, server):
    rpc_method_handlers = {'SpotPrice': grpc.unary_unary_rpc_method_handler(servicer.SpotPrice, request_deserializer=osmosis_dot_gamm_dot_v2_dot_query__pb2.QuerySpotPriceRequest.FromString, response_serializer=osmosis_dot_gamm_dot_v2_dot_query__pb2.QuerySpotPriceResponse.SerializeToString)}
    generic_handler = grpc.method_handlers_generic_handler('osmosis.gamm.v2.Query', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))

class Query(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def SpotPrice(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/osmosis.gamm.v2.Query/SpotPrice', osmosis_dot_gamm_dot_v2_dot_query__pb2.QuerySpotPriceRequest.SerializeToString, osmosis_dot_gamm_dot_v2_dot_query__pb2.QuerySpotPriceResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)