import streamlit as st
import pandas as pd

st.title("Umfrage – Restoration Layers (nachhaltiger Erdbau)")

st.header("Allgemeine Angaben")

proj_lsw = st.selectbox(
    "In wie vielen Projekten mit Lärmschutzwällen/Böschungen waren Sie in den letzten 5 Jahren tätig?",
    ["0", "1-5", "6-10", "mehr als 10"]
)

reuse_exp = st.selectbox(
    "Hat Ihre Organisation bereits Erfahrungen mit gezielter Wiederverwendung von Aushubmaterial?",
    ["Ja", "Nein", "Nicht bekannt"]
)

involved = st.radio(
    "Sind Sie an Planung/Genehmigung/Ausführung im Erdbau beteiligt?",
    ["Ja", "Nein"]
)

st.header("Organisation & Rolle")

org_type = st.selectbox(
    "Zu welcher Gruppe gehört Ihre Organisation?",
    [
        "Bauunternehmen / Tiefbau",
        "Planungs- oder Ingenieurbüro",
        "Behörde / Öffentliche Verwaltung",
        "Landschaftsarchitektur",
        "Infrastrukturbetreiber",
        "Spezialbetrieb für Erdbau",
        "Forschungseinrichtung",
        "Sonstiges"
    ]
)

plz = st.text_input("PLZ Ihrer Organisation")

position = st.selectbox(
    "Welche Position bekleiden Sie?",
    [
        "Geschäftsführung / Inhaber",
        "Projektleitung",
        "Technische Leitung / Bereichsleitung",
        "Fachkraft / Spezialist",
        "Öffentlicher Entscheidungsträger / Beamter",
        "Sonstiges"
    ]
)

st.header("Bewertung (1 = niedrig, 5 = hoch)")

readiness = st.slider("Bereitschaft zur Nutzung von Restoration Layers", 1, 5, 3)

st.subheader("Einflussfaktoren")

costs = st.slider("Anschaffungskosten", 1, 5, 3)
availability = st.slider("Verfügbarkeit", 1, 5, 3)
quality = st.slider("Materialqualität", 1, 5, 3)
stability = st.slider("Technische Stabilität", 1, 5, 3)
legal = st.slider("Rechtliche Sicherheit", 1, 5, 3)
longterm = st.slider("Langfristige Stabilität", 1, 5, 3)

st.subheader("Potenzial")

infra = st.slider("Infrastrukturflächen", 1, 5, 3)
parks = st.slider("Parks / Grünanlagen", 1, 5, 3)
residential = st.slider("Wohngebiete", 1, 5, 3)
commercial = st.slider("Gewerbliche Flächen", 1, 5, 3)

st.header("Barrieren")

barriers = st.multiselect(
    "Welche Barrieren sehen Sie?",
    [
        "Unklare Haftungsverhältnisse",
        "Fehlende Langzeiterfahrungen",
        "Hoher bürokratischer Aufwand",
        "Mangelnde Akzeptanz bei Auftraggebern",
        "Sonstiges"
    ]
)

barriers_general = st.radio(
    "Sehen Sie grundsätzlich wesentliche Barrieren?",
    ["Ja", "Nein"]
)

st.header("Zukunft & Entscheidung")

future_use = st.slider("Einsatzwahrscheinlichkeit in 5 Jahren", 1, 5, 3)
decision_power = st.slider("Einfluss auf Materialentscheidungen", 1, 5, 3)

# -------------------
# SPEICHERN
# -------------------
if st.button("Absenden"):

    data = {
        "proj_lsw": proj_lsw,
        "reuse_exp": reuse_exp,
        "involved": involved,
        "org_type": org_type,
        "plz": plz,
        "position": position,
        "readiness": readiness,
        "costs": costs,
        "availability": availability,
        "quality": quality,
        "stability": stability,
        "legal": legal,
        "longterm": longterm,
        "infra": infra,
        "parks": parks,
        "residential": residential,
        "commercial": commercial,
        "barriers": barriers,
        "barriers_general": barriers_general,
        "future_use": future_use,
        "decision_power": decision_power
    }

    df = pd.DataFrame([data])

    st.success("Antwort gespeichert!")

    st.write(df)

    df.to_csv("umfrage_results.csv", mode="a", header=False, index=False)
