---
layout: page
title: Steuerungssoftware
permalink: steuerungssoftware.html
---

In den folgenden Sektionen wird das Backend unseres Praktikums vorgestellt.

## Kontrollflussgraph
Zur besseren Einordnung haben wir hier noch einmal den Kontrollflussgraphen angeführt:
[![Kontrollflussdiagramm](img/kontrollflussdiagramm500px.png "Kontrollflussdiagramm")](img/kontrollflussdiagramm.png)

## moveserver
Der moveserver ist ein Pythonskript, das beim Einschalten des Raspberry gestartet wird. Zuerst einmal stellt er sicher, dass die Servos zu Beginn in eine bekannte Stellung, die wir als die Standardposition bezeichnen, gebracht werden, da ein Auslesen der Position aus den Servos nicht möglich ist. Weiterhin füllt er die vom [WSGI-Skript](webserver.html) erhaltenen Requests in die Queue und startet den Worker (s.u.). Zusätzlich führt er die [Suspend](erweiterungen.html)-Funktionalität als Subprozess aus und verwaltet deren Zeit-Variable.


## Queue & Worker
Die eingehenden Requests werden in einer Queue (LIFO) der Länge 5 zwischengespeichert, dh die zuerst eingehenden Requests werden zuerst vom Worker abgearbeitet. Ist die Queue voll, wird der älteste Befehle verworfen.
Diese Form der Priorisierung hat sich als funktional erwiesen:
Auch in einer Testsituation, in der ein Testskript massiv viele Requests sendete, konnte ein Mensch die Steuerung, wenngleich nur mit intensivem Einsatz, beeinflussen.
