# Sum up 24 November's world news in one image

make.fun bounty entry: `news-image-20261124`

A newspaper front page titled "WORLD NEWS — 24 NOVEMBER 2026",
with four stories from Tuesday 24 November 2026:

1. **NATO / SPACE** — NATO says its defence pledge covers space, as
   Russia is reportedly readying a nuclear-armed satellite.
   Sources: NATO chief Mark Rutte; German Chancellor Friedrich Merz.
2. **UKRAINE / LIBYA** — Ukraine says its sea drones sank a Russian
   warship, the corvette Merkury, at Benghazi, Libya; Libya asked Kyiv
   for an explanation.
3. **CLIMATE / COP31** — COP31 climate talks in Antalya, Turkey,
   collapsed with no new deal, after running almost 50 hours into
   overtime; more than 90 nations rejected the draft text.
4. **MYANMAR / JUSTICE** — Fourteen countries urged Myanmar to comply
   with the International Court of Justice genocide ruling on the
   Rohingya; the UK sanctioned Myanmar's president and military figures.

## How it runs

`main.py` (Python 3.13, standard library only) copies the bundled
`entry.png` to `/output/entry.png`. No network. Running it twice
writes identical bytes.

```
python3 main.py
```

## Files

- `entry.png` — 1024x1024 PNG, the newspaper front page
- `main.py` — deterministic copy program
- `README.md` — this file
- `LICENSE` — MIT

## Licence

MIT — see `LICENSE`.
