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
* `vocal_parts_only`: Alternative version of the dataset containing no instrumental parts.

### Score-to-audio alignments

Version 2.3 introduces an additional set of tables of notes in the subfolder 
`vocal_parts_only/note_alignments`. They correspond to unfolded/expanded 
versions of the 303 chorale settings that have a counterpart in and have been aligned with the 
recordings made by the Chamber Choir Of Europe under Nicol Matt in 1999 (e.g., CDs 122 through 127 
(six CDs) of the release https://musicbrainz.org/release/5582b212-aea7-4355-8c4c-531ed438e5fc).
Unfolded/expanded, here, means that they correspond to a "playthrough" respecting repeat signs and 
first/second endings.
This representation is a prerequisite for aligning the notes with the corresponding sounding events 
in the recordings.

First, the MusicBrainz recording IDs contained in the column `mb:recording` of the file 
`metadata.tsv` were used to map the 303 scores (or rather, their unfolded notes TSVs) to the 
respective audio files (which are commercial and cannot be provided). 
Silence at the end of the audio files has been truncated beforehand using a 50 ms & -65 dB threshold. 

Then, the latest version of the `synctoolbox` (1.3.2) and 
[this Python script](https://github.com/johentsch/Aligning-audio-to-annotated-score-labels/blob/bach/align_bach.py) 
was used to compute start and end points of each note. The timecodes were added as two additional 
columns, `start` and `end`, to the unfolded notes TSVs.

An easy way to verify them (if you happen to have the recording of the Chamber Choir of Europe) 
is to make a copy of the relevant TSV file in `vocal_parts_only/note_alignments`,
keeping only the last six columns (at the very least, `midi`, `start`, and `end`).
This is because the [Sonic Visualizer](https://sonicvisualiser.org/) can only load the first few
columns of a TSV/CSV file.
Then you can load the aligned notes into the Sonic Visualizer like so:

![Screenshot showing how to import the reduced CSV file into the Sonic Visualizer](https://hostux.pics/images/2025/02/17/sonic_visualizerc836b5e2d792d532.png)



## Version history

See the [GitHub releases](https://github.com/johentsch/389_chorale_settings/releases).

## Questions, Suggestions, Corrections, Bug Reports

Please [create an issue](https://github.com/johentsch/389_chorale_settings/issues) and/or feel free to fork and submit pull requests.

## License

Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License ([CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/)).

## Cite as

```
Alberda, G. & Hentschel, J. (2024). A digital edition of the 389 Chorale Settings (Choralgesänge) by J.S. Bach (v2.3) [Data set]. Zenodo. https://doi.org/10.5281/zenodo.11358762
```


## File naming convention

The chorales are named `B###` where `###` is the chorale number with leading zeros.
The numbers are in accordance with the Breitkopf edition which orders them alphabetically by title.

## Score properties

This table keeps track of certain characteristics of the scores.

* `Measure numbers`: In these scores the measure numbers changed from `v1.0` to `v2.3`.
* `Parts`: These scores contain instrumental parts in the `original_complete` version, which have been removed in the 
  `vocal_parts_only` version.
* `Instrument staves`: The IDs of those staves that contain instrumental parts in the `original_complete` version
  which have been removed in the `vocal_parts_only` version. 1 stands for the uppermost staff. Chorales where the 
  upper staff was removed are marked with a bold **1**; these might be missing markup that is typically attached
  to the upper score, e.g. tempo markings.
* `Merge`: In the marked chorales, the four voices are written in individual staves in the `original_complete` version
  but have been merged into two staves in the `vocal_parts_only` version for homogeneity. `B199` is the only one
  that remains being typeset with four staves because it is not homophone.
* `Cue notes`: In the marked chorales, the vocal staves contain cue note in the `original_complete` version
  which have been removed for the `vocal_parts_only` version.

| Chorale | Measure<br>numbers | Parts | Instrument staves                               | Merge        | Cue notes |
|---------|--------------------|-------|-------------------------------------------------|--------------|-----------|
| B001    |                    |       | 3                                               |              |           |
| B002    |                    |       | 3                                               |              |           |
| B003    |                    |       | 3                                               |              |           |
| B004    |                    |       | 3                                               |              | x         |
| B005    | x                  |       | 3                                               |              |           |
| B006    | x                  |       | 3                                               |              |           |
| B007    | x                  |       | 3                                               |              |           |
| B008    |                    |       | 3                                               |              |           |
| B009    |                    |       | 3                                               |              |           |
| B010    |                    |       | 3                                               |              |           |
| B011    |                    |       | 3                                               |              | x         |
| B012    | x                  |       | 3, 4                                            |              |           |
| B013    | x                  |       | 3                                               |              | x         |
| B014    | x                  | x     | **1**, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14     |              | x         |
| B015    | x                  |       | 3, 4                                            |              |           |
| B016    | x                  |       | 3, 4, 5                                         |              | x         |
| B017    |                    |       | 3, 4                                            |              |           |
| B018    |                    |       | 3                                               |              |           |
| B019    |                    |       | 3                                               |              |           |
| B020    | x                  |       | 3, 4                                            |              |           |
| B021    | x                  |       | 3                                               |              |           |
| B022    |                    |       | 3                                               |              |           |
| B023    | x                  |       | 3, 4                                            |              |           |
| B024    |                    |       | 3                                               |              |           |
| B025    |                    |       | 3                                               |              |           |
| B026    |                    |       | 3                                               |              | x         |
| B027    |                    |       | **1**, 4, 5, 6, 7, 8, 9, 10                     |              | x         |
| B028    | x                  |       | 3                                               |              |           |
| B029    | x                  |       | 3                                               |              |           |
| B030    | x                  |       | 3                                               |              |           |
| B031    |                    |       | 3, 4, 5, 6, 7                                   |              | x         |
| B032    | x                  |       | 3, 4, 5, 6, 7                                   |              |           |
| B033    |                    |       | 3                                               |              |           |
| B034    |                    |       | 3                                               |              |           |
| B035    |                    |       | 3                                               |              |           |
| B036    | x                  |       | 3, 4                                            |              |           |
| B037    |                    |       | 3                                               |              |           |
| B038    |                    |       | 3, 4, 5, 6, 7                                   |              |           |
| B039    | x                  |       | 3                                               |              |           |
| B040    | x                  |       | 3                                               |              | x         |
| B041    | x                  |       | 3, 4                                            |              |           |
| B042    |                    |       | 3, 4                                            |              | x         |
| B043    | x                  |       | 3                                               |              |           |
| B044    | x                  |       | 3                                               |              | x         |
| B045    |                    |       | 3                                               |              | x         |
| B046    |                    |       | 3, 4, 5, 6, 7                                   |              |           |
| B047    |                    |       | 3                                               |              |           |
| B048    |                    |       | 3, 4                                            |              |           |
| B049    |                    |       | 3                                               |              | x         |
| B050    |                    |       | 3                                               |              |           |
| B051    |                    |       | 3, 4, 5                                         |              |           |
| B052    |                    |       | 3, 4                                            |              |           |
| B053    | x                  |       | 3                                               |              |           |
| B054    | x                  |       | 3                                               |              |           |
| B055    |                    |       | 3, 4                                            |              |           |
| B056    |                    |       | 3                                               |              |           |
| B057    |                    |       | 3                                               |              | x         |
| B058    |                    |       | 3                                               |              |           |
| B059    |                    |       | 3                                               |              |           |
| B060    |                    |       | 3                                               |              |           |
| B061    |                    |       | 3                                               |              |           |
| B062    | x                  |       | 3                                               |              |           |
| B063    |                    |       | 3                                               |              |           |
| B064    |                    |       | 3                                               |              |           |
| B065    |                    |       | 3, 4, 5, 6, 7                                   |              |           |
| B066    |                    |       | 3                                               |              |           |
| B067    | x                  |       | 2, 4                                            |              |           |
| B068    | x                  |       | 3                                               |              | x         |
| B069    | x                  |       | 3                                               |              |           |
| B070    |                    |       | 3, 4, 5, 6, 7                                   |              |           |
| B071    |                    |       | 3                                               |              |           |
| B072    |                    |       | 3                                               |              | x         |
| B073    | x                  |       | 3, 4, 5, 6, 7                                   |              |           |
| B074    |                    |       | 3, 4, 5, 6, 7                                   |              |           |
| B075    | x                  |       | 3, 4, 5, 6, 7                                   |              |           |
| B076    |                    |       | 3, 4, 5, 6, 7                                   |              |           |
| B077    | x                  |       | 3                                               |              |           |
| B078    | x                  |       | 3                                               |              |           |
| B079    |                    |       | 3                                               |              |           |
| B080    | x                  |       | 3, 4                                            |              | x         |
| B081    |                    |       | 3                                               |              |           |
| B082    |                    | x     | 5-23                                            | (1,2)(3,4)   |           |
| B083    |                    |       | 3, 4                                            |              |           |
| B084    |                    |       | 3                                               |              |           |
| B085    |                    |       | 3                                               |              |           |
| B086    | x                  |       | 3                                               |              |           |
| B087    | x                  |       | 3, 4                                            |              | x         |
| B088    | x                  |       | 3                                               |              |           |
| B089    | x                  |       | **1**, 4                                        |              | x         |
| B090    | x                  |       | 3, 4                                            |              | x         |
| B091    |                    |       | 3                                               |              | x         |
| B092    | x                  |       | 3, 4, 5, 6, 7                                   |              |           |
| B093    | x                  |       |                                                 |              |           |
| B094    |                    |       | 3                                               |              |           |
| B095    | x                  |       | 3                                               |              |           |
| B096    | x                  |       | 3                                               |              |           |
| B097    | x                  |       | **1**, 2, 3, 4, 7, 8, 9, 10                     |              | x         |
| B098    |                    |       | 3                                               |              |           |
| B099    |                    |       | **1**, 2, 5                                     |              |           |
| B100    |                    |       | 3                                               |              | x         |
| B101    |                    |       | 3                                               |              |           |
| B102    |                    |       | 3                                               |              | x         |
| B103    |                    |       | 3                                               |              | x         |
| B104    |                    |       | 3                                               |              | x         |
| B105    |                    |       | 2, 4                                            |              |           |
| B106    | x                  |       | 2, 4                                            |              |           |
| B107    |                    |       |                                                 |              |           |
| B108    |                    |       | 3                                               |              | x         |
| B109    |                    |       | **1**, 2, 5, 6                                  |              |           |
| B110    |                    |       | 3                                               |              | x         |
| B111    | x                  |       | 3                                               |              |           |
| B112    | x                  |       | 2, 4, 5                                         |              |           |
| B113    |                    |       | 3                                               |              |           |
| B114    |                    |       | 3                                               |              | x         |
| B115    |                    |       | 3                                               |              |           |
| B116    |                    |       | 3                                               |              |           |
| B117    |                    |       | 3                                               |              |           |
| B118    |                    |       | 3                                               |              |           |
| B119    | x                  |       | 3                                               |              |           |
| B120    |                    |       | 3                                               |              |           |
| B121    |                    |       | 3, 4, 5                                         |              | x         |
| B122    |                    |       | 3, 4                                            |              | x         |
| B123    |                    |       | 3                                               |              |           |
| B124    | x                  |       | 3                                               |              | x         |
| B125    | x                  |       | 3                                               |              |           |
| B126    | x                  |       | 3                                               |              |           |
| B127    | x                  |       | 3                                               |              |           |
| B128    | x                  |       | 3                                               |              | x         |
| B129    |                    |       | 3                                               |              |           |
| B130    |                    |       | **1**, 2, 5, 6, 7, 8                            |              |           |
| B131    |                    |       | **1**, 2, 3, 4, 5, 6, 7, 8, 9, 12, 13           |              | x         |
| B132    |                    |       | 3, 4                                            |              |           |
| B133    | x                  |       | 3                                               |              |           |
| B134    |                    |       | 3                                               |              |           |
| B135    |                    |       | 3                                               |              | x         |
| B136    |                    |       | 3                                               |              |           |
| B137    |                    |       | 3                                               |              |           |
| B138    |                    |       | 3                                               |              |           |
| B139    |                    |       | 3                                               |              |           |
| B140    | x                  |       | 3                                               |              |           |
| B141    | x                  |       | 3                                               |              |           |
| B142    | x                  |       | 3                                               |              |           |
| B143    | x                  |       | 3                                               |              |           |
| B144    | x                  |       | 3                                               |              |           |
| B145    |                    |       | 3                                               |              |           |
| B146    |                    |       | 3                                               |              |           |
| B147    |                    |       | 3                                               |              |           |
| B148    |                    |       | 3                                               |              |           |
| B149    | x                  |       | 3                                               |              |           |
| B150    | x                  |       | 3, 4                                            |              |           |
| B151    |                    |       | 3                                               |              |           |
| B152    | x                  |       | 3                                               |              |           |
| B153    | x                  |       | 3                                               |              | x         |
| B154    | x                  |       | 3                                               |              |           |
| B155    | x                  |       | **1**, 4                                        |              | x         |
| B156    | x                  |       | 3                                               |              |           |
| B157    | x                  |       | 3                                               |              |           |
| B158    | x                  |       | 3                                               |              |           |
| B159    | x                  |       | 3                                               |              |           |
| B160    | x                  |       | 3                                               |              |           |
| B161    | x                  |       | **1**, 2, 5                                     |              |           |
| B162    | x                  |       | 3                                               |              |           |
| B163    | x                  |       | 3                                               |              | x         |
| B164    | x                  |       | 3                                               |              | x         |
| B165    | x                  |       | 3                                               |              | x         |
| B166    |                    |       | 3                                               |              | x         |
| B167    |                    |       | 3                                               |              |           |
| B168    |                    |       | 3                                               |              | x         |
| B169    |                    |       | 3                                               |              | x         |
| B170    |                    |       | 3                                               |              |           |
| B171    |                    |       | 3                                               |              |           |
| B172    | x                  |       | 3                                               |              |           |
| B173    |                    |       | 3                                               |              |           |
| B174    | x                  |       | 3                                               |              |           |
| B175    |                    |       | 3                                               |              |           |
| B176    | x                  |       | 3                                               |              |           |
| B177    | x                  |       | 3                                               |              |           |
| B178    | x                  |       | 3                                               |              |           |
| B179    |                    | x     | 3                                               |              |           |
| B180    |                    |       | 3                                               |              |           |
| B181    | x                  |       | 3                                               |              | x         |
| B182    |                    |       | 3                                               |              |           |
| B183    | x                  |       | 3                                               |              | x         |
| B184    | x                  |       | **1**, 4                                        |              | x         |
| B185    |                    | x     | 3, 4, 5, 6, 7                                   |              |           |
| B186    |                    |       | 3                                               |              |           |
| B187    |                    |       | 3                                               |              |           |
| B188    |                    |       | 3                                               |              | x         |
| B189    |                    |       | 3                                               |              |           |
| B190    |                    |       | 3                                               |              |           |
| B191    |                    |       |                                                 |              | x         |
| B192    |                    |       | 3                                               |              | x         |
| B193    |                    |       | 3                                               |              |           |
| B194    |                    |       | 3                                               |              | x         |
| B195    |                    | x     | 3, 4, 5, 6, 7                                   |              |           |
| B196    |                    |       | 3                                               |              |           |
| B197    |                    |       | 3                                               |              |           |
| B198    |                    |       | 2, 4                                            |              |           |
| B199    |                    |       | 5                                               |              |           |
| B200    |                    |       | 3                                               |              |           |
| B201    |                    |       | 3                                               |              | x         |
| B202    |                    |       | 3                                               |              |           |
| B203    | x                  |       | 3                                               |              |           |
| B204    | x                  |       | 3                                               |              |           |
| B205    | x                  | x     | **1**, 2, 3, 4, 5, 6, 7, 8, 9, 10, 13, 14, 15   |              |           |
| B206    |                    |       | 3                                               |              |           |
| B207    |                    |       | 3                                               |              |           |
| B208    |                    |       | 3                                               |              | x         |
| B209    |                    |       | 3                                               |              |           |
| B210    |                    |       | 3                                               |              |           |
| B211    |                    |       | 3                                               |              |           |
| B212    | x                  |       | **1**, 4                                        |              | x         |
| B213    |                    |       | 3                                               |              |           |
| B214    |                    |       | 3, 4                                            |              | x         |
| B215    |                    |       | 3, 4, 5, 6, 7                                   |              |           |
| B216    | x                  |       | 3                                               |              | x         |
| B217    | x                  |       | 3                                               |              |           |
| B218    |                    |       | 3                                               |              |           |
| B219    |                    |       | **1**, 4                                        |              |           |
| B220    |                    | x     | **1**, 2, 5                                     |              |           |
| B221    |                    |       | 3                                               |              |           |
| B222    |                    |       | 3, 4                                            |              |           |
| B223    |                    |       | 3                                               |              | x         |
| B224    |                    |       | 3                                               |              | x         |
| B225    |                    |       | 3                                               |              |           |
| B226    | x                  |       | 3                                               |              |           |
| B227    | x                  |       | 3                                               |              | x         |
| B228    |                    |       | 3                                               |              |           |
| B229    |                    |       | 3                                               |              |           |
| B230    |                    | x     | **1**, 2, 3, 4, 5, 8, 9, 10                     |              | x         |
| B231    |                    |       | 3                                               |              |           |
| B232    |                    |       | 3                                               |              |           |
| B233    |                    |       | 3                                               |              |           |
| B234    |                    |       | 3                                               |              |           |
| B235    |                    |       | 3                                               |              | x         |
| B236    |                    |       | **1**, 2, 3, 4, 5, 6, 7, 8, 9, 12, 13           |              |           |
| B237    | x                  |       | 3                                               |              |           |
| B238    | x                  |       | 3                                               |              |           |
| B239    | x                  |       | 3                                               |              | x         |
| B240    |                    |       | 3                                               |              |           |
| B241    |                    |       | 3                                               |              |           |
| B242    |                    |       | 3                                               |              |           |
| B243    |                    | x     | **1**, 2, 3, 4, 7, 8, 9                         |              | x         |
| B244    |                    |       | 3                                               |              | x         |
| B245    |                    |       | 3, 4                                            |              |           |
| B246    |                    |       | 3                                               |              | x         |
| B247    |                    |       | 3                                               |              | x         |
| B248    |                    |       | 3                                               |              |           |
| B249    |                    |       | 3                                               |              |           |
| B250    |                    |       | 3                                               |              |           |
| B251    |                    |       | 3                                               |              |           |
| B252    |                    |       | 3                                               |              |           |
| B253    | x                  |       | 3                                               |              |           |
| B254    |                    |       | 3                                               |              |           |
| B255    |                    |       | 3                                               |              |           |
| B256    |                    |       | 3                                               |              | x         |
| B257    | x                  |       | 3                                               |              |           |
| B258    | x                  |       | **1**, 2, 3, 4, 5, 6, 9                         |              | x         |
| B259    | x                  |       | **1**, 2, 3, 4, 5, 6, 7, 8, 9, 10, 13, 14       |              |           |
| B260    |                    |       | 3                                               |              |           |
| B261    | x                  |       | 3                                               |              |           |
| B262    | x                  |       | 3                                               |              |           |
| B263    | x                  |       | 3, 4                                            |              |           |
| B264    |                    |       | 3                                               |              | x         |
| B265    |                    |       | 3                                               |              | x         |
| B266    |                    |       | 3                                               |              | x         |
| B267    |                    |       | **1**, 2, 4, 5, 6, 7, 8, 10, 11, 12             |              |           |
| B268    |                    |       | **1**, 4                                        |              |           |
| B269    | x                  |       | 3                                               |              |           |
| B270    | x                  |       | 3                                               |              |           |
| B271    | x                  |       | 3                                               |              |           |
| B272    | x                  | x     | **1**, 2, 3, 4, 5, 6, 7, 8, 10, 12, 13          |              |           |
| B273    | x                  |       | 3                                               |              |           |
| B274    |                    |       | 3                                               |              |           |
| B275    |                    |       | 3                                               |              |           |
| B276    | x                  |       | 3                                               |              |           |
| B277    |                    |       | 3                                               |              |           |
| B278    |                    |       | 3                                               |              | x         |
| B279    |                    |       | **1**, 2, 3, 6, 7, 8, 9, 10, 11, 12, 13, 14     |              |           |
| B280    |                    |       | 2, 3, 4, 5, 6, 8, 9, 10                         |              |           |
| B281    |                    |       | 3                                               |              | x         |
| B282    | x                  |       | 3                                               |              |           |
| B283    | x                  |       | 3, 4                                            |              | x         |
| B284    |                    |       | 3                                               |              |           |
| B285    | x                  |       | 3                                               |              |           |
| B286    | x                  |       | 3                                               |              |           |
| B287    |                    |       | 3                                               |              |           |
| B288    |                    |       | 3                                               |              |           |
| B289    |                    |       | 3                                               |              |           |
| B290    |                    |       | 3                                               |              |           |
| B291    |                    |       | 3                                               |              |           |
| B292    |                    |       | 3, 4, 5, 6, 7                                   |              |           |
| B293    |                    |       | 3                                               |              |           |
| B294    |                    |       | 3                                               |              |           |
| B295    |                    |       | 3                                               |              | x         |
| B296    |                    |       | 3                                               |              |           |
| B297    |                    |       | **1**, 2, 3, 5, 6, 7, 8, 10, 11, 12, 13, 14, 15 |              |           |
| B298    |                    |       | 3                                               |              |           |
| B299    |                    |       | 3                                               |              |           |
| B300    |                    |       | 3                                               |              |           |
| B301    |                    |       | 3                                               |              |           |
| B302    |                    |       | 3                                               |              |           |
| B303    |                    |       | 3                                               |              |           |
| B304    |                    |       | 3                                               |              |           |
| B305    |                    |       | 3, 4                                            |              |           |
| B306    |                    |       | 3                                               |              |           |
| B307    |                    |       | 3                                               |              |           |
| B308    |                    |       | 3                                               |              |           |
| B309    |                    |       | 3, 4                                            |              |           |
| B310    |                    |       | 3                                               |              |           |
| B311    |                    |       | 3                                               |              |           |
| B312    |                    |       | 3                                               |              | x         |
| B313    | x                  |       | 3                                               |              |           |
| B314    | x                  |       | 3                                               |              |           |
| B315    | x                  |       | 3, 4                                            |              |           |
| B316    |                    |       | 3                                               |              |           |
| B317    |                    |       | 3                                               |              | x         |
| B318    |                    |       | 3                                               |              |           |
| B319    |                    |       | 3                                               |              | x         |
| B320    |                    |       | 3                                               |              | x         |
| B321    |                    |       | 3                                               |              | x         |
| B322    |                    |       | 3                                               |              | x         |
| B323    |                    |       | 3                                               |              | x         |
| B324    | x                  |       | 3                                               |              |           |
| B325    |                    |       | 3                                               |              |           |
| B326    | x                  |       | 3                                               |              |           |
| B327    |                    |       | 3                                               |              |           |
| B328    | x                  |       | 3                                               |              |           |
| B329    |                    |       | 3, 4                                            |              |           |
| B330    |                    |       | 3                                               |              | x         |
| B331    |                    |       | 3                                               |              |           |
| B332    |                    |       | 3                                               |              |           |
| B333    |                    |       | 3                                               |              |           |
| B334    |                    |       | 3                                               |              |           |
| B335    |                    |       | 3                                               |              | x         |
| B336    |                    |       | 3                                               |              |           |
| B337    |                    |       | 3                                               |              |           |
| B338    | x                  |       | 3, 4, 5, 6, 7                                   |              |           |
| B339    | x                  |       | **1**, 4, 5, 6, 7, 8                            |              | x         |
| B340    | x                  |       | **1**, 4                                        |              |           |
| B341    | x                  |       | 3, 4                                            |              |           |
| B342    | x                  |       | 3                                               |              |           |
| B343    | x                  |       | 3                                               |              |           |
| B344    | x                  |       | 3                                               |              | x         |
| B345    | x                  |       | 3                                               |              | x         |
| B346    | x                  |       | 3                                               |              |           |
| B347    | x                  |       | 3                                               |              |           |
| B348    | x                  |       | 3                                               |              |           |
| B349    |                    |       | 3                                               |              |           |
| B350    |                    |       | 2, 4                                            |              |           |
| B351    |                    |       | 3                                               |              |           |
| B352    |                    |       | 3                                               |              |           |
| B353    |                    |       | 3                                               |              |           |
| B354    |                    |       | 3                                               |              |           |
| B355    |                    |       | 3                                               |              |           |
| B356    |                    |       | **1**, 4                                        |              |           |
| B357    | x                  |       | **1**, 2, 3, 4, 5, 7, 9, 10, 11, 12, 13, 14     |              |           |
| B358    |                    |       | 3                                               |              |           |
| B359    |                    |       | 3                                               |              |           |
| B360    |                    |       | 3                                               |              |           |
| B361    |                    |       |                                                 |              |           |
| B362    |                    |       | 3                                               |              |           |
| B363    |                    |       | 3                                               |              |           |
| B364    |                    |       | 3                                               |              |           |
| B365    |                    |       | 3                                               |              |           |
| B366    |                    |       | 3                                               |              |           |
| B367    | x                  |       | 3                                               |              |           |
| B368    | x                  |       | 3                                               |              |           |
| B369    | x                  |       | 3, 4                                            |              |           |
| B370    | x                  |       | 3                                               |              |           |
| B371    | x                  |       | 3                                               |              | x         |
| B372    | x                  |       | 3                                               |              |           |
| B373    | x                  |       | 3                                               |              |           |
| B374    |                    |       | 3                                               |              |           |
| B375    |                    |       | 3                                               |              | x         |
| B376    | x                  |       | **1**, 3, 5, 6, 7, 8, 9                         |              |           |
| B377    | x                  |       | 3                                               |              | x         |
| B378    | x                  |       | **1**-7, 12-21                                  | (8,9)(10,11) |           |
| B379    |                    |       | 3                                               |              |           |
| B380    | x                  |       | 3                                               |              |           |
| B381    |                    |       | 3                                               |              | x         |
| B382    |                    |       | 3                                               |              |           |
| B383    | x                  |       | 3                                               |              |           |
| B384    | x                  |       | 3                                               |              | x         |
| B385    | x                  |       | 3                                               |              |           |
| B386    | x                  |       | 3                                               |              |           |
| B387    |                    |       | **1**, 4                                        |              |           |
| B388    | x                  |       | 3                                               |              |           |
| B389    |                    |       | 3, 4, 5, 6, 7                                   |              |           |