"""
Library for representing a set of repository items and collections via a csv file
Deals with multiple item types, assigning items to collections, file uploads and downloads from URLs
Initial implementation is for use with Omeka, but we are planning to use this with other repositories
such as Fedora Commons 4, 
"""
from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
from future import standard_library
standard_library.install_aliases()
from builtins import range
from builtins import object

import csv
import copy
from rdflib import Graph, Literal, BNode,RDF, URIRef
from rdflib.namespace import DC, FOAF
import sys
from pcdmlite.pcdmlite import Item, Namespace

def item_from_row(row):
    item = Item()
    populate_item_from_row(item, row)
    return item

def populate_item_from_row(item, row):
    def _add_field(item, field, array):
        if field.repeats:
            for v in field.value.split(","):
                new_field = copy.deepcopy(field)
                new_field.value = v.strip()
                array.append(new_field)
        else:
            array.append(field)
            
    for key, value in list(row.items()):
        f = Field(key)
        f.value = value
        if value:
            if f.type == Field.URL:
                _add_field(item, f, item.URLs)
            elif f.type == Field.FILE:
                _add_field(item, f, item.files)
            elif f.type == Field.RELATION:
                _add_field(item, f, item.relations)
            elif f.type == Field.IN_COLLECTION: #TODO - allow multiples?
                item.in_collection = value # Should be an id
            elif f.type == Field.TEXT:
                # Some fields are special, want these to bubble up as
                # properties of the Item
                # TODO - maybe make what's special configurable but
                # these are good defaults
                if f.qualified_name == "dcterms:title":
                    item.title = value
                elif f.qualified_name == "dcterms:identifier":
                    item.id = value

                _add_field(item, f, item.text_fields)

            elif f.type == Field.ITEM_TYPE:
                item.type = value
                if value == "pcdm:Collection":
                    item.is_collection = True

    for f in item.text_fields:
       item.graph.add((URIRef(""), URIRef(f.URI), Literal(f.value)))
   

class Field(object):
    """Class for decoding CSV column names"""
    TEXT, FILE, URL, RELATION, ITEM_TYPE, IN_COLLECTION = list(range(6))
    def  __init__(self, field_name):
        self.type = None
        self.namespace = Namespace("")
        self.field_name = None
        self.qualified_name = None
        self.URI = None
        self.value = None
        self.item_type_field = "dcterms:type" #TODO add a method to change
        self.collection_field = "pcdm:Collection"
        self.repeats = False

        if ":" in field_name:
            ns, name = field_name.split(":", 1)
            #If field name has a plus, then interpret the contents as multiple fields
            #TODO: add a test
            if name.endswith("+"):
                name = name[:-1]
                self.repeats = True
            if ns == "FILE":
                self.type = self.FILE
                self.field_name = name
            elif ns == "URL":
                self.type = self.URL
                self.field_name = name
            elif (ns == "REL" or ns == "RELATION"):
                if  ":" in name:
                    self.type = self.RELATION
                    ns, self.field_name = name.split(":", 1)
                    self.namespace = Namespace(ns)
                    self.qualified_name = ':'.join([self.namespace.prefix, self.field_name])
                    self.URI = ":".join([self.namespace.URI, self.field_name])  if self.URI else self.qualified_name
            else:
                self.namespace = Namespace(ns)
                self.field_name = name
                self.qualified_name = ':'.join([self.namespace.prefix, self.field_name])
                self.URI = ":".join([self.namespace.URI, self.field_name]) if self.namespace.URI else self.qualified_name
                if self.qualified_name == self.item_type_field:
                    self.type = self.ITEM_TYPE
                    self.repeats = False
                elif self.qualified_name == self.collection_field:
                    self.type = self.IN_COLLECTION
                else:
                    self.type = self.TEXT
                    

class CSVData(object):
    def __init__(self, stream):
        self._reader = csv.DictReader(stream)
        self.fieldnames = self._reader.fieldnames
        self.fields = {}
        self.items = []
        self.collections = []
        for name in self.fieldnames:
            self.fields[name] =  Field(name)
            
    def get_items(self):
        """ Get a set of abstract repository items and collections from the rows in the CSV"""
        for row in self._reader:
            item = item_from_row(row)
            if item.is_collection:
                self.collections.append(item)
            else:
                self.items.append(item)


            
    def serialize_RDF(self):
        return self.graph.serialize(format="n3") 
