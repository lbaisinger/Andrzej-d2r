# Andrzej
Andrzej walczy z potworami! Teraz może działać na dwa sposoby - profit i PG.

- Zmiana szukania z pyautogui() na openCV() - kilkukrotnie szybszy Andrzej! Teraz cała pętla spokojnie mieści się w 2 sekundowym CD na czary ofensywne i zawiera 2 sprawdzenia (co 1 sek) stanu zdrowia Andrzeja (HP/MP)
- Zmodyfikowane pg_mode() - teraz przyjmuje listę hotkeyów z czarami do rotacji (póki co na AOE, tj. +2+ potwory)
- Zmodyfikowane szukanie WP w centrum - szuka w obszarze +/-2 SQM od środka, więc nawet jak potwór stanie na WP to nie przeszkadza
- Dodany GRACZ_Profit (patrz logika poniżej), GRACZ_EK_PG.py zmienione na GRACZ_PG.py

### To-Do
- [x] WP_specjal - potrzebne szczególnie do zaminy poziomów, żeby wykonywał określoną akcję (rope/shovel/ladder) oraz zapewnić, żeby Andrzej stawał DOKŁADNIE NA ŚRODKU WP (dokładnie na rope/shovel/ladder spocie)
- [ ] Generator listy waypointów (wps) - przy inicjowaniu Andrzeja zadać mu ile WP ma obecny hunt i niech robi swoje

### LOGIKA 
| Algorytm 'PG'                      | Algorytm 'Profit                        |
|------------------------------------|-----------------------------------------|
| Andrzej ZAPIERDALA do WP, staje na środku i zaczyna wywijać bronią + rotacja czarów. Jeśli wymaga tego konieczność, rzuca Exeta Res aby moby nie uciekały. Po wyeliminowaniu zagrożenia lootuje i idzie do następnego WP. Wymaga no-follow-mode. | Andrzej stale sprawdza, czy na BW są jakieś potwory. Jeśli tak to atakuje, po zabiciu każdego potwora lootuje. Jeśli niebezpieczeństwo zostało wyeliminowane, idzie do WP. Wymaga follow-mode. |
| ![](src/img/flowchart_logika_andrzeja_pg.svg) | ![](src/img/flowchart_logika_andrzeja_profitujacego.svg) |

