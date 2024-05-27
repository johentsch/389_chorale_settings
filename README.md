![Version](https://img.shields.io/github/v/release/johentsch/389_chorale_settings?display_name=tag)
[![DOI](https://zenodo.org/badge/805086079.svg)](https://zenodo.org/badge/latestdoi/805086079)
![GitHub repo size](https://img.shields.io/github/repo-size/johentsch/389_chorale_settings)
![License](https://img.shields.io/badge/license-CC%20BY--NC--SA%204.0-9cf)


# A digital edition of the 389 Chorale Settings (Choralgesänge) by J.S. Bach


This repository has been made possible by Gertim Alberda, 
who ‘manually’ digitalized all the 389 Bach 4-voice chorales, 
as published by the [Breitkopf edition 'nr. 3765'](https://imslp.org/wiki/Special:ReverseLookup/348824). 
For this he meticulously transcribed all the notes and lyrics of that edition, by using the music notation editor MuseScore (MS). 
He checked it against both BGA and NBA (Bach-Gesellschaft Ausgabe and Neue Bach-Ausgabe), 
if there was any reasonable doubt for it, and even found and improved a couple of mistakes that way (<10).
Solely for performance reasons, he also applied many hidden (grey) extras in MS to make the scores and its phrasing 
sound as realistic as possible; hidden fermatas, tempo changes, breath pauses, phrasing, note-cutbacks, etc. 
This was all done to 'humanize' the playback and make it sound like a real choir performance (without words), 
and given the technical limitations at that time (2016-2018). 
Also see the [Info](https://gertim-alberda.com/chorales/info.html) tab on his website.

The full corpus resides on Gertim Alberda’s [dedicated website](https://gertim-alberda.com/chorales). 
The scores there have synchronized play back (synthesized and human performances) available 
and can be downloaded in various formats (mscz/xml/midi/mp3/pdf). 
[Here is an example](https://gertim-alberda.com/chorales/BachChorales/B288.html) of his playback page. 
His intention is to have only human performances available (YT videos and/or mp3’s) for all the scores, 
but that is still an ongoing process 
(see the [changelog](https://gertim-alberda.com/chorales/changelog_bach_chorales.html) on his website). 
He has agreed to share his MS files under a [Creative Commons BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/) license. 
The license prohibits the use of the scores for any commercial purpose, including the training of machine learning models for use in commercial products.


## Contents

The "mother of all datasets" is available as two versions, each contained in a separate folder:

* `original_complete`: Gertim Alberda's original MuseScore files converted to uncompressed 
  MuseScore 3 format (`.mscx`)

## Version history

See the [GitHub releases](https://github.com/johentsch/389_chorale_settings/releases).

## Questions, Suggestions, Corrections, Bug Reports

Please [create an issue](https://github.com/johentsch/389_chorale_settings/issues) and/or feel free to fork and submit pull requests.

## License

Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License ([CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/)).

## Cite as

```
Alberda, G. & Hentschel, J. (2024). A digital edition of the 389 Chorale Settings (Choralgesänge) by J.S. Bach (v1.0) [Data set]. Zenodo. https://doi.org/10.5281/zenodo.11358762
```


## File naming convention

The chorales are named `B###` where `###` is the chorale number with leading zeros.
The numbers are in accordance with the Breitkopf edition which orders them alphabetically by title.

## Score properties

This table keeps track of certain characteristics of the scores.

* `Measure numbers`: In these scores the measure numbers changed from `v1.0` to `v2.0`.

| Chorale | Measure<br/>numbers | Parts  |
|---------|---------------------|--------|
| B001    |                     |        |
| B002    |                     |        |
| B003    |                     |        |
| B004    |                     |        |
| B005    | x                   |        |
| B006    | x                   |        |
| B007    | x                   |        |
| B008    |                     |        |
| B009    |                     |        |
| B010    |                     |        |
| B011    |                     |        |
| B012    | x                   |        |
| B013    | x                   |        |
| B014    | x                   | x      |
| B015    | x                   |        |
| B016    | x                   |        |
| B017    |                     |        |
| B018    |                     |        |
| B019    |                     |        |
| B020    | x                   |        |
| B021    | x                   |        |
| B022    |                     |        |
| B023    | x                   |        |
| B024    |                     |        |
| B025    |                     |        |
| B026    |                     |        |
| B027    |                     |        |
| B028    | x                   |        |
| B029    | x                   |        |
| B030    | x                   |        |
| B031    |                     |        |
| B032    | x                   |        |
| B033    |                     |        |
| B034    |                     |        |
| B035    |                     |        |
| B036    | x                   |        |
| B037    |                     |        |
| B038    |                     |        |
| B039    | x                   |        |
| B040    | x                   |        |
| B041    | x                   |        |
| B042    |                     |        |
| B043    | x                   |        |
| B044    | x                   |        |
| B045    |                     |        |
| B046    |                     |        |
| B047    |                     |        |
| B048    |                     |        |
| B049    |                     |        |
| B050    |                     |        |
| B051    |                     |        |
| B052    |                     |        |
| B053    | x                   |        |
| B054    | x                   |        |
| B055    |                     |        |
| B056    |                     |        |
| B057    |                     |        |
| B058    |                     |        |
| B059    |                     |        |
| B060    |                     |        |
| B061    |                     |        |
| B062    | x                   |        |
| B063    |                     |        |
| B064    |                     |        |
| B065    |                     |        |
| B066    |                     |        |
| B067    | x                   |        |
| B068    | x                   |        |
| B069    | x                   |        |
| B070    |                     |        |
| B071    |                     |        |
| B072    |                     |        |
| B073    | x                   |        |
| B074    |                     |        |
| B075    | x                   |        |
| B076    |                     |        |
| B077    | x                   |        |
| B078    | x                   |        |
| B079    |                     |        |
| B080    | x                   |        |
| B081    |                     |        |
| B082    |                     | x      |
| B083    |                     |        |
| B084    |                     |        |
| B085    |                     |        |
| B086    | x                   |        |
| B087    | x                   |        |
| B088    | x                   |        |
| B089    | x                   |        |
| B090    | x                   |        |
| B091    |                     |        |
| B092    | x                   |        |
| B093    | x                   |        |
| B094    |                     |        |
| B095    | x                   |        |
| B096    | x                   |        |
| B097    | x                   |        |
| B098    |                     |        |
| B099    |                     |        |
| B100    |                     |        |
| B101    |                     |        |
| B102    |                     |        |
| B103    |                     |        |
| B104    |                     |        |
| B105    |                     |        |
| B106    | x                   |        |
| B107    |                     |        |
| B108    |                     |        |
| B109    |                     |        |
| B110    |                     |        |
| B111    | x                   |        |
| B112    | x                   |        |
| B113    |                     |        |
| B114    |                     |        |
| B115    |                     |        |
| B116    |                     |        |
| B117    |                     |        |
| B118    |                     |        |
| B119    | x                   |        |
| B120    |                     |        |
| B121    |                     |        |
| B122    |                     |        |
| B123    |                     |        |
| B124    | x                   |        |
| B125    | x                   |        |
| B126    | x                   |        |
| B127    | x                   |        |
| B128    | x                   |        |
| B129    |                     |        |
| B130    |                     |        |
| B131    |                     |        |
| B132    |                     |        |
| B133    | x                   |        |
| B134    |                     |        |
| B135    |                     |        |
| B136    |                     |        |
| B137    |                     |        |
| B138    |                     |        |
| B139    |                     |        |
| B140    | x                   |        |
| B141    | x                   |        |
| B142    | x                   |        |
| B143    | x                   |        |
| B144    | x                   |        |
| B145    |                     |        |
| B146    |                     |        |
| B147    |                     |        |
| B148    |                     |        |
| B149    | x                   |        |
| B150    | x                   |        |
| B151    |                     |        |
| B152    | x                   |        |
| B153    | x                   |        |
| B154    | x                   |        |
| B155    | x                   |        |
| B156    | x                   |        |
| B157    | x                   |        |
| B158    | x                   |        |
| B159    | x                   |        |
| B160    | x                   |        |
| B161    | x                   |        |
| B162    | x                   |        |
| B163    | x                   |        |
| B164    | x                   |        |
| B165    | x                   |        |
| B166    |                     |        |
| B167    |                     |        |
| B168    |                     |        |
| B169    |                     |        |
| B170    |                     |        |
| B171    |                     |        |
| B172    | x                   |        |
| B173    |                     |        |
| B174    | x                   |        |
| B175    |                     |        |
| B176    | x                   |        |
| B177    | x                   |        |
| B178    | x                   |        |
| B179    |                     | x      |
| B180    |                     |        |
| B181    | x                   |        |
| B182    |                     |        |
| B183    | x                   |        |
| B184    | x                   |        |
| B185    |                     | x      |
| B186    |                     |        |
| B187    |                     |        |
| B188    |                     |        |
| B189    |                     |        |
| B190    |                     |        |
| B191    |                     |        |
| B192    |                     |        |
| B193    |                     |        |
| B194    |                     |        |
| B195    |                     | x      |
| B196    |                     |        |
| B197    |                     |        |
| B198    |                     |        |
| B199    |                     |        |
| B200    |                     |        |
| B201    |                     |        |
| B202    |                     |        |
| B203    | x                   |        |
| B204    | x                   |        |
| B205    | x                   | x      |
| B206    |                     |        |
| B207    |                     |        |
| B208    |                     |        |
| B209    |                     |        |
| B210    |                     |        |
| B211    |                     |        |
| B212    | x                   |        |
| B213    |                     |        |
| B214    |                     |        |
| B215    |                     |        |
| B216    | x                   |        |
| B217    | x                   |        |
| B218    |                     |        |
| B219    |                     |        |
| B220    |                     | x      |
| B221    |                     |        |
| B222    |                     |        |
| B223    |                     |        |
| B224    |                     |        |
| B225    |                     |        |
| B226    | x                   |        |
| B227    | x                   |        |
| B228    |                     |        |
| B229    |                     |        |
| B230    |                     | x      |
| B231    |                     |        |
| B232    |                     |        |
| B233    |                     |        |
| B234    |                     |        |
| B235    |                     |        |
| B236    |                     |        |
| B237    | x                   |        |
| B238    | x                   |        |
| B239    | x                   |        |
| B240    |                     |        |
| B241    |                     |        |
| B242    |                     |        |
| B243    |                     | x      |
| B244    |                     |        |
| B245    |                     |        |
| B246    |                     |        |
| B247    |                     |        |
| B248    |                     |        |
| B249    |                     |        |
| B250    |                     |        |
| B251    |                     |        |
| B252    |                     |        |
| B253    | x                   |        |
| B254    |                     |        |
| B255    |                     |        |
| B256    |                     |        |
| B257    | x                   |        |
| B258    | x                   |        |
| B259    | x                   |        |
| B260    |                     |        |
| B261    | x                   |        |
| B262    | x                   |        |
| B263    | x                   |        |
| B264    |                     |        |
| B265    |                     |        |
| B266    |                     |        |
| B267    |                     |        |
| B268    |                     |        |
| B269    | x                   |        |
| B270    | x                   |        |
| B271    | x                   |        |
| B272    | x                   | x      |
| B273    | x                   |        |
| B274    |                     |        |
| B275    |                     |        |
| B276    | x                   |        |
| B277    |                     |        |
| B278    |                     |        |
| B279    |                     |        |
| B280    |                     |        |
| B281    |                     |        |
| B282    | x                   |        |
| B283    | x                   |        |
| B284    |                     |        |
| B285    | x                   |        |
| B286    | x                   |        |
| B287    |                     |        |
| B288    |                     |        |
| B289    |                     |        |
| B290    |                     |        |
| B291    |                     |        |
| B292    |                     |        |
| B293    |                     |        |
| B294    |                     |        |
| B295    |                     |        |
| B296    |                     |        |
| B297    |                     |        |
| B298    |                     |        |
| B299    |                     |        |
| B300    |                     |        |
| B301    |                     |        |
| B302    |                     |        |
| B303    |                     |        |
| B304    |                     |        |
| B305    |                     |        |
| B306    |                     |        |
| B307    |                     |        |
| B308    |                     |        |
| B309    |                     |        |
| B310    |                     |        |
| B311    |                     |        |
| B312    |                     |        |
| B313    | x                   |        |
| B314    | x                   |        |
| B315    | x                   |        |
| B316    |                     |        |
| B317    |                     |        |
| B318    |                     |        |
| B319    |                     |        |
| B320    |                     |        |
| B321    |                     |        |
| B322    |                     |        |
| B323    |                     |        |
| B324    | x                   |        |
| B325    |                     |        |
| B326    | x                   |        |
| B327    |                     |        |
| B328    | x                   |        |
| B329    |                     |        |
| B330    |                     |        |
| B331    |                     |        |
| B332    |                     |        |
| B333    |                     |        |
| B334    |                     |        |
| B335    |                     |        |
| B336    |                     |        |
| B337    |                     |        |
| B338    | x                   |        |
| B339    | x                   |        |
| B340    | x                   |        |
| B341    | x                   |        |
| B342    | x                   |        |
| B343    | x                   |        |
| B344    | x                   |        |
| B345    | x                   |        |
| B346    | x                   |        |
| B347    | x                   |        |
| B348    | x                   |        |
| B349    |                     |        |
| B350    |                     |        |
| B351    |                     |        |
| B352    |                     |        |
| B353    |                     |        |
| B354    |                     |        |
| B355    |                     |        |
| B356    |                     |        |
| B357    | x                   |        |
| B358    |                     |        |
| B359    |                     |        |
| B360    |                     |        |
| B361    |                     |        |
| B362    |                     |        |
| B363    |                     |        |
| B364    |                     |        |
| B365    |                     |        |
| B366    |                     |        |
| B367    | x                   |        |
| B368    | x                   |        |
| B369    | x                   |        |
| B370    | x                   |        |
| B371    | x                   |        |
| B372    | x                   |        |
| B373    | x                   |        |
| B374    |                     |        |
| B375    |                     |        |
| B376    | x                   |        |
| B377    | x                   |        |
| B378    | x                   |        |
| B379    |                     |        |
| B380    | x                   |        |
| B381    |                     |        |
| B382    |                     |        |
| B383    | x                   |        |
| B384    | x                   |        |
| B385    | x                   |        |
| B386    | x                   |        |
| B387    |                     |        |
| B388    | x                   |        |
| B389    |                     |        |