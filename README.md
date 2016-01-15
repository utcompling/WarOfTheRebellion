# WarOfTheRebellion

WarOfTheRebellion is an annotated corpus of data from War of The Rebellion (a large set of American Civil War archives). It was built using [GeoAnnotate](https://github.com/utcompling/GeoAnnotate/).

It consists of two parts: a toponym corpus and a document-geolocation corpus.

To download the corpus, download and unzip the [zip file](https://github.com/utcompling/WarOfTheRebellion/archive/master.zip).

## Document geolocation corpus

The document geolocation corpus is found in two JSON files.
* `wotr-docgeo-jan-5-2016-625pm-by-vol.json` gives the spans by volume.
* `wotr-docgeo-jan-5-2016-625pm-80-0-20-by-split.json` gives the spans by split, with an 80-20 training/test split.

In both cases, the JSON data for an individual span consists of the following information:
* The volume number, from War of the Rebellion.
* The span character offsets, from corrected OCR'd text.
* The text of the span in question.
* The counts of individual words, using the tokenization algorithm followed in the paper (FIXME, name of paper). They are stored in a string, with a space separating word-count pairs and a colon separating the word from the count. The word itself is URL-encoded, i.e. a colon is represented as `%3A` and a percent character as `%25`.
* The date (if available), extracted from the text using regular expressions.
* The full [GeoJSON](http://geojson.org/) of the points and polygons annotated for the span.
* The centroid of the points and polygons, computed first by taking the centroid of each polygon and then taking the centroid of the resulting set of annotated points and polygon-centroid points. The centroid is in the form of a size-2 array of longitude and latitude (the same as how points are stored in GeoJSON).

## Toponym corpus

(document me)
