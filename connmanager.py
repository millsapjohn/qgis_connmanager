import os
try:
    from qgis.PyQt.QtWidgets import QAction
except ImportError:
    from qgis.PyQt.QtGui import QAction
from qgis.PyQt.QtGui import QIcon
from qgis.core import QgsProject

conn_icon = QIcon(':/images/themes/default/mIconConnect.svg')
gpkg_icon = QIcon(':/images/themes/default/mGeoPackage.svg')
sptlt_icon = QIcon(':/images/themes/default/mIconSpatialite.svg')
pg_icon = QIcon(':/images/themes/default/mIconPostgis.svg')
stac_icon = QIcon(':/images/themes/default/mIconStac.svg')
wms_icon = QIcon(':/images/themes/default/mIconWms.svg')
cloud_icon = QIcon(':/images/themes/default/mIconCloud.svg')
vtile_icon = QIcon(':/images/themes/default/mIconVectorTileLayer.svg')
wcs_icon = QIcon(':/images/themes/default/mIconWcs.svg')
wfs_icon = QIcon(':/images/themes/default/mIconWfs.svg')
rest_icon = QIcon(':/images/icons/qbrowser_icon.svg')
bkmk_icon = QIcon(':/images/themes/default/mActionShowBookmarks.svg')


class ConnManagerPlugin:
    def __init__(self, iface):
        self.iface = iface

    def initGui(self):
        self.globalAction = QAction(conn_icon, "Manage Global Connections")
        self.iface.addPluginToMenu("Manage Connections", self.globalAction)
        self.globalAction.triggered.connect(self.globalManager)

        self.projectAction = QAction(conn_icon, "Manage Project Connections")
        self.iface.addPluginToMenu("Manage Connections", self.projectAction)
        self.projectAction.triggered.connect(self.projectManager)

    def unload(self):
        self.iface.removePluginMenu("Manage Connections", self.globalAction)
        self.iface.removePluginMenu("Manage Connections", self.projectAction)
        self.globalAction.deleteLater()
        self.projectAction.deleteLater()

    def globalManager(self):
        pass

    def projectManager(self):
        pass
