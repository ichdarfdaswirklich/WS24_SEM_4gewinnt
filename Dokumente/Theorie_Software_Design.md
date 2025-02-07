# Theorie Software Design

## Aufgabe laut Angabe Projekt:

<p>Beantworten Sie die Frage in einem Dokument in Ihrem Dokumentationsbereich des Projekts. <br>
Sie beginnen als Entwickler*in in einem neuen Unternehmen und bekommen die Verantwortung für ein Modul. Das Modul ist über eine lange Zeit hinweg gewachsen und besteht nur aus sehr wenigen Klassen. Die Methoden dieser Klassen sind meist sehr lange, oftmals einige hundert Zeilen oder länger, und sie sind auch eher spärlich dokumentiert. Was für Nachteile ergeben sich für Sie durch diesen Code? Welche grundlegenden Software Design Prinzipien werden evtl. nicht eingehalten? </p>

## Antwort

<p>Probleme die sich durch das beschriebene Szenario ergeben können sind sehr vielfältig. Solange die bestehenden Methoden der wenigen Klassen genau so funktionieren wie sie funktionieren sollen UND zukünftig keinerlei Erweiterungen/Veränderungen vorgesehen sind, kann das Ganze sogar weiterhin "funktionieren". <br>
<br>
Wenn jedoch Bugs auftreten sollten, wird der Debugging Prozess sehr langwierig. Ohne entsprechende Dokumentation wird zunächst eine sehr zähe, langwierige Einarbeitungsphase in den Code notwendig sein. <br>
Da dieser nicht einzelne Funktionalitäten in eigenen Methoden umgesetzt hat, sondern mehrere in sehr lange Methoden gepackt hat, können bereits kleine Veränderungen die gesamte Methode zerbröseln lassen.
<br>
<br>
Software Design Prinzipien die hier nicht eingehalten werden sind u.A.:
  <ul>
    <li>
      SOLID Principles: Single Responsibility der Klassen wird definitiv nicht eingehalten, Interface Segregation ebenso
    </li>
    <li>DAS Design Prinzip: Da Methoden hier sehr lang sind und nur wenige Klassen, ist die Wahrscheinlichkeit, dass sich ändernde Teile und gleich bleibende Teile der Applikation/des Moduls nicht komplett umgesetzt wurde </li>
  </ul>
</p>
