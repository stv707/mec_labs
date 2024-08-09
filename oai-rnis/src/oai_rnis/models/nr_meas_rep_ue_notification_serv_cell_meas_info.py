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
from oai_rnis.models.n_rcgi import NRcgi  # noqa: F401,E501
from oai_rnis.models.nr_meas_rep_ue_notification_n_cell import NrMeasRepUeNotificationNCell  # noqa: F401,E501
from oai_rnis.models.nr_meas_rep_ue_notification_s_cell import NrMeasRepUeNotificationSCell  # noqa: F401,E501
from oai_rnis.utils import util


class NrMeasRepUeNotificationServCellMeasInfo(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, n_cell: NrMeasRepUeNotificationNCell=None, nrcgi: NRcgi=None, s_cell: NrMeasRepUeNotificationSCell=None):  # noqa: E501
        """NrMeasRepUeNotificationServCellMeasInfo - a model defined in Swagger

        :param n_cell: The n_cell of this NrMeasRepUeNotificationServCellMeasInfo.  # noqa: E501
        :type n_cell: NrMeasRepUeNotificationNCell
        :param nrcgi: The nrcgi of this NrMeasRepUeNotificationServCellMeasInfo.  # noqa: E501
        :type nrcgi: NRcgi
        :param s_cell: The s_cell of this NrMeasRepUeNotificationServCellMeasInfo.  # noqa: E501
        :type s_cell: NrMeasRepUeNotificationSCell
        """
        self.swagger_types = {
            'n_cell': NrMeasRepUeNotificationNCell,
            'nrcgi': NRcgi,
            's_cell': NrMeasRepUeNotificationSCell
        }

        self.attribute_map = {
            'n_cell': 'nCell',
            'nrcgi': 'nrcgi',
            's_cell': 'sCell'
        }
        self._n_cell = n_cell
        self._nrcgi = nrcgi
        self._s_cell = s_cell

    @classmethod
    def from_dict(cls, dikt) -> 'NrMeasRepUeNotificationServCellMeasInfo':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The NrMeasRepUeNotification_servCellMeasInfo of this NrMeasRepUeNotificationServCellMeasInfo.  # noqa: E501
        :rtype: NrMeasRepUeNotificationServCellMeasInfo
        """
        return util.deserialize_model(dikt, cls)

    @property
    def n_cell(self) -> NrMeasRepUeNotificationNCell:
        """Gets the n_cell of this NrMeasRepUeNotificationServCellMeasInfo.


        :return: The n_cell of this NrMeasRepUeNotificationServCellMeasInfo.
        :rtype: NrMeasRepUeNotificationNCell
        """
        return self._n_cell

    @n_cell.setter
    def n_cell(self, n_cell: NrMeasRepUeNotificationNCell):
        """Sets the n_cell of this NrMeasRepUeNotificationServCellMeasInfo.


        :param n_cell: The n_cell of this NrMeasRepUeNotificationServCellMeasInfo.
        :type n_cell: NrMeasRepUeNotificationNCell
        """

        self._n_cell = n_cell

    @property
    def nrcgi(self) -> NRcgi:
        """Gets the nrcgi of this NrMeasRepUeNotificationServCellMeasInfo.


        :return: The nrcgi of this NrMeasRepUeNotificationServCellMeasInfo.
        :rtype: NRcgi
        """
        return self._nrcgi

    @nrcgi.setter
    def nrcgi(self, nrcgi: NRcgi):
        """Sets the nrcgi of this NrMeasRepUeNotificationServCellMeasInfo.


        :param nrcgi: The nrcgi of this NrMeasRepUeNotificationServCellMeasInfo.
        :type nrcgi: NRcgi
        """

        self._nrcgi = nrcgi

    @property
    def s_cell(self) -> NrMeasRepUeNotificationSCell:
        """Gets the s_cell of this NrMeasRepUeNotificationServCellMeasInfo.


        :return: The s_cell of this NrMeasRepUeNotificationServCellMeasInfo.
        :rtype: NrMeasRepUeNotificationSCell
        """
        return self._s_cell

    @s_cell.setter
    def s_cell(self, s_cell: NrMeasRepUeNotificationSCell):
        """Sets the s_cell of this NrMeasRepUeNotificationServCellMeasInfo.


        :param s_cell: The s_cell of this NrMeasRepUeNotificationServCellMeasInfo.
        :type s_cell: NrMeasRepUeNotificationSCell
        """

        self._s_cell = s_cell
