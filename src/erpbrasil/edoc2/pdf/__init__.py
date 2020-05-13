__version__ = '0.0.0'

from lxml import objectify, etree

lookup = etree.ElementNamespaceClassLookup(
    objectify.ObjectifyElementClassLookup())
parser = etree.XMLParser()
parser.set_element_class_lookup(lookup)

from erpbrasil.edoc2.pdf import nfe
from erpbrasil.edoc2.pdf.base import ImprimirXml
