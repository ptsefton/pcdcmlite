"""
Super simple Library for representing a set of repository objects and collections in a very cut down version of the
Portland Common Data Model

Abstracts items and collections to be items.


Deals with multiple item types, assigning items to collections, file uploads and downloads from URLs
Initial implementation is for use with Omeka, but we are planning to use this with other repositories
such as Fedora Commons 4.
"""
from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
from builtins import str
from future import standard_library
standard_library.install_aliases()
from builtins import object
from rdflib import Graph, Literal, BNode, Namespace, RDF, URIRef




class Namespace(object):
    """ Crude way of handling vocabs - ATM there is no checking involved
        TODO: Allow user to load more of these from a file"""
    
    def __init__(self, prefix):
        dc = {"name": "Dublin Core", "URI": "http://purl.org/dc/terms/", "prefix": "dcterms"}
        bibo = {"name": "BIBO", "URI": "http://purl.org/ontology/bibo/", "prefix": "bibo"}
        foaf = {"name": "FOAF", "URI": "http://xmlns.com/foaf/0.1/", "prefix": "foaf"}
        custom = {"name": "custom", "URI": "", "prefix": "custom"}
        frbr = {"name": "FRBR", "URI": "http://purl.org/vocab/frbr/core#", "prefix": "foaf"}
        vocabs = {"dc": dc, "dcterms": dc, "foaf": foaf, "bibo": bibo, "custom": custom, "FRBDR": frbr}
        self.prefix = None
        self.name = None
        self.URI = None
        if prefix in list(vocabs.keys()):
            self.prefix = vocabs[prefix]["prefix"]
            self.name = vocabs[prefix]["name"]
            self.URI = vocabs[prefix]["URI"]
        else:
            self.prefix = prefix



class repository(object):
    pass
    



class Item(object):
    """(very) Abstract repository item could be a PCDM object or a file"""
    def __init__(self):
        self.files = []
        self.URLs = []
        self.relations = []
        self.text_fields = []
        self.is_collection = False
        self.in_collection = None
        self.type = None
        #self.dc_id = None
        self.id = None
        self.title = None
        self.graph = Graph()
        
    def serialize_RDF(self):
        # I don't understand how to get "<>" like Fedora wants
        # so HACK!  
        return str(self.graph.serialize(format="n3")).replace('"<>"','<>')