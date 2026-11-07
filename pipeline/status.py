"""Last successful read per source, kept in <raw>/status.json and shown by the dashboard's data-status panel.
mark(raw_dir, key, ok, note): 'tried' is every attempt, 'at' only the successful ones."""
import json, os, datetime as dt

def mark(raw, key, ok, note=''):
    p = os.path.join(raw, 'status.json')
    try: st = json.load(open(p))
    except Exception: st = {}
    now = dt.datetime.now(dt.timezone.utc).strftime('%Y-%m-%dT%H:%MZ')
    e = st.get(key) or {}
    e['tried'] = now
    if ok: e['at'] = now
    e['ok'] = bool(ok); e['note'] = str(note)[:160]
    st[key] = e
    json.dump(st, open(p, 'w'), indent=0)
