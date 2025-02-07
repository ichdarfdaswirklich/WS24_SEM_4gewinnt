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
  Wish us luck! </p>

### Klassen/Methoden - Umsetzung Schritt für Schritt

<ol>
  <li>VierGewinnt Klasse</li>
  <p>Umsetzung/Methoden:
  <ul>
    <li>welcome_message</li>
    <li>game_loop</li>
  </ul></p>
  <p>Konkrete Unterschiede zur initialen Planung:
  <ul>
    <li>Geplante Initialisierung der VierGewinn Klasse wurde nicht umgesetzt, da sich im Laufe des Projekts andere/bessere Varianten zur Umsetzung ergeben haben.</li>
    <li>__repr__ Methode (noch?) nicht umgesetzt</li>
    <li>Die geplante Methode start_game wurde zu gamne_loop. Diese Methode übernimmt den Aufruf der notwendigen Methoden der anderen Klassen sowie die Übergabe bestimmter Ausgaben.</li>
    <li>welcome_message wurde als Methode hinzugefügt um den Spielstart grafisch/textuell etwas von den restlichen Zügen abzugrenzen (for Fun! and for Science)</li>
  </ul>
  </p>
  
  <li>Board Klasse</li>
  <p>Umsetzung/Methoden:
    <ul>
      <li>__init__</li>
      <li>__repr__</li>
      <li>show_board</li>
      <li>check_for_win</li>
      <li>update_board</li>
    </ul>
  </p>
<p>Zuerst umgesetzte Methode - display_board als staticmethod. Da Initiale Board Generierung unserer Ansicht nach stets gleich passiert. Zusätzlich eine staticmethod mit "Begrüßungstext".</p>
<p>Konkrete Unterschiede zur initialen Planung:
<ul>
  <li>__init__ Methode fast ident wie Planung umgesetzt -> zusätzliche Parameter/Attribute (die nicht direkt übergeben werden): self.__class_gameboard initialisiert bei Erstellung des Board Objekts das Spielfeld und speichert im Laufe des Spiels den aktuellen Zustand.</li>
  <li>__repr__ Methode wurde u.A. zum Ausprobieren des Überschreibens in der Praxis erstellt (for Science!) </li>
  <li>geplante win_check Methode wurde zu check_for_win (Name gefiel besser). Gewinnüberprüfung wurde für 4 mögliche Richtungen ausgehend vom gelegten Spielstein umgesetzt.</li>
  <li>geplante reset Methode wurde nicht umgesetzt (Notwendigkeit nicht gegeben)</li>
  <li>geplante display_board Methode wurde zu show_board (Name gefiel besser)</li>
</ul>
</p>



<li>Player Klasse</li>
<p>Umsetzung/Methoden:
<ul>
  <li>__init__</li>
  <li>get_move</li>
  <li>Parameter/Attribute: player_id (Token/Spielstein), current_move (zu übergebener Zug des Player Objekts an Board)</li>
</ul>
</p>
<p>Konkrete Unterschiede zur initialen Planung:
<ul>
<li>Wurde nicht mittels abstrakter Klasse umgesetzt, da Nunserer Meinung nach nicht notwendig</li>
  <li>Initialisierung wurde im ersten Klassendiagramm nicht dediziert aufgeführt, ist jedoch für Spieler Objekt Generierung notwendig.</li>
  <li>Geplante "forfeit" Methode wurde in anderen Methoden untergebracht. Abfrage ob beendet werden soll mittels Eingabe von "0"</li>
</ul>
</p>


<li>PlayerAI von Player abgeleitete Klasse</li>
<p>Umsetzung/Methoden:
<ul>
  <li>__init__</li>
  <li>get_move</li>
    <li>Parameter/Attribute: player_id="O", current_move (zu übergebener Zug des Player Objekts an Board) -> wird über Player Klasse super().__init__ initialisiert</li>
</ul>
</p>
<p>Konkrete Unterschiede zur initialen Planung:
<ul>
  <li>Statt der initial geplanten Umsetzung über abstrakte Player Klasse, wurde PlayerAI Klasse "nur" als abgeleitete Klasse der Player Klasse umgesetzt. Diese Entscheidung hat sich für uns im Laufe der Umsetzung als praktikabel herausgestellt.</li>
    <li>Initialisierung wurde im ersten Klassendiagramm nicht dediziert aufgeführt, ist jedoch für Spieler Objekt Generierung notwendig.</li>

</ul>
</p>

</ol>
