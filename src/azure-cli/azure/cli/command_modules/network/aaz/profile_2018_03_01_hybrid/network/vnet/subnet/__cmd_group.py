# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------

# pylint: skip-file
# flake8: noqa

from azure.cli.core.aaz import *


@register_command_group(
    "network vnet subnet",
)
class __CMDGroup(AAZCommandGroup):
    """Manage subnets in an Azure Virtual Network.

    To learn more about subnets visit https://learn.microsoft.com/azure/virtual-network/virtual-network-manage-subnet.
    """
    pass


__all__ = ["__CMDGroup"]
