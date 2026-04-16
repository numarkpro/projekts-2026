# LingoQuiz Bot

Kāds varētu būt projekta nosaukums?\
LingoQuiz Bot

Ko projekts dara vienā teikumā?\
Izglītojošs bots, kas ļauj lietotājam izveidot savu angļu valodas vārdiņu vārdnīcu un regulāri pārbauda zināšanas ar interaktīviem testiem.

Kādu problēmu šis projekts risina? (Vai tas ir rīks produktivitātei, izklaidei, datu analīze vai kas cits?)\
Rīks mācībām. Vārdiņu kalšana no burtnīcas ir garlaicīga. Eksistējošās lietotnes (Kahoots, Quizlet) bieži ir maksas vai prasa pāriet uz pārlūkprogrammu. Šeit viss notiek tieši čatā.

Kas būs šī rīka galvenais lietotājs? (Piemēram, paši studenti, uzņēmēji, spēlētāji vai datu pētnieki)\
Skolēni, kas apgūst svešvalodas, vai cilvēki, kuri vēlas atsvaidzināt zināšanas.

Kā lietotājs mijiedarbosies ar programmu (konsolē, Telegram bots, vienkāršā GUI)?\
Telegram bots sūtīs ziņas ar pogām (Inline Keyboard). Pārbaudes laikā lietotājam jāizvēlas pareizais tulkojums no variantiem.

Kādas ir 3–5 galvenās funkcijas (must-have)?\
Iespēja pievienot jaunu vārdu pāri (angļu - latviešu), kas tiek saglabāts JSON failā.
"Quiz" jeb pārbaudes režīms – bots nejaušā secībā izvēlas vārdus no vārdnīcas un piedāvā 4 atbilžu variantus.
Lietotāja statistikas uzskaite (pareizo/nepareizo atbilžu procents), izmantojot klases (OOP) vai vārdnīcas struktūru.
Pārbaude un kļūdu apstrāde – bots neļauj sākt testu, ja datubāzē nav pievienoti vismaz 4 vārdi, un neļauj ievadīt tukšus vārdus.

5 funkcionālās prasības
1. Lietotājs var pievienot jaunu vārdu pāri, ievadot angļu un latviešu vārdu, kas tiek saglabāts JSON formātā.
2. Lietotājs var sākt "Quiz" režīmu, kur bots nejaušā secībā izvēlas vārdus no vārdnīcas un piedāvā 4 atbilžu variantus.
3. Lietotājs var redzēt savu statistiku, tostarp pareizo un nepareizo atbilžu procentu, izmantojot klases vai vārdnīcas struktūru.
4. Bots pārbauda, vai datubāzē ir vismaz 4 vārdi, pirms ļauj sākt testu, un neļauj ievadīt tukšus vārdus.
5. Lietotājs var saņemt atgriezenisko saiti par katru atbildi, un pēc testa beigām saņemt kopsavilkumu par savu sniegumu.

3 nefunkcionālās prasības
1. Botam jābūt pieejamam 24/7, lai lietotāji varētu mācīties jebkurā laikā.
2. Botam jābūt ātram un responsīvam, lai nodrošinātu labu lietotāja pieredzi.
3. Datu glabāšanai jābūt drošai, lai aizsargātu lietotāju informāciju un vārdnīcu.

Vai mani aizrauj šī tēma?	3	
Projekts ir skaidri orientēts uz izglītību un valodu apguvi - ļoti aktuāla tēma, kurā redzama praktiski noderīga risinājuma ideja.

Cik viegli realizējama atbilstoši zināšanu līmenim?	4	
Telegram bot ar JSON datubāzi ir reālistiska grūtības pakāpe. Šeit ir jāizmanto Python (python-telegram-bot bibliotēka), JSON darbības un nejaušas izvēles (random), kas ir vidēja grūtības līmeņa uzdevumi.

Vai atrisina reālu problēmu?	3	
Jā, skaidri atrisina reālu problēmu - vārdiņu pārbaudīšana ģeometriski bieži ir nespēka vieta studentiem, un jūsu rīks ļauj to vienkāršot un automatizēt.

Atbilst vērtēšanas kritērijiem?	5	
Ekscelenti! Ir jasnas funkcijas, prasības, target audience, un risinājums ir konkrēts (Telegram bots, JSON, interaktīvas pārbaudes).

Demonstrējamība klasei?	5	
Ļoti labi demonstrējams! Varat tiešraides laikā iepazīstināt klasi ar botu, parādīt vārdu pievienošanu, palaist testa režīmu un rādīt statistiku.


Līdzīgi esoši risinājumi:
Quizlet
