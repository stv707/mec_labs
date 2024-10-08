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


class MeasQuantityResultsNr(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, rsrp: int=None, rsrq: int=None, sinr: int=None):  # noqa: E501
        """MeasQuantityResultsNr - a model defined in Swagger

        :param rsrp: The rsrp of this MeasQuantityResultsNr.  # noqa: E501
        :type rsrp: int
        :param rsrq: The rsrq of this MeasQuantityResultsNr.  # noqa: E501
        :type rsrq: int
        :param sinr: The sinr of this MeasQuantityResultsNr.  # noqa: E501
        :type sinr: int
        """
        self.swagger_types = {
            'rsrp': int,
            'rsrq': int,
            'sinr': int
        }

        self.attribute_map = {
            'rsrp': 'rsrp',
            'rsrq': 'rsrq',
            'sinr': 'sinr'
        }
        self._rsrp = rsrp
        self._rsrq = rsrq
        self._sinr = sinr

    @classmethod
    def from_dict(cls, dikt) -> 'MeasQuantityResultsNr':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The MeasQuantityResultsNr of this MeasQuantityResultsNr.  # noqa: E501
        :rtype: MeasQuantityResultsNr
        """
        return util.deserialize_model(dikt, cls)

    @property
    def rsrp(self) -> int:
        """Gets the rsrp of this MeasQuantityResultsNr.

        Reference Signal Received Power as defined in ETSI TS 138 331 [i.13].  # noqa: E501

        :return: The rsrp of this MeasQuantityResultsNr.
        :rtype: int
        """
        return self._rsrp

    @rsrp.setter
    def rsrp(self, rsrp: int):
        """Sets the rsrp of this MeasQuantityResultsNr.

        Reference Signal Received Power as defined in ETSI TS 138 331 [i.13].  # noqa: E501

        :param rsrp: The rsrp of this MeasQuantityResultsNr.
        :type rsrp: int
        """

        self._rsrp = rsrp

    @property
    def rsrq(self) -> int:
        """Gets the rsrq of this MeasQuantityResultsNr.

        Reference Signal Received Quality as defined in ETSI TS 138 331 [i.13].  # noqa: E501

        :return: The rsrq of this MeasQuantityResultsNr.
        :rtype: int
        """
        return self._rsrq

    @rsrq.setter
    def rsrq(self, rsrq: int):
        """Sets the rsrq of this MeasQuantityResultsNr.

        Reference Signal Received Quality as defined in ETSI TS 138 331 [i.13].  # noqa: E501

        :param rsrq: The rsrq of this MeasQuantityResultsNr.
        :type rsrq: int
        """

        self._rsrq = rsrq

    @property
    def sinr(self) -> int:
        """Gets the sinr of this MeasQuantityResultsNr.

        Reference Signal to Interference & Noise Ratio as defined in ETSI TS 138 331 [i.13].  # noqa: E501

        :return: The sinr of this MeasQuantityResultsNr.
        :rtype: int
        """
        return self._sinr

    @sinr.setter
    def sinr(self, sinr: int):
        """Sets the sinr of this MeasQuantityResultsNr.

        Reference Signal to Interference & Noise Ratio as defined in ETSI TS 138 331 [i.13].  # noqa: E501

        :param sinr: The sinr of this MeasQuantityResultsNr.
        :type sinr: int
        """

        self._sinr = sinr
