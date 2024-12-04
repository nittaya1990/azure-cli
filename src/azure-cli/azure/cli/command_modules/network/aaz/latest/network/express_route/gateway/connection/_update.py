# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------

# pylint: skip-file
# flake8: noqa

from azure.cli.core.aaz import *


@register_command(
    "network express-route gateway connection update",
)
class Update(AAZCommand):
    """Update an ExpressRoute gateway connection.

    :example: Update an ExpressRoute gateway connection.
        az network express-route gateway connection update --gateway-name MyGateway -n MyExpressRouteConnection -g MyResourceGroup --peering /subscriptions/MySub/resourceGroups/MyResourceGroup/providers/Microsoft.Network/expressRouteCircuits/MyCircuit/peerings/AzurePrivatePeering --associated-route-table /MySub/resourceGroups/MyResourceGroup/providers/Microsoft.Network/virtualHubs/MyHub/hubRouteTables/MyRouteTable1 --propagated-route-tables [/MySub/resourceGroups/MyResourceGroup/providers/Microsoft.Network/virtualHubs/MyHub/hubRouteTables/MyRouteTable1,/MySub/resourceGroups/MyResourceGroup/providers/Microsoft.Network/virtualHubs/MyHub/hubRouteTables/MyRouteTable2] --labels [label1,label2]
    """

    _aaz_info = {
        "version": "2022-07-01",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.network/expressroutegateways/{}/expressrouteconnections/{}", "2022-07-01"],
        ]
    }

    AZ_SUPPORT_NO_WAIT = True

    AZ_SUPPORT_GENERIC_UPDATE = True

    def _handler(self, command_args):
        super()._handler(command_args)
        return self.build_lro_poller(self._execute_operations, self._output)

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.name = AAZStrArg(
            options=["-n", "--name"],
            help="ExpressRoute connection name.",
            required=True,
            id_part="child_name_1",
        )
        _args_schema.gateway_name = AAZStrArg(
            options=["--gateway-name"],
            help="ExpressRoute gateway name.",
            required=True,
            id_part="name",
        )
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )
        _args_schema.authorization_key = AAZStrArg(
            options=["--authorization-key"],
            help="Authorization key to establish the connection.",
            nullable=True,
        )
        _args_schema.internet_security = AAZBoolArg(
            options=["--internet-security"],
            help="Enable internet security. A virtual hub can have the ability to propagate a learned default route to this ExpressRoute connection. This ref https://review.learn.microsoft.com/en-us/azure/virtual-wan/effective-routes-virtual-hub?branch=pr-en-us-91866#aboutdefaultroute might be helpful.",
            nullable=True,
        )
        _args_schema.routing_weight = AAZIntArg(
            options=["--routing-weight"],
            help="Routing weight associated with the connection.",
            nullable=True,
        )

        # define Arg Group "Peering"

        _args_schema = cls._args_schema
        _args_schema.peering = AAZStrArg(
            options=["--peering"],
            arg_group="Peering",
            help="Name or ID of an ExpressRoute peering.",
            nullable=True,
        )

        # define Arg Group "Properties"

        # define Arg Group "PutExpressRouteConnectionParameters"

        # define Arg Group "Routing Configuration"

        _args_schema = cls._args_schema
        _args_schema.associated_id = AAZObjectArg(
            options=["--associated-id"],
            arg_group="Routing Configuration",
            help="The resource id of route table associated with this routing configuration.",
            nullable=True,
        )
        cls._build_args_sub_resource_update(_args_schema.associated_id)
        _args_schema.propagated_ids = AAZListArg(
            options=["--propagated-ids"],
            arg_group="Routing Configuration",
            help="Space-separated list of resource id of propagated route tables.",
            nullable=True,
        )
        _args_schema.labels = AAZListArg(
            options=["--labels"],
            arg_group="Routing Configuration",
            help="Space-separated list of labels for propagated route tables.",
            is_preview=True,
            nullable=True,
        )

        propagated_ids = cls._args_schema.propagated_ids
        propagated_ids.Element = AAZObjectArg(
            nullable=True,
        )
        cls._build_args_sub_resource_update(propagated_ids.Element)

        labels = cls._args_schema.labels
        labels.Element = AAZStrArg(
            nullable=True,
        )

        # define Arg Group "RoutingConfiguration"

        _args_schema = cls._args_schema
        _args_schema.inbound_route_map = AAZObjectArg(
            options=["--inbound-route-map"],
            arg_group="RoutingConfiguration",
            help="The resource id of the RouteMap associated with this RoutingConfiguration for inbound learned routes.",
            nullable=True,
        )
        cls._build_args_sub_resource_update(_args_schema.inbound_route_map)
        _args_schema.outbound_route_map = AAZObjectArg(
            options=["--outbound-route-map"],
            arg_group="RoutingConfiguration",
            help="The resource id of theRouteMap associated with this RoutingConfiguration for outbound advertised routes.",
            nullable=True,
        )
        cls._build_args_sub_resource_update(_args_schema.outbound_route_map)
        return cls._args_schema

    _args_sub_resource_update = None

    @classmethod
    def _build_args_sub_resource_update(cls, _schema):
        if cls._args_sub_resource_update is not None:
            _schema.id = cls._args_sub_resource_update.id
            return

        cls._args_sub_resource_update = AAZObjectArg(
            nullable=True,
        )

        sub_resource_update = cls._args_sub_resource_update
        sub_resource_update.id = AAZStrArg(
            options=["id"],
            help="Resource ID.",
            nullable=True,
        )

        _schema.id = cls._args_sub_resource_update.id

    def _execute_operations(self):
        self.pre_operations()
        self.ExpressRouteConnectionsGet(ctx=self.ctx)()
        self.pre_instance_update(self.ctx.vars.instance)
        self.InstanceUpdateByJson(ctx=self.ctx)()
        self.InstanceUpdateByGeneric(ctx=self.ctx)()
        self.post_instance_update(self.ctx.vars.instance)
        yield self.ExpressRouteConnectionsCreateOrUpdate(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    @register_callback
    def pre_instance_update(self, instance):
        pass

    @register_callback
    def post_instance_update(self, instance):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance, client_flatten=True)
        return result

    class ExpressRouteConnectionsGet(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [200]:
                return self.on_200(session)

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/expressRouteGateways/{expressRouteGatewayName}/expressRouteConnections/{connectionName}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "GET"

        @property
        def error_format(self):
            return "ODataV4Format"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "connectionName", self.ctx.args.name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "expressRouteGatewayName", self.ctx.args.gateway_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "resourceGroupName", self.ctx.args.resource_group,
                    required=True,
                ),
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2022-07-01",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        def on_200(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200
            )

        _schema_on_200 = None

        @classmethod
        def _build_schema_on_200(cls):
            if cls._schema_on_200 is not None:
                return cls._schema_on_200

            cls._schema_on_200 = AAZObjectType()
            _UpdateHelper._build_schema_express_route_connection_read(cls._schema_on_200)

            return cls._schema_on_200

    class ExpressRouteConnectionsCreateOrUpdate(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [202]:
                return self.client.build_lro_polling(
                    self.ctx.args.no_wait,
                    session,
                    self.on_200_201,
                    self.on_error,
                    lro_options={"final-state-via": "azure-async-operation"},
                    path_format_arguments=self.url_parameters,
                )
            if session.http_response.status_code in [200, 201]:
                return self.client.build_lro_polling(
                    self.ctx.args.no_wait,
                    session,
                    self.on_200_201,
                    self.on_error,
                    lro_options={"final-state-via": "azure-async-operation"},
                    path_format_arguments=self.url_parameters,
                )

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/expressRouteGateways/{expressRouteGatewayName}/expressRouteConnections/{connectionName}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "PUT"

        @property
        def error_format(self):
            return "ODataV4Format"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "connectionName", self.ctx.args.name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "expressRouteGatewayName", self.ctx.args.gateway_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "resourceGroupName", self.ctx.args.resource_group,
                    required=True,
                ),
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2022-07-01",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Content-Type", "application/json",
                ),
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        @property
        def content(self):
            _content_value, _builder = self.new_content_builder(
                self.ctx.args,
                value=self.ctx.vars.instance,
            )

            return self.serialize_content(_content_value)

        def on_200_201(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200_201
            )

        _schema_on_200_201 = None

        @classmethod
        def _build_schema_on_200_201(cls):
            if cls._schema_on_200_201 is not None:
                return cls._schema_on_200_201

            cls._schema_on_200_201 = AAZObjectType()
            _UpdateHelper._build_schema_express_route_connection_read(cls._schema_on_200_201)

            return cls._schema_on_200_201

    class InstanceUpdateByJson(AAZJsonInstanceUpdateOperation):

        def __call__(self, *args, **kwargs):
            self._update_instance(self.ctx.vars.instance)

        def _update_instance(self, instance):
            _instance_value, _builder = self.new_content_builder(
                self.ctx.args,
                value=instance,
                typ=AAZObjectType
            )
            _builder.set_prop("name", AAZStrType, ".name", typ_kwargs={"flags": {"required": True}})
            _builder.set_prop("properties", AAZObjectType, typ_kwargs={"flags": {"client_flatten": True}})

            properties = _builder.get(".properties")
            if properties is not None:
                properties.set_prop("authorizationKey", AAZStrType, ".authorization_key")
                properties.set_prop("enableInternetSecurity", AAZBoolType, ".internet_security")
                properties.set_prop("expressRouteCircuitPeering", AAZObjectType, ".", typ_kwargs={"flags": {"required": True}})
                properties.set_prop("routingConfiguration", AAZObjectType)
                properties.set_prop("routingWeight", AAZIntType, ".routing_weight")

            express_route_circuit_peering = _builder.get(".properties.expressRouteCircuitPeering")
            if express_route_circuit_peering is not None:
                express_route_circuit_peering.set_prop("id", AAZStrType, ".peering")

            routing_configuration = _builder.get(".properties.routingConfiguration")
            if routing_configuration is not None:
                _UpdateHelper._build_schema_sub_resource_update(routing_configuration.set_prop("associatedRouteTable", AAZObjectType, ".associated_id"))
                _UpdateHelper._build_schema_sub_resource_update(routing_configuration.set_prop("inboundRouteMap", AAZObjectType, ".inbound_route_map"))
                _UpdateHelper._build_schema_sub_resource_update(routing_configuration.set_prop("outboundRouteMap", AAZObjectType, ".outbound_route_map"))
                routing_configuration.set_prop("propagatedRouteTables", AAZObjectType)

            propagated_route_tables = _builder.get(".properties.routingConfiguration.propagatedRouteTables")
            if propagated_route_tables is not None:
                propagated_route_tables.set_prop("ids", AAZListType, ".propagated_ids")
                propagated_route_tables.set_prop("labels", AAZListType, ".labels")

            ids = _builder.get(".properties.routingConfiguration.propagatedRouteTables.ids")
            if ids is not None:
                _UpdateHelper._build_schema_sub_resource_update(ids.set_elements(AAZObjectType, "."))

            labels = _builder.get(".properties.routingConfiguration.propagatedRouteTables.labels")
            if labels is not None:
                labels.set_elements(AAZStrType, ".")

            return _instance_value

    class InstanceUpdateByGeneric(AAZGenericInstanceUpdateOperation):

        def __call__(self, *args, **kwargs):
            self._update_instance_by_generic(
                self.ctx.vars.instance,
                self.ctx.generic_update_args
            )


class _UpdateHelper:
    """Helper class for Update"""

    @classmethod
    def _build_schema_sub_resource_update(cls, _builder):
        if _builder is None:
            return
        _builder.set_prop("id", AAZStrType, ".id")

    _schema_express_route_connection_read = None

    @classmethod
    def _build_schema_express_route_connection_read(cls, _schema):
        if cls._schema_express_route_connection_read is not None:
            _schema.id = cls._schema_express_route_connection_read.id
            _schema.name = cls._schema_express_route_connection_read.name
            _schema.properties = cls._schema_express_route_connection_read.properties
            return

        cls._schema_express_route_connection_read = _schema_express_route_connection_read = AAZObjectType()

        express_route_connection_read = _schema_express_route_connection_read
        express_route_connection_read.id = AAZStrType()
        express_route_connection_read.name = AAZStrType(
            flags={"required": True},
        )
        express_route_connection_read.properties = AAZObjectType(
            flags={"client_flatten": True},
        )

        properties = _schema_express_route_connection_read.properties
        properties.authorization_key = AAZStrType(
            serialized_name="authorizationKey",
        )
        properties.enable_internet_security = AAZBoolType(
            serialized_name="enableInternetSecurity",
        )
        properties.enable_private_link_fast_path = AAZBoolType(
            serialized_name="enablePrivateLinkFastPath",
        )
        properties.express_route_circuit_peering = AAZObjectType(
            serialized_name="expressRouteCircuitPeering",
            flags={"required": True},
        )
        properties.express_route_gateway_bypass = AAZBoolType(
            serialized_name="expressRouteGatewayBypass",
        )
        properties.provisioning_state = AAZStrType(
            serialized_name="provisioningState",
            flags={"read_only": True},
        )
        properties.routing_configuration = AAZObjectType(
            serialized_name="routingConfiguration",
        )
        properties.routing_weight = AAZIntType(
            serialized_name="routingWeight",
        )

        express_route_circuit_peering = _schema_express_route_connection_read.properties.express_route_circuit_peering
        express_route_circuit_peering.id = AAZStrType()

        routing_configuration = _schema_express_route_connection_read.properties.routing_configuration
        routing_configuration.associated_route_table = AAZObjectType(
            serialized_name="associatedRouteTable",
        )
        cls._build_schema_sub_resource_read(routing_configuration.associated_route_table)
        routing_configuration.inbound_route_map = AAZObjectType(
            serialized_name="inboundRouteMap",
        )
        cls._build_schema_sub_resource_read(routing_configuration.inbound_route_map)
        routing_configuration.outbound_route_map = AAZObjectType(
            serialized_name="outboundRouteMap",
        )
        cls._build_schema_sub_resource_read(routing_configuration.outbound_route_map)
        routing_configuration.propagated_route_tables = AAZObjectType(
            serialized_name="propagatedRouteTables",
        )
        routing_configuration.vnet_routes = AAZObjectType(
            serialized_name="vnetRoutes",
        )

        propagated_route_tables = _schema_express_route_connection_read.properties.routing_configuration.propagated_route_tables
        propagated_route_tables.ids = AAZListType()
        propagated_route_tables.labels = AAZListType()

        ids = _schema_express_route_connection_read.properties.routing_configuration.propagated_route_tables.ids
        ids.Element = AAZObjectType()
        cls._build_schema_sub_resource_read(ids.Element)

        labels = _schema_express_route_connection_read.properties.routing_configuration.propagated_route_tables.labels
        labels.Element = AAZStrType()

        vnet_routes = _schema_express_route_connection_read.properties.routing_configuration.vnet_routes
        vnet_routes.bgp_connections = AAZListType(
            serialized_name="bgpConnections",
            flags={"read_only": True},
        )
        vnet_routes.static_routes = AAZListType(
            serialized_name="staticRoutes",
        )
        vnet_routes.static_routes_config = AAZObjectType(
            serialized_name="staticRoutesConfig",
        )

        bgp_connections = _schema_express_route_connection_read.properties.routing_configuration.vnet_routes.bgp_connections
        bgp_connections.Element = AAZObjectType()
        cls._build_schema_sub_resource_read(bgp_connections.Element)

        static_routes = _schema_express_route_connection_read.properties.routing_configuration.vnet_routes.static_routes
        static_routes.Element = AAZObjectType()

        _element = _schema_express_route_connection_read.properties.routing_configuration.vnet_routes.static_routes.Element
        _element.address_prefixes = AAZListType(
            serialized_name="addressPrefixes",
        )
        _element.name = AAZStrType()
        _element.next_hop_ip_address = AAZStrType(
            serialized_name="nextHopIpAddress",
        )

        address_prefixes = _schema_express_route_connection_read.properties.routing_configuration.vnet_routes.static_routes.Element.address_prefixes
        address_prefixes.Element = AAZStrType()

        static_routes_config = _schema_express_route_connection_read.properties.routing_configuration.vnet_routes.static_routes_config
        static_routes_config.propagate_static_routes = AAZBoolType(
            serialized_name="propagateStaticRoutes",
            flags={"read_only": True},
        )
        static_routes_config.vnet_local_route_override_criteria = AAZStrType(
            serialized_name="vnetLocalRouteOverrideCriteria",
        )

        _schema.id = cls._schema_express_route_connection_read.id
        _schema.name = cls._schema_express_route_connection_read.name
        _schema.properties = cls._schema_express_route_connection_read.properties

    _schema_sub_resource_read = None

    @classmethod
    def _build_schema_sub_resource_read(cls, _schema):
        if cls._schema_sub_resource_read is not None:
            _schema.id = cls._schema_sub_resource_read.id
            return

        cls._schema_sub_resource_read = _schema_sub_resource_read = AAZObjectType()

        sub_resource_read = _schema_sub_resource_read
        sub_resource_read.id = AAZStrType()

        _schema.id = cls._schema_sub_resource_read.id


__all__ = ["Update"]
