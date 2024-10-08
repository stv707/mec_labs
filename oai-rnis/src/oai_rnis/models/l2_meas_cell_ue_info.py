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
from oai_rnis.models.associate_id import AssociateId  # noqa: F401,E501
from oai_rnis.models.ecgi import Ecgi  # noqa: F401,E501
from oai_rnis.utils import util


class L2MeasCellUEInfo(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, associate_id: AssociateId=None, dl_gbr_data_volume_ue: int=None, dl_gbr_delay_ue: int=None, dl_gbr_pdr_ue: int=None, dl_gbr_throughput_ue: int=None, dl_nongbr_data_volume_ue: int=None, dl_nongbr_delay_ue: int=None, dl_nongbr_pdr_ue: int=None, dl_nongbr_throughput_ue: int=None, ecgi: Ecgi=None, ul_gbr_data_volume_ue: int=None, ul_gbr_delay_ue: int=None, ul_gbr_pdr_ue: int=None, ul_gbr_throughput_ue: int=None, ul_nongbr_data_volume_ue: int=None, ul_nongbr_delay_ue: int=None, ul_nongbr_pdr_ue: int=None, ul_nongbr_throughput_ue: int=None):  # noqa: E501
        """L2MeasCellUEInfo - a model defined in Swagger

        :param associate_id: The associate_id of this L2MeasCellUEInfo.  # noqa: E501
        :type associate_id: AssociateId
        :param dl_gbr_data_volume_ue: The dl_gbr_data_volume_ue of this L2MeasCellUEInfo.  # noqa: E501
        :type dl_gbr_data_volume_ue: int
        :param dl_gbr_delay_ue: The dl_gbr_delay_ue of this L2MeasCellUEInfo.  # noqa: E501
        :type dl_gbr_delay_ue: int
        :param dl_gbr_pdr_ue: The dl_gbr_pdr_ue of this L2MeasCellUEInfo.  # noqa: E501
        :type dl_gbr_pdr_ue: int
        :param dl_gbr_throughput_ue: The dl_gbr_throughput_ue of this L2MeasCellUEInfo.  # noqa: E501
        :type dl_gbr_throughput_ue: int
        :param dl_nongbr_data_volume_ue: The dl_nongbr_data_volume_ue of this L2MeasCellUEInfo.  # noqa: E501
        :type dl_nongbr_data_volume_ue: int
        :param dl_nongbr_delay_ue: The dl_nongbr_delay_ue of this L2MeasCellUEInfo.  # noqa: E501
        :type dl_nongbr_delay_ue: int
        :param dl_nongbr_pdr_ue: The dl_nongbr_pdr_ue of this L2MeasCellUEInfo.  # noqa: E501
        :type dl_nongbr_pdr_ue: int
        :param dl_nongbr_throughput_ue: The dl_nongbr_throughput_ue of this L2MeasCellUEInfo.  # noqa: E501
        :type dl_nongbr_throughput_ue: int
        :param ecgi: The ecgi of this L2MeasCellUEInfo.  # noqa: E501
        :type ecgi: Ecgi
        :param ul_gbr_data_volume_ue: The ul_gbr_data_volume_ue of this L2MeasCellUEInfo.  # noqa: E501
        :type ul_gbr_data_volume_ue: int
        :param ul_gbr_delay_ue: The ul_gbr_delay_ue of this L2MeasCellUEInfo.  # noqa: E501
        :type ul_gbr_delay_ue: int
        :param ul_gbr_pdr_ue: The ul_gbr_pdr_ue of this L2MeasCellUEInfo.  # noqa: E501
        :type ul_gbr_pdr_ue: int
        :param ul_gbr_throughput_ue: The ul_gbr_throughput_ue of this L2MeasCellUEInfo.  # noqa: E501
        :type ul_gbr_throughput_ue: int
        :param ul_nongbr_data_volume_ue: The ul_nongbr_data_volume_ue of this L2MeasCellUEInfo.  # noqa: E501
        :type ul_nongbr_data_volume_ue: int
        :param ul_nongbr_delay_ue: The ul_nongbr_delay_ue of this L2MeasCellUEInfo.  # noqa: E501
        :type ul_nongbr_delay_ue: int
        :param ul_nongbr_pdr_ue: The ul_nongbr_pdr_ue of this L2MeasCellUEInfo.  # noqa: E501
        :type ul_nongbr_pdr_ue: int
        :param ul_nongbr_throughput_ue: The ul_nongbr_throughput_ue of this L2MeasCellUEInfo.  # noqa: E501
        :type ul_nongbr_throughput_ue: int
        """
        self.swagger_types = {
            'associate_id': AssociateId,
            'dl_gbr_data_volume_ue': int,
            'dl_gbr_delay_ue': int,
            'dl_gbr_pdr_ue': int,
            'dl_gbr_throughput_ue': int,
            'dl_nongbr_data_volume_ue': int,
            'dl_nongbr_delay_ue': int,
            'dl_nongbr_pdr_ue': int,
            'dl_nongbr_throughput_ue': int,
            'ecgi': Ecgi,
            'ul_gbr_data_volume_ue': int,
            'ul_gbr_delay_ue': int,
            'ul_gbr_pdr_ue': int,
            'ul_gbr_throughput_ue': int,
            'ul_nongbr_data_volume_ue': int,
            'ul_nongbr_delay_ue': int,
            'ul_nongbr_pdr_ue': int,
            'ul_nongbr_throughput_ue': int
        }

        self.attribute_map = {
            'associate_id': 'associateId',
            'dl_gbr_data_volume_ue': 'dl_gbr_data_volume_ue',
            'dl_gbr_delay_ue': 'dl_gbr_delay_ue',
            'dl_gbr_pdr_ue': 'dl_gbr_pdr_ue',
            'dl_gbr_throughput_ue': 'dl_gbr_throughput_ue',
            'dl_nongbr_data_volume_ue': 'dl_nongbr_data_volume_ue',
            'dl_nongbr_delay_ue': 'dl_nongbr_delay_ue',
            'dl_nongbr_pdr_ue': 'dl_nongbr_pdr_ue',
            'dl_nongbr_throughput_ue': 'dl_nongbr_throughput_ue',
            'ecgi': 'ecgi',
            'ul_gbr_data_volume_ue': 'ul_gbr_data_volume_ue',
            'ul_gbr_delay_ue': 'ul_gbr_delay_ue',
            'ul_gbr_pdr_ue': 'ul_gbr_pdr_ue',
            'ul_gbr_throughput_ue': 'ul_gbr_throughput_ue',
            'ul_nongbr_data_volume_ue': 'ul_nongbr_data_volume_ue',
            'ul_nongbr_delay_ue': 'ul_nongbr_delay_ue',
            'ul_nongbr_pdr_ue': 'ul_nongbr_pdr_ue',
            'ul_nongbr_throughput_ue': 'ul_nongbr_throughput_ue'
        }
        self._associate_id = associate_id
        self._dl_gbr_data_volume_ue = dl_gbr_data_volume_ue
        self._dl_gbr_delay_ue = dl_gbr_delay_ue
        self._dl_gbr_pdr_ue = dl_gbr_pdr_ue
        self._dl_gbr_throughput_ue = dl_gbr_throughput_ue
        self._dl_nongbr_data_volume_ue = dl_nongbr_data_volume_ue
        self._dl_nongbr_delay_ue = dl_nongbr_delay_ue
        self._dl_nongbr_pdr_ue = dl_nongbr_pdr_ue
        self._dl_nongbr_throughput_ue = dl_nongbr_throughput_ue
        self._ecgi = ecgi
        self._ul_gbr_data_volume_ue = ul_gbr_data_volume_ue
        self._ul_gbr_delay_ue = ul_gbr_delay_ue
        self._ul_gbr_pdr_ue = ul_gbr_pdr_ue
        self._ul_gbr_throughput_ue = ul_gbr_throughput_ue
        self._ul_nongbr_data_volume_ue = ul_nongbr_data_volume_ue
        self._ul_nongbr_delay_ue = ul_nongbr_delay_ue
        self._ul_nongbr_pdr_ue = ul_nongbr_pdr_ue
        self._ul_nongbr_throughput_ue = ul_nongbr_throughput_ue

    @classmethod
    def from_dict(cls, dikt) -> 'L2MeasCellUEInfo':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The L2Meas_cellUEInfo of this L2MeasCellUEInfo.  # noqa: E501
        :rtype: L2MeasCellUEInfo
        """
        return util.deserialize_model(dikt, cls)

    @property
    def associate_id(self) -> AssociateId:
        """Gets the associate_id of this L2MeasCellUEInfo.


        :return: The associate_id of this L2MeasCellUEInfo.
        :rtype: AssociateId
        """
        return self._associate_id

    @associate_id.setter
    def associate_id(self, associate_id: AssociateId):
        """Sets the associate_id of this L2MeasCellUEInfo.


        :param associate_id: The associate_id of this L2MeasCellUEInfo.
        :type associate_id: AssociateId
        """

        self._associate_id = associate_id

    @property
    def dl_gbr_data_volume_ue(self) -> int:
        """Gets the dl_gbr_data_volume_ue of this L2MeasCellUEInfo.

        It indicates the data volume of the downlink GBR traffic of a UE, as defined in ETSI TS 136 314 [i.11].  # noqa: E501

        :return: The dl_gbr_data_volume_ue of this L2MeasCellUEInfo.
        :rtype: int
        """
        return self._dl_gbr_data_volume_ue

    @dl_gbr_data_volume_ue.setter
    def dl_gbr_data_volume_ue(self, dl_gbr_data_volume_ue: int):
        """Sets the dl_gbr_data_volume_ue of this L2MeasCellUEInfo.

        It indicates the data volume of the downlink GBR traffic of a UE, as defined in ETSI TS 136 314 [i.11].  # noqa: E501

        :param dl_gbr_data_volume_ue: The dl_gbr_data_volume_ue of this L2MeasCellUEInfo.
        :type dl_gbr_data_volume_ue: int
        """

        self._dl_gbr_data_volume_ue = dl_gbr_data_volume_ue

    @property
    def dl_gbr_delay_ue(self) -> int:
        """Gets the dl_gbr_delay_ue of this L2MeasCellUEInfo.

        It indicates the packet delay of the downlink GBR traffic of a UE, as defined in ETSI TS 136 314 [i.11].  # noqa: E501

        :return: The dl_gbr_delay_ue of this L2MeasCellUEInfo.
        :rtype: int
        """
        return self._dl_gbr_delay_ue

    @dl_gbr_delay_ue.setter
    def dl_gbr_delay_ue(self, dl_gbr_delay_ue: int):
        """Sets the dl_gbr_delay_ue of this L2MeasCellUEInfo.

        It indicates the packet delay of the downlink GBR traffic of a UE, as defined in ETSI TS 136 314 [i.11].  # noqa: E501

        :param dl_gbr_delay_ue: The dl_gbr_delay_ue of this L2MeasCellUEInfo.
        :type dl_gbr_delay_ue: int
        """

        self._dl_gbr_delay_ue = dl_gbr_delay_ue

    @property
    def dl_gbr_pdr_ue(self) -> int:
        """Gets the dl_gbr_pdr_ue of this L2MeasCellUEInfo.

        It indicates the packet discard rate in percentage of the downlink GBR traffic of a UE, as defined in ETSI TS 136 314 [i.11].  # noqa: E501

        :return: The dl_gbr_pdr_ue of this L2MeasCellUEInfo.
        :rtype: int
        """
        return self._dl_gbr_pdr_ue

    @dl_gbr_pdr_ue.setter
    def dl_gbr_pdr_ue(self, dl_gbr_pdr_ue: int):
        """Sets the dl_gbr_pdr_ue of this L2MeasCellUEInfo.

        It indicates the packet discard rate in percentage of the downlink GBR traffic of a UE, as defined in ETSI TS 136 314 [i.11].  # noqa: E501

        :param dl_gbr_pdr_ue: The dl_gbr_pdr_ue of this L2MeasCellUEInfo.
        :type dl_gbr_pdr_ue: int
        """

        self._dl_gbr_pdr_ue = dl_gbr_pdr_ue

    @property
    def dl_gbr_throughput_ue(self) -> int:
        """Gets the dl_gbr_throughput_ue of this L2MeasCellUEInfo.

        It indicates the scheduled throughput of the downlink GBR traffic of a UE, as defined in ETSI TS 136 314 [i.11].  # noqa: E501

        :return: The dl_gbr_throughput_ue of this L2MeasCellUEInfo.
        :rtype: int
        """
        return self._dl_gbr_throughput_ue

    @dl_gbr_throughput_ue.setter
    def dl_gbr_throughput_ue(self, dl_gbr_throughput_ue: int):
        """Sets the dl_gbr_throughput_ue of this L2MeasCellUEInfo.

        It indicates the scheduled throughput of the downlink GBR traffic of a UE, as defined in ETSI TS 136 314 [i.11].  # noqa: E501

        :param dl_gbr_throughput_ue: The dl_gbr_throughput_ue of this L2MeasCellUEInfo.
        :type dl_gbr_throughput_ue: int
        """

        self._dl_gbr_throughput_ue = dl_gbr_throughput_ue

    @property
    def dl_nongbr_data_volume_ue(self) -> int:
        """Gets the dl_nongbr_data_volume_ue of this L2MeasCellUEInfo.

        It indicates the data volume of the downlink non-GBR traffic of a UE, as defined in ETSI TS 136 314 [i.11].  # noqa: E501

        :return: The dl_nongbr_data_volume_ue of this L2MeasCellUEInfo.
        :rtype: int
        """
        return self._dl_nongbr_data_volume_ue

    @dl_nongbr_data_volume_ue.setter
    def dl_nongbr_data_volume_ue(self, dl_nongbr_data_volume_ue: int):
        """Sets the dl_nongbr_data_volume_ue of this L2MeasCellUEInfo.

        It indicates the data volume of the downlink non-GBR traffic of a UE, as defined in ETSI TS 136 314 [i.11].  # noqa: E501

        :param dl_nongbr_data_volume_ue: The dl_nongbr_data_volume_ue of this L2MeasCellUEInfo.
        :type dl_nongbr_data_volume_ue: int
        """

        self._dl_nongbr_data_volume_ue = dl_nongbr_data_volume_ue

    @property
    def dl_nongbr_delay_ue(self) -> int:
        """Gets the dl_nongbr_delay_ue of this L2MeasCellUEInfo.

        It indicates the packet delay of the downlink non-GBR traffic of a UE, as defined in ETSI TS 136 314 [i.11].  # noqa: E501

        :return: The dl_nongbr_delay_ue of this L2MeasCellUEInfo.
        :rtype: int
        """
        return self._dl_nongbr_delay_ue

    @dl_nongbr_delay_ue.setter
    def dl_nongbr_delay_ue(self, dl_nongbr_delay_ue: int):
        """Sets the dl_nongbr_delay_ue of this L2MeasCellUEInfo.

        It indicates the packet delay of the downlink non-GBR traffic of a UE, as defined in ETSI TS 136 314 [i.11].  # noqa: E501

        :param dl_nongbr_delay_ue: The dl_nongbr_delay_ue of this L2MeasCellUEInfo.
        :type dl_nongbr_delay_ue: int
        """

        self._dl_nongbr_delay_ue = dl_nongbr_delay_ue

    @property
    def dl_nongbr_pdr_ue(self) -> int:
        """Gets the dl_nongbr_pdr_ue of this L2MeasCellUEInfo.

        It indicates the packet discard rate in percentage of the downlink nonGBR traffic of a UE, as defined in ETSI TS 136 314 [i.11].  # noqa: E501

        :return: The dl_nongbr_pdr_ue of this L2MeasCellUEInfo.
        :rtype: int
        """
        return self._dl_nongbr_pdr_ue

    @dl_nongbr_pdr_ue.setter
    def dl_nongbr_pdr_ue(self, dl_nongbr_pdr_ue: int):
        """Sets the dl_nongbr_pdr_ue of this L2MeasCellUEInfo.

        It indicates the packet discard rate in percentage of the downlink nonGBR traffic of a UE, as defined in ETSI TS 136 314 [i.11].  # noqa: E501

        :param dl_nongbr_pdr_ue: The dl_nongbr_pdr_ue of this L2MeasCellUEInfo.
        :type dl_nongbr_pdr_ue: int
        """

        self._dl_nongbr_pdr_ue = dl_nongbr_pdr_ue

    @property
    def dl_nongbr_throughput_ue(self) -> int:
        """Gets the dl_nongbr_throughput_ue of this L2MeasCellUEInfo.

        It indicates the scheduled throughput of the downlink nonGBR traffic of a UE, as defined in ETSI TS 136 314 [i.11].  # noqa: E501

        :return: The dl_nongbr_throughput_ue of this L2MeasCellUEInfo.
        :rtype: int
        """
        return self._dl_nongbr_throughput_ue

    @dl_nongbr_throughput_ue.setter
    def dl_nongbr_throughput_ue(self, dl_nongbr_throughput_ue: int):
        """Sets the dl_nongbr_throughput_ue of this L2MeasCellUEInfo.

        It indicates the scheduled throughput of the downlink nonGBR traffic of a UE, as defined in ETSI TS 136 314 [i.11].  # noqa: E501

        :param dl_nongbr_throughput_ue: The dl_nongbr_throughput_ue of this L2MeasCellUEInfo.
        :type dl_nongbr_throughput_ue: int
        """

        self._dl_nongbr_throughput_ue = dl_nongbr_throughput_ue

    @property
    def ecgi(self) -> Ecgi:
        """Gets the ecgi of this L2MeasCellUEInfo.


        :return: The ecgi of this L2MeasCellUEInfo.
        :rtype: Ecgi
        """
        return self._ecgi

    @ecgi.setter
    def ecgi(self, ecgi: Ecgi):
        """Sets the ecgi of this L2MeasCellUEInfo.


        :param ecgi: The ecgi of this L2MeasCellUEInfo.
        :type ecgi: Ecgi
        """

        self._ecgi = ecgi

    @property
    def ul_gbr_data_volume_ue(self) -> int:
        """Gets the ul_gbr_data_volume_ue of this L2MeasCellUEInfo.

        It indicates the data volume of the uplink GBR traffic of a UE, as defined in ETSI TS 136 314 [i.11].  # noqa: E501

        :return: The ul_gbr_data_volume_ue of this L2MeasCellUEInfo.
        :rtype: int
        """
        return self._ul_gbr_data_volume_ue

    @ul_gbr_data_volume_ue.setter
    def ul_gbr_data_volume_ue(self, ul_gbr_data_volume_ue: int):
        """Sets the ul_gbr_data_volume_ue of this L2MeasCellUEInfo.

        It indicates the data volume of the uplink GBR traffic of a UE, as defined in ETSI TS 136 314 [i.11].  # noqa: E501

        :param ul_gbr_data_volume_ue: The ul_gbr_data_volume_ue of this L2MeasCellUEInfo.
        :type ul_gbr_data_volume_ue: int
        """

        self._ul_gbr_data_volume_ue = ul_gbr_data_volume_ue

    @property
    def ul_gbr_delay_ue(self) -> int:
        """Gets the ul_gbr_delay_ue of this L2MeasCellUEInfo.

        It indicates the packet delay of the uplink GBR traffic of a UE, as defined in ETSI TS 136 314 [i.11].  # noqa: E501

        :return: The ul_gbr_delay_ue of this L2MeasCellUEInfo.
        :rtype: int
        """
        return self._ul_gbr_delay_ue

    @ul_gbr_delay_ue.setter
    def ul_gbr_delay_ue(self, ul_gbr_delay_ue: int):
        """Sets the ul_gbr_delay_ue of this L2MeasCellUEInfo.

        It indicates the packet delay of the uplink GBR traffic of a UE, as defined in ETSI TS 136 314 [i.11].  # noqa: E501

        :param ul_gbr_delay_ue: The ul_gbr_delay_ue of this L2MeasCellUEInfo.
        :type ul_gbr_delay_ue: int
        """

        self._ul_gbr_delay_ue = ul_gbr_delay_ue

    @property
    def ul_gbr_pdr_ue(self) -> int:
        """Gets the ul_gbr_pdr_ue of this L2MeasCellUEInfo.

        It indicates the packet discard rate in percentage of the uplink GBR traffic of a UE, as defined in ETSI TS 136 314 [i.11].  # noqa: E501

        :return: The ul_gbr_pdr_ue of this L2MeasCellUEInfo.
        :rtype: int
        """
        return self._ul_gbr_pdr_ue

    @ul_gbr_pdr_ue.setter
    def ul_gbr_pdr_ue(self, ul_gbr_pdr_ue: int):
        """Sets the ul_gbr_pdr_ue of this L2MeasCellUEInfo.

        It indicates the packet discard rate in percentage of the uplink GBR traffic of a UE, as defined in ETSI TS 136 314 [i.11].  # noqa: E501

        :param ul_gbr_pdr_ue: The ul_gbr_pdr_ue of this L2MeasCellUEInfo.
        :type ul_gbr_pdr_ue: int
        """

        self._ul_gbr_pdr_ue = ul_gbr_pdr_ue

    @property
    def ul_gbr_throughput_ue(self) -> int:
        """Gets the ul_gbr_throughput_ue of this L2MeasCellUEInfo.

        It indicates the scheduled throughput of the uplink GBR traffic of a UE, as defined in ETSI TS 136 314 [i.11].  # noqa: E501

        :return: The ul_gbr_throughput_ue of this L2MeasCellUEInfo.
        :rtype: int
        """
        return self._ul_gbr_throughput_ue

    @ul_gbr_throughput_ue.setter
    def ul_gbr_throughput_ue(self, ul_gbr_throughput_ue: int):
        """Sets the ul_gbr_throughput_ue of this L2MeasCellUEInfo.

        It indicates the scheduled throughput of the uplink GBR traffic of a UE, as defined in ETSI TS 136 314 [i.11].  # noqa: E501

        :param ul_gbr_throughput_ue: The ul_gbr_throughput_ue of this L2MeasCellUEInfo.
        :type ul_gbr_throughput_ue: int
        """

        self._ul_gbr_throughput_ue = ul_gbr_throughput_ue

    @property
    def ul_nongbr_data_volume_ue(self) -> int:
        """Gets the ul_nongbr_data_volume_ue of this L2MeasCellUEInfo.

        It indicates the data volume of the uplink non-GBR traffic of a UE, as defined in ETSI TS 136 314 [i.11].  # noqa: E501

        :return: The ul_nongbr_data_volume_ue of this L2MeasCellUEInfo.
        :rtype: int
        """
        return self._ul_nongbr_data_volume_ue

    @ul_nongbr_data_volume_ue.setter
    def ul_nongbr_data_volume_ue(self, ul_nongbr_data_volume_ue: int):
        """Sets the ul_nongbr_data_volume_ue of this L2MeasCellUEInfo.

        It indicates the data volume of the uplink non-GBR traffic of a UE, as defined in ETSI TS 136 314 [i.11].  # noqa: E501

        :param ul_nongbr_data_volume_ue: The ul_nongbr_data_volume_ue of this L2MeasCellUEInfo.
        :type ul_nongbr_data_volume_ue: int
        """

        self._ul_nongbr_data_volume_ue = ul_nongbr_data_volume_ue

    @property
    def ul_nongbr_delay_ue(self) -> int:
        """Gets the ul_nongbr_delay_ue of this L2MeasCellUEInfo.

        It indicates the packet delay of the uplink non-GBR traffic of a UE, as defined in ETSI TS 136 314 [i.11].  # noqa: E501

        :return: The ul_nongbr_delay_ue of this L2MeasCellUEInfo.
        :rtype: int
        """
        return self._ul_nongbr_delay_ue

    @ul_nongbr_delay_ue.setter
    def ul_nongbr_delay_ue(self, ul_nongbr_delay_ue: int):
        """Sets the ul_nongbr_delay_ue of this L2MeasCellUEInfo.

        It indicates the packet delay of the uplink non-GBR traffic of a UE, as defined in ETSI TS 136 314 [i.11].  # noqa: E501

        :param ul_nongbr_delay_ue: The ul_nongbr_delay_ue of this L2MeasCellUEInfo.
        :type ul_nongbr_delay_ue: int
        """

        self._ul_nongbr_delay_ue = ul_nongbr_delay_ue

    @property
    def ul_nongbr_pdr_ue(self) -> int:
        """Gets the ul_nongbr_pdr_ue of this L2MeasCellUEInfo.

        It indicates the packet discard rate in percentage of the uplink nonGBR traffic of a UE, as defined in ETSI TS 136 314 [i.11].  # noqa: E501

        :return: The ul_nongbr_pdr_ue of this L2MeasCellUEInfo.
        :rtype: int
        """
        return self._ul_nongbr_pdr_ue

    @ul_nongbr_pdr_ue.setter
    def ul_nongbr_pdr_ue(self, ul_nongbr_pdr_ue: int):
        """Sets the ul_nongbr_pdr_ue of this L2MeasCellUEInfo.

        It indicates the packet discard rate in percentage of the uplink nonGBR traffic of a UE, as defined in ETSI TS 136 314 [i.11].  # noqa: E501

        :param ul_nongbr_pdr_ue: The ul_nongbr_pdr_ue of this L2MeasCellUEInfo.
        :type ul_nongbr_pdr_ue: int
        """

        self._ul_nongbr_pdr_ue = ul_nongbr_pdr_ue

    @property
    def ul_nongbr_throughput_ue(self) -> int:
        """Gets the ul_nongbr_throughput_ue of this L2MeasCellUEInfo.

        It indicates the scheduled throughput of the uplink non-GBR traffic of a UE, as defined in ETSI TS 136 314 [i.11].  # noqa: E501

        :return: The ul_nongbr_throughput_ue of this L2MeasCellUEInfo.
        :rtype: int
        """
        return self._ul_nongbr_throughput_ue

    @ul_nongbr_throughput_ue.setter
    def ul_nongbr_throughput_ue(self, ul_nongbr_throughput_ue: int):
        """Sets the ul_nongbr_throughput_ue of this L2MeasCellUEInfo.

        It indicates the scheduled throughput of the uplink non-GBR traffic of a UE, as defined in ETSI TS 136 314 [i.11].  # noqa: E501

        :param ul_nongbr_throughput_ue: The ul_nongbr_throughput_ue of this L2MeasCellUEInfo.
        :type ul_nongbr_throughput_ue: int
        """

        self._ul_nongbr_throughput_ue = ul_nongbr_throughput_ue
