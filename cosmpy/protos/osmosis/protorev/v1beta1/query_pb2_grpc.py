"""Client and server classes corresponding to protobuf-defined services."""
import grpc
from ....osmosis.protorev.v1beta1 import query_pb2 as osmosis_dot_protorev_dot_v1beta1_dot_query__pb2

class QueryStub(object):
    """Query defines the gRPC querier service.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Params = channel.unary_unary('/osmosis.protorev.v1beta1.Query/Params', request_serializer=osmosis_dot_protorev_dot_v1beta1_dot_query__pb2.QueryParamsRequest.SerializeToString, response_deserializer=osmosis_dot_protorev_dot_v1beta1_dot_query__pb2.QueryParamsResponse.FromString)
        self.GetProtoRevNumberOfTrades = channel.unary_unary('/osmosis.protorev.v1beta1.Query/GetProtoRevNumberOfTrades', request_serializer=osmosis_dot_protorev_dot_v1beta1_dot_query__pb2.QueryGetProtoRevNumberOfTradesRequest.SerializeToString, response_deserializer=osmosis_dot_protorev_dot_v1beta1_dot_query__pb2.QueryGetProtoRevNumberOfTradesResponse.FromString)
        self.GetProtoRevProfitsByDenom = channel.unary_unary('/osmosis.protorev.v1beta1.Query/GetProtoRevProfitsByDenom', request_serializer=osmosis_dot_protorev_dot_v1beta1_dot_query__pb2.QueryGetProtoRevProfitsByDenomRequest.SerializeToString, response_deserializer=osmosis_dot_protorev_dot_v1beta1_dot_query__pb2.QueryGetProtoRevProfitsByDenomResponse.FromString)
        self.GetProtoRevAllProfits = channel.unary_unary('/osmosis.protorev.v1beta1.Query/GetProtoRevAllProfits', request_serializer=osmosis_dot_protorev_dot_v1beta1_dot_query__pb2.QueryGetProtoRevAllProfitsRequest.SerializeToString, response_deserializer=osmosis_dot_protorev_dot_v1beta1_dot_query__pb2.QueryGetProtoRevAllProfitsResponse.FromString)
        self.GetProtoRevStatisticsByRoute = channel.unary_unary('/osmosis.protorev.v1beta1.Query/GetProtoRevStatisticsByRoute', request_serializer=osmosis_dot_protorev_dot_v1beta1_dot_query__pb2.QueryGetProtoRevStatisticsByRouteRequest.SerializeToString, response_deserializer=osmosis_dot_protorev_dot_v1beta1_dot_query__pb2.QueryGetProtoRevStatisticsByRouteResponse.FromString)
        self.GetProtoRevAllRouteStatistics = channel.unary_unary('/osmosis.protorev.v1beta1.Query/GetProtoRevAllRouteStatistics', request_serializer=osmosis_dot_protorev_dot_v1beta1_dot_query__pb2.QueryGetProtoRevAllRouteStatisticsRequest.SerializeToString, response_deserializer=osmosis_dot_protorev_dot_v1beta1_dot_query__pb2.QueryGetProtoRevAllRouteStatisticsResponse.FromString)
        self.GetProtoRevTokenPairArbRoutes = channel.unary_unary('/osmosis.protorev.v1beta1.Query/GetProtoRevTokenPairArbRoutes', request_serializer=osmosis_dot_protorev_dot_v1beta1_dot_query__pb2.QueryGetProtoRevTokenPairArbRoutesRequest.SerializeToString, response_deserializer=osmosis_dot_protorev_dot_v1beta1_dot_query__pb2.QueryGetProtoRevTokenPairArbRoutesResponse.FromString)
        self.GetProtoRevAdminAccount = channel.unary_unary('/osmosis.protorev.v1beta1.Query/GetProtoRevAdminAccount', request_serializer=osmosis_dot_protorev_dot_v1beta1_dot_query__pb2.QueryGetProtoRevAdminAccountRequest.SerializeToString, response_deserializer=osmosis_dot_protorev_dot_v1beta1_dot_query__pb2.QueryGetProtoRevAdminAccountResponse.FromString)
        self.GetProtoRevDeveloperAccount = channel.unary_unary('/osmosis.protorev.v1beta1.Query/GetProtoRevDeveloperAccount', request_serializer=osmosis_dot_protorev_dot_v1beta1_dot_query__pb2.QueryGetProtoRevDeveloperAccountRequest.SerializeToString, response_deserializer=osmosis_dot_protorev_dot_v1beta1_dot_query__pb2.QueryGetProtoRevDeveloperAccountResponse.FromString)
        self.GetProtoRevPoolWeights = channel.unary_unary('/osmosis.protorev.v1beta1.Query/GetProtoRevPoolWeights', request_serializer=osmosis_dot_protorev_dot_v1beta1_dot_query__pb2.QueryGetProtoRevPoolWeightsRequest.SerializeToString, response_deserializer=osmosis_dot_protorev_dot_v1beta1_dot_query__pb2.QueryGetProtoRevPoolWeightsResponse.FromString)
        self.GetProtoRevMaxPoolPointsPerTx = channel.unary_unary('/osmosis.protorev.v1beta1.Query/GetProtoRevMaxPoolPointsPerTx', request_serializer=osmosis_dot_protorev_dot_v1beta1_dot_query__pb2.QueryGetProtoRevMaxPoolPointsPerTxRequest.SerializeToString, response_deserializer=osmosis_dot_protorev_dot_v1beta1_dot_query__pb2.QueryGetProtoRevMaxPoolPointsPerTxResponse.FromString)
        self.GetProtoRevMaxPoolPointsPerBlock = channel.unary_unary('/osmosis.protorev.v1beta1.Query/GetProtoRevMaxPoolPointsPerBlock', request_serializer=osmosis_dot_protorev_dot_v1beta1_dot_query__pb2.QueryGetProtoRevMaxPoolPointsPerBlockRequest.SerializeToString, response_deserializer=osmosis_dot_protorev_dot_v1beta1_dot_query__pb2.QueryGetProtoRevMaxPoolPointsPerBlockResponse.FromString)
        self.GetProtoRevBaseDenoms = channel.unary_unary('/osmosis.protorev.v1beta1.Query/GetProtoRevBaseDenoms', request_serializer=osmosis_dot_protorev_dot_v1beta1_dot_query__pb2.QueryGetProtoRevBaseDenomsRequest.SerializeToString, response_deserializer=osmosis_dot_protorev_dot_v1beta1_dot_query__pb2.QueryGetProtoRevBaseDenomsResponse.FromString)
        self.GetProtoRevEnabled = channel.unary_unary('/osmosis.protorev.v1beta1.Query/GetProtoRevEnabled', request_serializer=osmosis_dot_protorev_dot_v1beta1_dot_query__pb2.QueryGetProtoRevEnabledRequest.SerializeToString, response_deserializer=osmosis_dot_protorev_dot_v1beta1_dot_query__pb2.QueryGetProtoRevEnabledResponse.FromString)

class QueryServicer(object):
    """Query defines the gRPC querier service.
    """

    def Params(self, request, context):
        """Params queries the parameters of the module.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetProtoRevNumberOfTrades(self, request, context):
        """GetProtoRevNumberOfTrades queries the number of arbitrage trades the module
        has executed
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetProtoRevProfitsByDenom(self, request, context):
        """GetProtoRevProfitsByDenom queries the profits of the module by denom
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetProtoRevAllProfits(self, request, context):
        """GetProtoRevAllProfits queries all of the profits from the module
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetProtoRevStatisticsByRoute(self, request, context):
        """GetProtoRevStatisticsByRoute queries the number of arbitrages and profits
        that have been executed for a given route
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetProtoRevAllRouteStatistics(self, request, context):
        """GetProtoRevAllRouteStatistics queries all of routes that the module has
        arbitraged against and the number of trades and profits that have been
        accumulated for each route
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetProtoRevTokenPairArbRoutes(self, request, context):
        """GetProtoRevTokenPairArbRoutes queries all of the hot routes that the module
        is currently arbitraging
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetProtoRevAdminAccount(self, request, context):
        """GetProtoRevAdminAccount queries the admin account of the module
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetProtoRevDeveloperAccount(self, request, context):
        """GetProtoRevDeveloperAccount queries the developer account of the module
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetProtoRevPoolWeights(self, request, context):
        """GetProtoRevPoolWeights queries the weights of each pool type currently
        being used by the module
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetProtoRevMaxPoolPointsPerTx(self, request, context):
        """GetProtoRevMaxPoolPointsPerTx queries the maximum number of pool points
        that can be consumed per transaction
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetProtoRevMaxPoolPointsPerBlock(self, request, context):
        """GetProtoRevMaxPoolPointsPerBlock queries the maximum number of pool points
        that can consumed per block
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetProtoRevBaseDenoms(self, request, context):
        """GetProtoRevBaseDenoms queries the base denoms that the module is currently
        utilizing for arbitrage
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetProtoRevEnabled(self, request, context):
        """GetProtoRevEnabled queries whether the module is enabled or not
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

def add_QueryServicer_to_server(servicer, server):
    rpc_method_handlers = {'Params': grpc.unary_unary_rpc_method_handler(servicer.Params, request_deserializer=osmosis_dot_protorev_dot_v1beta1_dot_query__pb2.QueryParamsRequest.FromString, response_serializer=osmosis_dot_protorev_dot_v1beta1_dot_query__pb2.QueryParamsResponse.SerializeToString), 'GetProtoRevNumberOfTrades': grpc.unary_unary_rpc_method_handler(servicer.GetProtoRevNumberOfTrades, request_deserializer=osmosis_dot_protorev_dot_v1beta1_dot_query__pb2.QueryGetProtoRevNumberOfTradesRequest.FromString, response_serializer=osmosis_dot_protorev_dot_v1beta1_dot_query__pb2.QueryGetProtoRevNumberOfTradesResponse.SerializeToString), 'GetProtoRevProfitsByDenom': grpc.unary_unary_rpc_method_handler(servicer.GetProtoRevProfitsByDenom, request_deserializer=osmosis_dot_protorev_dot_v1beta1_dot_query__pb2.QueryGetProtoRevProfitsByDenomRequest.FromString, response_serializer=osmosis_dot_protorev_dot_v1beta1_dot_query__pb2.QueryGetProtoRevProfitsByDenomResponse.SerializeToString), 'GetProtoRevAllProfits': grpc.unary_unary_rpc_method_handler(servicer.GetProtoRevAllProfits, request_deserializer=osmosis_dot_protorev_dot_v1beta1_dot_query__pb2.QueryGetProtoRevAllProfitsRequest.FromString, response_serializer=osmosis_dot_protorev_dot_v1beta1_dot_query__pb2.QueryGetProtoRevAllProfitsResponse.SerializeToString), 'GetProtoRevStatisticsByRoute': grpc.unary_unary_rpc_method_handler(servicer.GetProtoRevStatisticsByRoute, request_deserializer=osmosis_dot_protorev_dot_v1beta1_dot_query__pb2.QueryGetProtoRevStatisticsByRouteRequest.FromString, response_serializer=osmosis_dot_protorev_dot_v1beta1_dot_query__pb2.QueryGetProtoRevStatisticsByRouteResponse.SerializeToString), 'GetProtoRevAllRouteStatistics': grpc.unary_unary_rpc_method_handler(servicer.GetProtoRevAllRouteStatistics, request_deserializer=osmosis_dot_protorev_dot_v1beta1_dot_query__pb2.QueryGetProtoRevAllRouteStatisticsRequest.FromString, response_serializer=osmosis_dot_protorev_dot_v1beta1_dot_query__pb2.QueryGetProtoRevAllRouteStatisticsResponse.SerializeToString), 'GetProtoRevTokenPairArbRoutes': grpc.unary_unary_rpc_method_handler(servicer.GetProtoRevTokenPairArbRoutes, request_deserializer=osmosis_dot_protorev_dot_v1beta1_dot_query__pb2.QueryGetProtoRevTokenPairArbRoutesRequest.FromString, response_serializer=osmosis_dot_protorev_dot_v1beta1_dot_query__pb2.QueryGetProtoRevTokenPairArbRoutesResponse.SerializeToString), 'GetProtoRevAdminAccount': grpc.unary_unary_rpc_method_handler(servicer.GetProtoRevAdminAccount, request_deserializer=osmosis_dot_protorev_dot_v1beta1_dot_query__pb2.QueryGetProtoRevAdminAccountRequest.FromString, response_serializer=osmosis_dot_protorev_dot_v1beta1_dot_query__pb2.QueryGetProtoRevAdminAccountResponse.SerializeToString), 'GetProtoRevDeveloperAccount': grpc.unary_unary_rpc_method_handler(servicer.GetProtoRevDeveloperAccount, request_deserializer=osmosis_dot_protorev_dot_v1beta1_dot_query__pb2.QueryGetProtoRevDeveloperAccountRequest.FromString, response_serializer=osmosis_dot_protorev_dot_v1beta1_dot_query__pb2.QueryGetProtoRevDeveloperAccountResponse.SerializeToString), 'GetProtoRevPoolWeights': grpc.unary_unary_rpc_method_handler(servicer.GetProtoRevPoolWeights, request_deserializer=osmosis_dot_protorev_dot_v1beta1_dot_query__pb2.QueryGetProtoRevPoolWeightsRequest.FromString, response_serializer=osmosis_dot_protorev_dot_v1beta1_dot_query__pb2.QueryGetProtoRevPoolWeightsResponse.SerializeToString), 'GetProtoRevMaxPoolPointsPerTx': grpc.unary_unary_rpc_method_handler(servicer.GetProtoRevMaxPoolPointsPerTx, request_deserializer=osmosis_dot_protorev_dot_v1beta1_dot_query__pb2.QueryGetProtoRevMaxPoolPointsPerTxRequest.FromString, response_serializer=osmosis_dot_protorev_dot_v1beta1_dot_query__pb2.QueryGetProtoRevMaxPoolPointsPerTxResponse.SerializeToString), 'GetProtoRevMaxPoolPointsPerBlock': grpc.unary_unary_rpc_method_handler(servicer.GetProtoRevMaxPoolPointsPerBlock, request_deserializer=osmosis_dot_protorev_dot_v1beta1_dot_query__pb2.QueryGetProtoRevMaxPoolPointsPerBlockRequest.FromString, response_serializer=osmosis_dot_protorev_dot_v1beta1_dot_query__pb2.QueryGetProtoRevMaxPoolPointsPerBlockResponse.SerializeToString), 'GetProtoRevBaseDenoms': grpc.unary_unary_rpc_method_handler(servicer.GetProtoRevBaseDenoms, request_deserializer=osmosis_dot_protorev_dot_v1beta1_dot_query__pb2.QueryGetProtoRevBaseDenomsRequest.FromString, response_serializer=osmosis_dot_protorev_dot_v1beta1_dot_query__pb2.QueryGetProtoRevBaseDenomsResponse.SerializeToString), 'GetProtoRevEnabled': grpc.unary_unary_rpc_method_handler(servicer.GetProtoRevEnabled, request_deserializer=osmosis_dot_protorev_dot_v1beta1_dot_query__pb2.QueryGetProtoRevEnabledRequest.FromString, response_serializer=osmosis_dot_protorev_dot_v1beta1_dot_query__pb2.QueryGetProtoRevEnabledResponse.SerializeToString)}
    generic_handler = grpc.method_handlers_generic_handler('osmosis.protorev.v1beta1.Query', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))

class Query(object):
    """Query defines the gRPC querier service.
    """

    @staticmethod
    def Params(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/osmosis.protorev.v1beta1.Query/Params', osmosis_dot_protorev_dot_v1beta1_dot_query__pb2.QueryParamsRequest.SerializeToString, osmosis_dot_protorev_dot_v1beta1_dot_query__pb2.QueryParamsResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetProtoRevNumberOfTrades(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/osmosis.protorev.v1beta1.Query/GetProtoRevNumberOfTrades', osmosis_dot_protorev_dot_v1beta1_dot_query__pb2.QueryGetProtoRevNumberOfTradesRequest.SerializeToString, osmosis_dot_protorev_dot_v1beta1_dot_query__pb2.QueryGetProtoRevNumberOfTradesResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetProtoRevProfitsByDenom(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/osmosis.protorev.v1beta1.Query/GetProtoRevProfitsByDenom', osmosis_dot_protorev_dot_v1beta1_dot_query__pb2.QueryGetProtoRevProfitsByDenomRequest.SerializeToString, osmosis_dot_protorev_dot_v1beta1_dot_query__pb2.QueryGetProtoRevProfitsByDenomResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetProtoRevAllProfits(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/osmosis.protorev.v1beta1.Query/GetProtoRevAllProfits', osmosis_dot_protorev_dot_v1beta1_dot_query__pb2.QueryGetProtoRevAllProfitsRequest.SerializeToString, osmosis_dot_protorev_dot_v1beta1_dot_query__pb2.QueryGetProtoRevAllProfitsResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetProtoRevStatisticsByRoute(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/osmosis.protorev.v1beta1.Query/GetProtoRevStatisticsByRoute', osmosis_dot_protorev_dot_v1beta1_dot_query__pb2.QueryGetProtoRevStatisticsByRouteRequest.SerializeToString, osmosis_dot_protorev_dot_v1beta1_dot_query__pb2.QueryGetProtoRevStatisticsByRouteResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetProtoRevAllRouteStatistics(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/osmosis.protorev.v1beta1.Query/GetProtoRevAllRouteStatistics', osmosis_dot_protorev_dot_v1beta1_dot_query__pb2.QueryGetProtoRevAllRouteStatisticsRequest.SerializeToString, osmosis_dot_protorev_dot_v1beta1_dot_query__pb2.QueryGetProtoRevAllRouteStatisticsResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetProtoRevTokenPairArbRoutes(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/osmosis.protorev.v1beta1.Query/GetProtoRevTokenPairArbRoutes', osmosis_dot_protorev_dot_v1beta1_dot_query__pb2.QueryGetProtoRevTokenPairArbRoutesRequest.SerializeToString, osmosis_dot_protorev_dot_v1beta1_dot_query__pb2.QueryGetProtoRevTokenPairArbRoutesResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetProtoRevAdminAccount(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/osmosis.protorev.v1beta1.Query/GetProtoRevAdminAccount', osmosis_dot_protorev_dot_v1beta1_dot_query__pb2.QueryGetProtoRevAdminAccountRequest.SerializeToString, osmosis_dot_protorev_dot_v1beta1_dot_query__pb2.QueryGetProtoRevAdminAccountResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetProtoRevDeveloperAccount(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/osmosis.protorev.v1beta1.Query/GetProtoRevDeveloperAccount', osmosis_dot_protorev_dot_v1beta1_dot_query__pb2.QueryGetProtoRevDeveloperAccountRequest.SerializeToString, osmosis_dot_protorev_dot_v1beta1_dot_query__pb2.QueryGetProtoRevDeveloperAccountResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetProtoRevPoolWeights(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/osmosis.protorev.v1beta1.Query/GetProtoRevPoolWeights', osmosis_dot_protorev_dot_v1beta1_dot_query__pb2.QueryGetProtoRevPoolWeightsRequest.SerializeToString, osmosis_dot_protorev_dot_v1beta1_dot_query__pb2.QueryGetProtoRevPoolWeightsResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetProtoRevMaxPoolPointsPerTx(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/osmosis.protorev.v1beta1.Query/GetProtoRevMaxPoolPointsPerTx', osmosis_dot_protorev_dot_v1beta1_dot_query__pb2.QueryGetProtoRevMaxPoolPointsPerTxRequest.SerializeToString, osmosis_dot_protorev_dot_v1beta1_dot_query__pb2.QueryGetProtoRevMaxPoolPointsPerTxResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetProtoRevMaxPoolPointsPerBlock(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/osmosis.protorev.v1beta1.Query/GetProtoRevMaxPoolPointsPerBlock', osmosis_dot_protorev_dot_v1beta1_dot_query__pb2.QueryGetProtoRevMaxPoolPointsPerBlockRequest.SerializeToString, osmosis_dot_protorev_dot_v1beta1_dot_query__pb2.QueryGetProtoRevMaxPoolPointsPerBlockResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetProtoRevBaseDenoms(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/osmosis.protorev.v1beta1.Query/GetProtoRevBaseDenoms', osmosis_dot_protorev_dot_v1beta1_dot_query__pb2.QueryGetProtoRevBaseDenomsRequest.SerializeToString, osmosis_dot_protorev_dot_v1beta1_dot_query__pb2.QueryGetProtoRevBaseDenomsResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetProtoRevEnabled(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/osmosis.protorev.v1beta1.Query/GetProtoRevEnabled', osmosis_dot_protorev_dot_v1beta1_dot_query__pb2.QueryGetProtoRevEnabledRequest.SerializeToString, osmosis_dot_protorev_dot_v1beta1_dot_query__pb2.QueryGetProtoRevEnabledResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)