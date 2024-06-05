# coding=utf-8
"""DockWidget test.

.. note:: This program is free software; you can redistribute it and/or modify
     it under the terms of the GNU General Public License as published by
     the Free Software Foundation; either version 2 of the License, or
     (at your option) any later version.

"""

__author__ = 'kwundram@uni-muenster.de'
__date__ = '2024-06-05'
__copyright__ = 'Copyright 2024, Kjell Wundram'

import unittest

from qgis.PyQt.QtGui import QDockWidget

from exercise_8_1_dockwidget import MuensterCityDistrictTools.DockWidget

from utilities import get_qgis_app

QGIS_APP = get_qgis_app()


class MuensterCityDistrictTools.DockWidgetTest(unittest.TestCase):
    """Test dockwidget works."""

    def setUp(self):
        """Runs before each test."""
        self.dockwidget = MuensterCityDistrictTools.DockWidget(None)

    def tearDown(self):
        """Runs after each test."""
        self.dockwidget = None

    def test_dockwidget_ok(self):
        """Test we can click OK."""
        pass

if __name__ == "__main__":
    suite = unittest.makeSuite(MuensterCityDistrictTools.DialogTest)
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)

