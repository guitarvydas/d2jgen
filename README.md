# Parser-building SCN
WIP
## Goal
convert `d2j.ohm` into Python parser
## Progress: 
- run `./@make`
- paste generated code into `test.py` (replacing only one def `main`)
- run `python test.py`
- (it parses `test.ohm` and results in `success`)
## Files
- `ohmjsmin.ohm` grammar for parsing `d2j.ohm`
- `ohmjsmin.rwr` rewrite spec for rewriting `d2j.ohm` into Python
- `plib2.py` - parser library (set `debugprogress` and `debutrace` to True to trace the parsing)
- `kernel.drawio.json` ultimate target to parse with generated parser (not tried at this point, 2026-11-04)

## Concessions
- parenthesized alternates must use (| ... | ...) syntax instead of ( ... | ... ) 
  - makes it easier to parse and to differentate parenthesized **sequences** from parenthesized **alternates**
- `([x|y])+` nested constructs must be written as two rules `z+` and `[x|y]`
  - nested constructs can be parsed, but are more difficult for code generation
  - separating them makes code generation easy, and forces the parser to tell us what is going on
  - nested constructs would be easy to generate if the grammar used recursion instead of Kleene+ and if it generated Lisp code (nested by default) instead of
    linear code like for Python
- alternates must be written with preceding `|`, e.g. `KVorObjectPlain = | KV | Object` instead of `KVorObjectPlain = KV | Object`
  - easier to differentiate between **sequences** and **alternates** for code generation
  - the point of parsing is not only to get away with what is possible to parse, but, also to help the code generator differentiate between cases

### Ideas
- maybe it's possible to write the parser to use `&"|"` after a MatchSequence to help decide whether the MatchSequence is part of an alternation or just a plain Sequence
- but, is it worth it? What does such "improved" syntax gain? It conflates two completely different use-cases (alternation vs. sequencing)

## Related Substack Article
[SCNs - Building Them Quickly and Easily](https://programmingsimplicity.substack.com/p/scns-building-them-quickly-and-easily?r=1egdky)
