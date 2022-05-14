# Andrzej
Andrzej BEDZIE walczyl z potworami, obecnie przygotowuje się do walki
# DEFINITION #

![](src/img/updated_flowchart.svg)

The aim of this branch is to introduce an optimized script for efficient and deadly hunting with maximum dmg output.
To achieve this the main loop must be short enough to not extend any ability/spell CDs.
Since deadly hunting is a two-edged sword, healing must also be maximized.

TO-DOs:
- [x] add flowchart_idea.img
- [ ] total loop duration must be 2-2.1 s (maybe 2.1 even better to ensure the EK hits with meelee first?)
- [ ] 1 s CD for healing spells, so ideally the main loop will contain 2x status checks (is_allright() method)
- [ ] must ensure timing between each submethod (hplow check, etc.) is ~1.1 s apart, a lot of datetime checks :/

