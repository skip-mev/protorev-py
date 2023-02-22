"""Client and server classes corresponding to protobuf-defined services."""
import grpc
from ....osmosis.tokenfactory.v1beta1 import query_pb2 as osmosis_dot_tokenfactory_dot_v1beta1_dot_query__pb2

class QueryStub(object):
    """Query defines the gRPC querier service.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Params = channel.unary_unary('/osmosis.tokenfactory.v1beta1.Query/Params', request_serializer=osmosis_dot_tokenfactory_dot_v1beta1_dot_query__pb2.QueryParamsRequest.SerializeToString, response_deserializer=osmosis_dot_tokenfactory_dot_v1beta1_dot_query__pb2.QueryParamsResponse.FromString)
        self.DenomAuthorityMetadata = channel.unary_unary('/osmosis.tokenfactory.v1beta1.Query/DenomAuthorityMetadata', request_serializer=osmosis_dot_tokenfactory_dot_v1beta1_dot_query__pb2.QueryDenomAuthorityMetadataRequest.SerializeToString, response_deserializer=osmosis_dot_tokenfactory_dot_v1beta1_dot_query__pb2.QueryDenomAuthorityMetadataResponse.FromString)
        self.DenomsFromCreator = channel.unary_unary('/osmosis.tokenfactory.v1beta1.Query/DenomsFromCreator', request_serializer=osmosis_dot_tokenfactory_dot_v1beta1_dot_query__pb2.QueryDenomsFromCreatorRequest.SerializeToString, response_deserializer=osmosis_dot_tokenfactory_dot_v1beta1_dot_query__pb2.QueryDenomsFromCreatorResponse.FromString)

class QueryServicer(object):
    """Query defines the gRPC querier service.
    """

    def Params(self, request, context):
        """Params defines a gRPC query method that returns the tokenfactory module's
        parameters.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DenomAuthorityMetadata(self, request, context):
        """DenomAuthorityMetadata defines a gRPC query method for fetching
        DenomAuthorityMetadata for a particular denom.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DenomsFromCreator(self, request, context):
        """DenomsFromCreator defines a gRPC query method for fetching all
        denominations created by a specific admin/creator.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

def add_QueryServicer_to_server(servicer, server):
    rpc_method_handlers = {'Params': grpc.unary_unary_rpc_method_handler(servicer.Params, request_deserializer=osmosis_dot_tokenfactory_dot_v1beta1_dot_query__pb2.QueryParamsRequest.FromString, response_serializer=osmosis_dot_tokenfactory_dot_v1beta1_dot_query__pb2.QueryParamsResponse.SerializeToString), 'DenomAuthorityMetadata': grpc.unary_unary_rpc_method_handler(servicer.DenomAuthorityMetadata, request_deserializer=osmosis_dot_tokenfactory_dot_v1beta1_dot_query__pb2.QueryDenomAuthorityMetadataRequest.FromString, response_serializer=osmosis_dot_tokenfactory_dot_v1beta1_dot_query__pb2.QueryDenomAuthorityMetadataResponse.SerializeToString), 'DenomsFromCreator': grpc.unary_unary_rpc_method_handler(servicer.DenomsFromCreator, request_deserializer=osmosis_dot_tokenfactory_dot_v1beta1_dot_query__pb2.QueryDenomsFromCreatorRequest.FromString, response_serializer=osmosis_dot_tokenfactory_dot_v1beta1_dot_query__pb2.QueryDenomsFromCreatorResponse.SerializeToString)}
    generic_handler = grpc.method_handlers_generic_handler('osmosis.tokenfactory.v1beta1.Query', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))

class Query(object):
    """Query defines the gRPC querier service.
    """

    @staticmethod
    def Params(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/osmosis.tokenfactory.v1beta1.Query/Params', osmosis_dot_tokenfactory_dot_v1beta1_dot_query__pb2.QueryParamsRequest.SerializeToString, osmosis_dot_tokenfactory_dot_v1beta1_dot_query__pb2.QueryParamsResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DenomAuthorityMetadata(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/osmosis.tokenfactory.v1beta1.Query/DenomAuthorityMetadata', osmosis_dot_tokenfactory_dot_v1beta1_dot_query__pb2.QueryDenomAuthorityMetadataRequest.SerializeToString, osmosis_dot_tokenfactory_dot_v1beta1_dot_query__pb2.QueryDenomAuthorityMetadataResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DenomsFromCreator(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/osmosis.tokenfactory.v1beta1.Query/DenomsFromCreator', osmosis_dot_tokenfactory_dot_v1beta1_dot_query__pb2.QueryDenomsFromCreatorRequest.SerializeToString, osmosis_dot_tokenfactory_dot_v1beta1_dot_query__pb2.QueryDenomsFromCreatorResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)