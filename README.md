# WS24_SEM_4gewinnt
### WS24 SEM Projektarbeit <br>
#### Team: VU, AZ


<p>Dies ist das GitHub Repository unserer WS24 SEM Projektarbeit.<br>
Ziel ist es gemeinsam das allseits bekannte 4 Gewinnt / Connect 4 Spiel in Python umzusetzen. <br>
<br>
Vorgaben hierzu wurden in der dazugehörigen Vorlesung bereitgestellt.<br>
</p>

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
<li>(welche Packages installiert werden müssen so notwendig: vorläufig Python Version 3.12.8, zu importierende Module math, numpy</li>
</ul>

#### Projektstruktur

<p>Vorgeschlagene Projektstruktur mit geplanten Modulen/Packages.<br>
Aufgrund fehlender Vorerfahrung, wurden in die Planung/ die Überlegungen folgende bereits bestehende Ressourcen herangezogen:<br>

Connectfour Repo von pvmoura <https://github.com/pvmoura/ConnectFour/tree/master> <br>

Connect-Four von erickackermann <https://github.com/erikackermann/Connect-Four/tree/master>

Connect-Four-Game Guide von askpython <https://www.askpython.com/python/examples/connect-four-game>

</p>    

<ul>
<li>main.py oder game.py - Hauptdatei mit Klassen für Spielzüge (Player oder AI)</li>
<li>players.py Modul/Package wo Spieler 1, Spieler 2 und AI in Klassen definiert werden</li>
<li>(eventuell board.py um Spielfläche in eigenem File zu definieren)</li>
<li>für tests notwendige Dateien</li>
</ul>
