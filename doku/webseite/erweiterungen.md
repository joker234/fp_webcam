---
layout: page
title: Erweiterungen
permalink: erweiterungen.html
---

## Standby (Suspend)
Diese Funktionalität dient dazu die Kamera bei Inaktivität in einen Zustand zu bringen, in dem sie nicht mehr die Personen im Raum in filmt und dies für ebenjene Personen ersichtlich ist. Dazu wird gespeichert, wann der letzte Steuerbefehl gesendet wurde. Wird für 10 Minuten kein Steuerbefehl vorgenommen, bewegt sich die Kamera in eine Position, in der nurnoch eine Ecke der Verkleidung auf dem Bild zu sehen ist. Somit wird gewährleistet, dass für im Raum befindliche Personen erkennbar ist, ob sie gefilmt werden, und dass der Wechsel zischen Filmen und nicht-Filmen nicht so abrupt ist, da die Kamera nur recht langsam bewegt werden kann.

Dies wird im [moveserver](steuerungssoftware.html#moveserver) durch die folgende Subroutine abgedeckt:

~~~python
def suspend(move_lock,last_updated,q):
  global curr4, curr17
  suspendtime = 600 # time in seconds after that the raspi will "suspend"
  while 1:
    sleep(1)
    while curr4.value > 1000:
      if last_updated.value + suspendtime < time():
        move_lock.acquire()
        curr4.value, curr17.value = move(curr4.value, curr17.value, "right")
        move_lock.release()
      else:
        break
      sleep(.25)
    while curr17.value > 1000:
      if last_updated.value + suspendtime < time():
        move_lock.acquire()
        curr4.value, curr17.value = move(curr4.value, curr17.value, "down")
        move_lock.release()
      else:
        break
      sleep(.25)
~~~

## Reboot
Da es gelegentlich zu Abstürzen des Ethernetcontrollers kam und damit folglich keine Zugriffe auf den Server mehr möglich waren, haben wir diese Funktion implementiert. Diese überprüft in regelmäßigen Abständen, ob die Internetverbindung noch besteht und startet den Raspberry gegebenenfalls neu, damit die Verbindung wiederhergestellt wird.

Das Skript, das von einem cronjob alle paar Minuten ausgeführt wird, findet sich [hier](https://github.com/joker234/fp_webcam/blob/master/scripts/restartnetworkoff.sh).
