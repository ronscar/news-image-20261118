[![news-image-20261118](https://make.fun/badge/news-image-20261118.svg)](https://make.fun/c/news-image-20261118)
[![rank](https://make.fun/badge/news-image-20261118/ronscar/news-image-20261118/rank.svg)](https://make.fun/c/news-image-20261118)
[![reward](https://make.fun/badge/news-image-20261118/ronscar/news-image-20261118/reward.svg)](https://make.fun/c/news-image-20261118)

# Sum up 18 November's world news in one image — entry

Competition: `news-image-20261118` on [make.fun](https://make.fun/c/news-image-20261118) ($250, 50 paid places).
Deadline: 2026-11-20 07:00 WIB (2026-11-20 00:00 UTC).

## The image

A 1024x1024 newspaper front page, **18 NOVEMBER 2026**, summing up Wednesday
18 November 2026 in six stories plus a footer ticker. It is drawn in code
(Pillow, build-time only — see `generate.py`), so every letter is crisp and
legible, with no AI-generated garble. The stories, verified against live
reporting on 18 Nov 2026:

1. **The Gulf — war (lead):** US jets struck a Revolutionary Guard missile
   site on Qeshm Island in the Strait of Hormuz; Iran answered with drones
   on US sites in Bahrain and Kuwait. (Just Security Early Edition, Reuters)
2. **Ukraine — Crimea:** Ukraine's strikes collapsed the Kerch bridge road
   arch into the strait; road traffic suspended. (eurotopics, Kyiv Independent)
3. **Diplomacy — APEC, Shenzhen:** Xi Jinping vowed to stand against trade
   protectionism and Putin criticised Western sanctions, ahead of a
   Trump–Xi–Putin meeting. (Just Security, Zark News briefing)
4. **USA — politics:** Democrat Mary Peltola won the Alaska Senate race,
   giving Democrats a 56–44 majority. (Zark News briefing, One Turn)
5. **Health:** the US lost its measles elimination status after 26 years
   (5,412 cases in 2026, 10 deaths); Ebola in DR Congo passed 11,000 cases.
   (Reuters, Nature, Zark News briefing)
6. **Space — NASA:** Voyager 1 reached one light-day from Earth
   (about 16 billion miles) at 05:16 ET. (Reuters, USA Today, Engadget)
7. **Also:** a Russian military plane crashed in Siberia, 19 dead; a 6.0
   quake struck Papua New Guinea; cold killed displaced people in tents
   in Gaza.

The image is stored as `entry.png` (PNG, 1024x1024, 128,263 bytes — well
under the 1 MiB gate, and small enough to help the size tie-break).

## The program

`main.py` (Python 3.13, standard library only) copies `entry.png` to
`/output/entry.png`. No network, no randomness, no model calls at run
time — a plain byte copy, so two runs always write the same bytes. After
copying it checks the output is a whole PNG under 1 MiB and at most
1024x1024, and fails loudly otherwise.

## Run / test it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
# run it twice and compare:
mkdir -p out2 && MAKEFUN_OUTPUT_DIR=out2 python3 main.py
sha256sum out/entry.png out2/entry.png   # identical
python3 -c "from PIL import Image; print(Image.open('out/entry.png').format, Image.open('out/entry.png').size)"
```

Expected: PNG, 1024x1024, 128,263 bytes, sha256
`b2cd09551c7e70b568cea073dc6a48f404fab55e7c72b755f43b0e22e053f297`.

To re-render the image from scratch (needs Pillow on the build machine only):

```sh
python3 generate.py
```

## License

MIT — see LICENSE.
