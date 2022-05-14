# Andrzej
Andrzej BEDZIE walczyl z potworami, obecnie przygotowuje się do walki
# DEFINITION #
The aim of this branch is to introduce an optimized script for efficient and deadly hunting with maximum dmg output.
To achieve this the main loop must be short enough to not extend any ability/spell CDs.
Since deadly hunting is a two-edged sword, healing must also be maximized. 
Andrew must ensure appropriate timing between each status check (hplow check, manahigh etc.)

#### To-do:
- [x] add flowchart_idea.img
- [ ] total loop duration must be 2-2.1 s (maybe 2.1 even better to ensure the EK hits with meelee first?)
- [ ] 1 s CD for healing spells, so ideally the main loop will contain 2x status checks (is_allright() method)
- [ ] datetime checks for each module duration, make sure status checks are once every ~1.1 s

![](src/img/updated_flowchart.svg)

