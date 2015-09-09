#!/usr/bin/env python
#
# Copyright (C) 2015 GNS3 Technologies Inc.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


import json
import copy
import collections


class ApplianceError(Exception):
    pass


class Appliance(collections.Mapping):
    def __init__(self, path):

        try:
            with open(path) as f:
                self._appliance = json.load(f)
        except (OSError, ValueError) as e:
            raise ApplianceError("Could not read appliance {}: {}".format(path, str(e)))
        self._check_config()
        self._resolve_version()

    def _check_config(self):
        """
        :param appliance: Sanity check on the appliance configuration
        """
        if "registry_version" not in self._appliance:
            raise ApplianceError("Invalid appliance configuration please report the issue on https://github.com/GNS3/gns3-registry")
        if self._appliance["registry_version"] != 1:
            raise ApplianceError("Please update GNS3 marketplace in order to install this appliance")

    def __getitem__(self, key):
        return self._appliance.__getitem__(key)

    def __iter__(self):
        return self._appliance.__iter__()

    def __len__(self):
        return self._appliance.__len__()

    def _resolve_version(self):
        """
        Replace image field in versions by their the complete information from images
        """

        for version in self._appliance["versions"]:
            for image_type, filename in version["images"].items():
                for file in self._appliance["images"]:
                    if file["filename"] == filename:
                        version["images"][image_type] = copy.copy(file)


