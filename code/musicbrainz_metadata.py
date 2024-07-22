#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Get track list(s) for MusicBrainz release ID.
"""
import os
import argparse
import json
from urllib import request

import pandas as pd
import musicbrainzngs as mb
from musicbrainzngs import VALID_INCLUDES
import pretty_json

__author__ = "johentsch"
__copyright__ = "École Polytechnique Fédérale de Lausanne"
__license__ = "gpl3"


INCLUDE_ARGS = [
    'aliases',
    'annotation',
    'area-rels',
    'artist-credits',
    'artist-rels',
    'artists',
    'discids',
    'event-rels',
    'instrument-rels',
    'isrcs',
    'label-rels',
    'labels',
    'media',
    'place-rels',
    'recording-level-rels',
    'recording-rels',
    'recordings',
    'release-group-rels',
    'release-groups',
    'release-rels',
    'series-rels',
    'tags',
    'url-rels',
    # 'user-tags',
    'work-level-rels',
    'work-rels',
]
## user-tags and user-ratings require auth

# region utils

def get_type_of_mbid(mbid):
    url = f"https://musicbrainz.org/track/{mbid}"
    try:
        _ = request.urlopen(url)
        return "track"
    except Exception:
        pass
    for typ in ['area', 'artist', 'event', 'genre', 'instrument', 'label', 'place', 'recording', 'release', 'release-group', 'series', 'work', 'url',
                'rating', 'tag', 'collection', 'track', # non-core resources
                ]:
        url = f"https://musicbrainz.org/ws/2/{typ}/{mbid}"
        try:
            _ = request.urlopen(url)
            return typ
        except Exception:
            pass
    return "unknown"

def musicbrainz_useragent():
    mb.set_useragent(app="dcml_metadata",
                     version="0.0.1",
                     contact="dcml.annotators@epfl.ch")

# endregion utils

def pretty_print(json, style="friendly_grayscale"):
    print(pretty_json.format_json(json, style=style))

def pretty_print_all_styles(json):
    for style in pretty_json.AVAILABLE_STYLES:
        print("\n", style)
        pretty_print(json, style=style)


def get_release(mbid: str) -> dict:
    release = mb.get_release_by_id(id=mbid,
                                   includes=['recordings']
                                   )
    return release

def pprint_release(mbid: str):
    release = get_release(mbid)
    release_title = release["release"]["title"]
    print("Tracklist(s) for " + release_title)
    track_lists = get_track_lists(release)
    pretty_print(track_lists)

def print_json_styles():
    """Prints the available strings for format_json(style=) argument."""
    print(pretty_json.AVAILABLE_STYLES)

def get_track_lists(release: dict) -> dict:
    """A dictionary as returned by get_release()"""
    print(type(release))
    print(release)
    result = {}
    assert "release" in release, "Pass a release as returned by the API. First key is 'release'."
    release = release["release"]
    for medium in release["medium-list"]:
        cd = f"{medium['format']} {medium['position']}"
        track_list = {track["position"]: track["recording"] for track in medium["track-list"]}
        result[cd] = track_list
    return result


def main(args):
    mbid = args.ID
    typ = get_type_of_mbid(mbid)
    if typ == 'unknown':
        raise ValueError(f"Not a valid MusicBrainz ID: {mbid}")
    print(f"MBID {mbid} belongs to a {typ}.")
    method_name = f"get_{typ}_by_id"
    method = getattr(mb, method_name)
    includes = [] if args.quick else VALID_INCLUDES[typ]
    json_obj = method(id=mbid, includes=includes)
    if args.output:
        filepath, ext = os.path.splitext(args.output)
        if ext == ".json":
            json_str = json.dumps(json_obj, indent=2)
            json_str = bytes(json_str, "utf-8").decode("unicode_escape")
            with open(args.output, "w") as f:
                f.write(json_str)
            # with open(args.output, "w") as f:
            #     json.dump(json_obj, f, indent=2)
        elif ext in [".csv", ".tsv"]:
            table = pd.json_normalize(json_obj)
            table.to_csv(args.output, sep="\t" if ext == ".tsv" else ",")
        else:
            raise ValueError(f"Output file extension must be .json or .csv/.tsv, but is {ext}.")
        print(f"Metadata stored to {args.output}.")
    else:
        pretty_print(json_obj)





if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Get track list(s) for MusicBrainz release ID.')
    parser.add_argument('ID', help='MusicBrainz ID for a release.')
    parser.add_argument("-o", "--output", help="Store metadata to this filepath. Can be a .json or .csv/.tsv path.")
    # parser.add_argument("-r", "--rels",
    #                     help="When storing as .csv/.tsv, you usually want to convert one of the types of relation lists "
    #                          "into a table rather than obtaining a table with a single row. Available relations are:\n"
    #                          "area, artist, label, place, event, recording, release, release-group, series, work, url, instrument")
    parser.add_argument('-q', "--quick", action="store_true", help="Retrieve only the entity, no other related entities.")
    args = parser.parse_args()
    musicbrainz_useragent()
    main(args)

