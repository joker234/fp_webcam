---
layout: page
title: Erweiterungen
permalink: erweiterungen.html
---

## Standby (Suspend)
Diese Funktionalität dient dazu die Kamera bei Inaktivität in einen Zustand zu bringen, in dem sie nicht mehr die Personen im Raum in filmt und dies für ebenjene Personen ersichtlich ist. Dazu wird gespeichert, wann der letzte Steuerbefehl gesendet wurde. Wird für 10 Minuten kein Steuerbefehl vorgenommen, bewegt sich die Kamera in eine Position, in der nurnoch eine Ecke der Verkleidung auf dem Bild zu sehen ist. Somit wird gewährleistet, dass für im Raum befindliche Personen ersichtlich ist, ob sie gefilmt werden, und dass der Wechsel zischen Filmen und nicht-Filmen nicht so abrupt ist, da die Kamera stückweise bewegt wird.

## Reboot
Da es gelegentlich zu Abstürzen des Ethernetcontrollers kam und damit folglich keine Zugriffe auf den Server mehr möglich waren, haben wir diese Funktion implementiert. Diese überprüft in regelmäßigen Abständen, ob die Internetverbindung noch besteht und startet den Raspberry gegebenenfalls neu, damit die Verbindung wiederhergestellt wird.
