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

The Toponym corpus, otherwise known as WoTR-Topo, is given in two different formats. The first format is JSON format files, split into train and test. Here is subsection of wotr-topo-train.json, simplified for display purposes:

```
[
     {
          "vol": "77", 
          "text": "Numbers 10. Report of Colonel Franklin Campbell, Eighty- first Illinois Infantry.\n\nHDQRS. EIGHTY- FIRST Illinois VOLUNTEER INFANTRY,\nSaint Charles, Ark., August 10, 1864.\n\nSIR: I have the honor to transmit, in compliance with your request, my part taken in the engagement at Guntown, Miss.", 
          "docid": 14, 
          "vol_charrange": "73019-76287", 
          "named_entities": [
               {
                    "char_end": 47, 
                    "char_start": 30, 
                    "geo": "", 
                    "entity_string": "Franklin Campbell", 
                    "entity_type": "person"
               }, 
               {
                    "char_end": 80, 
                    "char_start": 49, 
                    "geo": "", 
                    "entity_string": "Eighty- first Illinois Infantry", 
                    "entity_type": "org"
               }, 
               {
                    "char_end": 131, 
                    "char_start": 90, 
                    "geo": "", 
                    "entity_string": "EIGHTY- FIRST Illinois VOLUNTEER INFANTRY", 
                    "entity_type": "org"
               }, 
               {
                    "char_end": 146, 
                    "char_start": 133, 
                    "geo": "{\"type\":\"Point\",\"coordinates\":[ -91.136667\t,34.374167]}", 
                    "entity_string": "Saint Charles", 
                    "entity_type": "place"
               }, 
               {
                    "char_end": 152, 
                    "char_start": 148, 
                    "geo": "{\"type\":\"MultiPolygon\",\"coordinates\":[[[[-94.53813776875315,36.4750515822705],[-90.20952448750022,36.492718127950745],[-90.12163386250148,36.40434512685882],[-90.29741511249897,36.0320808383389],[-90.36333308124577,35.96097270693884],[-89.74809870625012,35.96097270693884],[-89.72612604999999,35.818564245961255],[-90.03374323750275,35.15660300197383],[-90.53911433125222,34.56162216439406],[-91.08843073749658,33.74338300069125],[-91.19829401874725,33.4138753832596],[-91.13237605000043,33.04628424100146],[-94.01079401875174,32.991012472641636],[-94.03276667500367,33.52385099797542],[-94.5161651125012,33.578786444376625],[-94.3843291749986,35.532980007494515],[-94.53813776875315,36.4750515822705]]]]}", 
                    "entity_string": "Ark.", 
                    "entity_type": "place"
               }, 
               {
                    "char_end": 282, 
                    "char_start": 275, 
                    "geo": "{\"type\":\"Point\",\"coordinates\":[-88.66305599999998,34.44499999999999]}", 
                    "entity_string": "Guntown", 
                    "entity_type": "place"
               }, 
               {
                    "char_end": 289, 
                    "char_start": 284, 
                    "geo": "{\"type\":\"MultiPolygon\",\"coordinates\":[[[[-90.34960017109394,34.96550717485067],[-88.17430720234331,35.0015123192762],[-88.13036188984304,34.83936455981574],[-88.43797907734312,32.090340438762695],[-88.41600642109296,30.361825589745635],[-89.53661188984259,30.077026111698977],[-89.84422907734447,30.607983114847507],[-89.73436579609289,31.02313420297064],[-91.68993220234488,31.00430267080129],[-91.55809626484228,31.51144398416993],[-91.22850642109027,31.99721562091857],[-91.00877985858894,32.31345287347353],[-91.1845611085954,32.9610591345928],[-91.20653376484732,33.786765659842295],[-90.85497126484341,34.31471489623916],[-90.34960017109394,34.96550717485067]]]]}", 
                    "entity_string": "Miss.", 
                    "entity_type": "place"
               }
          ]
     }, 
     {
          "vol": "77", 
          "text": "[Inclosure.]\n\nCOVINGTON, KY., January 12, 1865.\n\nADJUTANT- GENERAL OF THE ARMY,\n\nWashington, D. C.:\n\nSIR: As a great many malicious misrepresentations have been spread before the county in regard to my conduct of the campaign into Northeast MISSISSIPPI last summer", 
          "docid": 6, 
          "vol_charrange": "7272-8910", 
          "named_entities": [
               {
                    "char_end": 23, 
                    "char_start": 14, 
                    "geo": "{\"type\":\"Point\",\"coordinates\":[ -84.509722\t,39.065]}", 
                    "entity_string": "COVINGTON", 
                    "entity_type": "place"
               }, 
               {
                    "char_end": 28, 
                    "char_start": 25, 
                    "geo": "{\"type\":\"MultiPolygon\",\"coordinates\":[[[[-89.31139216327693,36.539073640160055],[-88.14684138202705,36.486093645404075],[-88.01500544452713,36.644924778217344],[-87.88316950702725,36.680176216589686],[-87.6634429445268,36.66255251541968],[-86.58678278827746,36.66255251541968],[-83.86217341327709,36.60965719869816],[-83.29088435077722,36.71541150786632],[-83.00523981952728,36.83860778367614],[-82.56578669452729,37.13697340069469],[-81.99449763202743,37.4690537311464],[-82.47789606952767,37.95575696273079],[-82.60973200702756,38.249693177844044],[-82.6317046632768,38.40482733295352],[-82.85143122577723,38.748379703072764],[-82.89537653827752,38.67980071229266],[-83.18102106952745,38.62832330087655],[-84.03795466327725,38.851124779960216],[-84.56529841327686,39.0902867814717],[-85.40025935077745,38.64548654818031],[-85.99352106952745,38.059634164966596],[-86.43297419452743,38.09422718425207],[-87.57555231952716,37.92109853026757],[-87.90514216327739,37.85173264757507],[-88.21275935077745,37.48649099911802],[-89.06969294452726,37.11945489217114],[-89.31139216327693,36.539073640160055]]]]}", 
                    "entity_string": "KY.", 
                    "entity_type": "place"
               }, 
               {
                    "char_end": 91, 
                    "char_start": 81, 
                    "geo": "{\"type\":\"Point\",\"coordinates\":[-77.0726226320272,38.86823455473613]}", 
                    "entity_string": "Washington", 
                    "entity_type": "place"
               }, 
               {
                    "char_end": 98, 
                    "char_start": 93, 
                    "geo": "{\"type\":\"MultiPolygon\",\"coordinates\":[[[[-77.21544489765128,38.953721662025714],[-77.1165679445266,39.05190450651943],[-76.86937556171438,39.013501360321925],[-76.84190974140172,38.87251135515992],[-76.91332087421374,38.816892881362776],[-77.20445856952621,38.80405167509718],[-77.21544489765128,38.953721662025714]]]]}", 
                    "entity_string": "D. C.", 
                    "entity_type": "place"
               }, 
               {
                    "char_end": 252, 
                    "char_start": 231, 
                    "geo": "{\"type\":\"MultiPolygon\",\"coordinates\":[[[[-89.44872126484026,34.96550717485143],[-89.8002837648397,32.88728457632749],[-88.35008845233989,32.66559233881516],[-88.13036188984034,34.96550717485143],[-89.44872126484026,34.96550717485143]]]]}", 
                    "entity_string": "Northeast MISSISSIPPI", 
                    "entity_type": "place"
               }
          ]
     }
]
```

As can be seen, the geographic information for toponyms is given by the geojson standard, with annotations done in a stand-off style. 

The second format that Wotr-Topo is offered in is a simplified xml format, in the folder trconll-classixml. This format was created so that the data could be fed into the TR systems of [Topocluster](http://www.jasonbaldridge.com/papers/DelozierBaldridgeLondon_AAAI2015.pdf?attredirects=0) and [Fielspring](http://www.jasonbaldridge.com/papers/speriosu-baldridge-acl2013.pdf). One thing that compatibility with these TR systems required was simplification of the complex geojson geometry to a centroid, so these xml files have simplified centroid geometries.

An simplified example of the format is given below:

```
<?xml version="1.0" encoding="utf-8"?>
<doc id="105-12" title="105" domain="wotr">
<s id="s1">
<w tok="["/>
<w tok="Inclosure"/>
<w tok="N."/>
<w tok="]"/>
<w tok="HEADQUARTERS"/>
<w tok="DEPARTMENT"/>
<w tok="OF"/>
<w tok="NEW"/>
<w tok="MEXICO"/>
<w tok=","/>
<toponym term="Santa Fe.">
<candidates>
<cand lat="35.6951223872" long="-105.910483543" selected="yes"/>
</candidates>
</toponym>
<toponym term="N. Mex.">
<candidates>
<cand lat="34.4361527922" long="-106.092270975" selected="yes"/>
</candidates>
</toponym>
<w tok="August"/>
<w tok="21"/>
<w tok=","/>
<w tok="1862"/>
<w tok="."/>
<w tok="Brigadier"/>
<w tok="General"/>
<w tok="JAMES"/>
<w tok="H."/>
<w tok="CARLETON"/>
<w tok=","/>
<w tok="Commanding"/>
<w tok="District"/>
<w tok="of"/>
<toponym term="Arizona">
<candidates>
<cand lat="34.2787291101" long="-111.659954425" selected="yes"/>
</candidates>
</toponym>
<toponym term="Fort Bliss">
<candidates>
<cand lat="31.801847" long="-106.424608" selected="yes"/>
</candidates>
</toponym>
<toponym term="Tex.">
<candidates>
<cand lat="31.4264675693" long="-99.224702175" selected="yes"/>
</candidates>
</toponym>
<w tok="GENERAL"/>
<w tok=":"/>
<w tok="The"/>
<w tok="commanding"/>
<w tok="general"/>
<w tok="desires"/>
<w tok="that"/>
<w tok="you"/>
<w tok="will"/>
<w tok="arrange"/>
<w tok="the"/>
<w tok="affairs"/>
<w tok="of"/>
<w tok="your"/>
<w tok="district"/>
</s>
</doc>
```

Not everything that has been annotated is guaranteed to be correct. We encourage others to correct errors that they find in a branched repository and submit pull requests when corrections are made. 

For questions regarding the corpus, please contact its creators Ben Wing (ben@benwing.com) and Grant DeLozier (grantdelozier@gmail.com)

[The ACL LAW paper describing the corpus and performing benchmark evaluation](http://aclanthology.info/papers/creating-a-novel-geolocation-corpus-from-historical-texts)
