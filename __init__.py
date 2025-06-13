from .connmanager import ConnManagerPlugin

def classFactory(iface):
    return ConnManagerPlugin(iface)
