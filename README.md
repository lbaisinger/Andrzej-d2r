# Andrzej
Andrzej walczy z potworami na dwa sposoby - profit i PG.
- lista przetestowanym miejscówek w ./caves
- wymaga dobrze zdefiniowanych regionów na ekranie (battle, HP/mana bar, itp...)
- dobrze rozmieszczone waypointy (WP) to podstawa dobrego expa - poznaj resp! (sprawdź ./caves)


### LOGIKA
| <div style="width:400px">PG</div>                                                                                                                                                                                                                                               | <div style="width:400px">Profit</div>                                                                                                                                                                                          |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <div style="width:400px">Andrzej ZAPIERDALA do WP, staje na środku i zaczyna wywijać bronią + rotacja czarów. Jeśli wymaga tego konieczność, rzuca Exeta Res aby moby nie uciekały. Po wyeliminowaniu zagrożenia lootuje i idzie do następnego WP. Wymaga no-follow-mode.</div> | <div style="width:400px"> Andrzej stale sprawdza, czy na BW są jakieś potwory. Jeśli tak to atakuje, po zabiciu każdego potwora lootuje. Jeśli niebezpieczeństwo zostało wyeliminowane, idzie do WP. Wymaga follow-mode. <div> |
| <div style="width:400px"> ![](src/img/flowchart_logika_andrzeja_pg.svg) </div>                                                                                                                                                                                                  | <div style="width:400px"> ![](src/img/flowchart_logika_andrzeja_profitujacego.svg) </div>                                                                                                                                      | 

### To-Do
- [ ] GUI
- [ ] Windows support
- [ ] wywalić stare pliki GRACZA?

v2.0 log
- Zmiana szukania z pyautogui() na openCV() - kilkukrotnie szybszy Andrzej! Teraz cała pętla spokojnie mieści się w 2 sekundowym CD na czary ofensywne i zawiera 2 sprawdzenia (co 1 sek) stanu zdrowia Andrzeja (HP/MP)
- Zmodyfikowane pg_mode() - teraz przyjmuje listę hotkeyów z czarami do rotacji (póki co na AOE, tj. +2+ potwory)
- Zmodyfikowane szukanie WP w centrum - szuka w obszarze x pikseli od środka, więc nawet jak potwór stanie na WP to nie przeszkadza
- Dodany GRACZ_Profit (patrz logika poniżej), GRACZ_EK_PG.py zmienione na GRACZ_PG.py