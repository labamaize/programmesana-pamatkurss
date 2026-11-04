# Koda lauzējs
Autors: **Meldra Visendorfa** jeb **labamaize**

## Palaišanas instrukcija
- Caur savu termināli

## Algoritma skaidrojums jeb O(log n)
Tiek izmantota binārā meklēšana - dators meklēšanas lauku katrā gājienā samazina uz pusi.
- 100 skaitļiem vajag lielākais 7 gājienus, lai atrastu pareizo skaitli. Tas ir izskaidrojams pavisam vienkārši - ar logaritma palīdzību, jo  \(\log_2(100)\) ir ~6.6, bet to noapaļojot uz augšu (svarīgi ir apaļot uz augšu, lai nekādas vērtības nepazaudētu) iegūst 7.
- 1000 skaitļiem vajag lielākais 10 gājieni, jo \(\log_2(1000)\) ir ~9.9 un noapaļojot iegūst 10.

## Testa piemērs ar pretrunīgu spēli
Mans minējums ir 50.
Vai tas ir tavs skaitlis? Vai tas ir Lielāks/Mazāks/Pareizs? L/M/P:M
Mans minējums ir 25.
Vai tas ir tavs skaitlis? Vai tas ir Lielāks/Mazāks/Pareizs? L/M/P:L
Tā nav opcija!
Mans minējums ir 37.
Vai tas ir tavs skaitlis? Vai tas ir Lielāks/Mazāks/Pareizs? L/M/P:L
Tā nav opcija!
Mans minējums ir 43.
Vai tas ir tavs skaitlis? Vai tas ir Lielāks/Mazāks/Pareizs? L/M/P:L
Tā nav opcija!
Mans minējums ir 46.
Vai tas ir tavs skaitlis? Vai tas ir Lielāks/Mazāks/Pareizs? L/M/P:L
Tā nav opcija!
Mans minējums ir 48.
Vai tas ir tavs skaitlis? Vai tas ir Lielāks/Mazāks/Pareizs? L/M/P:L
Tā nav opcija!
Mans minējums ir 49.
Vai tas ir tavs skaitlis? Vai tas ir Lielāks/Mazāks/Pareizs? L/M/P:L
Tā nav opcija!
Tavi apgalvojumi nesakrīt! Ja negribi sadarboties, es beidzu spēli!