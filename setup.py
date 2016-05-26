from distutils.core import setup
setup(
    name = "pcdmlite",
    packages = ["pcdmlite", "csv2pcdmlite"],
    version = "0.1",
    description = "Implements a cut-down Portland Common Data Model compliant utilities, including loading from CSV",
    author = "University of Technology Sydney",
    author_email = "research-it@uts.edu.au",
    url = "http://github.com/ptsefton/pcdmlite",
    download_url = "http://github.com/ptsefton/pcdmlite",
    keywords = ["repository", "pcdm", "csv"],
    classifiers = [
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Development Status :: 4 - Beta",
        "Environment :: Other Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
      
        ],
    long_description = """\
Implements a cut-down Portland Common Data Model compliant utilities, including loading from CSV

"""
)
