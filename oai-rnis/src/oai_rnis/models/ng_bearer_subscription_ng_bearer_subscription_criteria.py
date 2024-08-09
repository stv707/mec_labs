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
from oai_rnis.models.associate_id import AssociateId  # noqa: F401,E501
from oai_rnis.models.ecgi import Ecgi  # noqa: F401,E501
from oai_rnis.utils import util


class NGBearerSubscriptionNGBearerSubscriptionCriteria(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, associate_id: List[AssociateId]=None, ecgi: List[Ecgi]=None, erab_id: List[int]=None):  # noqa: E501
        """NGBearerSubscriptionNGBearerSubscriptionCriteria - a model defined in Swagger

        :param associate_id: The associate_id of this NGBearerSubscriptionNGBearerSubscriptionCriteria.  # noqa: E501
        :type associate_id: List[AssociateId]
        :param ecgi: The ecgi of this NGBearerSubscriptionNGBearerSubscriptionCriteria.  # noqa: E501
        :type ecgi: List[Ecgi]
        :param erab_id: The erab_id of this NGBearerSubscriptionNGBearerSubscriptionCriteria.  # noqa: E501
        :type erab_id: List[int]
        """
        self.swagger_types = {
            'associate_id': List[AssociateId],
            'ecgi': List[Ecgi],
            'erab_id': List[int]
        }

        self.attribute_map = {
            'associate_id': 'associateId',
            'ecgi': 'ecgi',
            'erab_id': 'erabId'
        }
        self._associate_id = associate_id
        self._ecgi = ecgi
        self._erab_id = erab_id

    @classmethod
    def from_dict(cls, dikt) -> 'NGBearerSubscriptionNGBearerSubscriptionCriteria':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The NGBearerSubscription_NGBearerSubscriptionCriteria of this NGBearerSubscriptionNGBearerSubscriptionCriteria.  # noqa: E501
        :rtype: NGBearerSubscriptionNGBearerSubscriptionCriteria
        """
        return util.deserialize_model(dikt, cls)

    @property
    def associate_id(self) -> List[AssociateId]:
        """Gets the associate_id of this NGBearerSubscriptionNGBearerSubscriptionCriteria.

        0 to N identifiers to associate the events for a specific UE or a flow.  # noqa: E501

        :return: The associate_id of this NGBearerSubscriptionNGBearerSubscriptionCriteria.
        :rtype: List[AssociateId]
        """
        return self._associate_id

    @associate_id.setter
    def associate_id(self, associate_id: List[AssociateId]):
        """Sets the associate_id of this NGBearerSubscriptionNGBearerSubscriptionCriteria.

        0 to N identifiers to associate the events for a specific UE or a flow.  # noqa: E501

        :param associate_id: The associate_id of this NGBearerSubscriptionNGBearerSubscriptionCriteria.
        :type associate_id: List[AssociateId]
        """

        self._associate_id = associate_id

    @property
    def ecgi(self) -> List[Ecgi]:
        """Gets the ecgi of this NGBearerSubscriptionNGBearerSubscriptionCriteria.

        E-UTRAN Cell Global Identifier.  # noqa: E501

        :return: The ecgi of this NGBearerSubscriptionNGBearerSubscriptionCriteria.
        :rtype: List[Ecgi]
        """
        return self._ecgi

    @ecgi.setter
    def ecgi(self, ecgi: List[Ecgi]):
        """Sets the ecgi of this NGBearerSubscriptionNGBearerSubscriptionCriteria.

        E-UTRAN Cell Global Identifier.  # noqa: E501

        :param ecgi: The ecgi of this NGBearerSubscriptionNGBearerSubscriptionCriteria.
        :type ecgi: List[Ecgi]
        """

        self._ecgi = ecgi

    @property
    def erab_id(self) -> List[int]:
        """Gets the erab_id of this NGBearerSubscriptionNGBearerSubscriptionCriteria.

        The attribute that uniquely identifies a NG bearer for a specific UE, as defined in ETSI TS 136 413 [i.3].  # noqa: E501

        :return: The erab_id of this NGBearerSubscriptionNGBearerSubscriptionCriteria.
        :rtype: List[int]
        """
        return self._erab_id

    @erab_id.setter
    def erab_id(self, erab_id: List[int]):
        """Sets the erab_id of this NGBearerSubscriptionNGBearerSubscriptionCriteria.

        The attribute that uniquely identifies a NG bearer for a specific UE, as defined in ETSI TS 136 413 [i.3].  # noqa: E501

        :param erab_id: The erab_id of this NGBearerSubscriptionNGBearerSubscriptionCriteria.
        :type erab_id: List[int]
        """

        self._erab_id = erab_id
