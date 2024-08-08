# Copyright © 2023 the OAI-MEP Authors

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

from oai_mep.models.base_model_ import Model
from oai_mep.models.param import Param  # noqa: F401,E501
from oai_mep.utils import util


class Endpoint(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, name: str=None, path: str=None, parameters: List[Param]=None, method: str=None, description: str=None):  # noqa: E501
        """Endpoint - a model defined in Swagger

        :param name: The name of this Endpoint.  # noqa: E501
        :type name: str
        :param path: The path of this Endpoint.  # noqa: E501
        :type path: str
        :param parameters: The parameters of this Endpoint.  # noqa: E501
        :type parameters: List[Param]
        :param method: The method of this Endpoint.  # noqa: E501
        :type method: str
        :param description: The description of this Endpoint.  # noqa: E501
        :type description: str
        """
        self.swagger_types = {
            'name': str,
            'path': str,
            'parameters': List[Param],
            'method': str,
            'description': str
        }

        self.attribute_map = {
            'name': 'name',
            'path': 'path',
            'parameters': 'parameters',
            'method': 'method',
            'description': 'description'
        }
        self._name = name
        self._path = path
        self._parameters = parameters
        self._method = method
        self._description = description

    @classmethod
    def from_dict(cls, dikt) -> 'Endpoint':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Endpoint of this Endpoint.  # noqa: E501
        :rtype: Endpoint
        """
        return util.deserialize_model(dikt, cls)

    @property
    def name(self) -> str:
        """Gets the name of this Endpoint.


        :return: The name of this Endpoint.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this Endpoint.


        :param name: The name of this Endpoint.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def path(self) -> str:
        """Gets the path of this Endpoint.

        The path to consume the service  # noqa: E501

        :return: The path of this Endpoint.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path: str):
        """Sets the path of this Endpoint.

        The path to consume the service  # noqa: E501

        :param path: The path of this Endpoint.
        :type path: str
        """
        if path is None:
            raise ValueError("Invalid value for `path`, must not be `None`")  # noqa: E501

        self._path = path

    @property
    def parameters(self) -> List[Param]:
        """Gets the parameters of this Endpoint.


        :return: The parameters of this Endpoint.
        :rtype: List[Param]
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters: List[Param]):
        """Sets the parameters of this Endpoint.


        :param parameters: The parameters of this Endpoint.
        :type parameters: List[Param]
        """

        self._parameters = parameters

    @property
    def method(self) -> str:
        """Gets the method of this Endpoint.

        If the field is not present, the service is exposed with more then one endpoint, then refer to its documentation  # noqa: E501

        :return: The method of this Endpoint.
        :rtype: str
        """
        return self._method

    @method.setter
    def method(self, method: str):
        """Sets the method of this Endpoint.

        If the field is not present, the service is exposed with more then one endpoint, then refer to its documentation  # noqa: E501

        :param method: The method of this Endpoint.
        :type method: str
        """
        allowed_values = ["GET", "HEAD", "POST", "PUT", "DELETE", "CONNECT", "OPTIONS", "TRACE", "PATH"]  # noqa: E501
        if method not in allowed_values:
            raise ValueError(
                "Invalid value for `method` ({0}), must be one of {1}"
                .format(method, allowed_values)
            )

        self._method = method

    @property
    def description(self) -> str:
        """Gets the description of this Endpoint.

        A brief description of what the endpoint does.  # noqa: E501

        :return: The description of this Endpoint.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description: str):
        """Sets the description of this Endpoint.

        A brief description of what the endpoint does.  # noqa: E501

        :param description: The description of this Endpoint.
        :type description: str
        """

        self._description = description