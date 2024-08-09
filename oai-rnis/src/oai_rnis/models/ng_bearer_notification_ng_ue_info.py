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
from oai_rnis.models.cell_change_notification_temp_ue_id import CellChangeNotificationTempUeId  # noqa: F401,E501
from oai_rnis.models.ecgi import Ecgi  # noqa: F401,E501
from oai_rnis.models.ng_bearer_info_ng_bearer_info_detailed import NGBearerInfoNgBearerInfoDetailed  # noqa: F401,E501
from oai_rnis.utils import util


class NGBearerNotificationNgUeInfo(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, associate_id: List[AssociateId]=None, ecgi: List[Ecgi]=None, ng_bearer_info: List[NGBearerInfoNgBearerInfoDetailed]=None, temp_ue_id: CellChangeNotificationTempUeId=None):  # noqa: E501
        """NGBearerNotificationNgUeInfo - a model defined in Swagger

        :param associate_id: The associate_id of this NGBearerNotificationNgUeInfo.  # noqa: E501
        :type associate_id: List[AssociateId]
        :param ecgi: The ecgi of this NGBearerNotificationNgUeInfo.  # noqa: E501
        :type ecgi: List[Ecgi]
        :param ng_bearer_info: The ng_bearer_info of this NGBearerNotificationNgUeInfo.  # noqa: E501
        :type ng_bearer_info: List[NGBearerInfoNgBearerInfoDetailed]
        :param temp_ue_id: The temp_ue_id of this NGBearerNotificationNgUeInfo.  # noqa: E501
        :type temp_ue_id: CellChangeNotificationTempUeId
        """
        self.swagger_types = {
            'associate_id': List[AssociateId],
            'ecgi': List[Ecgi],
            'ng_bearer_info': List[NGBearerInfoNgBearerInfoDetailed],
            'temp_ue_id': CellChangeNotificationTempUeId
        }

        self.attribute_map = {
            'associate_id': 'associateId',
            'ecgi': 'ecgi',
            'ng_bearer_info': 'ngBearerInfo',
            'temp_ue_id': 'tempUeId'
        }
        self._associate_id = associate_id
        self._ecgi = ecgi
        self._ng_bearer_info = ng_bearer_info
        self._temp_ue_id = temp_ue_id

    @classmethod
    def from_dict(cls, dikt) -> 'NGBearerNotificationNgUeInfo':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The NGBearerNotification_ngUeInfo of this NGBearerNotificationNgUeInfo.  # noqa: E501
        :rtype: NGBearerNotificationNgUeInfo
        """
        return util.deserialize_model(dikt, cls)

    @property
    def associate_id(self) -> List[AssociateId]:
        """Gets the associate_id of this NGBearerNotificationNgUeInfo.

        0 to N identifiers to associate the information for a specific UE or flow.  # noqa: E501

        :return: The associate_id of this NGBearerNotificationNgUeInfo.
        :rtype: List[AssociateId]
        """
        return self._associate_id

    @associate_id.setter
    def associate_id(self, associate_id: List[AssociateId]):
        """Sets the associate_id of this NGBearerNotificationNgUeInfo.

        0 to N identifiers to associate the information for a specific UE or flow.  # noqa: E501

        :param associate_id: The associate_id of this NGBearerNotificationNgUeInfo.
        :type associate_id: List[AssociateId]
        """

        self._associate_id = associate_id

    @property
    def ecgi(self) -> List[Ecgi]:
        """Gets the ecgi of this NGBearerNotificationNgUeInfo.

        E-UTRAN Cell Global Identifier.  # noqa: E501

        :return: The ecgi of this NGBearerNotificationNgUeInfo.
        :rtype: List[Ecgi]
        """
        return self._ecgi

    @ecgi.setter
    def ecgi(self, ecgi: List[Ecgi]):
        """Sets the ecgi of this NGBearerNotificationNgUeInfo.

        E-UTRAN Cell Global Identifier.  # noqa: E501

        :param ecgi: The ecgi of this NGBearerNotificationNgUeInfo.
        :type ecgi: List[Ecgi]
        """
        if ecgi is None:
            raise ValueError("Invalid value for `ecgi`, must not be `None`")  # noqa: E501

        self._ecgi = ecgi

    @property
    def ng_bearer_info(self) -> List[NGBearerInfoNgBearerInfoDetailed]:
        """Gets the ng_bearer_info of this NGBearerNotificationNgUeInfo.

        NG bearer information as defined below.  # noqa: E501

        :return: The ng_bearer_info of this NGBearerNotificationNgUeInfo.
        :rtype: List[NGBearerInfoNgBearerInfoDetailed]
        """
        return self._ng_bearer_info

    @ng_bearer_info.setter
    def ng_bearer_info(self, ng_bearer_info: List[NGBearerInfoNgBearerInfoDetailed]):
        """Sets the ng_bearer_info of this NGBearerNotificationNgUeInfo.

        NG bearer information as defined below.  # noqa: E501

        :param ng_bearer_info: The ng_bearer_info of this NGBearerNotificationNgUeInfo.
        :type ng_bearer_info: List[NGBearerInfoNgBearerInfoDetailed]
        """
        if ng_bearer_info is None:
            raise ValueError("Invalid value for `ng_bearer_info`, must not be `None`")  # noqa: E501

        self._ng_bearer_info = ng_bearer_info

    @property
    def temp_ue_id(self) -> CellChangeNotificationTempUeId:
        """Gets the temp_ue_id of this NGBearerNotificationNgUeInfo.


        :return: The temp_ue_id of this NGBearerNotificationNgUeInfo.
        :rtype: CellChangeNotificationTempUeId
        """
        return self._temp_ue_id

    @temp_ue_id.setter
    def temp_ue_id(self, temp_ue_id: CellChangeNotificationTempUeId):
        """Sets the temp_ue_id of this NGBearerNotificationNgUeInfo.


        :param temp_ue_id: The temp_ue_id of this NGBearerNotificationNgUeInfo.
        :type temp_ue_id: CellChangeNotificationTempUeId
        """

        self._temp_ue_id = temp_ue_id
