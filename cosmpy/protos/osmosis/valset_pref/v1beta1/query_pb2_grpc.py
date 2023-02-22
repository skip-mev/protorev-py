"""Client and server classes corresponding to protobuf-defined services."""
import grpc
from ....osmosis.valset_pref.v1beta1 import query_pb2 as osmosis_dot_valset__pref_dot_v1beta1_dot_query__pb2

class QueryStub(object):
    """Query defines the gRPC querier service.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.UserValidatorPreferences = channel.unary_unary('/osmosis.valsetpref.v1beta1.Query/UserValidatorPreferences', request_serializer=osmosis_dot_valset__pref_dot_v1beta1_dot_query__pb2.UserValidatorPreferencesRequest.SerializeToString, response_deserializer=osmosis_dot_valset__pref_dot_v1beta1_dot_query__pb2.UserValidatorPreferencesResponse.FromString)

class QueryServicer(object):
    """Query defines the gRPC querier service.
    """

    def UserValidatorPreferences(self, request, context):
        """Returns the list of ValidatorPreferences for the user.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

def add_QueryServicer_to_server(servicer, server):
    rpc_method_handlers = {'UserValidatorPreferences': grpc.unary_unary_rpc_method_handler(servicer.UserValidatorPreferences, request_deserializer=osmosis_dot_valset__pref_dot_v1beta1_dot_query__pb2.UserValidatorPreferencesRequest.FromString, response_serializer=osmosis_dot_valset__pref_dot_v1beta1_dot_query__pb2.UserValidatorPreferencesResponse.SerializeToString)}
    generic_handler = grpc.method_handlers_generic_handler('osmosis.valsetpref.v1beta1.Query', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))

class Query(object):
    """Query defines the gRPC querier service.
    """

    @staticmethod
    def UserValidatorPreferences(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/osmosis.valsetpref.v1beta1.Query/UserValidatorPreferences', osmosis_dot_valset__pref_dot_v1beta1_dot_query__pb2.UserValidatorPreferencesRequest.SerializeToString, osmosis_dot_valset__pref_dot_v1beta1_dot_query__pb2.UserValidatorPreferencesResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)