#!/usr/bin/env python
# -*- coding: utf-8 -*-
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
import os


from gns3.registry.registry import Registry, RegistryError


def test_resolve_version(tmpdir):

    with open("tests/registry/appliances/microcore-linux.json") as f:
        config = json.load(f)

    registry = Registry(str(tmpdir))
    new_config = registry._resolve_version(config)
    assert new_config["versions"][0]["images"] == {"hda_disk_image": config["images"][0]}


def test_search_images_for_version(linux_microcore_img, images_dir):

    with open("tests/registry/appliances/microcore-linux.json") as f:
        config = json.load(f)

    registry = Registry(images_dir)
    detected = registry.search_images_for_version(config, "3.4.1")
    assert detected["name"] == "Micro Core Linux 3.4.1"
    assert detected["images"][0]["type"] == "hda_disk_image"
    assert detected["images"][0]["path"] == linux_microcore_img


def test_list_installable_versions(linux_microcore_img, images_dir):

    with open("tests/registry/appliances/microcore-linux.json") as f:
        config = json.load(f)

    registry = Registry(images_dir)
    assert registry.list_installable_versions(config) == ["3.4.1"]


def test_search_images_for_version_unknow_version(linux_microcore_img, images_dir):

    with open("tests/registry/appliances/microcore-linux.json") as f:
        config = json.load(f)

    registry = Registry(images_dir)
    with pytest.raises(RegistryError):
        detected = registry.search_images_for_version(config, "42")



def test_search_images_for_version_invalid_registry(linux_microcore_img, images_dir):

    with open("tests/registry/appliances/microcore-linux.json") as f:
        config = json.load(f)
        config["registry_version"] = 2

    registry = Registry(images_dir)
    with pytest.raises(RegistryError):
        detected = registry.search_images_for_version(config, "3.4.1")


def test_search_images_for_version_missing_file(images_dir):

    with open("tests/registry/appliances/microcore-linux.json") as f:
        config = json.load(f)

    registry = Registry(images_dir)
    with pytest.raises(RegistryError):
        detected = registry.search_images_for_version(config, "4.0.2")


def test_search_image_file(tmpdir):

    os.makedirs(str(tmpdir / "QEMU"))
    with open(str(tmpdir / "QEMU" / "a"), "w+") as f:
        f.write("ALPHA")
    with open(str(tmpdir / "QEMU" / "b"), "w+") as f:
        f.write("BETA")

    registry = Registry(str(tmpdir))
    image = registry.search_image_file("36b84f8e3fba5bf993e3ba352d62d146")
    assert image == str(tmpdir / "QEMU" / "b")

    assert registry.search_image_file("00000000000000000000000000000000") is None


def test_list_images(tmpdir):
    os.makedirs(str(tmpdir / "QEMU"))
    with open(str(tmpdir / "QEMU" / ".DS_Store"), "w+") as f:
        f.write("garbage")
    with open(str(tmpdir / "QEMU" / "a"), "w+") as f:
        f.write("ALPHA")
    with open(str(tmpdir / "QEMU" / "a.md5sum"), "w+") as f:
        f.write("e13d0d1c0b3999ae2386bba70417930c")
    with open(str(tmpdir / "QEMU" / "b"), "w+") as f:
        f.write("BETA")


    registry = Registry(str(tmpdir))
    images = registry.list_images()
    assert len(images) == 2

