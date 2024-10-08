# Copyright © 2023 the MEP-OAI Authors

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
# API Version: 0.0.1
# Contact: netsoft@eurecom.fr

# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from oai_rnis.models.base_model_ import Model
from oai_rnis.utils import util


class AssociateId(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, type: int=None, value: str=None):  # noqa: E501
        """AssociateId - a model defined in Swagger

        :param type: The type of this AssociateId.  # noqa: E501
        :type type: int
        :param value: The value of this AssociateId.  # noqa: E501
        :type value: str
        """
        self.swagger_types = {
            'type': int,
            'value': str
        }

        self.attribute_map = {
            'type': 'type',
            'value': 'value'
        }
        self._type = type
        self._value = value

    @classmethod
    def from_dict(cls, dikt) -> 'AssociateId':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The AssociateId of this AssociateId.  # noqa: E501
        :rtype: AssociateId
        """
        return util.deserialize_model(dikt, cls)

    @property
    def type(self) -> int:
        """Gets the type of this AssociateId.

        Numeric value (0-255) corresponding to specified type of identifier as following: <p>0 = reserved. <p>1 = UE_IPv4_ADDRESS. <p>2 = UE_IPV6_ADDRESS. <p>3 = NATED_IP_ADDRESS. <p>4 = GTP_TEID.  # noqa: E501

        :return: The type of this AssociateId.
        :rtype: int
        """
        return self._type

    @type.setter
    def type(self, type: int):
        """Sets the type of this AssociateId.

        Numeric value (0-255) corresponding to specified type of identifier as following: <p>0 = reserved. <p>1 = UE_IPv4_ADDRESS. <p>2 = UE_IPV6_ADDRESS. <p>3 = NATED_IP_ADDRESS. <p>4 = GTP_TEID.  # noqa: E501

        :param type: The type of this AssociateId.
        :type type: int
        """
        allowed_values = ["0", "1", "2", "3", "4"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def value(self) -> str:
        """Gets the value of this AssociateId.

        Value for the identifier.  # noqa: E501

        :return: The value of this AssociateId.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value: str):
        """Sets the value of this AssociateId.

        Value for the identifier.  # noqa: E501

        :param value: The value of this AssociateId.
        :type value: str
        """

        self._value = value
