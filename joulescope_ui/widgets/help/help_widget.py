# Copyright 2023 Jetperch LLC
#
# Licensed under the Apache License, Version 2.0 (the 'License');
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an 'AS IS' BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from PySide6 import QtWidgets
from joulescope_ui import register
from joulescope_ui.help_ui import format_help


_TALK = """\
<html>
<head>
{style}
</head>
<body>

<p><a href="https://forum.joulescope.com/">Visit forum</a> ⭐</p>

<p><a href="">Joulescope source code:</a></p>
<ul>
<li><a href="https://github.com/jetperch/pyjoulescope_ui">UI</a></li>
<li><a href="https://github.com/jetperch/joulescope_driver">driver</a></li>
<li><a href="https://github.com/jetperch/jls">JLS</a> (file format)</li>
<li><a href="https://github.com/jetperch/pyjoulescope_examples">Python scripting examples</a></li>
</ul>

<p><a href="https://www.joulescope.com/pages/contact">Contact support</a></p>
</body>
"""


@register
class HelpWidget(QtWidgets.QWidget):
    CAPABILITIES = []

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setObjectName('talk_widget')
        self.setSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        self._layout = QtWidgets.QVBoxLayout()
        self._layout.setContentsMargins(0, 0, 0, 0)
        self._layout.setSpacing(0)
        self.setLayout(self._layout)

        _, html = format_help('Help', _TALK)
        self._label = QtWidgets.QLabel(html, self)
        self._label.setWordWrap(True)
        self._label.setOpenExternalLinks(True)
        self._layout.addWidget(self._label)

        self._spacer = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self._layout.addItem(self._spacer)