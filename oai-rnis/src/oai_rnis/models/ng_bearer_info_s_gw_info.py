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
from oai_rnis.utils import util


class NGBearerInfoSGwInfo(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, ip_address: str=None, tunnel_id: str=None):  # noqa: E501
        """NGBearerInfoSGwInfo - a model defined in Swagger

        :param ip_address: The ip_address of this NGBearerInfoSGwInfo.  # noqa: E501
        :type ip_address: str
        :param tunnel_id: The tunnel_id of this NGBearerInfoSGwInfo.  # noqa: E501
        :type tunnel_id: str
        """
        self.swagger_types = {
            'ip_address': str,
            'tunnel_id': str
        }

        self.attribute_map = {
            'ip_address': 'ipAddress',
            'tunnel_id': 'tunnelId'
        }
        self._ip_address = ip_address
        self._tunnel_id = tunnel_id

    @classmethod
    def from_dict(cls, dikt) -> 'NGBearerInfoSGwInfo':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The NGBearerInfo_sGwInfo of this NGBearerInfoSGwInfo.  # noqa: E501
        :rtype: NGBearerInfoSGwInfo
        """
        return util.deserialize_model(dikt, cls)

    @property
    def ip_address(self) -> str:
        """Gets the ip_address of this NGBearerInfoSGwInfo.

        SGW transport layer address of this NG bearer.  # noqa: E501

        :return: The ip_address of this NGBearerInfoSGwInfo.
        :rtype: str
        """
        return self._ip_address

    @ip_address.setter
    def ip_address(self, ip_address: str):
        """Sets the ip_address of this NGBearerInfoSGwInfo.

        SGW transport layer address of this NG bearer.  # noqa: E501

        :param ip_address: The ip_address of this NGBearerInfoSGwInfo.
        :type ip_address: str
        """
        if ip_address is None:
            raise ValueError("Invalid value for `ip_address`, must not be `None`")  # noqa: E501

        self._ip_address = ip_address

    @property
    def tunnel_id(self) -> str:
        """Gets the tunnel_id of this NGBearerInfoSGwInfo.

        SGW GTP-U TEID of this NG bearer.  # noqa: E501

        :return: The tunnel_id of this NGBearerInfoSGwInfo.
        :rtype: str
        """
        return self._tunnel_id

    @tunnel_id.setter
    def tunnel_id(self, tunnel_id: str):
        """Sets the tunnel_id of this NGBearerInfoSGwInfo.

        SGW GTP-U TEID of this NG bearer.  # noqa: E501

        :param tunnel_id: The tunnel_id of this NGBearerInfoSGwInfo.
        :type tunnel_id: str
        """
        if tunnel_id is None:
            raise ValueError("Invalid value for `tunnel_id`, must not be `None`")  # noqa: E501

        self._tunnel_id = tunnel_id
