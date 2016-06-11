# pcdcm-lite

Portland Common Data Model Lite - very very simple repository-agnostic class compatible with the [PCDM](https://github.com/duraspace/pcdm/wiki).

Should work with either Python2 or 3, but go for 3 if you can.

This is designed to work with repository specific code, such as [this test code for creating PCDM-compatible collections and objects in Fedora 4](https://github.com/ptsefton/spreadsheet-to-fedora-commons-4).

## Status

This is pre-alpha, under-documented, experimental code. It may work
for you and we're happy to help out if you are interested in getting
it running but it is not  production quality, yet. Raise an issue here if you have a question.


##  Install
1.  Get yourself into a Python Virtual environment for your project. (Really, you are going to be messing with non-production code here)
2.  Check out this repository, eg by:
  ```git clone https://github.com/ptsefton/pcdcmlite```
3. Install it (in your Virtual Environment!):
   ```cd pcdmlite
    python setup.py install```

There are some rudimentary tests. 

## Describing a simple repository via a CSV file. 

TODO: Document the CSV format.

Quick notes for CSV format. 

* Use commas as separators 
*  Put one item or collection per row. 
*  Use these columns:


Column Header        |      Description 
----------------|-----------------------------------------------------------
dcterms:identifier :  | Required, an ID unique to (at least) your data. TODO: code should assign an ID to the whole spreadsheet to create a unique namespace for these IDs
dcterms:type           | What kind of resource this is. You could use a string or a URI.  If this row describes a collection put pdcdm:Collection
pdcm:Collection      |Optional, the ID collection that *contains* this object or collection, this should appear in the dcterms:identifier column elsewhere in the data file
dcterms:*term*       |  Any other Dublin Core Metatada
FILE:                       | Path for a file to upload

