# Andrzej
Andrzej walczy z potworami!
### DEFINITION #
Andrzej może działać na dwa sposoby - profit i PG.
1. Profit - Andrzej stale sprawdza, czy na BW są jakieś potwory. Jeśli tak to atakuje, po zabiciu każdego potwora (znika 'czerwony kwadracik' otaczający atakowanego potwora na BW) lootuje, powtarza do póki nie zabije wszystkich potworów na ekranie. Jeśli niebezpieczeństwo zostało wyeliminowane, idzie do WP. Wymaga follow monster.
2. PG - Andrzej ZAPIERDALA do WP, staje na środku jak kamień i zaczyna kręcić młynki bronią + rotacja (póki co Exori/Exori Gran). Jeśli wymaga tego konieczność rzuca Exeta Res aby moby nie uciekały. Po wyeliminowaniu zagrożenia lootuje i idzie do następnego WP. Wymaga not-follow.
 
### To-do:
- [ ] Algorytm 'Profit'
- [ ] Zamienić szukanie WP w centrum minimapy na szukanie w obszarze dookoła centrum (+/- 2-3 px), aby akceptował też sąsiednie SQMy - potrzebne na wypadek kiedy potwór stoi na WP i nie chce się przesunąć.
- [ ] Zmienić pyautogui.locateonscreen na funkcję opencv2 (15x szybszciej). Umożliwi to maksymalną optymalizację leczenia (status checks) i rotacji (exori/exori gran/exori mas).


### Algorytm 'PG'
![](src/img/updated_flowchart.svg)
