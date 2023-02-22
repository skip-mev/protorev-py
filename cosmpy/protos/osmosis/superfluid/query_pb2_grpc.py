"""Client and server classes corresponding to protobuf-defined services."""
import grpc
from ...osmosis.superfluid import query_pb2 as osmosis_dot_superfluid_dot_query__pb2

class QueryStub(object):
    """Query defines the gRPC querier service.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Params = channel.unary_unary('/osmosis.superfluid.Query/Params', request_serializer=osmosis_dot_superfluid_dot_query__pb2.QueryParamsRequest.SerializeToString, response_deserializer=osmosis_dot_superfluid_dot_query__pb2.QueryParamsResponse.FromString)
        self.AssetType = channel.unary_unary('/osmosis.superfluid.Query/AssetType', request_serializer=osmosis_dot_superfluid_dot_query__pb2.AssetTypeRequest.SerializeToString, response_deserializer=osmosis_dot_superfluid_dot_query__pb2.AssetTypeResponse.FromString)
        self.AllAssets = channel.unary_unary('/osmosis.superfluid.Query/AllAssets', request_serializer=osmosis_dot_superfluid_dot_query__pb2.AllAssetsRequest.SerializeToString, response_deserializer=osmosis_dot_superfluid_dot_query__pb2.AllAssetsResponse.FromString)
        self.AssetMultiplier = channel.unary_unary('/osmosis.superfluid.Query/AssetMultiplier', request_serializer=osmosis_dot_superfluid_dot_query__pb2.AssetMultiplierRequest.SerializeToString, response_deserializer=osmosis_dot_superfluid_dot_query__pb2.AssetMultiplierResponse.FromString)
        self.AllIntermediaryAccounts = channel.unary_unary('/osmosis.superfluid.Query/AllIntermediaryAccounts', request_serializer=osmosis_dot_superfluid_dot_query__pb2.AllIntermediaryAccountsRequest.SerializeToString, response_deserializer=osmosis_dot_superfluid_dot_query__pb2.AllIntermediaryAccountsResponse.FromString)
        self.ConnectedIntermediaryAccount = channel.unary_unary('/osmosis.superfluid.Query/ConnectedIntermediaryAccount', request_serializer=osmosis_dot_superfluid_dot_query__pb2.ConnectedIntermediaryAccountRequest.SerializeToString, response_deserializer=osmosis_dot_superfluid_dot_query__pb2.ConnectedIntermediaryAccountResponse.FromString)
        self.TotalDelegationByValidatorForDenom = channel.unary_unary('/osmosis.superfluid.Query/TotalDelegationByValidatorForDenom', request_serializer=osmosis_dot_superfluid_dot_query__pb2.QueryTotalDelegationByValidatorForDenomRequest.SerializeToString, response_deserializer=osmosis_dot_superfluid_dot_query__pb2.QueryTotalDelegationByValidatorForDenomResponse.FromString)
        self.TotalSuperfluidDelegations = channel.unary_unary('/osmosis.superfluid.Query/TotalSuperfluidDelegations', request_serializer=osmosis_dot_superfluid_dot_query__pb2.TotalSuperfluidDelegationsRequest.SerializeToString, response_deserializer=osmosis_dot_superfluid_dot_query__pb2.TotalSuperfluidDelegationsResponse.FromString)
        self.SuperfluidDelegationAmount = channel.unary_unary('/osmosis.superfluid.Query/SuperfluidDelegationAmount', request_serializer=osmosis_dot_superfluid_dot_query__pb2.SuperfluidDelegationAmountRequest.SerializeToString, response_deserializer=osmosis_dot_superfluid_dot_query__pb2.SuperfluidDelegationAmountResponse.FromString)
        self.SuperfluidDelegationsByDelegator = channel.unary_unary('/osmosis.superfluid.Query/SuperfluidDelegationsByDelegator', request_serializer=osmosis_dot_superfluid_dot_query__pb2.SuperfluidDelegationsByDelegatorRequest.SerializeToString, response_deserializer=osmosis_dot_superfluid_dot_query__pb2.SuperfluidDelegationsByDelegatorResponse.FromString)
        self.SuperfluidUndelegationsByDelegator = channel.unary_unary('/osmosis.superfluid.Query/SuperfluidUndelegationsByDelegator', request_serializer=osmosis_dot_superfluid_dot_query__pb2.SuperfluidUndelegationsByDelegatorRequest.SerializeToString, response_deserializer=osmosis_dot_superfluid_dot_query__pb2.SuperfluidUndelegationsByDelegatorResponse.FromString)
        self.SuperfluidDelegationsByValidatorDenom = channel.unary_unary('/osmosis.superfluid.Query/SuperfluidDelegationsByValidatorDenom', request_serializer=osmosis_dot_superfluid_dot_query__pb2.SuperfluidDelegationsByValidatorDenomRequest.SerializeToString, response_deserializer=osmosis_dot_superfluid_dot_query__pb2.SuperfluidDelegationsByValidatorDenomResponse.FromString)
        self.EstimateSuperfluidDelegatedAmountByValidatorDenom = channel.unary_unary('/osmosis.superfluid.Query/EstimateSuperfluidDelegatedAmountByValidatorDenom', request_serializer=osmosis_dot_superfluid_dot_query__pb2.EstimateSuperfluidDelegatedAmountByValidatorDenomRequest.SerializeToString, response_deserializer=osmosis_dot_superfluid_dot_query__pb2.EstimateSuperfluidDelegatedAmountByValidatorDenomResponse.FromString)
        self.TotalDelegationByDelegator = channel.unary_unary('/osmosis.superfluid.Query/TotalDelegationByDelegator', request_serializer=osmosis_dot_superfluid_dot_query__pb2.QueryTotalDelegationByDelegatorRequest.SerializeToString, response_deserializer=osmosis_dot_superfluid_dot_query__pb2.QueryTotalDelegationByDelegatorResponse.FromString)
        self.UnpoolWhitelist = channel.unary_unary('/osmosis.superfluid.Query/UnpoolWhitelist', request_serializer=osmosis_dot_superfluid_dot_query__pb2.QueryUnpoolWhitelistRequest.SerializeToString, response_deserializer=osmosis_dot_superfluid_dot_query__pb2.QueryUnpoolWhitelistResponse.FromString)

class QueryServicer(object):
    """Query defines the gRPC querier service.
    """

    def Params(self, request, context):
        """Params returns the total set of superfluid parameters.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AssetType(self, request, context):
        """Returns superfluid asset type, whether if it's a native asset or an lp
        share.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AllAssets(self, request, context):
        """Returns all registered superfluid assets.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AssetMultiplier(self, request, context):
        """Returns the osmo equivalent multiplier used in the most recent epoch.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AllIntermediaryAccounts(self, request, context):
        """Returns all superfluid intermediary accounts.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ConnectedIntermediaryAccount(self, request, context):
        """Returns intermediary account connected to a superfluid staked lock by id
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def TotalDelegationByValidatorForDenom(self, request, context):
        """Returns the amount of delegations of specific denom for all validators
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def TotalSuperfluidDelegations(self, request, context):
        """Returns the total amount of osmo superfluidly staked.
        Response is denominated in uosmo.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SuperfluidDelegationAmount(self, request, context):
        """Returns the coins superfluid delegated for the delegator, validator, denom
        triplet
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SuperfluidDelegationsByDelegator(self, request, context):
        """Returns all the delegated superfluid poistions for a specific delegator.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SuperfluidUndelegationsByDelegator(self, request, context):
        """Returns all the undelegating superfluid poistions for a specific delegator.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SuperfluidDelegationsByValidatorDenom(self, request, context):
        """Returns all the superfluid positions of a specific denom delegated to one
        validator
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def EstimateSuperfluidDelegatedAmountByValidatorDenom(self, request, context):
        """Returns the amount of a specific denom delegated to a specific validator
        This is labeled an estimate, because the way it calculates the amount can
        lead rounding errors from the true delegated amount
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def TotalDelegationByDelegator(self, request, context):
        """Returns the specified delegations for a specific delegator
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UnpoolWhitelist(self, request, context):
        """Returns a list of whitelisted pool ids to unpool.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

def add_QueryServicer_to_server(servicer, server):
    rpc_method_handlers = {'Params': grpc.unary_unary_rpc_method_handler(servicer.Params, request_deserializer=osmosis_dot_superfluid_dot_query__pb2.QueryParamsRequest.FromString, response_serializer=osmosis_dot_superfluid_dot_query__pb2.QueryParamsResponse.SerializeToString), 'AssetType': grpc.unary_unary_rpc_method_handler(servicer.AssetType, request_deserializer=osmosis_dot_superfluid_dot_query__pb2.AssetTypeRequest.FromString, response_serializer=osmosis_dot_superfluid_dot_query__pb2.AssetTypeResponse.SerializeToString), 'AllAssets': grpc.unary_unary_rpc_method_handler(servicer.AllAssets, request_deserializer=osmosis_dot_superfluid_dot_query__pb2.AllAssetsRequest.FromString, response_serializer=osmosis_dot_superfluid_dot_query__pb2.AllAssetsResponse.SerializeToString), 'AssetMultiplier': grpc.unary_unary_rpc_method_handler(servicer.AssetMultiplier, request_deserializer=osmosis_dot_superfluid_dot_query__pb2.AssetMultiplierRequest.FromString, response_serializer=osmosis_dot_superfluid_dot_query__pb2.AssetMultiplierResponse.SerializeToString), 'AllIntermediaryAccounts': grpc.unary_unary_rpc_method_handler(servicer.AllIntermediaryAccounts, request_deserializer=osmosis_dot_superfluid_dot_query__pb2.AllIntermediaryAccountsRequest.FromString, response_serializer=osmosis_dot_superfluid_dot_query__pb2.AllIntermediaryAccountsResponse.SerializeToString), 'ConnectedIntermediaryAccount': grpc.unary_unary_rpc_method_handler(servicer.ConnectedIntermediaryAccount, request_deserializer=osmosis_dot_superfluid_dot_query__pb2.ConnectedIntermediaryAccountRequest.FromString, response_serializer=osmosis_dot_superfluid_dot_query__pb2.ConnectedIntermediaryAccountResponse.SerializeToString), 'TotalDelegationByValidatorForDenom': grpc.unary_unary_rpc_method_handler(servicer.TotalDelegationByValidatorForDenom, request_deserializer=osmosis_dot_superfluid_dot_query__pb2.QueryTotalDelegationByValidatorForDenomRequest.FromString, response_serializer=osmosis_dot_superfluid_dot_query__pb2.QueryTotalDelegationByValidatorForDenomResponse.SerializeToString), 'TotalSuperfluidDelegations': grpc.unary_unary_rpc_method_handler(servicer.TotalSuperfluidDelegations, request_deserializer=osmosis_dot_superfluid_dot_query__pb2.TotalSuperfluidDelegationsRequest.FromString, response_serializer=osmosis_dot_superfluid_dot_query__pb2.TotalSuperfluidDelegationsResponse.SerializeToString), 'SuperfluidDelegationAmount': grpc.unary_unary_rpc_method_handler(servicer.SuperfluidDelegationAmount, request_deserializer=osmosis_dot_superfluid_dot_query__pb2.SuperfluidDelegationAmountRequest.FromString, response_serializer=osmosis_dot_superfluid_dot_query__pb2.SuperfluidDelegationAmountResponse.SerializeToString), 'SuperfluidDelegationsByDelegator': grpc.unary_unary_rpc_method_handler(servicer.SuperfluidDelegationsByDelegator, request_deserializer=osmosis_dot_superfluid_dot_query__pb2.SuperfluidDelegationsByDelegatorRequest.FromString, response_serializer=osmosis_dot_superfluid_dot_query__pb2.SuperfluidDelegationsByDelegatorResponse.SerializeToString), 'SuperfluidUndelegationsByDelegator': grpc.unary_unary_rpc_method_handler(servicer.SuperfluidUndelegationsByDelegator, request_deserializer=osmosis_dot_superfluid_dot_query__pb2.SuperfluidUndelegationsByDelegatorRequest.FromString, response_serializer=osmosis_dot_superfluid_dot_query__pb2.SuperfluidUndelegationsByDelegatorResponse.SerializeToString), 'SuperfluidDelegationsByValidatorDenom': grpc.unary_unary_rpc_method_handler(servicer.SuperfluidDelegationsByValidatorDenom, request_deserializer=osmosis_dot_superfluid_dot_query__pb2.SuperfluidDelegationsByValidatorDenomRequest.FromString, response_serializer=osmosis_dot_superfluid_dot_query__pb2.SuperfluidDelegationsByValidatorDenomResponse.SerializeToString), 'EstimateSuperfluidDelegatedAmountByValidatorDenom': grpc.unary_unary_rpc_method_handler(servicer.EstimateSuperfluidDelegatedAmountByValidatorDenom, request_deserializer=osmosis_dot_superfluid_dot_query__pb2.EstimateSuperfluidDelegatedAmountByValidatorDenomRequest.FromString, response_serializer=osmosis_dot_superfluid_dot_query__pb2.EstimateSuperfluidDelegatedAmountByValidatorDenomResponse.SerializeToString), 'TotalDelegationByDelegator': grpc.unary_unary_rpc_method_handler(servicer.TotalDelegationByDelegator, request_deserializer=osmosis_dot_superfluid_dot_query__pb2.QueryTotalDelegationByDelegatorRequest.FromString, response_serializer=osmosis_dot_superfluid_dot_query__pb2.QueryTotalDelegationByDelegatorResponse.SerializeToString), 'UnpoolWhitelist': grpc.unary_unary_rpc_method_handler(servicer.UnpoolWhitelist, request_deserializer=osmosis_dot_superfluid_dot_query__pb2.QueryUnpoolWhitelistRequest.FromString, response_serializer=osmosis_dot_superfluid_dot_query__pb2.QueryUnpoolWhitelistResponse.SerializeToString)}
    generic_handler = grpc.method_handlers_generic_handler('osmosis.superfluid.Query', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))

class Query(object):
    """Query defines the gRPC querier service.
    """

    @staticmethod
    def Params(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/osmosis.superfluid.Query/Params', osmosis_dot_superfluid_dot_query__pb2.QueryParamsRequest.SerializeToString, osmosis_dot_superfluid_dot_query__pb2.QueryParamsResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def AssetType(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/osmosis.superfluid.Query/AssetType', osmosis_dot_superfluid_dot_query__pb2.AssetTypeRequest.SerializeToString, osmosis_dot_superfluid_dot_query__pb2.AssetTypeResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def AllAssets(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/osmosis.superfluid.Query/AllAssets', osmosis_dot_superfluid_dot_query__pb2.AllAssetsRequest.SerializeToString, osmosis_dot_superfluid_dot_query__pb2.AllAssetsResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def AssetMultiplier(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/osmosis.superfluid.Query/AssetMultiplier', osmosis_dot_superfluid_dot_query__pb2.AssetMultiplierRequest.SerializeToString, osmosis_dot_superfluid_dot_query__pb2.AssetMultiplierResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def AllIntermediaryAccounts(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/osmosis.superfluid.Query/AllIntermediaryAccounts', osmosis_dot_superfluid_dot_query__pb2.AllIntermediaryAccountsRequest.SerializeToString, osmosis_dot_superfluid_dot_query__pb2.AllIntermediaryAccountsResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ConnectedIntermediaryAccount(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/osmosis.superfluid.Query/ConnectedIntermediaryAccount', osmosis_dot_superfluid_dot_query__pb2.ConnectedIntermediaryAccountRequest.SerializeToString, osmosis_dot_superfluid_dot_query__pb2.ConnectedIntermediaryAccountResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def TotalDelegationByValidatorForDenom(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/osmosis.superfluid.Query/TotalDelegationByValidatorForDenom', osmosis_dot_superfluid_dot_query__pb2.QueryTotalDelegationByValidatorForDenomRequest.SerializeToString, osmosis_dot_superfluid_dot_query__pb2.QueryTotalDelegationByValidatorForDenomResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def TotalSuperfluidDelegations(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/osmosis.superfluid.Query/TotalSuperfluidDelegations', osmosis_dot_superfluid_dot_query__pb2.TotalSuperfluidDelegationsRequest.SerializeToString, osmosis_dot_superfluid_dot_query__pb2.TotalSuperfluidDelegationsResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SuperfluidDelegationAmount(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/osmosis.superfluid.Query/SuperfluidDelegationAmount', osmosis_dot_superfluid_dot_query__pb2.SuperfluidDelegationAmountRequest.SerializeToString, osmosis_dot_superfluid_dot_query__pb2.SuperfluidDelegationAmountResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SuperfluidDelegationsByDelegator(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/osmosis.superfluid.Query/SuperfluidDelegationsByDelegator', osmosis_dot_superfluid_dot_query__pb2.SuperfluidDelegationsByDelegatorRequest.SerializeToString, osmosis_dot_superfluid_dot_query__pb2.SuperfluidDelegationsByDelegatorResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SuperfluidUndelegationsByDelegator(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/osmosis.superfluid.Query/SuperfluidUndelegationsByDelegator', osmosis_dot_superfluid_dot_query__pb2.SuperfluidUndelegationsByDelegatorRequest.SerializeToString, osmosis_dot_superfluid_dot_query__pb2.SuperfluidUndelegationsByDelegatorResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SuperfluidDelegationsByValidatorDenom(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/osmosis.superfluid.Query/SuperfluidDelegationsByValidatorDenom', osmosis_dot_superfluid_dot_query__pb2.SuperfluidDelegationsByValidatorDenomRequest.SerializeToString, osmosis_dot_superfluid_dot_query__pb2.SuperfluidDelegationsByValidatorDenomResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def EstimateSuperfluidDelegatedAmountByValidatorDenom(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/osmosis.superfluid.Query/EstimateSuperfluidDelegatedAmountByValidatorDenom', osmosis_dot_superfluid_dot_query__pb2.EstimateSuperfluidDelegatedAmountByValidatorDenomRequest.SerializeToString, osmosis_dot_superfluid_dot_query__pb2.EstimateSuperfluidDelegatedAmountByValidatorDenomResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def TotalDelegationByDelegator(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/osmosis.superfluid.Query/TotalDelegationByDelegator', osmosis_dot_superfluid_dot_query__pb2.QueryTotalDelegationByDelegatorRequest.SerializeToString, osmosis_dot_superfluid_dot_query__pb2.QueryTotalDelegationByDelegatorResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UnpoolWhitelist(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/osmosis.superfluid.Query/UnpoolWhitelist', osmosis_dot_superfluid_dot_query__pb2.QueryUnpoolWhitelistRequest.SerializeToString, osmosis_dot_superfluid_dot_query__pb2.QueryUnpoolWhitelistResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)