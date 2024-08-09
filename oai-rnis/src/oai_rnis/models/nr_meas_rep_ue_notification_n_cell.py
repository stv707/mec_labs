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
from oai_rnis.models.meas_quantity_results_nr import MeasQuantityResultsNr  # noqa: F401,E501
from oai_rnis.models.rs_index_results import RsIndexResults  # noqa: F401,E501
from oai_rnis.utils import util


class NrMeasRepUeNotificationNCell(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, meas_quantity_results_csi_rs_cell: MeasQuantityResultsNr=None, meas_quantity_results_ssb_cell: MeasQuantityResultsNr=None, rs_index_results: RsIndexResults=None):  # noqa: E501
        """NrMeasRepUeNotificationNCell - a model defined in Swagger

        :param meas_quantity_results_csi_rs_cell: The meas_quantity_results_csi_rs_cell of this NrMeasRepUeNotificationNCell.  # noqa: E501
        :type meas_quantity_results_csi_rs_cell: MeasQuantityResultsNr
        :param meas_quantity_results_ssb_cell: The meas_quantity_results_ssb_cell of this NrMeasRepUeNotificationNCell.  # noqa: E501
        :type meas_quantity_results_ssb_cell: MeasQuantityResultsNr
        :param rs_index_results: The rs_index_results of this NrMeasRepUeNotificationNCell.  # noqa: E501
        :type rs_index_results: RsIndexResults
        """
        self.swagger_types = {
            'meas_quantity_results_csi_rs_cell': MeasQuantityResultsNr,
            'meas_quantity_results_ssb_cell': MeasQuantityResultsNr,
            'rs_index_results': RsIndexResults
        }

        self.attribute_map = {
            'meas_quantity_results_csi_rs_cell': 'measQuantityResultsCsiRsCell',
            'meas_quantity_results_ssb_cell': 'measQuantityResultsSsbCell',
            'rs_index_results': 'rsIndexResults'
        }
        self._meas_quantity_results_csi_rs_cell = meas_quantity_results_csi_rs_cell
        self._meas_quantity_results_ssb_cell = meas_quantity_results_ssb_cell
        self._rs_index_results = rs_index_results

    @classmethod
    def from_dict(cls, dikt) -> 'NrMeasRepUeNotificationNCell':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The NrMeasRepUeNotification_nCell of this NrMeasRepUeNotificationNCell.  # noqa: E501
        :rtype: NrMeasRepUeNotificationNCell
        """
        return util.deserialize_model(dikt, cls)

    @property
    def meas_quantity_results_csi_rs_cell(self) -> MeasQuantityResultsNr:
        """Gets the meas_quantity_results_csi_rs_cell of this NrMeasRepUeNotificationNCell.


        :return: The meas_quantity_results_csi_rs_cell of this NrMeasRepUeNotificationNCell.
        :rtype: MeasQuantityResultsNr
        """
        return self._meas_quantity_results_csi_rs_cell

    @meas_quantity_results_csi_rs_cell.setter
    def meas_quantity_results_csi_rs_cell(self, meas_quantity_results_csi_rs_cell: MeasQuantityResultsNr):
        """Sets the meas_quantity_results_csi_rs_cell of this NrMeasRepUeNotificationNCell.


        :param meas_quantity_results_csi_rs_cell: The meas_quantity_results_csi_rs_cell of this NrMeasRepUeNotificationNCell.
        :type meas_quantity_results_csi_rs_cell: MeasQuantityResultsNr
        """

        self._meas_quantity_results_csi_rs_cell = meas_quantity_results_csi_rs_cell

    @property
    def meas_quantity_results_ssb_cell(self) -> MeasQuantityResultsNr:
        """Gets the meas_quantity_results_ssb_cell of this NrMeasRepUeNotificationNCell.


        :return: The meas_quantity_results_ssb_cell of this NrMeasRepUeNotificationNCell.
        :rtype: MeasQuantityResultsNr
        """
        return self._meas_quantity_results_ssb_cell

    @meas_quantity_results_ssb_cell.setter
    def meas_quantity_results_ssb_cell(self, meas_quantity_results_ssb_cell: MeasQuantityResultsNr):
        """Sets the meas_quantity_results_ssb_cell of this NrMeasRepUeNotificationNCell.


        :param meas_quantity_results_ssb_cell: The meas_quantity_results_ssb_cell of this NrMeasRepUeNotificationNCell.
        :type meas_quantity_results_ssb_cell: MeasQuantityResultsNr
        """

        self._meas_quantity_results_ssb_cell = meas_quantity_results_ssb_cell

    @property
    def rs_index_results(self) -> RsIndexResults:
        """Gets the rs_index_results of this NrMeasRepUeNotificationNCell.


        :return: The rs_index_results of this NrMeasRepUeNotificationNCell.
        :rtype: RsIndexResults
        """
        return self._rs_index_results

    @rs_index_results.setter
    def rs_index_results(self, rs_index_results: RsIndexResults):
        """Sets the rs_index_results of this NrMeasRepUeNotificationNCell.


        :param rs_index_results: The rs_index_results of this NrMeasRepUeNotificationNCell.
        :type rs_index_results: RsIndexResults
        """

        self._rs_index_results = rs_index_results
