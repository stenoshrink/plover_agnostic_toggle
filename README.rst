Plover Agnostic Toggle
======================
*Adds a universal retrospective toggle macro to Plover.*

**============MACROS============**

**TOGGLE_KEY**

``=toggle_key:Key_A,Key_B,....``

Toggles keys A, B, etc. in prior stroke. The keys are written with their implicit hyphen. This means that keys in the beginning of steno order are written with a "-" to the right, and those towards the end are written with a "-" to the left. See examples for clarification.

Examples:

``=toggle_key:S-``

This toggles the S-key at the start of steno order in the prior stroke. For instance, STAR becomes TAR, and RAU becomes SRAU.

``=toggle_key:*``

This mimics the effect of the {*} macro (also known as =toggle_asterisk). Note the absense of a hyphen.

``=toggle_key:R-,-R``

This toggles both R-keys in steno order. For instance, if the preceeding stroke was HRUF, this macro replaces that with HUFR.

**STROKE_NEGATIVE**

``=stroke_negative``

Toggles ALL keys in steno order, effectively creating a "negative" stroke. I added this for the lols, but maybe someone will find it useful.

**============NOTES============**

This plugin is system-agnostic, so it can be used with whatever system you are using with Plover. I use the Palantype system, for which ``=toggle_key:-^`` is a useful macro. Note that -^ is a key not found in standard English stenotype.
