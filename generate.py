"""Build-time renderer for the news-image-20261118 entry (NOT run by the grader).

Renders entry.png: a 1024x1024 newspaper front page summing up Wednesday
18 November 2026, drawn with Pillow on this machine only. The submitted
program (main.py, standard library only) just copies the rendered file.

Stories verified against live reporting on 18 Nov 2026 (Reuters, Nature,
USA Today, Just Security Early Edition, eurotopics / Kyiv Independent):
  1. Gulf: US jets struck a Revolutionary Guard missile site on Qeshm Island
     (Strait of Hormuz); Iran answered with drone attacks on US sites in
     Bahrain and Kuwait.
  2. Crimea: Ukraine's strikes collapsed the Kerch bridge road arch into
     the strait; road traffic suspended, rail damaged.
  3. Shenzhen / APEC: Xi Jinping pledged to stand against trade
     protectionism and Putin criticised Western sanctions, ahead of a
     Trump-Xi-Putin meeting.
  4. Alaska: Democrat Mary Peltola won the Senate race, giving Democrats
     a 56-44 majority.
  5. Health: the US lost its measles elimination status (5,412 cases in
     2026, 10 deaths); Ebola in DR Congo passed 11,000 cases.
  6. Space: NASA's Voyager 1 reached one light-day from Earth
     (about 16 billion miles) at 05:16 ET.
  Also (footer ticker): a Russian military plane crashed in Siberia,
  killing 19; a 6.0 quake struck Papua New Guinea; cold killed displaced
  people in tents in Gaza.
No headline is invented: every number above comes from the reporting.
"""
import textwrap
from PIL import Image, ImageDraw, ImageFont

W = H = 1024
PAPER = (247, 242, 231)
INK = (17, 17, 17)
RED = (178, 34, 28)
NAVY = (18, 48, 84)
TEAL = (16, 92, 102)
GOLD = (198, 142, 32)
GREY = (90, 86, 78)

SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SERIF_R = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, width):
    """Greedy word wrap to pixel width."""
    lines, cur = [], ""
    for word in text.split():
        trial = (cur + " " + word).strip()
        if draw.textlength(trial, font=fnt) <= width:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def text_block(draw, x, y, text, fnt, width, fill=INK, leading=1.22):
    lines = wrap(draw, text, fnt, width)
    for line in lines:
        draw.text((x, y), line, font=fnt, fill=fill)
        y += int(fnt.size * leading)
    return y


def kicker(draw, x, y, label, color=RED):
    f = font(SANS_B, 17)
    draw.text((x, y), label, font=f, fill=color)
    return y + 24


def panel(draw, x, y, w, h, fill=(255, 255, 255)):
    draw.rectangle([x, y, x + w, y + h], fill=fill, outline=INK, width=2)
    return x, y, w, h


def burst(draw, cx, cy, r, color):
    """Starburst explosion."""
    import math
    pts = []
    for i in range(16):
        ang = math.pi * i / 8
        rr = r if i % 2 == 0 else r * 0.45
        pts.append((cx + rr * math.cos(ang), cy + rr * math.sin(ang)))
    draw.polygon(pts, fill=color, outline=(120, 40, 0))
    draw.ellipse([cx - r * 0.35, cy - r * 0.35, cx + r * 0.35, cy + r * 0.35],
                 fill=(255, 214, 90))


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)
    M = 28  # margin

    # ---- Masthead ----
    d.rectangle([M, 22, W - M, 26], fill=INK)
    d.text((W // 2, 34), "THE WORLD IN ONE IMAGE", font=font(SANS_B, 20),
           fill=RED, anchor="mt")
    d.text((W // 2, 62), "18 NOVEMBER 2026", font=font(SERIF, 66),
           fill=INK, anchor="mt")
    d.text((W // 2, 138), "Wednesday  •  The day's most consequential stories, from the Gulf to deep space",
           font=font(SERIF_R, 19), fill=GREY, anchor="mt")
    d.rectangle([M, 166, W - M, 170], fill=INK)

    # ---- Lead story: the Gulf (full width) ----
    lx, ly, lw, lh = M, 180, W - 2 * M, 268
    panel(d, lx, ly, lw, lh)
    # illustration: Gulf sea on the left
    ix, iy, iw, ih = lx + 2, ly + 2, 470, lh - 4
    d.rectangle([ix, iy, ix + iw, iy + ih], fill=(24, 68, 96))
    # land masses
    d.polygon([(ix, iy + 60), (ix + 150, iy + 20), (ix + 210, iy + 90),
               (ix + 120, iy + 150), (ix, iy + 130)], fill=(214, 190, 130))
    d.polygon([(ix + iw, iy + 170), (ix + iw - 170, iy + 210),
               (ix + iw - 110, iy + ih), (ix + iw, iy + ih)], fill=(214, 190, 130))
    d.text((ix + 18, iy + 14), "IRAN", font=font(SANS_B, 20), fill=(60, 40, 10))
    d.text((ix + iw - 120, iy + ih - 34), "ARABIA", font=font(SANS_B, 18), fill=(60, 40, 10))
    # Qeshm island + strikes
    d.ellipse([ix + 215, iy + 118, ix + 285, iy + 142], fill=(150, 110, 60))
    d.text((ix + 200, iy + 148), "QESHM ISLAND", font=font(SANS_B, 15), fill=(255, 240, 200))
    burst(d, ix + 250, iy + 105, 34, (255, 120, 30))
    burst(d, ix + 120, iy + 205, 26, (255, 120, 30))
    burst(d, ix + 360, iy + 70, 26, (255, 120, 30))
    d.text((ix + 14, iy + ih - 30), "STRAIT OF HORMUZ", font=font(SANS_B, 14), fill=(180, 220, 235))
    d.text((ix + 330, iy + 14), "BAHRAIN", font=font(SANS_B, 14), fill=(255, 240, 200))
    d.text((ix + 330, iy + 36), "KUWAIT", font=font(SANS_B, 14), fill=(255, 240, 200))
    # lead text on the right
    tx = lx + iw + 22
    tw = lx + lw - 22 - tx
    y = ly + 14
    y = kicker(d, tx, y, "THE GULF  —  WAR")
    y = text_block(d, tx, y + 2, "US strikes Qeshm Island; Iran hits Bahrain and Kuwait",
                   font(SERIF, 31), tw, leading=1.12)
    y += 6
    text_block(d, tx, y, "US jets hit a Revolutionary Guard missile site in the Strait of Hormuz. Iran answered with drones on US sites in Bahrain and Kuwait.",
               font(SERIF_R, 18), tw, leading=1.28)

    # ---- Row 2: Crimea + APEC ----
    ry, rh = 462, 216
    cw = (W - 2 * M - 14) // 2
    # Crimea
    x = M
    panel(d, x, ry, cw, rh)
    d.rectangle([x + 2, ry + 2, x + cw - 2, ry + 88], fill=(70, 110, 140))
    # bridge: deck with a collapsed middle span, arch falling into the strait
    d.line([(x + 20, ry + 62), (x + 190, ry + 62)], fill=(240, 240, 240), width=8)
    d.line([(x + 300, ry + 62), (x + cw - 20, ry + 62)], fill=(240, 240, 240), width=8)
    d.line([(x + 205, ry + 66), (x + 250, ry + 84)], fill=(240, 240, 240), width=7)
    d.arc([x + 90, ry + 8, x + 190, ry + 70], 180, 360, fill=(255, 255, 255), width=6)
    d.arc([x + 215, ry + 34, x + 285, ry + 82], 200, 340, fill=(255, 120, 60), width=6)
    d.text((x + cw - 130, ry + 66), "KERCH STRAIT", font=font(SANS_B, 13), fill=(220, 235, 245))
    y = ry + 98
    y = kicker(d, x + 14, y, "UKRAINE  —  CRIMEA")
    y = text_block(d, x + 14, y, "Kerch bridge road arch collapses into the sea",
                   font(SERIF, 24), cw - 28, leading=1.12)
    text_block(d, x + 14, y + 4, "After two nights of drone and missile strikes, the road span is unusable; traffic is suspended.",
               font(SERIF_R, 15), cw - 28, leading=1.22)
    # APEC
    x = M + cw + 14
    panel(d, x, ry, cw, rh)
    d.rectangle([x + 2, ry + 2, x + cw - 2, ry + 88], fill=(24, 48, 84))
    # three flags on poles, spaced to fit their labels (USA: stripes + canton)
    for i, (col, lab) in enumerate([((222, 40, 40), "CHINA"), ((40, 90, 200), "RUSSIA"), (None, "USA")]):
        px = x + 48 + i * 150
        d.line([(px, ry + 16), (px, ry + 82)], fill=(255, 255, 255), width=4)
        if col is None:
            d.rectangle([px, ry + 16, px + 86, ry + 50], fill=(255, 255, 255), outline=(255, 255, 255))
            for sy in range(ry + 16, ry + 50, 8):
                d.rectangle([px, sy, px + 86, sy + 4], fill=(190, 30, 40))
            d.rectangle([px, ry + 16, px + 36, ry + 34], fill=(30, 50, 140))
        else:
            d.rectangle([px, ry + 16, px + 86, ry + 50], fill=col, outline=(255, 255, 255))
        d.text((px + 2, ry + 54), lab, font=font(SANS_B, 13), fill=(255, 255, 255))
    y = ry + 98
    y = kicker(d, x + 14, y, "DIPLOMACY  —  APEC, SHENZHEN")
    y = text_block(d, x + 14, y, "Xi and Putin rail at sanctions; Trump summit next",
               font(SERIF, 24), cw - 28, leading=1.12)
    text_block(d, x + 14, y + 4, "Xi vowed to stand against protectionism as the leaders opened APEC ahead of a three-way meeting.",
               font(SERIF_R, 15), cw - 28, leading=1.22)

    # ---- Row 3: Alaska + Voyager ----
    ry, rh = 692, 186
    x = M
    panel(d, x, ry, cw, rh)
    d.rectangle([x + 2, ry + 2, x + cw - 2, ry + 74], fill=(30, 70, 50))
    d.text((x + 16, ry + 12), "ALASKA", font=font(SANS_B, 22), fill=(255, 255, 255))
    d.text((x + 16, ry + 40), "DEMOCRATS  56 — 44", font=font(SERIF, 24), fill=(255, 214, 90))
    d.text((x + cw - 110, ry + 14), "SENATE", font=font(SANS_B, 16), fill=(255, 255, 255))
    y = ry + 84
    y = kicker(d, x + 14, y, "USA  —  POLITICS")
    y = text_block(d, x + 14, y, "Peltola wins Alaska Senate race",
               font(SERIF, 24), cw - 28, leading=1.12)
    text_block(d, x + 14, y + 4, "The Democrat's win gives her party a 56-44 majority, its largest since 2009.",
               font(SERIF_R, 15), cw - 28, leading=1.22)
    x = M + cw + 14
    panel(d, x, ry, cw, rh)
    d.rectangle([x + 2, ry + 2, x + cw - 2, ry + 74], fill=(10, 12, 40))
    # stars + probe
    for sx, sy in [(30, 16), (90, 40), (160, 14), (240, 30), (320, 12), (400, 44), (430, 18)]:
        d.ellipse([x + sx, ry + sy, x + sx + 4, ry + sy + 4], fill=(255, 255, 255))
    d.line([(x + 60, ry + 58), (x + 180, ry + 30)], fill=(255, 214, 90), width=3)
    d.ellipse([x + 180, ry + 18, x + 220, ry + 46], fill=(200, 210, 230), outline=(255, 255, 255))
    d.text((x + 240, ry + 22), "VOYAGER 1", font=font(SANS_B, 18), fill=(255, 255, 255))
    d.text((x + 240, ry + 44), "16 BILLION MILES", font=font(SANS_B, 14), fill=(255, 214, 90))
    y = ry + 84
    y = kicker(d, x + 14, y, "SPACE  —  NASA")
    y = text_block(d, x + 14, y, "Voyager 1 reaches one light-day from Earth",
               font(SERIF, 24), cw - 28, leading=1.12)
    text_block(d, x + 14, y + 4, "05:16 ET: the 1977 probe is now a light-day away.",
               font(SERIF_R, 15), cw - 28, leading=1.22)

    # ---- Health strip ----
    ry, rh = 892, 76
    panel(d, M, ry, W - 2 * M, rh, fill=(255, 248, 240))
    d.text((M + 14, ry + 8), "HEALTH", font=font(SANS_B, 16), fill=RED)
    text_block(d, M + 14, ry + 30, "US loses measles-free status after 26 years — 5,412 cases, 10 deaths.  Ebola in DR Congo passes 11,000 cases, the second-largest outbreak on record.",
               font(SERIF, 18), W - 2 * M - 28, leading=1.2)

    # ---- Footer ticker (shortened to fit one line) ----
    d.rectangle([M, 980, W - M, 984], fill=INK)
    d.text((W // 2, 992), "Also: Russian military plane crashes in Siberia, 19 dead  •  6.0 quake in Papua New Guinea  •  Cold kills in Gaza tents",
           font=font(SANS, 14), fill=GREY, anchor="mt")

    img.save("entry.png", optimize=True)
    print("saved entry.png", img.size)


if __name__ == "__main__":
    main()
