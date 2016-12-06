# pcdcm-lite

Portland Common Data Model Lite - very very simple repository-agnostic class compatible with the [PCDM](https://github.com/duraspace/pcdm/wiki).

Should work with either Python2 or 3, but go for 3 if you can.

This is designed to work with repository specific code, such as [this test code for creating PCDM-compatible collections and objects in Fedora 4](https://github.com/ptsefton/spreadsheet-to-fedora-commons-4).

## Status

This is pre-alpha, under-documented, experimental code. It may work
for you and we're happy to help out if you are interested in getting
it running but it is not  production quality, yet. Raise an issue here if you have a question.

This is also embarassingly simple.


##  Install
1.  Get yourself into a Python Virtual environment for your project. TODO - how (Really, you are going to be messing with non-production code here)
2.  Check out this repository, eg by:
  ```git clone https://github.com/ptsefton/pcdcmlite```
3. Install it (in your Virtual Environment!):
   ```cd pcdmlite
    python setup.py install```

There are some rudimentary tests.

There are two classes:
pcdmlite: this is a essentially just a simple data structure (even simpler than PCDM)

## Load repository data via a CSV file


Quick notes for CSV format. 

* Use commas as separators 
*  Put one item or collection per row. 
*  Use these columns:


Column Header        |      Description 
----------------|-----------------------------------------------------------
dc:identifier :  | Required, an ID unique to (at least) your data. TODO: code should assign an ID to the whole spreadsheet to create a unique namespace for these IDs
dc:type           | What kind of resource this is. You could use a string or a URI.  If this row describes a collection put pdcdm:Collection
pdcm:Collection      |Optional, the ID collection that *contains* this object or collection, this should appear in the dcterms:identifier column elsewhere in the data file
dc:*meta*       |  Any other Dublin Core Metatada
FILE:                       | Path for a file to upload
REL:*predicate*     | Create an RDF relationship between this item or collection (the *subject*) and another using (prediate could be  a dublin core element like dc:subject, or a full URI), the row would contain the ID or URI of the *object*.

To make relationships between existing items using a separate sheet
you can use:

Column Header        | Description
----------------|-----------------------------------------------------------
subject                     | Subject ID (matches a dcterms:identifier)
predicate                  | An RDF predicate - either a URI or something with dc: frbr: or foaf: namespace (for now)
object                       | Object ID (matching a dcterms:identifier)

