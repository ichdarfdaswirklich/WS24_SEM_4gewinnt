# WS24_SEM_4gewinnt
### WS24 SEM Projektarbeit <br>
#### Team: VU, AZ


<p>Dies ist das GitHub Repository unserer WS24 SEM Projektarbeit.<br>
Ziel ist es gemeinsam das allseits bekannte 4 Gewinnt / Connect 4 Spiel in Python umzusetzen. <br>
<br>
Vorgaben hierzu wurden in der dazugehörigen Vorlesung bereitgestellt.<br>
</p>

### Unser 4gewinnt spielen

<p>Python Version: 3.12.8 <br>
Notwendige zu importierende Libraries/Module: <br>
<ul>
  <li>random (random, randint)</li>
  <li>math (je nach finaler Implementation nicht notwendig)</li>
  <li>numpy (je nach finaler Implementation nicht notwendig)</li>
</ul></p>
<p>Starten des Spiels über Aufruf der game.py Datei. <br>
Zu Beginn wird man aufgefordert auszuwählen ob "Mensch oder AI" als Gegner gewünscht ist. Auswahl mittels Eingabe von "M" (Mensch) oder "A" (AI). <br>
Die Spielteilnehmer sind nun abwechselnd an der Reihe die gewünschte Spaltennummer für die Platzierung des eigenen Spielsteins auszuwählen. <br>
Spieler 1 Token: X <br>
Spieler 2 und AI Token: O <br></p>
<p>Bei jedem Zug kann alternativ "0" eingegeben und das Spiel beendet werden. <br>
Wenn die Gewinnkonditionen erreicht wurden (4 in einer Reihe - horizontal, vertikal, diagonal) oder keine gültigen Züge mehr möglich sind, wird das Spiel beendet. </p>

#### GitHub Spielregeln

<ul>
<li>Commit Nachrichten sowie Dokumentation wird in Deutsch verfasst</li>
<li>Teammitglieder arbeiten aktiv über regelmäßige Commits gemeinsam am Projekt</li>
<li>Es werden Branches erstellt, auf das Remote Repository übertragen und mittels "pull request" in den main branch übertragen</li>
<li>Jegliche Dokumentation ist als "in Arbeit" zu betrachten, Änderungen vorbehalten</li>
<li>Nerven verlieren ist ab und an erlaubt</li></ul>



#### README.md Vorgaben

<ul>
<li>in 1-2 Absätzen beschreiben worum es geht.</li>
<li>danach kurz erläutern wie man das Spiel startet bzw. spielt: 2 Spieler "bespielen" das 7 Spalten breite und 6 Zeilen hohe "Spielfeld". Nacheinander darf ein Steinchen in eine der Spalten geworfen werden. Sobald 4 Steinchen der selben Person nebeneinander (auch diagonal) platziert wurden, gewinnt man.</li>
<li>(welche Packages installiert werden müssen so notwendig: Python Version 3.12.8, zu importierende Module math, numpy, random</li>
</ul>

#### Projektstruktur

<p>Vorgeschlagene Projektstruktur mit geplanten Modulen/Packages.<br>
Aufgrund fehlender Vorerfahrung, wurden in die Planung/ die Überlegungen folgende bereits bestehende Ressourcen herangezogen:<br>

Connectfour Repo von pvmoura <https://github.com/pvmoura/ConnectFour/tree/master> <br>

Connect-Four von erickackermann <https://github.com/erikackermann/Connect-Four/tree/master> <br>

Connect-Four-Game Guide von askpython <https://www.askpython.com/python/examples/connect-four-game> <br>

Connect-Four-Terminal-Application von GabrielWongAu <https://github.com/GabrielWongAu/connect-four-terminal-application> <br>

Connect-Four von HaseeGarfinkel <https://github.com/HaseebGarfinkel/Connect-Four> <br>

</p> 

<ul>
<li>main.py oder game.py - Hauptdatei mit Klassen für Spielzüge (Player oder AI)</li>
<li>players.py Modul/Package wo Spieler 1, Spieler 2 und AI in Klassen definiert werden</li>
<li>(eventuell board.py um Spielfläche in eigenem File zu definieren)</li>
<li>für tests notwendige Dateien</li>
</ul>

<p>Nähere Informationen über von dieser initialen Planung abweichenden Implementationen befinden sich im Dokumente Ordner.</p>

## Have fun!
