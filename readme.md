## Summary

A simple addon that matches configured regexes when adding a new note and turns the note into "Basic (and reverse)" if the regex matches.
The default configuration matches "§" with numbers (e.g. §12), intended for law students who forget to enable the correct note type when adding paragraphs :)

## Installation

Install it via AnkiWeb using the [Addon page](https://ankiweb.net/shared/info/197088151).

## Configuration

The config contains these properties:
- noteType: the note type the note should be converted to if a regex matches. Defaults to "Basic (and reverse)".
- regexes: the regexes. If one is matched, the note is converted to noteType above. 

