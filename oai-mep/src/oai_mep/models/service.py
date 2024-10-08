#   Copyright 2023 OAI-MEP Authors
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#   Contact: netsoft@eurecom.fr

# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from oai_mep.models.base_model_ import Model
from oai_mep.models.endpoint import Endpoint  # noqa: F401,E501
from oai_mep.utils import util


class Service(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, sid: str=None, name: str=None, type: str=None, host: str=None, port: int=None, path: str=None, endpoints: List[Endpoint]=None, description: str=None):  # noqa: E501
        """Service - a model defined in Swagger

        :param sid: The sid of this Service.  # noqa: E501
        :type sid: str
        :param name: The name of this Service.  # noqa: E501
        :type name: str
        :param type: The type of this Service.  # noqa: E501
        :type type: str
        :param host: The host of this Service.  # noqa: E501
        :type host: str
        :param port: The port of this Service.  # noqa: E501
        :type port: int
        :param path: The path of this Service.  # noqa: E501
        :type path: str
        :param endpoints: The endpoints of this Service.  # noqa: E501
        :type endpoints: List[Endpoint]
        :param description: The description of this Service.  # noqa: E501
        :type description: str
        """
        self.swagger_types = {
            'sid': str,
            'name': str,
            'type': str,
            'host': str,
            'port': int,
            'path': str,
            'endpoints': List[Endpoint],
            'description': str
        }

        self.attribute_map = {
            'sid': 'sid',
            'name': 'name',
            'type': 'type',
            'host': 'host',
            'port': 'port',
            'path': 'path',
            'endpoints': 'endpoints',
            'description': 'description'
        }
        self._sid = sid
        self._name = name
        self._type = type
        self._host = host
        self._port = port
        self._path = path
        self._endpoints = endpoints
        self._description = description

    @classmethod
    def from_dict(cls, dikt) -> 'Service':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Service of this Service.  # noqa: E501
        :rtype: Service
        """
        return util.deserialize_model(dikt, cls)

    @property
    def sid(self) -> str:
        """Gets the sid of this Service.

        the service identifier within the registry service  # noqa: E501

        :return: The sid of this Service.
        :rtype: str
        """
        return self._sid

    @sid.setter
    def sid(self, sid: str):
        """Sets the sid of this Service.

        the service identifier within the registry service  # noqa: E501

        :param sid: The sid of this Service.
        :type sid: str
        """

        self._sid = sid

    @property
    def name(self) -> str:
        """Gets the name of this Service.

        The service name  # noqa: E501

        :return: The name of this Service.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this Service.

        The service name  # noqa: E501

        :param name: The name of this Service.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def type(self) -> str:
        """Gets the type of this Service.

        What category of service is provided. The value must be a standard value from the specification.  # noqa: E501

        :return: The type of this Service.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type: str):
        """Sets the type of this Service.

        What category of service is provided. The value must be a standard value from the specification.  # noqa: E501

        :param type: The type of this Service.
        :type type: str
        """
        allowed_values = ["AVEncoding", "SigProc", "Traffic", "ML", "ImgProc", "VidProc", "Compression", "RadioNetworkInformation", "LocalisationAPI", "TrafficAPI"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def host(self) -> str:
        """Gets the host of this Service.

        The app fqdn dns name  # noqa: E501

        :return: The host of this Service.
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host: str):
        """Sets the host of this Service.

        The app fqdn dns name  # noqa: E501

        :param host: The host of this Service.
        :type host: str
        """
        if host is None:
            raise ValueError("Invalid value for `host`, must not be `None`")  # noqa: E501

        self._host = host

    @property
    def port(self) -> int:
        """Gets the port of this Service.

        The port to which the service is listenting to  # noqa: E501

        :return: The port of this Service.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port: int):
        """Sets the port of this Service.

        The port to which the service is listenting to  # noqa: E501

        :param port: The port of this Service.
        :type port: int
        """
        if port is None:
            raise ValueError("Invalid value for `port`, must not be `None`")  # noqa: E501

        self._port = port

    @property
    def path(self) -> str:
        """Gets the path of this Service.

        The path to consume the service  # noqa: E501

        :return: The path of this Service.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path: str):
        """Sets the path of this Service.

        The path to consume the service  # noqa: E501

        :param path: The path of this Service.
        :type path: str
        """
        if path is None:
            raise ValueError("Invalid value for `path`, must not be `None`")  # noqa: E501

        self._path = path

    @property
    def endpoints(self) -> List[Endpoint]:
        """Gets the endpoints of this Service.


        :return: The endpoints of this Service.
        :rtype: List[Endpoint]
        """
        return self._endpoints

    @endpoints.setter
    def endpoints(self, endpoints: List[Endpoint]):
        """Sets the endpoints of this Service.


        :param endpoints: The endpoints of this Service.
        :type endpoints: List[Endpoint]
        """
        if endpoints is None:
            raise ValueError("Invalid value for `endpoints`, must not be `None`")  # noqa: E501

        self._endpoints = endpoints

    @property
    def description(self) -> str:
        """Gets the description of this Service.

        A brief description of what the service does.  # noqa: E501

        :return: The description of this Service.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description: str):
        """Sets the description of this Service.

        A brief description of what the service does.  # noqa: E501

        :param description: The description of this Service.
        :type description: str
        """

        self._description = description