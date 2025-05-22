# Mein Personalisiertes Django Website-Projekt

Dieses Django-Projekt dient als flexible Plattform zur Erstellung und Verwaltung einer personalisierten Website. Es bietet umfangreiche Anpassungsmöglichkeiten für Farben, Layouts, Menüführung und Inhalte direkt über das Django-Admin-Interface.

## Inhaltsverzeichnis

1.  [Über das Projekt](#über-das-projekt)
2.  [Features](#features)
3.  [Installation](#installation)
    * [Voraussetzungen](#voraussetzungen)
    * [Projekt klonen](#projekt-klonen)
    * [Virtuelle Umgebung einrichten](#virtuelle-umgebung-einrichten)
    * [Abhängigkeiten installieren](#abhängigkeiten-installieren)
    * [Datenbank einrichten](#datenbank-einrichten)
    * [Administrator-Benutzer erstellen](#administrator-benutzer-erstellen)
    * [Statische Dateien vorbereiten](#statische-dateien-vorbereiten)
    * [Entwicklungsserver starten](#entwicklungsserver-starten)
4.  [Apps des Projekts](#apps-des-projekts)
    * [`website_settings` App](#website_settings-app)
5.  [Modelle](#modelle)
6.  [Views](#views)
7.  [URLs](#urls)
8.  [Verwendete Libraries & Tools](#verwendete-libraries--tools)
9.  [Einstellungen (`settings.py`)](#einstellungen-settingspy)
10. [Deployment](#deployment)
11. [Beitragen](#beitragen)
12. [Lizenz](#lizenz)

---

## 1. Über das Projekt

Dieses Django-Projekt ist ein leichtgewichtiges Content-Management-System (CMS), das speziell für die Erstellung einer flexiblen Homepage mit dynamischen Inhaltssektionen entwickelt wurde. Administratoren können die visuellen Einstellungen der Website, die Menüpunkte und den Inhalt verschiedener Sektionen einfach über das Django-Admin-Backend konfigurieren, ohne Code ändern zu müssen. Der Fokus liegt auf der dynamischen Gestaltung der Homepage mit verschiedenen Layouts.

## 2. Features

* **Dynamische Homepage-Sektionen:** Erstelle und verwalte verschiedene Inhaltssektionen für deine Homepage.
* **Vielfältige Layout-Optionen:** Wähle aus mehreren vorgegebenen Layouts pro Sektion, z.B. einspaltig, zweispaltig mit Bild links/rechts, oder ein spezielles "Paper-Artikel"-Layout mit zweispaltigem Text und hervorgehobenem ersten Absatz.
* **Anpassbare Website-Einstellungen:** Konfiguriere globale Farben (Menü, Hintergrund, Text) und Logo-Details (Bild, Größe, Position) zentral für die gesamte Website.
* **Flexibles Menümanagement:** Definiere Menüpunkte, deren Reihenfolge und verknüpfe sie mit spezifischen Sektionen auf deiner Homepage.
* **Rich-Text-Bearbeitung:** Nutze den integrierten TinyMCE WYSIWYG-Editor für die einfache und formatierte Inhaltseingabe (Text, Bilder, Listen etc.) in den Sektionen.
* **Responsives Design:** Das Projekt basiert auf Bootstrap 5 und ist standardmäßig für eine gute Darstellung auf verschiedenen Geräten (Desktops, Tablets, Smartphones) optimiert.

## 3. Installation

Befolge diese Schritte, um das Projekt lokal einzurichten und auszuführen.

### Voraussetzungen

Stelle sicher, dass die folgenden Tools auf deinem System installiert sind:

* **Python 3.8+:** Die Programmiersprache, auf der Django basiert.
* **pip:** Der Python-Paketmanager, der automatisch mit Python installiert wird.
* **Git:** Ein Versionskontrollsystem, um das Projekt von GitHub zu klonen.

### Projekt klonen

Öffne dein Terminal oder deine Kommandozeile und klone das Projekt von GitHub:
git clone https://github.com/DEIN_USERNAME/DEIN_REPOSITORY_NAME.git

cd DEIN_REPOSITORY_NAME
*Ersetze `DEIN_USERNAME` und `DEIN_REPOSITORY_NAME` durch die tatsächlichen Werte deines GitHub-Repositorys.*

### Virtuelle Umgebung einrichten

Es wird dringend empfohlen, eine virtuelle Umgebung zu verwenden, um die Projektabhängigkeiten zu isolieren und Konflikte mit anderen Python-Projekten auf deinem System zu vermeiden.

1.  **Virtuelle Umgebung erstellen:**
    ```
    python3 -m venv venv
    ```

2.  **Virtuelle Umgebung aktivieren:**
    * **Auf Linux / macOS:**
        ```
        source venv/bin/activate
        ```
    * **Auf Windows (PowerShell):**
        ```
        .\venv\Scripts\activate
        ```
    * **Auf Windows (CMD):**
        ```
        venv\Scripts\activate.bat
        ```
    Nach der Aktivierung siehst du `(venv)` vor deinem Prompt, was anzeigt, dass du dich in der virtuellen Umgebung befindest.

### Abhängigkeiten installieren

Installiere alle benötigten Python-Pakete, die in der `requirements.txt`-Datei aufgeführt sind:
pip install -r requirements.txt

### Datenbank einrichten

Wende die Django-Datenbankmigrationen an, um die erforderlichen Datenbanktabellen für deine Modelle zu erstellen:
python manage.py migrate

### Administrator-Benutzer erstellen

Um Zugang zum Django-Admin-Bereich zu erhalten und Inhalte zu verwalten, musst du einen Superuser erstellen:
python manage.py createsuperuser

Folge den Anweisungen im Terminal, um einen Benutzernamen, eine E-Mail-Adresse und ein Passwort festzulegen.

### Statische Dateien vorbereiten

Sammle alle statischen Dateien (CSS, JavaScript, Bilder) der Django-Apps in einem einzigen Verzeichnis. Dies ist wichtig für das Deployment und auch gut für den Entwicklungsserver, um sicherzustellen, dass alle Assets gefunden werden:
python manage.py collectstatic

Bestätige die Operation, wenn du dazu aufgefordert wirst (mit `yes`).

### Entwicklungsserver starten

Jetzt kannst du den Django-Entwicklungsserver starten:
python manage.py runserver

Öffne anschließend deinen Webbrowser und navigiere zu:

* **Homepage:** `http://127.0.0.1:8000/`
* **Admin-Bereich:** `http://127.0.0.1:8000/admin/` (Melde dich hier mit den zuvor erstellten Superuser-Zugangsdaten an.)

**Erste Schritte im Admin-Bereich:**
Im Admin-Bereich kannst du:
* Unter **`Website-Einstellungen`** die globalen Einstellungen wie Logo, Menü- und Hintergrundfarben anpassen.
* Unter **`Menüpunkte`** die Einträge für deine Navigation definieren und deren Reihenfolge festlegen.
* Unter **`Homepage Sections`** die eigentlichen Inhaltsbereiche erstellen, deren Layout auswählen und den Inhalt mit dem TinyMCE-Editor bearbeiten.

## 4. Apps des Projekts

### `website_settings` App

Dies ist die Kern-App des Projekts, die alle Modelle und Logik für die Website-Konfiguration und Inhalte enthält. Sie ist darauf ausgelegt, eine flexible und über das Admin-Interface verwaltbare Homepage zu ermöglichen.

## 5. Modelle

Die Datenbankstruktur des Projekts wird durch folgende Modelle definiert (zu finden in `website_settings/models.py`):

* **`SiteSettings`**: Enthält globale Website-Einstellungen wie Menü-, Hintergrund- und Textfarben sowie Logo-Details (Bild, Höhe, Versatz). Dieses Modell ist als Singleton konfiguriert, sodass nur ein Objekt davon im System existiert, um globale Einstellungen zu verwalten.
* **`MenuItem`**: Definiert die einzelnen Einträge für das Hauptmenü der Website.
    * **Wichtige Felder:** `title` (Anzeigetext im Menü), `slug` (für die URL und Anker-ID auf der Seite), `order` (Reihenfolge im Menü), `is_active` (ob der Menüpunkt aktiv ist).
* **`PageSection`**: Repräsentiert einen einzelnen, dynamischen Inhaltsbereich auf der Homepage.
    * **Wichtige Felder:** `menu_item` (OneToOne-Beziehung zu `MenuItem`, verknüpft die Sektion mit einem Menüpunkt), `title` (Überschrift der Sektion), `content` (ein `HTMLField` für Rich-Text-Inhalte, bearbeitet mit TinyMCE), `image` (optionales Bild für die Sektion), `order` (Reihenfolge auf der Homepage), `is_active`, `slug`, `author`, `publication_date`.
    * **`layout`**: Ein `CharField` mit Choices, das das visuelle Layout der Sektion definiert. Aktuell unterstützte Layouts sind:
        * `one-column` (Einspaltiger Text)
        * `two-columns-left` (Zweispaltig mit Bild links)
        * `two-columns-right` (Zweispaltig mit Bild rechts)
        * `paper-article` (Speziallayout für Artikel, oft zweispaltig mit hervorgehobenem ersten Absatz)
    * **Darstellungsoptionen:** Zusätzliche Felder wie `section_text_color`, `background_color`, `border`, `rounded`, `shadow`, `font_weight`, `font_italic`, `text_align`, `padding`, `margin` ermöglichen eine detaillierte visuelle Anpassung jeder Sektion.

## 6. Views

Die Hauptlogik für die Darstellung der Webseiten ist in `website_settings/views.py` implementiert:

* **`homepage_view`**: Diese View ist für das Rendern der Hauptseite verantwortlich. Sie ruft alle aktiven `MenuItem`-Objekte (sortiert nach deren `order`) und deren verknüpfte `PageSection`-Inhalte ab. Außerdem werden die globalen `SiteSettings` an das Template übergeben, um die Website dynamisch zu gestalten.

## 7. URLs

Die URL-Routen des Projekts sind in zwei Dateien definiert:

* **Globale URLs** (`myproject/urls.py`):
    * Konfiguriert den Zugang zum Django-Admin-Bereich (`/admin/`).
    * Inkludiert die URLs der `website_settings`-App.
    * Stellt im Entwicklungsmodus Mediendateien (hochgeladene Bilder) bereit.
* **App-spezifische URLs** (`website_settings/urls.py`):
    * Definiert die URL für die Hauptseite (`/`). Diese URL ist mit der `homepage_view` verknüpft.

## 8. Verwendete Libraries & Tools

Dieses Projekt nutzt die Leistungsfähigkeit verschiedener Python-Bibliotheken und Frontend-Tools:

* **Django:** Das Herzstück des Projekts – ein hochperformantes Web-Framework für Pythons.
* **Pillow:** Eine grundlegende Bildverarbeitungsbibliothek, die für die Handhabung von `ImageField` in Django unerlässlich ist.
* **django-tinymce:** Integriert den beliebten TinyMCE WYSIWYG-Editor nahtlos in das Django-Admin-Interface, um die Bearbeitung von Rich-Text-Inhalten zu vereinfachen.
* **django-colorfield:** Bietet ein benutzerfreundliches und visuelles Farbauswahlfeld im Django-Admin, um Farben für Website-Elemente einfach zu konfigurieren.
* **Bootstrap 5:** Ein weit verbreitetes CSS-Framework, das über ein CDN (`base.html`) eingebunden ist. Es sorgt für ein modernes, responsives Design und stellt viele vorgefertigte UI-Komponenten zur Verfügung.

## 9. Einstellungen (`settings.py`)

Die zentrale Konfigurationsdatei des Django-Projekts, `myproject/settings.py`, enthält wichtige globale Einstellungen:

* **`SECRET_KEY`**: Ein kritischer Sicherheitsschlüssel. **Für die Produktion sollte dieser Wert immer über Umgebungsvariablen (`os.environ.get`) gesetzt werden und niemals direkt im Code stehen oder im Git-Repository veröffentlicht werden.**
* **`DEBUG`**: Steuert den Debug-Modus von Django. Im Entwicklungsumfeld ist er auf `True` gesetzt, im Produktionsmodus MUSS er auf `False` geändert werden, um Sicherheitsrisiken und Informationslecks zu vermeiden.
* **`ALLOWED_HOSTS`**: Eine Liste von Host-/Domainnamen, auf denen diese Django-Installation bereitgestellt werden darf. Im Produktionsmodus muss diese Liste angepasst werden.
* **`STATIC_URL`**, `STATIC_ROOT`, `MEDIA_URL`, `MEDIA_ROOT`: Diese Einstellungen definieren, wie Django statische Dateien (CSS, JS, Bilder deiner Apps) und Mediendateien (Benutzer-hochgeladene Inhalte wie Bilder) handhabt und bereitstellt.
* **`INSTALLED_APPS`**: Eine Liste aller aktivierten Django-Apps im Projekt, darunter `tinymce`, `colorfield` und deine eigene App `website_settings`.

**Wichtiger Sicherheitshinweis:** Für den Produktionseinsatz ist es unerlässlich, alle sensiblen Daten (wie `SECRET_KEY`, Datenbank-Zugangsdaten) nicht direkt im `settings.py` zu speichern, sondern externe Konfigurationsmechanismen (z.B. Umgebungsvariablen, `.env`-Dateien in Kombination mit `python-dotenv`) zu verwenden.

## 10. Deployment

Um das Projekt für den Produktionsbetrieb vorzubereiten und auf einem Server bereitzustellen, sind folgende Schritte und Überlegungen entscheidend:

1.  **Umgebungsvariablen setzen:** Stelle sicher, dass auf deinem Produktionsserver die Umgebungsvariablen wie `DJANGO_SECRET_KEY` und `DJANGO_DEBUG` (auf `False` gesetzt) korrekt definiert sind, bevor die Anwendung gestartet wird.
2.  **Webserver konfigurieren:** In einer Live-Umgebung wird ein robuster Webserver wie **Nginx** oder **Apache** als Reverse Proxy vor deine Django-Anwendung geschaltet. Dieser Webserver leitet HTTP-Anfragen an deine Anwendung weiter.
3.  **WSGI-Server verwenden:** Django-Anwendungen werden im Produktionsbetrieb nicht mit `runserver` gestartet. Stattdessen wird ein WSGI-Server (z.B. **Gunicorn** oder **uWSGI**) eingesetzt, der die Kommunikation zwischen dem Webserver und deiner Django-Anwendung übernimmt.
4.  **Statische Dateien bereitstellen:** Konfiguriere deinen Webserver (Nginx/Apache) so, dass er die im `STATIC_ROOT` gesammelten statischen Dateien direkt bereitstellt. Dies entlastet Django und beschleunigt die Auslieferung von Assets.
5.  **Mediendateien verwalten:** Für hochgeladene Mediendateien (`MEDIA_ROOT`) wird in der Produktion oft ein Cloud-Speicheranbieter (z.B. AWS S3, Google Cloud Storage) empfohlen. Dies sorgt für Skalierbarkeit, Redundanz und erleichtert Backups.
6.  **HTTPS aktivieren:** Für eine sichere Datenübertragung ist es unerlässlich, HTTPS zu verwenden. Dies wird typischerweise durch die Installation von SSL-Zertifikaten (z.B. Let's Encrypt) auf deinem Webserver realisiert.

## 11. Beitragen

Wenn du zu diesem Projekt beitragen möchtest, folge bitte diesen Schritten:

1.  Forke das Repository auf GitHub.
2.  Erstelle einen neuen Branch für deine Features oder Bugfixes:
    ```
    git checkout -b feature/MeinNeuesFeature # Oder bugfix/BehobenerBug
    ```
3.  Implementiere deine Änderungen und teste sie gründlich.
4.  Commite deine Änderungen mit einer aussagekräftigen Nachricht:
    ```
    git commit -m 'feat: Add new feature for dynamic section layouts'
    ```
5.  Pushe deinen Branch zu deinem geforkten Repository auf GitHub:
    ```
    git push origin feature/MeinNeuesFeature
    ```
6.  Öffne einen Pull Request (PR) vom Branch deines Forks zum `main`-Branch dieses Repositorys. Beschreibe deine Änderungen detailliert im PR.

## 12. Lizenz

Dieses Projekt steht unter der MIT-Lizenz. Weitere Details findest du in der `LICENSE`-Datei im Stammverzeichnis des Projekts (falls vorhanden).