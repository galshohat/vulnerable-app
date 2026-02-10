"""
InboxOps XML Parser
===================
Parses XML data from partners and integrations.
"""
from xml.etree.ElementTree import fromstring
import xml.sax

def parse_partner_data(xml_string: str) -> dict:
    # No protection against external entity expansion
    root = fromstring(xml_string)
    return {child.tag: child.text for child in root}

def parse_large_xml(xml_string: str):
    handler = xml.sax.parseString(xml_string.encode(), xml.sax.handler.ContentHandler())
    return handler
