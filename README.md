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

```bash
git clone [https://github.com/DEIN_USERNAME/DEIN_REPOSITORY_NAME.git](https://github.com/DEIN_USERNAME/DEIN_REPOSITORY_NAME.git)
cd DEIN_REPOSITORY_NAME