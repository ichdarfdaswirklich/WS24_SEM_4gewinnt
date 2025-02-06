# Zusätzliche Projekt-Doku

<p>Hier sind alle etwaigen Ergänzungen bzw. geforderte Dokumenation laut Projektarbeits-Angabe zu finden. Viel Spaß!</p>

<p>(in Arbeit)</p>

## Planung Umsetzung

<p>Initiale Überlegungen der zu erstellenden Klassen wurden grafisch mittels DrawIO umgesetzt. Siehe .drawio und .png Files unter Dokumente.</p>

<p>Hauptklasse/Main -> "VierGewinnt". Bezieht von Klasse "Board" notwendige Methoden bzgl. Spielfeld, und von den von "Players" abgeleiteten Klassen die entsprechenden Züge. <br>
Methoden: start_game (ggf. mit Begrüßungstext, Anleitung wie zu spielen ist etc)</p>

<p> Klasse "Player" als abstrakte Klasse definieren und Klasse "HumanPlayer" und "AI" daraus ableiten. <br>
Player Methoden: place_token (Spielstein legen)
<br>
Spezielle Methoden HumanPlayer Klasse: forfeit (Spiel beenden/aufgeben)
</p>

<p> Klasse "Board" für das 4 gewinnt Spielfeld. <br>
Methoden: display_board (aktuelles Board anzeigen), reset (Board leeren), win_check (Abfrage ob Winning Condition vorliegt oder nicht)</p>

## Was bei der Umsetzung aus der Planung wurde....

<p>Da die Mitwirkenden in diesem Projekt davor noch nie ein in sich geschlossenes "Programm"/Spiel entwickelt haben, kam es bereits in den ersten Schritten der Planungsumsetzung zu einigen Änderungen. <br>
Wie im README.md beschrieben, haben wir auf bereits bestehende Ressourcen als Unterstützung zurückgegriffen. Dieses Projekt versteht sich daher als eigene Umsetzung der gesichteten ConnectFour Python Projekte. Unser Ziel war und ist es, soviel wie möglich ohne diese "Stützräder" zu schaffen. Wo nötig, nutzen wir diese jedoch, um überhaupt ein Basisverständnis uns zu erarbeiten. <br>
Die jeweiligen Code Abschnitte sind mit Quellenverweisen gekennzeichnet.</p>
<p>
  Was haben wir uns nun nach der initialen Grobplanung gedacht? Was haben wir gemacht?<br>
  Zunächst haben wir uns vorerst dazu entschieden, so wenig "Zusatzmodule"/Libraries wie nötig zur Umsetzung zu verwenden. So verlockend die Aussicht auf ein grafisch ansprechendes mittels PyGame o.Ä. umgesetzen Ergebnis auch klingt, werden wir auf den Charme einer Terminal Implementation des Spiels setzen. <br>
  <br>
  Wish us look! </p>

### Klassen/Methoden - Umsetzung Schritt für Schritt

<ol><li>Board</li>
<p>Zuerst umgesetzte Methode - display_board als staticmethod. Da Initiale Board Generierung unserer Ansicht nach stets gleich passiert. Zusätzlich eine staticmethod mit "Begrüßungstext".</p>

<li>(klasse 2)</li>
<p>(Veränderungen klasse 2 von initialer Planung) <br>
(Veränderungen bestimmter Methoden)</p>

<li>(klasse 3)</li>
<p>(Veränderungen klasse 3 von initialer Planung)
<br>
(Veränderungen bestimmter Methoden)</p>

</ol>
