# Party and event pricing model — Shoot 360 Denver

**Version** 1 · **Created** 2026-09-17 · **Status** Proposal for the owner to evaluate · **Supersedes** none
**Feeds** `events.html` (every price there is a yellow `class="tbd"` placeholder until the owner confirms)

## What the owner asked

Estimate the cost of a court-hour from membership revenue and opening hours (160 members × $160/month, 4 shooting
bays + 4 skills courts), then cost a 2-hour party with 30 minutes of set-up and clean-up (3 hours) plus staff at
$20/hour, with all food bought from the restaurant. Present the per-court-hour rate against a regular session. Then
price a whole-court (facility) takeover for Saturday nights after 6 PM on limited weekends.

## Inputs

| Input | Value | Source |
|---|---|---|
| Members × fee | 160 × $160 = **$25,600 / month** | owner |
| Courts | 8 (4 shooting bays + 4 skills courts) | owner |
| Hours open / week | Mon–Fri 2–9 PM (35 h) + Sat–Sun 10 AM–5 PM (14 h) = **49 h** | owner (weekday), HQ page (weekend, unconfirmed) |
| Hours open / month | 49 × 4.33 = **212 h** | derived |
| Staff | $20 / hour | owner |
| Party block | 2 h party + 0.5 h set-up + 0.5 h clean-up = **3 h** | owner |
| Drop-in yardstick | $42 per 30-minute session (owner's sheet, first block; the same sheet also shows $80) | owner |

## Result

| Line | Working | Result |
|---|---|---|
| Court-hours available / month | 8 courts × 212 h | 1,699 court-h |
| **Revenue per court-hour today** | $25,600 / 1,699 | **$15.07** |
| 2-court party, 3 h, 1 coach | 2 × 3 × $15.07 + 3 × $20 | **$150.42** cost ($25.07 per court-h) |
| Whole facility, 3 h, 2 coaches | 8 × 3 × $15.07 + 2 × 3 × $20 | **$481.70** cost ($20.07 per court-h) |
| Yardstick: a bay sold as drop-ins | $42 / 30 min × 2 | $84 per court-h at full use |
| Yardstick: a bay used by members | $160 / 8 sessions × 2 | $40 per court-h at full use |

Reading it: on average a court-hour earns $15 today because the building is not full. A party that displaces
members at 6 PM on a Tuesday costs more than $15 per court-hour in lost sessions (closer to the $40–84 yardsticks);
a Saturday-night takeover after closing costs only staff plus utilities. That is why the takeover belongs after
6 PM on Saturdays and why the 2-court party should price well above its $150 cost.

## Proposed list prices (all shown as yellow placeholders on the site)

| Product | Cost | Proposal | Comparables |
|---|---|---|---|
| 2-Court Party / Event, up to 12, 2 h + room, 1 coach | $150 | **$449** (members $399); +$20 per extra guest to 16 | Calgary tech-court party CAD $545–705 (≈ US $395–515); Kirkland/Lynnwood $495–650; Pittsburgh $500; EDH $425; Basketball Nation $400–450 |
| Full Facility Takeover, up to 24, 2 h + room, 2 coaches, Sat after 6 PM | $482 | **$1,295** (members $1,195) | Calgary full takeover CAD $905 (≈ US $660) for 3 h; Vero Beach full facility $550–575 for 2 h (smaller gym) |
| Date Night, 1 h for two, coach-run shootout | ≈ $50 | **$79** per couple; food and drink separate | no franchise comparable; the drop-in yardstick is $84 for two people-hours |
| Double Date, 1 h for four across 2 courts | ≈ $80 | **$139** | as above |

The 2-court price is 3× cost and sits inside the franchise range. The takeover is 2.7× cost and above every
comparable because it is the only product that closes the building; if the owner wants volume over margin, $995
still clears 2× cost. Corporate groups of 20+ should be quoted from the takeover price plus the restaurant's
catering.

## Rules the page assumes (owner to confirm)

50% deposit; final headcount 48 hours out; book two weeks ahead; reschedule free to 7 days out; all food and drink
from the on-site restaurant and bar, no outside food or cake; court shoes; waiver per participant; decorations off
the walls.

## Showing takeover availability when the events calendar is full

Recommendation: publish the **rule**, not the calendar. The page says "Saturday nights after 6 PM on select
weekends" and lists the next two or three open Saturdays as chips that retire themselves (`data-show-until`).
The owner edits three dates a month from the Boomtown operations sheet; the request form asks for two or three
preferred dates so the desk can steer. A live calendar embed would expose the whole fieldhouse schedule, go stale
the moment a tournament is added, and needs an integration nobody maintains.

## GST, since Calgary's prices say "+GST"

GST is Canada's federal Goods and Services Tax, 5%, added on top of the listed price. The Denver equivalent is
"plus tax": Aurora sales tax (the owner's sheet says 8%) is added at checkout, so the site says "Aurora sales tax
not included" and never bakes tax into a price.

## How to re-run

`python <scratchpad>/party_model.py` printed the table above; the same arithmetic is in this file so it can be
redone by hand. Change the member count, fee or hours and the court-hour cost moves proportionally.
