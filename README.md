# Pairwise-Disconnectivity-index

-------------------------------------

## PACKAGES

    python v2.7

    R v3.5.1

    Bioconductor

    STRING db-bioconductor

-------------------------------------

## INSTALLATION

$R

    source("https://bioconductor.org/biocLite.R")

    biocLite("STRINGdb")

FOR DEBIAN USING APT

    sudo apt-get install python-igraph

    sudo apt-get install python-matplotlib

USING PIP

    pip install python-igraph

    pip install matplotlib

----------------------------------------

## SCRIPTS

    String_data_download.r

    Stringdb_parse.py

    Pairwise_dis_index.py

    Pairwise_discon_vdisjoint_paths.py

    Mapping_on_annotation_file.py

    X.sh

-------------------------------------------

## USAGE AS BUNDLED PACKAGE

    $ chmod +x x.sh

    $ ./x.sh

------------------------------------------------

ABOUT x.sh

This is a pipeline which initialize the process and input from one script is passed to other script and at the end it will return the 3 files one with all crucial nodes ,non-crucial nodes ,moderately crucial nodes mapped onto the annotation file .This will first download the string data by taking species id from user as input Then the data will be unzipped and parsed on for the scripts which evaluates the pairwise dis connectivity index and similar using disjoint path return result files in a directory named out .

- SCRIPTS CAN ALSO BE USED AS STAND ALONE FOR USAGE AND MORE INFORMATION CHECK THE THESIS.

