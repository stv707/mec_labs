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
from oai_rnis.models.ecgi import Ecgi  # noqa: F401,E501
from oai_rnis.utils import util


class CaReconfNotificationSecondaryCellAdd(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, ecgi: Ecgi=None):  # noqa: E501
        """CaReconfNotificationSecondaryCellAdd - a model defined in Swagger

        :param ecgi: The ecgi of this CaReconfNotificationSecondaryCellAdd.  # noqa: E501
        :type ecgi: Ecgi
        """
        self.swagger_types = {
            'ecgi': Ecgi
        }

        self.attribute_map = {
            'ecgi': 'ecgi'
        }
        self._ecgi = ecgi

    @classmethod
    def from_dict(cls, dikt) -> 'CaReconfNotificationSecondaryCellAdd':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The CaReconfNotification_secondaryCellAdd of this CaReconfNotificationSecondaryCellAdd.  # noqa: E501
        :rtype: CaReconfNotificationSecondaryCellAdd
        """
        return util.deserialize_model(dikt, cls)

    @property
    def ecgi(self) -> Ecgi:
        """Gets the ecgi of this CaReconfNotificationSecondaryCellAdd.


        :return: The ecgi of this CaReconfNotificationSecondaryCellAdd.
        :rtype: Ecgi
        """
        return self._ecgi

    @ecgi.setter
    def ecgi(self, ecgi: Ecgi):
        """Sets the ecgi of this CaReconfNotificationSecondaryCellAdd.


        :param ecgi: The ecgi of this CaReconfNotificationSecondaryCellAdd.
        :type ecgi: Ecgi
        """

        self._ecgi = ecgi
