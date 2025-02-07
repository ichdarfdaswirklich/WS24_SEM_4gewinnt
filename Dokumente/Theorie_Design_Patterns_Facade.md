
# Theorie Design  Patterns #
## Das Facade Design Pattern ##
<p><strong>Quellen:</strong> <a href="https://www.philipphauer.de/study/se/design-pattern/facade.php">philipphauer.de</a>, <a href="https://refactoring.guru/design-patterns/facade">refactoring.guru</a></p>

### Angabe ###
<p>Wählen Sie 2 Design Patterns Ihrer Wahl und umschreiben Sie diese in eigenen Worten. Die Beschreibung muss nicht besonders detailliert sein, sondern nur ganz allgemein Problem und Umsetzung der Lösung bzw. Idee dahinter beschreiben.</p>
<p>Umfang ungefähr ½ - ¾ A4 Seite pro Pattern – Sie müssen das Pattern nicht genau im Detail verstehen. Direkte 1 zu 1 Übersetzungen oder Übernahmen sind nicht erwünscht – Sie können natürlich auch eigene Grafiken zur Unterstützung einbeziehen.</p>

### Beschreibung Design Pattern ###
<p><strong>Kurzfassung:</strong> Entwurfsmuster zur Vereinfachung komplexer Schnittstellen durch eine zentrale Steuerungseinheit.</p>
<p>Das Facade Design Pattern kommt zum Einsatz, wenn Systeme mit vielen Subsystemen oder Modulen für den Client unübersichtlich oder schwer bedienbar sind. Eine <strong>Facade</strong> bietet eine zentrale Schnittstelle, die die Komplexität versteckt und eine einfach zu nutzende API bereitstellt.</p>

### Idee und Umsetzung ###
<p>Die Facade empfängt Anfragen vom Client und leitet sie an die entsprechenden Subsysteme weiter. Dabei verbirgt sie deren interne Struktur und Implementierung, wodurch der Client nicht direkt mit den Subsystemen interagieren muss. Änderungen an den Subsystemen haben dadurch weniger Auswirkungen auf den Client.</p>
<p><strong>Hinweis:</strong> Die Fassade selbst enthält keine eigene Geschäftslogik, sondern fungiert lediglich als Vermittler zwischen dem Client und den internen Modulen.</p>

![Beispielbild](https://media.geeksforgeeks.org/wp-content/uploads/20240118172253/facade-method-banner.jpg)
### Vorteile ###
<ul>
    <li><strong>Entkopplung:</strong> Der Client interagiert nur mit der Facade, nicht mit den einzelnen Modulen.</li>
    <li><strong>Vereinfachung:</strong> Die Schnittstelle wird nutzerfreundlicher und leichter verständlich.</li>
    <li><strong>Wartbarkeit:</strong> Änderungen an Subsystemen müssen nicht direkt im Client berücksichtigt werden.</li>
</ul>

<h3>Anwendungsfälle</h3>
<p>Das Facade Pattern eignet sich besonders für Systeme mit hoher interner Komplexität, bei denen eine einfache Steuerung benötigt wird.</p>
<ul>
    <li><strong>Medienabspieler:</strong> Eine Facade steuert Audio-, Video- und Anzeige-Subsysteme.</li>
    <li><strong>Datenbanksysteme:</strong> Eine Facade kapselt komplexe Datenbankzugriffe.</li>
    <li><strong>Betriebssysteme:</strong> Eine Facade für Dateioperationen und Speicherverwaltung.</li>
    <li><strong>Bibliotheken und Frameworks:</strong> Eine Facade vereinfacht die Nutzung einer umfangreichen API.</li>
</ul>


