# vim: tabstop=4 shiftwidth=4 softtabstop=4

# Copyright 2013 Embrane, Inc.
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.
#
# @author: Ivar Lazzaro, Embrane, Inc.

from neutron.common import exceptions as neutron_exec


class EmbranePluginException(neutron_exec.NeutronException):
    message = _("An unexpected error occurred:%(err_msg)s")


# Not permitted operation
class NonPermitted(neutron_exec.BadRequest):
    pass


class StateConstraintException(NonPermitted):
    message = _("Operation not permitted due to state constraint violation:"
                "%(operation)s not allowed for DVA %(dva_id)s in state "
                " %(state)s")