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


import jinja2

from .utils.get_resource import get_resource
from .qt import QtCore, QtWidgets, QtWebKit, QtWebKitWidgets, QtGui
from .ui.appliance_window_ui import Ui_ApplianceWindow
from .registry.appliance import Appliance

import logging
log = logging.getLogger(__name__)


def human_filesize(num):
    for unit in ['B','KB','MB','GB']:
        if abs(num) < 1024.0:
            return "%3.1f%s" % (num, unit)
        num /= 1024.0
    return "%.1f%s" % (num, 'TB')


class ApplianceWindow(QtWidgets.QWidget, Ui_ApplianceWindow):

    def __init__(self, path, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowTitle(path)

        # Call linkClickedSlot() for all non local links
        self.uiWebView.page().setLinkDelegationPolicy(QtWebKitWidgets.QWebPage.DelegateExternalLinks)
        self.uiWebView.linkClicked.connect(self._linkClickedSlot)


        renderer = jinja2.Environment(loader=jinja2.FileSystemLoader(get_resource('templates')))
        renderer.filters['nl2br'] = lambda s: s.replace('\n', '<br />')
        renderer.filters['human_filesize'] = human_filesize
        template = renderer.get_template("appliance.html")
        #TODO: Catch error
        appliance = Appliance(path)
        self.uiWebView.setHtml(template.render(appliance=appliance))
        self.show()

    def _linkClickedSlot(self, url):
        """
        Open in a new browser other url
        """
        QtGui.QDesktopServices.openUrl(url)
