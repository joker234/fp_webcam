---
layout: page
title: Webserver
permalink: webserver.html
---

## Webseite

#### mJPG-Streamer

Das Frontend ist mehrstufig aufgebaut. Der mJPG-Streamer mit Plugin für die raspicam des Raspberry Pi ([source](https://github.com/jacksonliam/mjpg-streamer)) stellt den Stream in einer selbst gebauten HTML-Seite dar. Dieser wird als [Dienst](https://github.com/joker234/fp_webcam/blob/master/scripts/moveserver) beim booten gestartet und läuft (unabhängig von den anderen Komponenten des Setups).

[![Screenshot](img/websitescreenshot500px.png "Screenshot der Webseite")](img/websitescreenshot.png)

#### jQuery

Die Webcam kann auf verschiedene Arten in horizontaler und vertikaler Richtung gedreht werden.

Die Triviale Möglichkeit, die in allen Browsern mit JavaScript funktionieren sollte ist die Bedienung über die *Buttons* auf der Webseite. Diese werden von einer Funktion unter Zuhilfenahme der JavaScript-Bibliothek [jQuery](https://jquery.com/) abgefangen. Im Hintergrund wird dann über diese Funktion eine Anfrage an den Server gestellt, unter Übermittlung der gewünschten Bewegungsrichtung.

Die intuitive und schnellste Methode die Webcam zu bewegen sind die *Pfeiltasten*. Diese werden, ähnlich wie bei den Buttons, abgefangen und die gleiche Funktion aufgerufen bzw. Anfrage gestellt. Diese Möglichkeit funktioniert ebenso in allen gängigen, aktuellen Browsern, wurde aber auch erfolgreich mit einem ein Jahr alten Browser getestet.

Außerdem gibt es (vor allem) für mobile Clients noch die dritte Variante; das *Swipen* (auch Wischen genannt). Dies wird durch die [mobile Variante](https://jquerymobile.com/) von jQuery und ein [Skript](https://github.com/joker234/fp_webcam/blob/master/code/www/swipeupdown.js) von [stackoverflow](https://stackoverflow.com/questions/17131815/how-to-swipe-top-down-jquery-mobile) bereitgestellt. In der Anwendung funktioniert dies dann wie die beiden anderen Varianten. Die Wischbewegungen werden abgefangen und dann über die selbe Funktion eine Anfrage an den Server gestellt. Die Verwendung eines modernen, aktuellen Browsers ist hier zu empfehlen, da einige Funktionen noch nicht sehr lange weit verbreitet sind.

Die mobile Variante von jQuery sorgt gleichzeitig für ein schöneres (Grund-)Design der Webseite.

Der Quelltext der JavaScript-Funktionen findet sich [hier](https://github.com/joker234/fp_webcam/blob/master/code/www/scripts.js).

#### Apache

Als Webserver wird Apache verwendet, der als sehr stabil gilt. Dieser fungiert als Instanz, die mit dem Browser des Clients kommuniziert. Sämtlicher Datenverkehr (auch zum [mJPG-Streamer](#mjpg-streamer)) läuft über Apache. Der Webserver nimmt auch die Steuerbefehle entgegen und leitet sie über ein [WSGI-Skript](https://github.com/joker234/fp_webcam/blob/master/code/app.wsgi), das eine Verbindung zum [moveserver](steuerungssoftware.html#moveserver) aufbaut, an denselben weiter. Dieses WSGI-Skript überprüft auch, ob die Bewegungsrichtung erlaubt ist. So können falsche Werte nicht an den moveserver weitergegeben werden.

[![Kontrollfluss](img/kontrollflussdiagramm500px.png "Kontrollflussdiagramm")](img/kontrollflussdiagramm.png)


## Sicherheit

Da der Raspberry Pi als ganz normaler Computer bzw. Server im öffentlichen Netz hängt, musste sich überlegt werden wie dieser gegenüber Angriffe aus dem Internet abgesichert wird.

Als Firewall wird die populäre Firewall *iptables* und zur einfacheren Konfiguriation derselben *firehol* verwendet. Diese ist so konfiguriert, dass nur Anfragen aus dem Universitätsnetz, das als sicher gilt, akzeptiert werden. Außerdem sind nur die Dienste *http* (Port 80, für den Webserver) und *ssh* (Port 22, zur Konfiguriation und Wartung) freigegeben.

Durch ständige Updates und die oben erwähnte Firewall wird gewährleistet, dass der Raspberry Pi im Internet mindestens so geschützt ist, wie die meisten anderen Server.
