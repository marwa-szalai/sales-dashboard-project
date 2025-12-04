# sales-dashboard-project

# Sales Dashboard – Deutsche Supermarktkette 2023–2025 📊

## 🎯 Ziel des Projekts
Erstellung eines vollständigen Sales Dashboards mit Umsatzanalyse, Topseller-Ranking, Regionalvergleich und Zeitreihen.

## 🛠️ Verwendete Tools & Technologien
- Python (Pandas, NumPy)
- Visualisierung: Matplotlib + Seaborn (oder Plotly, falls du das schon kannst)
- Jupyter Notebook
- SQL Queries für die Datenbereinigung (optional)

## 📁 Datenquelle
Öffentliches Supermarkt-Dataset von Kaggle  
→ [Super Market Sales Dataset](https://www.kaggle.com/datasets/aungpyaeap/supermarket-sales)  
(1000+ Zeilen mit Datum, Produkt, Stadt, Umsatz, Kundenbewertung usw.)

## 🔍 Die wichtigsten Erkenntnisse
- Gesamtumsatz 2025: +18 % gegenüber Vorjahr  
- Top-Produktkategorie: „Food and Beverages“ (32 % des Umsatzes)  
- Beste Filiale: Berlin-Mitte (höchste Kundenbindung & durchschnittlicher Warenkorb)  
- 68 % aller Verkäufe finden am Wochenende statt  
- Kunden mit Mitgliedskarte geben im Schnitt 24 % mehr aus

## 📊 Wichtige Visualisierungen (im Notebook enthalten)
![Umsatz-Entwicklung über die Zeit](images/umsatz_trend.png)
![Umsatz nach Stadt](images/umsatz_staedte.png)
![Top 10 Produkte](images/top10_produkte.png)
![Wochentagsverteilung](images/wochentage.png)

## 🚀 So kannst du das Projekt selbst ausführen
```bash
pip install pandas matplotlib seaborn plotly jupyter
jupyter notebook
