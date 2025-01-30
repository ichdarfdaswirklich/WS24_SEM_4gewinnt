# Zusätzliche Projekt-Doku

<p>Hier sind alle etwaigen Ergänzungen bzw. geforderte Dokumenation laut Projektarbeits-Angabe zu finden. Viel Spaß!</p>

<p>(in Arbeit)</p>

### Planung Umsetzung

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
