---
layout: page
title: Steuerungssoftware
permalink: steuerungssoftware.html
---

In den folgenden Sektionen wird das Backend unseres Praktikums vorgestellt.

## moveserver
Der moveserver ist ein Pythonskript, das beim Einschalten des Raspberry gestartet wird. Dieses stellt sicher, dass die Servos zu Beginn in eine bekannte Stellung, die wir als die Standardposition bezeichnen, gebracht werden, da ein Auslesen der Position aus den Servos nicht möglich ist. Desweiteren füllt es die vom [WSGI-Skript](webserver.html) erhaltenen Requests in die Queue und startet den Worker (s.u.).


## Queue & Worker
Die eingehenden Requests werden in einer Queue (LIFO) der Länge 5 zwischengespeichert, dh die zuerst eingehenden Requests werden zuerst vom Worker abgearbeitet. Ist die Queue voll, wird der älteste Befehle verworfen.
Diese Form der Priorisierung hat sich als funktional erwiesen:
Auch in einer Testsituation, in der ein Testskript massiv viele Requests sendete, konnte ein Mensch die Steuerung, wenngleich nur mit intensivem Einsatz, beeinflussen.


