# Copyright © 2023 the OAI-RNIS Authors

# Licensed under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at

#   http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License. 
# Contact: netsoft@eurecom.fr

# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from oai_rnis.models.base_model_ import Model
from oai_rnis.models.rab_mod_notification_erab_qos_parameters_qos_information import RabModNotificationErabQosParametersQosInformation  # noqa: F401,E501
from oai_rnis.utils import util


class RabModNotificationErabQosParameters(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, qci: int=None, qos_information: RabModNotificationErabQosParametersQosInformation=None):  # noqa: E501
        """RabModNotificationErabQosParameters - a model defined in Swagger

        :param qci: The qci of this RabModNotificationErabQosParameters.  # noqa: E501
        :type qci: int
        :param qos_information: The qos_information of this RabModNotificationErabQosParameters.  # noqa: E501
        :type qos_information: RabModNotificationErabQosParametersQosInformation
        """
        self.swagger_types = {
            'qci': int,
            'qos_information': RabModNotificationErabQosParametersQosInformation
        }

        self.attribute_map = {
            'qci': 'qci',
            'qos_information': 'qosInformation'
        }
        self._qci = qci
        self._qos_information = qos_information

    @classmethod
    def from_dict(cls, dikt) -> 'RabModNotificationErabQosParameters':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The RabModNotification_erabQosParameters of this RabModNotificationErabQosParameters.  # noqa: E501
        :rtype: RabModNotificationErabQosParameters
        """
        return util.deserialize_model(dikt, cls)

    @property
    def qci(self) -> int:
        """Gets the qci of this RabModNotificationErabQosParameters.

        QoS Class Identifier as defined in ETSI TS 123 401 [i.4].  # noqa: E501

        :return: The qci of this RabModNotificationErabQosParameters.
        :rtype: int
        """
        return self._qci

    @qci.setter
    def qci(self, qci: int):
        """Sets the qci of this RabModNotificationErabQosParameters.

        QoS Class Identifier as defined in ETSI TS 123 401 [i.4].  # noqa: E501

        :param qci: The qci of this RabModNotificationErabQosParameters.
        :type qci: int
        """
        if qci is None:
            raise ValueError("Invalid value for `qci`, must not be `None`")  # noqa: E501

        self._qci = qci

    @property
    def qos_information(self) -> RabModNotificationErabQosParametersQosInformation:
        """Gets the qos_information of this RabModNotificationErabQosParameters.


        :return: The qos_information of this RabModNotificationErabQosParameters.
        :rtype: RabModNotificationErabQosParametersQosInformation
        """
        return self._qos_information

    @qos_information.setter
    def qos_information(self, qos_information: RabModNotificationErabQosParametersQosInformation):
        """Sets the qos_information of this RabModNotificationErabQosParameters.


        :param qos_information: The qos_information of this RabModNotificationErabQosParameters.
        :type qos_information: RabModNotificationErabQosParametersQosInformation
        """

        self._qos_information = qos_information
