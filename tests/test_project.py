import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def test_scheme_records():
    records=json.loads((ROOT/'data'/'schemes.json').read_text(encoding='utf-8'))
    assert len(records)>=5
    for r in records:
        assert r['id'] and r['name'] and r['source_url'].startswith('https://')
def test_categories_and_source_fields():
    records=json.loads((ROOT/'data'/'schemes.json').read_text(encoding='utf-8'))
    assert all(r.get('category') and r.get('summary') and r.get('application') for r in records)
