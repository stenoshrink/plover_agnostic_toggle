#!/usr/bin/env python

from plover.translation import Translation
from plover.steno import Stroke
from plover import system

def toggle_key(translator, stroke, cmdline):
    # Toggle keys of previous stroke
    toggles = [key.strip().replace(" ","") for key in cmdline.split(',')]
    translations = translator.get_state().translations
    if not translations:
        return
    t = translations[-1]
    translator.untranslate_translation(t)
    
    keys = set(t.strokes[-1].steno_keys)
    allKeys = set(system.KEYS)
    
    for key in toggles:
        if key in keys:
            keys.remove(key)
        elif key in allKeys:
            keys.add(key)
    
    translator.translate_stroke(Stroke(keys))

def stroke_negative(translator, stroke, cmdline):
    # Toggle ALL keys of previous stroke
    translations = translator.get_state().translations
    if not translations:
        return
    t = translations[-1]
    translator.untranslate_translation(t)
    keys = set(t.strokes[-1].steno_keys)
    allKeys = set(system.KEYS)
    
    for key in allKeys:
        if key in keys:
            keys.remove(key)
        else:
            keys.add(key)
    
    translator.translate_stroke(Stroke(keys))
