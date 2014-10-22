---
layout: page
title: Steuerungssoftware
permalink: steuerungssoftware.html
---

In den folgenden Sektionen wird das Backend unseres Praktikums vorgestellt.

## moveserver
![foo](bla.jpg)



## Queue
Die eingehenden Requests werden in einer Queue (LIFO) der Länge 5 zwischengespeichert, dh die zuerst eingehenden Requests werden zuerst vom Worker abgearbeitet. Ist die Queue voll, wird der älteste Befehle verworfen.
Diese Form der Priorisierung hat sich als funktional erwiesen:
Auch in einer Testsituation, in der ein Testskript massiv viele Requests sendete, konnte ein Mensch die Steuerung, wenngleich nur mit intensivem Einsatz, beeinflussen.
