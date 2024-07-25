#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Get track list(s) for MusicBrainz release ID.
"""
import os
import argparse
import json
import warnings
from time import sleep
from typing import Optional
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

RELATION_TYPES = [
    'area',
    'artist',
    'event',
    'instrument',
    'label',
    'place',
    'recording',
    'recording-level',
    'release',
    'release-group',
    'series',
    'work',
    'work-level',
    'url',
]

# region utils

def get_type_of_mbid(mbid):
    # url = f"https://musicbrainz.org/track/{mbid}"
    # try:
    #     _ = request.urlopen(url)
    #     return "track"
    # except Exception:
    #     pass
    for typ in ['recording', 'release', 'release-group', 'series', 'work', 'area', 'artist', 'event', 'genre', 'instrument', 'label', 'place', 'url',
                'rating', 'tag', 'collection', 'track', # non-core resources
                ]:
        url = f"https://musicbrainz.org/ws/2/{typ}/{mbid}"
        try:
            _ = request.urlopen(url)
            return typ
        except Exception as e:
            sleep(1)
    return "unknown"

def musicbrainz_useragent():
    mb.set_useragent(app="dcml_metadata",
                     version="0.1.0",
                     contact="johannes.hentschel@epfl.ch")

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


def get_musicbrainz_data(
        mbid: str,
        rels: Optional[str] = None,
        quick: bool = False
) -> dict:
    """ Get data from MusicBrainz API for a given MBID.

    Args:
        mbid: ID of the entity.
        rels:
            Pass a type of relation to retrieve only a list of JSON objects for that relation type.
            Can be one of 'area', 'artist', 'event', 'instrument', 'label', 'place', 'recording', 'recording-level',
            'release', 'release-group', 'series', 'work', 'work-level', or 'url'.
        quick:

    Returns:

    """
    typ = get_type_of_mbid(mbid)
    if typ == 'unknown':
        raise ValueError(f"Not a valid MusicBrainz ID: {mbid}")
    print(f"MBID {mbid} belongs to a {typ}.")
    valid_includes = VALID_INCLUDES.get(typ, [])
    valid_includes = [incl for incl in valid_includes if not incl.startswith("user")] # would require auth
    method_name = f"get_{typ}_by_id"
    method = getattr(mb, method_name)
    json_key: Optional[str] = None
    if rels:
        assert rels in RELATION_TYPES, f"Invalid relation type {rels!r}."
        rels_include = f"{rels}-rels"
        json_key = f"{rels}-relation-list"
        assert rels_include in valid_includes, f"Relation type {rels !r} not available for entity type {typ!r}."
        includes = [rels_include]
        if quick:
            warnings.warn("Argument -q/--quick is without effect when -r/--rels is used.")
    elif quick:
        includes = []
    else:
        includes = valid_includes
    json_dict = method(id=mbid, includes=includes)
    if json_key:
        selection = json_dict[typ].get(json_key)
        if not selection:
            raise KeyError(f"Key {json_key!r} not found in JSON response. Available keys: {json_dict[typ].keys()}\n"
                             f"{json_dict}")
        return selection
    return json_dict


def store_json(json_object: dict | list, target: str) -> None:
    filepath, ext = os.path.splitext(target)
    if ext == ".json":
        json_str = json.dumps(json_object, indent=2)
        #json_str = bytes(json_str, "utf-8").decode("unicode_escape")  # gets rid of escaped unicode chars
        with open(target, "w") as f:
            f.write(json_str)
    elif ext in [".csv", ".tsv"]:
        table = pd.json_normalize(json_object)
        table.to_csv(target, sep="\t" if ext == ".tsv" else ",", index=False)
    else:
        raise ValueError(f"Output file extension must be .json or .csv/.tsv, but is {ext}.")
    print(f"Metadata stored to {target}.")

def main(args):
    json_obj = get_musicbrainz_data(args.ID, args.rels, args.quick)
    if args.output:
        store_json(json_obj, args.output)
    else:
        pretty_print(json_obj)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Get track list(s) for MusicBrainz release ID.')
    parser.add_argument('ID', help='MusicBrainz ID for a release.')
    parser.add_argument("-o", "--output", help="Store metadata to this filepath. Can be a .json or .csv/.tsv path.")
    parser.add_argument("-r", "--rels",
                        choices=RELATION_TYPES,
                        help=f"When storing as .csv/.tsv, you usually want to convert one of the types of relation lists "
                             f"into a table rather than obtaining a table with a single row.")
    parser.add_argument('-q', "--quick", action="store_true", help="Retrieve only the entity, without related entities.")
    args = parser.parse_args()
    musicbrainz_useragent()
    main(args)

