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
Der moveserver ist ein Pythonskript, das beim Einschalten des Raspberry gestartet wird. Zuerst einmal stellt er sicher, dass die Servos zu Beginn in eine bekannte Stellung, die wir als die Standardposition bezeichnen, gebracht werden, da ein Auslesen der Position aus den Servos nicht möglich ist. Weiterhin füllt er die vom [WSGI-Skript](webserver.html#apache) erhaltenen Requests in die Queue und startet den Worker (s.u.). Zusätzlich führt er die [Suspend](erweiterungen.html#standby-suspend)-Funktionalität als Subprozess aus und verwaltet deren Zeit-Variable.


## Queue & Worker
Die eingehenden Requests werden in einer [Queue](http://en.wikipedia.org/wiki/Queue_%28abstract_data_type%29) (FIFO) der Länge 5 zwischengespeichert, dh die zuerst eingehenden Requests werden zuerst vom Worker abgearbeitet. Ist die Queue voll, wird der älteste Befehle verworfen.
Diese Form der Priorisierung hat sich als funktional erwiesen:
Auch in einer Testsituation, in der ein Testskript massiv viele Requests sendete, konnte ein Mensch die Steuerung, wenngleich nur mit intensivem Einsatz, beeinflussen.

Der Worker holt sich Befehle aus der Queue, sichert sich das Zugriffsrecht auf die Servos, bewegt die Servos entsprechend der Befehle (move()) und gibt die Servos wieder frei.
Hier folgt die vom Worker aufgerufene Funktion move():

~~~python
def move(curr4, curr17, direction, step=3):
  # Abfangen ungültiger Eingaben
  if not direction in ("left","right","up","down","defaultpos"):
    print "You should use left, right, up or down.\n";
    return;
  # tmp: position to move
  # nr:  Number of the GPIO-pin. 4 = vertical move, 17 = horizontal move.
  # step: Schrittweite
  tmp = None;
  nr = None;
  step = 10*step;
  if direction == "left":
    print "move %s" % direction;
  # Festlegen welcher Servo bewegt wird
    nr = 4;
  # Überprüfen ob der maximale Ausrichtungswinkel nicht überschritten wird
  # Die Zahl gibt dabei die Signallänge, mit der die Servos angesprochen
  # werden, in Mikrosekunden an
  # Wir lassen eine Signallänge von 1000 bis 2000 zu; die lässt etwa eine
  # Drehung um 90 Grad in beide Richtungen von der Mittelstellung (1500) zu
    if curr4 + step <= 2000:
      curr4 += step;
    else:
      curr4 = 2000;
    tmp = curr4;
  # [...] hier folgen dann die entsprechenden Abfragen für Rechts, Oben und Unten sowie Defaultpos
  # Fehlermeldung bei falscher Eingabe
  else:
    print "false usage of move()";
  # Drehen des entsprechenden Servo (nr) zum angegebenen Ausrichtungswinkel (tmp)
  go_servo(nr, tmp);
  # Rückgabe der neuen Positionen der Servos
  return curr4, curr17
~~~
