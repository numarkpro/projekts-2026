## Testa piemēri

### Pozitīvais tests 1
- Nosaukums: Derīga pietura validācijai
- Priekšnosacījums: pieejams pieturas objekts ar `id="2091"`, `name="Ikšķiles iela"`, `direction="← no centra"`, `street="Prūšu iela"`
- Testa (darbību) soļi:
  1. izsaukt `validate_stop(stop)`
- Paredzētie rezultāti:
  - funkcija atgriež `True`

### Pozitīvais tests 2
- Nosaukums: Derīgs JSON ielādēšanai
- Priekšnosacījums: stops.json satur derīgu JSON ar lauku `stops` kā sarakstu un vienu pareizu pieturas ierakstu
- Testa (darbību) soļi:
  1. ielādēt failu ar mock vai testfailu
  2. izsaukt `load_stops()`
- Paredzētie rezultāti:
  - tiek atgriezts saraksts ar vienu pieturu
  - pieturas objekts satur `id="2091"`

### Negatīvais tests 1
- Nosaukums: Nederīgs pieturas ID validācijai
- Priekšnosacījums: pieejams pieturas objekts ar `id="0202asd"` un pārējo lauku korektu saturu
- Testa (darbību) soļi:
  1. izsaukt `validate_stop(stop)`
- Paredzētie rezultāti:
  - funkcija atgriež `Nederīgs pieturas ieraksts: {'id': '0202asd', 'name': 'Ikšķiles iela', 'direction': '→ uz centru', 'street': 'Latgales iela'}`

### Negatīvais tests 2
- Nosaukums: Sintakses kļūda JSON ielādēšanā
- Priekšnosacījums: stops.json vai mock dati satur nepareizu JSON, piemēram `{"stops": [invalid]}`
- Testa (darbību) soļi:
  1. ielādēt šo nepareizo JSON ar `load_stops()`
- Paredzētie rezultāti:
  - tiek atgriezts tukšs saraksts `[]`
  - netiek izmests neapstrādāts izņēmums


  