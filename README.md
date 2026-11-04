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

## Related Substack Article
[SCNs - Building Them Quickly and Easily](https://programmingsimplicity.substack.com/p/scns-building-them-quickly-and-easily?r=1egdky)
