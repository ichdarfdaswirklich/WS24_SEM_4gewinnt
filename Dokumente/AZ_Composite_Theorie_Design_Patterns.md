# Theorie Design Patterns

## Das Composite Design Pattern

<p>Quellen: https://www.philipphauer.de/study/se/design-pattern/composite.php, https://refactoring.guru/design-patterns/composite </p>

### Angabe

<p>Wählen Sie 2 Design Patterns Ihrer Wahl und umschreiben Sie diese in eigenen Worten. Die Beschreibung muss nicht besonders detailliert sein, sondern nur ganz allgemein Problem und Umsetzung der Lösung bzw. Idee dahinter beschreiben. <br><br>
Umfang ungefähr ½ - ¾ A4 Seite pro Pattern – Sie müssen das Pattern nicht genau im Detail verstehen. Direkte 1 zu 1 Übersetzungen oder Übernahmen sind nicht erwünscht – Sie können natürlich auch eigene Grafiken zur Unterstützung einbeziehen.</p>

### Beschreibung Design Pattern


<p>Kurzfassung: Entwurfmuster für Umgang mit verschachtelten (Baum) Struktur.</p>


<p>Composite Entwurfsmuster findet anwendung in Fragestellungen/Systemen, deren grundlegende Elemente in bestimmten, hierarchischen Beziehungen zueinander stehen.<br>
Zentral ist hierbei, dass es eine gemeinsame Schnittstelle für einzelne "Elementbehälter" = Composite (Kompositum; Aggregat, Knoten) und für "atomare Elemente" (Leaf, Blatt) gibt: Die Schnittstelle Component. <br> <br>
  Hinweis zu Composite: sie delegieren Aufrufe an ihre eigenen Components. Composites bestehen aus atomaren Leafs oder zusammengesetzten Composites. <br> <br>
Diese gemeinsame Schnittstelle übernimmt die Verwaltung von Methoden die auf Composite und Leaf angewendet werden. Es wird hier nicht zwischen diesen beiden unterschieden (=sie werden einheitlich behandelt) </p>

<p>Dieses Konstrukt erlaubt es einfacher allgemeingültigen Code zu schreiben und nicht auf spezifische Anwendungsfälle für entweder Composite oder Leaf zu unterscheiden.</p>

<p>Zentrale "Strategien" zur Definition der Componentschnittstelle sind Transparenz und Sicherheit. Beide haben ihre Daseinsberechtigung. <br><br><p>

<p><b>Transparenz</b>
<br>
"Breit" definierte Componentenschnittstelle = Summe aus Leaf- und Compositemethoden. Jedoch sind viele der Compositemethoden, nicht für einzelne Leafs anwendbar/sinnvoll. Dieses Problem kann man u.A. mit "Defaultimplementierungen" der betroffenen Methoden für die Components lösen. <br>
Bsp. Defaultrückgaben: false/null, leere Collection, Exception auswerfen etc.<br>
<br> So sind für den Client alle Methoden etc. Transparent, jedoch nimmt man mitunter "sinnlosen" Methodenaufruf auf Leafs in Kauf.</p>

<p><b>Sicherheit</b>
<br>
"Schmal" definierte Componentenschnittstelle = beschreibt kleinsten gemeinsamen Nenner aus Leaf- und Compositemethoden. <br> <br>
Client erhält hohen Sicherheitsgrad, da alle Methoden die auf Componenten aufgerufen werden können, definitiv sinnvoll implementiert sind. Dafür muss ggf. ein eingeschränkter Funktionsumfang in Kauf genommen werden.
</p>

<p><b>Anwendungsfälle</b>: <br>
  Grundsätzliches Einsatzgebiet dieses Design Patterns sind Fälle, bei denen Hierarchien von Objekten abgebildet werden sollen (Bestandteile, Inhalte, Mitglieder etc.) und es dem betroffene Client ermöglicht werden soll, zusammengesetzte und einzelne Objekte einheitlich zu behandeln.</p>
  
<ul>
  <li>
    Dateisystem</li>
  <li> Menü </li>
  <li>GUIs</li>
</ul>


