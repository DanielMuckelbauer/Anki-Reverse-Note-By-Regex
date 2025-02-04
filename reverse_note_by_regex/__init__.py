﻿import re
from anki.notes import Note
from aqt import mw, gui_hooks
from aqt.utils import showInfo, askUser

# addonId = 'reverse_note_by_regex'  # -> for local development
addonId = '197088151'
mappingsKey = 'mappings'
regexKey = 'regexes'
noteTypeKey = 'noteType'


def change_to_reverse(note: Note) -> None:
    config = mw.addonManager.getConfig(addonId)
    if any(re.search(regex, field) for field in note.fields for regex in config[regexKey]):
        if askUser("Should this note be converted to reverse?"):
            note.mid = mw.col.models.id_for_name(config[noteTypeKey])
            mw.col.update_note(note)
        else:
            return


gui_hooks.add_cards_did_add_note.append(change_to_reverse)

