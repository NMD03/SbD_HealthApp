# Dokumentation SbD - Projekt HealthApp <!-- omit in toc -->

## Inhaltsverzeichnis <!-- omit in toc -->
- [Technologien und Tools](#technologien-und-tools)
  - [Django](#django)
  - [Gunicorn](#gunicorn)
  - [Nginx](#nginx)
  - [Docker](#docker)
  - [PostgreSQL](#postgresql)
- [Architektur](#architektur)
- [Schutzobjekte und Schutzziele](#schutzobjekte-und-schutzziele)
- [Risikoregister](#risikoregister)
- [Implementierung](#implementierung)
  - [User Registrierung](#user-registrierung)
    - [E-Mail Bestätigung](#e-mail-bestätigung)
  - [User Login](#user-login)
  - [Datei Verschlüsselung](#datei-verschlüsselung)
  - [](#)
- [Testplan](#testplan)
- [Testergebnisse](#testergebnisse)

## Technologien und Tools
### Django
Django ist ein High-Level-Python-Webframework, das eine schnelle Entwicklung und ein sauberes, pragmatisches Design fördert. Es wurde von erfahrenen Entwicklern erstellt und nimmt Ihnen einen Großteil der Webentwicklung ab, sodass Sie sich auf das Schreiben Ihrer App konzentrieren können, ohne das Rad neu erfinden zu müssen. Es ist kostenlos und Open Source.
### Gunicorn
Gunicorn ist ein Python-WSGI-HTTP-Server für UNIX. Der Gunicorn-Server ist weitgehend kompatibel mit verschiedenen Web-Frameworks, ist vergleichsweise einfach implementiert, verbraucht wenig Serverressourcen und ist vergleichsweise schnell
### Nginx
Nginx (Engine X) ist ein Open-Source-Webserver, der für die Verarbeitung von HTTP-Anfragen und die Bereitstellung von Inhalten konzipiert ist. Nginx ist ein beliebter Webserver, der für seine hohe Geschwindigkeit und seine Fähigkeit bekannt ist, große Anfragen zu verarbeiten. Nginx ist ein beliebter Webserver, der für seine hohe Geschwindigkeit und seine Fähigkeit bekannt ist, große Anfragen zu verarbeiten.
### Docker
Docker ist eine Software, die es Entwicklern ermöglicht, Anwendungen in isolierten Umgebungen zu erstellen, zu testen und zu bereitstellen.
### PostgreSQL
PostgreSQL ist ein objektrelationales Datenbankmanagementsystem (ORDBMS) mit dem Fokus auf Standardskonformität und Erweiterbarkeit.

## Architektur
![Alt text](./img/Architektur.png)
## Schutzobjekte und Schutzziele
![Alt text](/img/Schutzobjekte1.png)
![Alt text](/img/Schutzobjekte2.png)
## Risikoregister

![Alt text](/img/R1.png)
![Alt text](/img/R2.png)
![Alt text](/img/R3.png)
![Alt text](/img/R4.png)
![Alt text](/img/R5.png)
![Alt text](/img/R6.png)
![Alt text](/img/R7.png)
![Alt text](/img/R8.png)
![Alt text](/img/R9.png)
![Alt text](/img/R10.png)
![Alt text](/img/R11.png)
![Alt text](/img/R12.png)
![Alt text](/img/R13.png)
![Alt text](/img/R14.png)
![Alt text](/img/R15.png)
![Alt text](/img/R16.png)


## Implementierung

### User Registrierung
Ein User registiert sich bei der Applikation mit seinen persönlichen Daten und einer gültigen E-Mail. Bei der Angabe des Passworts müssen festgelegte Passwortregeln beachtet werden. 

Das Passwort darf den Angaben zu den persönlichen Daten nicht zu ähnlich sein. Es  muss aus mindestens 8 Zeichen bestehen. Auch sollte das Passwort  kein häufig verwendetes Passwort sein und es darf nicht ausschließlich aus Zahlen bestehen.

#### E-Mail Bestätigung
Registirerung eines Users wird erst durch die Validierung eines Accounts anhand der E-Mail möglich. 

Dies wurde implementiert durch Django-Verify-Email 2.0.3.
Dazu wird ein Verifizierungslink generiert und zu der angegebenen Nutzer E-Mail-Adresse geschickt. Die Verifizierung geschieht dann über einen gehasten Token der in der Email mitgeliefert wird und den User eindeutig identifiziert.

### User Login
Zum einloggen wird die Kombination aus einem Benutzernamen und Passwort benötigt. 

### Datei Verschlüsselung
Alle Dateien werden vor dem abspeichern mit AES-CTR verschlüsselt. Bei einem Data Breach können die Daten somit nicht gelesen werden.

### Einschränkungen beim File-Upload
Um den Fiel-Upload etwas einzuschränken und Risiken zu mindern aber auch gleichzeitig die Funktionalität zu bewahren wurden zwei Einschränkungen implementiert. Es wird die File-Größe auf maximal 10 MB beschränlz und nur Dateien des Typs PDF zugelassen. Alle anderen Datentypen können nicht hochgeladen werden. Anpassungen können jedoch je nach ANforderung ohne Probleme durch das setzen eines Parameters implementiert werden.

### Session-Management
Bei jeder Authentifizierung wird eine neue Session-ID erstellt, die nicht in der URL zu finden ist.

### Clickjacking Protection
Django besitzt die sog. X-Frame-Options middleware. 
Diese verhindert, dass Seiten innerhalb eines Frames gerendert werden 
Hierbei werden die X-Frame-Options Header für alle Responses gesetzt.
Standardmäßig wird der Header auf DENY gesetzt. Damit blockiert der Browser das Laden der Ressource in einem Frame, unabhängig davon, von welcher Website die Anfrage stammt.

### Object Relational Mapper - ORM
Datenbank interaktion ohne SQL Statements werden im Code über Python Klassen realisiert. Querys werden mithilfe von Query Parameterization erstellt um SQL Injection zu verhindert.

### Cross Site Scripting Protection
Um den Schutz zu implementieren wurden folgende UMformungen definiert:
Automatic HTML escaping

'<' is converted to &lt

'>' is converted to &gt

' (single quote) is converted to &#x27

" (double quote) is converted to &quot

& is converted to &amp

### Cross site request forgery (CSRF) protection
In jedem POST request muss ein Secret vom Nutzer mitgeschickt werden, welches überprüft wird.
Dadurch wird sichergestellt, dass ein böswilliger Benutzer ein POST-Formular auf der Website nicht „wiederholen“ kann und einen anderen angemeldeten Benutzer dazu bringt, dieses Formular unwissentlich zu übermitteln. Der böswillige Benutzer müsste das Geheimnis kennen, das benutzerspezifisch ist (unter Verwendung eines Cookies.

### SSL/HTTPS
Die Anwendung läuft hinter HTTPS und mit verschlüsselte Kommunikation.

### Password Hashing
Alle Passwörter werden mit SHA356 gehasht. Hierfür wird der [PBKDF2 Algorithmus](https://de.wikipedia.org/wiki/PBKDF2) verwendet.

## Funktionalitäten

### Passwort Reset
Die User haben die Möglichkeit ihr Passwort jederzeit zuändern.
Über ihre E-Mail Adresse können User ein neues Passowrt erstellen, sollten sie ihr aktuelles vergessen haben.

### Doktor Lizensierung
Damit man eine Doktorrolle zugewiesen bekommt man man sich vorerst Lizensieren.
Die Lizensierung der Doktoren geschieht über den Upload einer PDF; der Lizenz Datei.
Diese Datei muss manuell von einem Admin, mit besonderen Rechten geprüft und bestätigt werden, damit der angefragte Nutzer zum Doktor wird.

### File Sharing
Patienten können ihre Dateien nur mit Doktoren teilen bei denen sie Patienten sind.
Dadurch soll ein versehentliches teilen mit einem falschen Doktor vorgebeugt werden.
Patienten aaben die Möglichkei können einzelne Files mit ihren Doktoren zu teilen und können ihre geteilten Files jederzeit einsehen sowie auch herunterladen.
Die Doktoren, mit denen die Dateien geteilt wurden, können die geteilten Files einsehen und ebenfalls herunterladen.

### Patient Request
Damit eine Beziehung zwischen einem Patienten und Doktor Beziehung entsteht, muss ein User (Patient) einen Doktor anfragen. Der angefragte Doktor kann diesen Patienten annehmen oder ablehnen. Erst bei Annahme der Anfrage entsteht eine Beziehung zwischen dem Patienten und dem Doktor. Daraufhin erscheint der DOktor unter MyDoctors beim Nutzer. 

### Datei Verwaltung
Patienten haben die Möglichkeit ihre Dateien anzupassen, zu löschen und herunterzuladen. 


## Testplan
|Test Case Type|Beschreibung|Test Schritte|Erwartetes Ergebnis|Status|
|----------|----------|--------|--------|----------|
| Functionality|Testen ob Nutzer erstellt und gelöscht werden kann|Mehrere Nutzer erstellen und danach löschen|Nutzer lässt sich erfolgreich erstellen und wieder löschen|Passed|
||Testen ob Login/Logout funktioniert|Erstellte Testnutzer einloggen und auf gültige bzw. nach dem Logout ungültige Session prüfen|Nach dem einloggen wird eine gültige Session erstellt und diese wird nach dem ausloggen ungültig und ist nicht mehr nutzbar|Passed|
||Testen ob Nutzer aktiv oder inaktiv - bei Inaktiv User löschen|Prüfen ob erstellte Nutzer ihre E-Mail verifiziert haben (und somit inactiv sind), falls die Verifizierung nicht erfolgt wird kein Konto erstellt und der Nutzer wieder gelöscht|Nicht verifizierte Konten werden identifiziert und dann gelöscht|Passed|
||Testen ob Patient/Doktor erstellbar|Nutzer mit Rollenzuweisung(Patient/Doktor) erstellen|Nutzer werden erstellt und entweder der Rolle Patient oder Doktor erfolgreich zugewiesen|Passed|
||Testen ob File Upload/Download funktioniert  |Eine PDF Datei hochladen/runterladen und auf gültige Rückmeldung prüfen|Es lässt sich eine PDF Datei hochladen und auch wieder herunterladen|Passed|
|Security|Zugriff auf Myfiles/shared files ohne Patientenrolle testen|MyFiles und SharedFiles aufrufen ohne eingeloggt oder registriert zu sein |Es ist nicht möglich auf MyFiles oder SharedFiles zuzugreifen|Passed|
||Zugriff auf Profile ohne Patientenrolle testen|Profile aufrufen ohne ein Patientenrolle zu haben - also nicht eingeloggt oder registriert |Profil darf nicht abrufbar sein|Passed|
||Zugriff auf All Doctors/My Doctors ohne Patientenrolle testen| All Doctors/ My Doctors - Seite aufrufen ohne ein Patientenrolle zu haben       |Zugriff auf die Seite darf nicht möglich sein ohne ein Patientenrolle zu haben|Passed|
||Zugriff auf Patient Data/Patient Request ohne Doktorrolle testen| Patient data bzw. Patient Request aufrufen ohne Doktorrolle zu besitzen     |Es darf keine Datenabruf möglich sein, wenn man keine Doktorrolle hat und Doktor vom jeweiligen Patienten ist|Passed|
||Testen ob Email Verifzierung mit falschem Token|Falschen Token für nicht aktiven Nutzer erstellen und mit GET-Request prüfen ob damit die E-Mail verifizierbar ist|Eine E-Mail Verifizierung mit dem falschen Token darf nicht erfolgen|Passed|


## Testergebnisse
Zum aktuellen Stand (12.12.2022) werden alle oben aufgeführten Test von unserer ANwendung bestanden.

Zusätzlich haben wir eine statische Codeanalyse mithilfe von CodeQL in unseren Testvorgang implementiert. Dieser konnte jedoch keine Schwachstelle in unserem Code finden: ![](./img/CodeQL.png)

Da wir in diesem Projekt viele Open-Source Libraries eingebunden haben, haben wir uns dazu entschieden FOSSA als open source dependencies Tool einzubinden. FOSSA prüft bei jedem Push auf den `main` branch die eingebundene open source Bibliotheken auf ihre Lizensen und gemeldete Schwachstellen:

![](./img/FOSSA_dependencies.png)
![](./img/FOSSA_Issues.png)
![](./img/FOSSA_Pillow.png)
![](./img/FOSAA_Licenses.png)

Die gefunden Issues können dann manuell reviewed und das Projekt angepasst bzw. die erforderlichen Lizensbedingungen akzeptiert werden:
![](./img/FOSSA_solved.png)

FOSSA generiert zudem einen Bericht mit allen Dependencies:
https://app.fossa.com/attribution/e255cdb3-2448-49e1-89d8-503bb1d49d38