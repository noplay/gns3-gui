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

import os
import copy

from .image import Image


class RegistryError(Exception):
    pass


class Registry:
    def __init__(self, images_dir):
        self._images_dir = images_dir

    def list_images(self):
        """
        List image on user computer
        """
        images = []

        directory = os.path.join(self._images_dir, "QEMU")
        if os.path.exists(directory):
            for filename in os.listdir(directory):
                if not filename.endswith(".md5sum") and not filename.startswith("."):
                    path = os.path.join(directory, filename)
                    if os.path.isfile(path):
                        images.append(Image(path))
        return images

    def search_image_file(self, md5sum):
        """
        Search an image based on its MD5 checksum

        :param md5sum: Hash of the image
        :returns: Image object or None
        """

        directory = os.path.join(self._images_dir, "QEMU")
        if os.path.exists(directory):
            for filename in os.listdir(directory):
                if not filename.endswith(".md5sum") and not filename.startswith("."):
                    path = os.path.join(directory, filename)
                    if os.path.isfile(path):
                        image = Image(path)
                        if image.md5sum == md5sum:
                            return image.path
        return None

    def search_images_for_version(self, appliance, version_name):
        """
        Search on disk the images required by this version.
        And keep only the require images in the images fields. Add to the images
        their disk type and path.

        :param appliance: Dictionary with appliance configuration
        :param version_name: Version name
        :returns: Appliance configuration
        """

        found = False
        for version in appliance["versions"]:
            if version["name"] == version_name:
                appliance["name"] = "{} {}".format(appliance["name"], version["name"])
                appliance["images"] = []
                for image_type, image in version["images"].items():
                    image["type"] = image_type
                    image["path"] = self.search_image_file(image["md5sum"])
                    if image["path"] is None:
                        raise RegistryError("File {} with checksum {} not found for {}".format(image["filename"], image["md5sum"], appliance["name"]))

                    appliance["images"].append(image)
                    found = True
                break

        if not found:
            raise RegistryError("Version {} not found for {}".format(version_name, appliance["name"]))

        return appliance

    def list_installable_versions(self, appliance):
        """
        Search on disk the version available for this appliance

        :param appliance: Dictionary with appliance configuration
        :returns: Array of version name available
        """

        installable = []
        self._check_config(appliance)
        for version in appliance["versions"]:
            try:
                self.search_images_for_version(appliance, version["name"])
            except RegistryError:
                continue
            installable.append(version["name"])
        return installable
