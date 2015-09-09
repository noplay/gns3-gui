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


import pytest
import json

from gns3.registry.appliance import Appliance, ApplianceError


def test_check_config(tmpdir):

    test_path = str(tmpdir / "test.json")

    with open(test_path, "w+") as f:
        f.write("")

    with pytest.raises(ApplianceError):
        Appliance("jkhj")

    with pytest.raises(ApplianceError):
        Appliance(test_path)

    with open(test_path, "w+") as f:
        f.write("{}")

    with pytest.raises(ApplianceError):
        Appliance(test_path)

    Appliance("tests/registry/appliances/microcore-linux.json")


def test_resolve_version(tmpdir):

    with open("tests/registry/appliances/microcore-linux.json") as f:
        config = json.load(f)

    new_config = Appliance("tests/registry/appliances/microcore-linux.json")
    assert new_config["versions"][0]["images"] == {"hda_disk_image": config["images"][0]}


