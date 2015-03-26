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

from .servers import Servers
from .local_config import LocalConfig
from .modules.module_error import ModuleError
import subprocess

import logging
log = logging.getLogger(__name__)


class Appliance:

    """Manage GNS3 appliance"""

    def autostart(self):
        """Auto start the GNS 3 appliance if required"""
        if self.settings()["auto_start"] == True:
            log.info("Start GNS3 Appliance")
            try:
                subprocess.check_output([self.vboxManage(), "startvm", "gns3"], stderr=subprocess.STDOUT)
            except (OSError, subprocess.SubprocessError) as e:
                msg = "Could not start appliance: {}\n{}".format(e, e.output.decode("utf-8"))
                log.warning(msg)
                print(msg)

    def autostart(self):
        """Auto stop the GNS 3 appliance if required"""
        if self.settings()["auto_start"] == True:
            log.info("Stop GNS3 Appliance")
            try:
                subprocess.check_output([self.vboxManage(), "stopvm", "gns3"], stderr=subprocess.STDOUT)
            except (OSError, subprocess.SubprocessError) as e:
                msg = "Could not stop appliance: {}\n{}".format(e, e.output.decode("utf-8"))
                log.warning(msg)
                print(msg)

    def settings(self):
        """Get appliance settings"""
        return Servers.instance().applianceSettings()

    def vboxManage(self):
        local_config = LocalConfig.instance()
        settings = local_config.loadSectionSettings("VirtualBox", {})

        vboxmanage_path = settings["vboxmanage_path"]
        if vboxmanage_path == "":
            raise ModuleError("VBoxManage path is not configured")
        return vboxmanage_path

    @staticmethod
    def instance():
        """
        Singleton to return only on instance of Appliance.

        :returns: instance of Appliance
        """

        if not hasattr(Appliance, "_instance"):
            Appliance._instance = Appliance()
        return Appliance._instance
