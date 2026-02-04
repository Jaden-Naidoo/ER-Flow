#File to store long functions to keep main web app file clean - this file covers main and prediction pages (decided to split other page into its own file)
import streamlit as st
import numpy as np
import joblib
import pandas as pd
import shap


model = joblib.load('ER_model.pkl')


def theme_main_page():
  st.markdown("""
    <style>

        html, body, [class*="css"] {
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto;
        background-color: #0F1117;
    }

        .card {
        background-color: #1C1F26;
        border-radius: 14px;
        padding: 24px;
        box-shadow: 0 8px 24px rgba(0,0,0,0.25);
    }


    .fade-in {
    animation: fadeIn 0.6s ease-in-out;
    }
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(6px); }
        to { opacity: 1; transform: translateY(0); }
    }


    .metric {
        font-size: 1.8rem;
        font-weight: 600;
        color: #2F80ED;
    }
    </style>
    """, unsafe_allow_html=True)
    
def feat_cards():
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Material+Symbols+Rounded:opsz,wght,FILL,GRAD@20..48,100..700,0..1,-50..200" />
        <div class="card">
        <h3>
            <span class="material-symbols-rounded" style="vertical-align: middle; color: cornflowerblue;">monitor_heart</span>
            Fast Triage Prediction
        </h3>
        <p>
            Instantly predict patient triage level using vital signs, arrival mode,
            and clinical indicators.
        </p>
        <ul>
            <li>XGBoost-powered</li>
            <li>Handles noisy data</li>
            <li>Designed to improve ER wait times and workflow</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="card">
        <h3>
            <span class="material-symbols-rounded" style="vertical-align: middle; color: cornflowerblue;">psychology</span>
            Explainable AI
        </h3>
        <p>
            Understand <em>why</em> a patient was assigned a triage level using SHAP
            explanations.
        </p>
        <ul>
            <li>Feature-level insights</li>
            <li>Clinically interpretable</li>
            <li>Model transparency</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="card">
        <h3>
            <span class="material-symbols-rounded" style="vertical-align: middle; color: cornflowerblue;">science</span> 
            Scenario Simulation
        </h3>
        <p>
            Simulate patient scenarios and observe how triage decisions are made in real time.
        </p>
        <ul>
            <li>Voiced actors</li>
            <li>Education & training use</li>
            <li>Operational insight</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)

def predict_page():
    #css styling for a more aesthetic dashboard page
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500;600&family=Syne:wght@400;500;600;700&family=DM+Sans:wght@300;400;500;600&display=swap');
    :root {
        --bg-deep:       #090b0f;
        --bg-surface:    #111418;
        --bg-card:       #161a22;
        --bg-card-alt:   #1c2129;
        --bg-input:      #1a1f28;
        --text-primary:  #eef0f3;
        --text-muted:    #6b7585;
        --text-dim:      #444d5c;
        --accent:        #38bdf8;
        --accent-dim:    rgba(56,189,248,0.12);
        --border:        rgba(255,255,255,0.055);
        --border-hover:  rgba(56,189,248,0.28);
        --radius:        16px;
        --radius-sm:     10px;

        --gap-xs:  6px;
        --gap-sm:  12px;
        --gap-md:  20px;
        --gap-lg:  32px;
        --gap-xl:  48px;
        --gap-2xl: 64px;
    }
    .stApp {
        background: #0E1117;
        color: var(--text-primary);
        font-family: 'DM Sans', sans-serif;
        padding-top: 8px;
    }
    h1, h2, h3, h4 { font-family: 'Syne', sans-serif; }

    .page-header {
        padding: var(--gap-lg) 0 var(--gap-lg);
        margin-bottom: var(--gap-lg);
        border-bottom: 1px solid var(--border);
    }
    .page-header .header-eyebrow {
        font-family: 'IBM Plex Mono', monospace;
        font-size: 0.7rem;
        font-weight: 500;
        color: var(--accent);
        text-transform: uppercase;
        letter-spacing: 2.2px;
        margin-bottom: var(--gap-sm);
    }
    .page-header h1 {
        font-size: 2rem;
        font-weight: 700;
        color: var(--text-primary);
        margin: 0 0 var(--gap-xs);
        line-height: 1.2;
    }
    .page-header h1 .hl { color: var(--accent); }
    .page-header .header-caption {
        font-size: 0.82rem;
        color: var(--text-muted);
        font-weight: 300;
    }
    .form-section-label {
        font-family: 'IBM Plex Mono', monospace;
        font-size: 0.68rem;
        font-weight: 600;
        color: var(--text-dim);
        text-transform: uppercase;
        letter-spacing: 1.6px;
        margin-bottom: var(--gap-sm);
        margin-top: var(--gap-md);
        padding-bottom: var(--gap-xs);
        border-bottom: 1px solid var(--border);
    }
    .spacer-lg  { height: var(--gap-lg); }
    .spacer-xl  { height: var(--gap-xl); }
    .spacer-md  { height: var(--gap-md); }
    @keyframes pulse-red {
        0%,100% { box-shadow: 0 0 14px rgba(232,0,0,0.3); }
        50%     { box-shadow: 0 0 42px rgba(232,0,0,0.9); }
    }
    @keyframes pulse-orange {
        0%,100% { box-shadow: 0 0 14px rgba(255,103,0,0.35); }
        50%     { box-shadow: 0 0 36px rgba(255,103,0,0.85); }
    }
    .pulse-red   { animation: pulse-red    1.9s ease-in-out infinite; }
    .pulse-orange{ animation: pulse-orange 1.9s ease-in-out infinite; }
                
    .triage-glow-wrap {
        position: relative;
        margin-top: var(--gap-md);
        margin-bottom: var(--gap-lg);
    }
    .triage-glow-wrap::before {
        content: '';
        position: absolute;
        top: 50%; left: 50%;
        transform: translate(-50%,-50%);
        width: 70%; height: 180%;
        background: radial-gradient(ellipse, var(--triage-glow-color, rgba(56,189,248,0.08)) 0%, transparent 70%);
        pointer-events: none;
        z-index: 0;
    }

    .triage-card {
        position: relative;
        z-index: 1;
        background: var(--bg-card);
        backdrop-filter: blur(16px);
        border-radius: 22px;
        padding: 36px 40px 32px;
        border-left: 10px solid;
        overflow: hidden;
    }
    
    .triage-card::before {
        content: '';
        position: absolute;
        inset: 0;
        background: linear-gradient(140deg, rgba(255,255,255,0.04) 0%, transparent 50%);
        pointer-events: none;
    }
   
    .triage-card .watermark {
        position: absolute;
        right: 28px;
        top: 50%;
        transform: translateY(-50%);
        font-family: 'Syne', sans-serif;
        font-size: 11rem;
        font-weight: 700;
        line-height: 1;
        color: rgba(255,255,255,0.035);
        pointer-events: none;
        user-select: none;
    }
    
    .triage-card .triage-content { position: relative; z-index: 1; }

    .triage-card .triage-level-row {
        display: flex; align-items: baseline; gap: var(--gap-sm);
    }
    .triage-card .level-num {
        font-family: 'Syne', sans-serif;
        font-size: 2.6rem;
        font-weight: 700;
        line-height: 1;
        letter-spacing: -0.5px;
    }
    .triage-card .level-word {
        font-family: 'IBM Plex Mono', monospace;
        font-size: 0.72rem;
        font-weight: 600;
        color: var(--text-dim);
        text-transform: uppercase;
        letter-spacing: 1.4px;
        align-self: flex-end;
        padding-bottom: 6px;
    }
    .triage-card .triage-label {
        font-size: 1.15rem;
        font-weight: 400;
        color: #d4d8df;
        margin-top: var(--gap-sm);
        line-height: 1.4;
    }
    .triage-card .triage-meta {
        font-size: 0.75rem;
        color: var(--text-dim);
        margin-top: var(--gap-sm);
    }
    .triage-card .triage-meta span { color: var(--text-muted); }

    .confidence-row {
        display: flex; align-items: center; gap: var(--gap-sm);
        margin-top: var(--gap-lg);
        padding-top: var(--gap-md);
        border-top: 1px solid var(--border);
    }
    .confidence-row .conf-label {
        font-family: 'IBM Plex Mono', monospace;
        font-size: 0.68rem; font-weight: 500;
        color: var(--text-dim);
        text-transform: uppercase; letter-spacing: 1px;
        white-space: nowrap;
    }
    .confidence-row .conf-bar-bg {
        flex: 1; height: 5px;
        background: var(--bg-card-alt); border-radius: 3px; overflow: hidden;
    }
    .confidence-row .conf-bar-fill {
        height: 100%; border-radius: 3px;
        background: linear-gradient(90deg, var(--accent), #7dd3fc);
        transition: width 0.7s cubic-bezier(.4,0,.2,1);
    }
    .confidence-row .conf-value {
        font-family: 'IBM Plex Mono', monospace;
        font-size: 0.78rem; font-weight: 600;
        color: var(--accent);
        min-width: 42px; text-align: right;
    }
    .vitals-row { margin-top: var(--gap-md); margin-bottom: var(--gap-xl); }

    .vital-card {
        background: var(--bg-card);
        border: 1px solid var(--border);
        border-radius: var(--radius);
        padding: 24px 20px 22px;
        text-align: center;
        transition: border-color 0.25s, transform 0.2s;
    }
    .vital-card:hover {
        border-color: var(--border-hover);
        transform: translateY(-2px);
    }
    .vital-card .vital-icon {
        display: flex; justify-content: center;
        margin-bottom: var(--gap-sm);
    }
    .vital-card .vital-icon svg {
        width: 22px; height: 22px;
        stroke: var(--text-dim); fill: none; stroke-width: 1.8;
        stroke-linecap: round; stroke-linejoin: round;
    }
    .vital-card .metric-val {
        font-family: 'IBM Plex Mono', monospace;
        font-size: 1.75rem;
        font-weight: 600;
        color: var(--text-primary);
        line-height: 1.2;
    }
    .vital-card .metric-label {
        font-size: 0.72rem;
        color: var(--text-muted);
        margin-top: var(--gap-xs);
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    .vital-card .metric-status {
        display: inline-block;
        margin-top: var(--gap-sm);
        padding: 3px 10px;
        border-radius: 20px;
        font-size: 0.66rem;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.6px;
    }
    .status-ok     { background: rgba(74,222,128,0.12); color: #4ade80; }
    .status-warn   { background: rgba(250,204,21,0.12); color: #facc15; }
    .status-danger { background: rgba(248,113,113,0.14); color: #f87171; }

    .section-divider {
        display: flex; align-items: center; gap: var(--gap-md);
        margin-top: var(--gap-xl);
        margin-bottom: var(--gap-lg);
    }
    .section-divider .div-line {
        flex: 1; height: 1px;
        background: var(--border);
    }
    .section-divider .div-label {
        font-family: 'IBM Plex Mono', monospace;
        font-size: 0.68rem;
        font-weight: 600;
        color: var(--text-dim);
        text-transform: uppercase;
        letter-spacing: 1.8px;
        white-space: nowrap;
        padding: 0 var(--gap-sm);
    }

    @keyframes shap-slide-in {
        from { opacity: 0; transform: translateY(10px); }
        to   { opacity: 1; transform: translateY(0);    }
    }
    .shap-row {
        display: flex; align-items: flex-start; gap: var(--gap-md);
        background: var(--bg-card);
        border: 1px solid var(--border);
        border-radius: var(--radius);
        padding: 18px 20px;
        margin-bottom: var(--gap-sm);
        transition: border-color 0.22s, transform 0.2s;
        
        opacity: 0;
        animation: shap-slide-in 0.38s ease forwards;
    }
    .shap-row:nth-child(1) { animation-delay: 0.05s; }
    .shap-row:nth-child(2) { animation-delay: 0.12s; }
    .shap-row:nth-child(3) { animation-delay: 0.19s; }
    .shap-row:nth-child(4) { animation-delay: 0.26s; }
    .shap-row:nth-child(5) { animation-delay: 0.33s; }
    .shap-row:hover {
        border-color: var(--border-hover);
        transform: translateY(-1px);
    }

   
    .shap-row .shap-rank {
        font-family: 'IBM Plex Mono', monospace;
        font-size: 0.68rem;
        font-weight: 600;
        color: var(--text-dim);
        background: var(--bg-card-alt);
        width: 26px; height: 26px;
        border-radius: 8px;
        display: flex; align-items: center; justify-content: center;
        flex-shrink: 0;
        margin-top: 1px;
    }

    .shap-row .shap-content { flex: 1; min-width: 0; }

    .shap-row .shap-top-line {
        display: flex; justify-content: space-between;
        align-items: center; margin-bottom: 10px;
    }
    .shap-row .shap-feature {
        font-size: 0.84rem; font-weight: 500;
        color: var(--text-primary);
    }
    .shap-row .shap-feature .feat-val {
        color: var(--text-muted); font-weight: 300;
        margin-left: 6px;
    }
    .shap-row .shap-badge {
        font-family: 'IBM Plex Mono', monospace;
        font-size: 0.66rem; font-weight: 600;
        padding: 3px 9px; border-radius: 12px;
        white-space: nowrap;
    }
    .badge-up   { background: rgba(248,113,113,0.13); color: #f87171; }
    .badge-down { background: rgba(74,222,128,0.13);  color: #4ade80; }

    
    .shap-row .shap-bar-bg {
        width: 100%; height: 7px;
        background: var(--bg-card-alt);
        border-radius: 4px; overflow: hidden;
    }
    .shap-row .shap-bar-fill {
        height: 100%; border-radius: 4px;
        transition: width 0.6s cubic-bezier(.4,0,.2,1);
    }
    .bar-up   { background: linear-gradient(90deg, #f87171, #ef4444); }
    .bar-down { background: linear-gradient(90deg, #4ade80, #22c55e); }

   
    .shap-row .shap-sentence {
        font-size: 0.74rem;
        color: var(--text-muted);
        margin-top: 10px;
        line-height: 1.55;
    }
    .shap-row .shap-sentence b { color: var(--text-primary); font-weight: 500; }

    .shap-rows-wrap { margin-top: 4px; }

    </style>
    """, unsafe_allow_html=True)

    #streamlit page layout
    st.set_page_config(layout="wide")

    st.markdown("""
    <div class="page-header">
        <div class="header-eyebrow">Emergency Department · Triage System</div>
        <h1><span class="hl">ER</span> Flow</h1>
        <div class="header-caption">Real-time triage level prediction &nbsp;·&nbsp; Australasian Triage Scale (ATS)</div>
    </div>
    """, unsafe_allow_html=True)

    #setting colours for triage levels
    triage_colours = {
        1: {"color": "#E80000", "glow": "0 0 28px rgba(232,0,0,0.85)", "pulse_class": "pulse-red"},
        2: {"color": "#FF6700", "glow": "0 0 22px rgba(255,103,0,0.75)", "pulse_class": "pulse-orange"},
        3: {"color": "#FFD700", "glow": "0 0 14px rgba(255,215,0,0.5)", "pulse_class": ""},
        4: {"color": "#90EE90", "glow": "0 0 10px rgba(144,238,144,0.4)", "pulse_class": ""},
        5: {"color": "#ADD8E6", "glow": "0 0  8px rgba(173,216,230,0.3)", "pulse_class": ""},
    }
    #label of triage level using Australasian Triage Scale (ATS)
    triage_labels = {          
        1: "Immediately Life Threatening",
        2: "Imminently Life Threatening",
        3: "Potentially Life Threatening",
        4: "Potentially Serious",
        5: "Less Urgent",
    }

    #input form to get patient's information
    with st.form("patient_info_form"):
        # split column into demographic and vitals 
        col_demo, col_vitals = st.columns([1, 1], gap="large")

        with col_demo:
            st.markdown('<div class="form-section-label">Demographics & Arrival</div>', unsafe_allow_html=True)
            gender          = st.selectbox('Sex',['Male', 'Female', 'Other/Unknown'])
            age             = st.number_input('Age',0, 100, 45)
            arrival         = st.selectbox('Arrival Mode',['Ambulance', 'Walk-In', 'Transfer'])
            chief_complaint = st.selectbox('Chief Complaint',['Chest Pain', 'Shortness of breath', 'Trauma','Fever','Abdominal Pain','Neurological', 'Other'])
            consciousness   = st.selectbox('Consciousness',['Alert', 'Voice', 'Pain', 'Unresponsive'])
            crit            = 1 if st.checkbox('Critical Event') else 0

        with col_vitals:
            st.markdown('<div class="form-section-label">Vitals & Pain</div>', unsafe_allow_html=True)
            heart_rate      = st.number_input('Heart Rate (bpm)',30,200,90)
            systolic_bp     = st.number_input('Systolic BP (mmHg)',60,220,120)
            diastolic_bp    = st.number_input('Diastolic BP (mmHg)',50,120,80)
            res_rate        = st.number_input('Respiratory Rate (breaths/min)',8,45,20)
            temp            = st.number_input('Temperature (°C)',34.0, 41.0, 36.8)
            o2              = st.number_input('Oxygen Saturation (%)',70,100,97)
            pain            = st.slider('Pain Level', 0, 10, 4)

        submitted = st.form_submit_button(":material/patient_list: Run Triage", use_container_width=True)

    #making maps for input preparation
    gender_map    = {"Female": 0, "Male": 1, "Other/Unknown": 2}
    complaint_map = {"Abdominal Pain": 0, "Chest Pain": 1, "Fever": 2,
                     "Neurological": 3, "Other": 4, "Shortness of breath": 5, "Trauma": 6}
    con_map       = {"Alert": 0, "Voice": 1, "Pain": 2, "Unresponsive": 3}
    arrival_map   = {"Ambulance": 0, "Transfer": 1, "Walk-In": 2}

    #processing submittted info
    if submitted:
        #create input datafram for model prediction
        input_df = pd.DataFrame([{
            "age": int(age),
            "sex": gender_map[gender],
            "arrival_mode": arrival_map[arrival],
            "chief_complaint": complaint_map[chief_complaint],
            "consciousness": con_map[consciousness],
            "heart_rate": float(heart_rate),
            "systolic_bp": float(systolic_bp),
            "diastolic_bp": float(diastolic_bp),
            "respiratory_rate": float(res_rate),
            "temperature": float(temp),
            "oxygen_saturation": float(o2),
            "pain_score": float(pain),
            "critical_event": crit,
        }])
        #predict triage level, based on inputted info, using model
        raw_pred= int(model.predict(input_df)[0])
        triage_level= raw_pred + 1

        #getting confidence level of model for explainability
        if hasattr(model, "predict_proba"):
            proba      = model.predict_proba(input_df)[0]          
            confidence = float(proba[raw_pred]) * 100             
        else:
            confidence = 100.0

        #showing triage level card UI
        ui = triage_colours[triage_level]
        glow_colors = {
            1: "rgba(232,0,0,0.1)",
            2: "rgba(255,103,0,0.1)",
            3: "rgba(255,215,0,0.07)",
            4: "rgba(144,238,144,0.06)",
            5: "rgba(173,216,230,0.05)",
        }
        st.markdown(f"""
        <div class="triage-glow-wrap" style="--triage-glow-color:{glow_colors[triage_level]};">
            <div class="triage-card {ui['pulse_class']}"
                 style="border-left-color:{ui['color']}; box-shadow:{ui['glow']};">
                <!-- watermark -->
                <div class="watermark">{triage_level}</div>
                <!-- main content -->
                <div class="triage-content">
                    <div class="triage-level-row">
                        <span class="level-num" style="color:{ui['color']};">{triage_level}</span>
                        <span class="level-word">Triage Level</span>
                    </div>
                    <div class="triage-label">{triage_labels[triage_level]}</div>
                    <div class="triage-meta">
                        Model-assisted clinical decision support &nbsp;·&nbsp;
                        <span>ATS Scale</span> &nbsp;·&nbsp;
                        <span>Predicted class {raw_pred}</span>
                    </div>
                    <div class="confidence-row">
                        <span class="conf-label">Confidence</span>
                        <div class="conf-bar-bg">
                            <div class="conf-bar-fill" style="width:{confidence:.1f}%;"></div>
                        </div>
                        <span class="conf-value">{confidence:.1f}%</span>
                    </div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

        #helpers for vital cards
        def vital_status(value, low, high):
            """Return CSS class key based on normal range."""
            if value < low or value > high:
                return "status-danger"
            if value == low or value == high:
                return "status-warn"
            return "status-ok"

        def status_label(css_class):
            return {"status-ok": "Normal", "status-warn": "Borderline", "status-danger": "Abnormal"}[css_class]

        hr_st= vital_status(heart_rate, 60,100)
        bp_st= vital_status(systolic_bp,90,140)
        o2_st= vital_status(o2,95,100)

        #showing vital cards
        col1, col2, col3 = st.columns(3, gap="medium")
        with col1:
            st.markdown(f"""
            <div class="vital-card">
                <div class="vital-icon">
                    <svg viewBox="0 0 24 24"><path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"/></svg>
                </div>
                <div class="metric-val">{heart_rate}</div>
                <div class="metric-label">Heart Rate (bpm)</div>
                <span class="metric-status {hr_st}">{status_label(hr_st)}</span>
            </div>""", unsafe_allow_html=True)
        with col2:
            st.markdown(f"""
            <div class="vital-card">
                <div class="vital-icon">
                    <svg viewBox="0 0 24 24"><polyline points="22 12 18 12 15 21 9 3 6 12 2 12"/></svg>
                </div>
                <div class="metric-val">{systolic_bp}/{diastolic_bp}</div>
                <div class="metric-label">Blood Pressure (mmHg)</div>
                <span class="metric-status {bp_st}">{status_label(bp_st)}</span>
            </div>""", unsafe_allow_html=True)
        with col3:
            st.markdown(f"""
            <div class="vital-card">
                <div class="vital-icon">
                    <svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"/><circle cx="12" cy="12" r="3" fill="currentColor" stroke="none"/></svg>
                </div>
                <div class="metric-val">{o2}%</div>
                <div class="metric-label">SpO₂</div>
                <span class="metric-status {o2_st}">{status_label(o2_st)}</span>
            </div>""", unsafe_allow_html=True)

        #explainable AI using SHAP
        explainer = shap.TreeExplainer(model)
        #get SHAP values for predicted class
        shap_values = explainer.shap_values(input_df)  
        if isinstance(shap_values, list):
            class_shap = shap_values[raw_pred][0]          
        else:
            class_shap = shap_values[0, :, raw_pred]

        shap_df = pd.DataFrame({
            "feature":       input_df.columns,
            "shap_value":    class_shap,
            "feature_value": input_df.iloc[0].values,
        })
        shap_df["abs_shap"] = shap_df["shap_value"].abs()
        shap_df = shap_df.sort_values("abs_shap", ascending=False).head(5).reset_index(drop=True)
        max_abs = shap_df["abs_shap"].max() or 1.0
        shap_df["bar_pct"] = (shap_df["abs_shap"] / max_abs * 100)
        #translating SHAP to basic human language
        feat_meta = {
            "oxygen_saturation": ("Oxygen Saturation",  "%",     "95–100 %"),
            "respiratory_rate":  ("Respiratory Rate",   "br/min","12–20 br/min"),
            "heart_rate":        ("Heart Rate",         "bpm",   "60–100 bpm"),
            "systolic_bp":       ("Systolic BP",        "mmHg",  "90–140 mmHg"),
            "diastolic_bp":      ("Diastolic BP",       "mmHg",  "60–90 mmHg"),
            "temperature":       ("Temperature",        "°C",    "36.1–37.2 °C"),
            "pain_score":        ("Pain Level",         "/10",   "—"),
            "arrival_mode":      ("Arrival Mode",       "",      "—"),
            "consciousness":     ("Consciousness",      "",      "—"),
            "age":               ("Age",                "yrs",   "—"),
            "sex":               ("Sex",                "",      "—"),
            "chief_complaint":   ("Chief Complaint",    "",      "—"),
            "critical_event":    ("Critical Event",     "",      "—"),
        }

        # Reverse maps for categorical display values
        arrival_dislay   = {v: k for k, v in arrival_map.items()}
        complaint_display = {v: k for k, v in complaint_map.items()}
        con_display      = {v: k for k, v in con_map.items()}
        gender_display    = {v: k for k, v in gender_map.items()}
        cat_display = {
            "arrival_mode":     arrival_dislay,
            "chief_complaint":  complaint_display,
            "consciousness":    con_display,
            "sex":              gender_display,
            "critical_event":   {0: "No", 1: "Yes"},
        }

        def format_value(feature, raw_val):
            #this helps return human-understandable lingo for values
            if feature in cat_display:
                return cat_display[feature].get(int(raw_val), str(raw_val))
            unit = feat_meta.get(feature, ("", "", ""))[1]
            #format floats
            if unit:
                if float(raw_val) == int(raw_val):
                    return f"{int(raw_val)} {unit}"
                return f"{raw_val:.1f} {unit}"
            return str(raw_val)

        def build_sentence(feature, shap_val, raw_val):
            #build a natural language explanation for shap vals
            name = feat_meta.get(feature, (feature.replace("_", " ").title(), "", ""))[0]
            normal = feat_meta.get(feature, ("", "", "—"))[2]
            val_str = format_value(feature, raw_val)
            direction = "raised" if shap_val > 0 else "lowered"

            #cat features get a simpler explanation
            if feature in cat_display:
                return f"{name} was <b>{val_str}</b>, which {direction} the predicted urgency."

            #explaination for numerical vals comparing them to normal range vitals 
            if normal != "—":
                return (f"{name} at <b>{val_str}</b> (normal {normal}) "
                        f"{direction} the predicted urgency.")
            return f"{name} at <b>{val_str}</b> {direction} the predicted urgency."

        st.markdown("""
        <div class="section-divider">
            <div class="div-line"></div>
            <div class="div-label">Decision Factors</div>
            <div class="div-line"></div>
        </div>""", unsafe_allow_html=True)

        rows_html = '<div class="shap-rows-wrap">'
        for i, row in shap_df.iterrows():
            is_up        = row["shap_value"] > 0
            bar_class    = "bar-up"   if is_up else "bar-down"
            badge_cls    = "badge-up" if is_up else "badge-down"
            badge_txt    = "↑ Urgency" if is_up else "↓ Urgency"
            sentence     = build_sentence(row["feature"], row["shap_value"], row["feature_value"])
            display_name = feat_meta.get(row["feature"], (row["feature"].replace("_", " ").title(), "", ""))[0]
            val_display  = format_value(row["feature"], row["feature_value"])

            rows_html += f"""
            <div class="shap-row">
                <div class="shap-rank">#{i+1}</div>
                <div class="shap-content">
                    <div class="shap-top-line">
                        <span class="shap-feature">{display_name}<span class="feat-val">· {val_display}</span></span>
                        <span class="shap-badge {badge_cls}">{badge_txt}</span>
                    </div>
                    <div class="shap-bar-bg">
                        <div class="shap-bar-fill {bar_class}" style="width:{row['bar_pct']:.1f}%;"></div>
                    </div>
                    <div class="shap-sentence">{sentence}</div>
                </div>
            </div>"""
        rows_html += '</div>'
        st.markdown(rows_html, unsafe_allow_html=True)
    else:
        st.info("Enter patient details and run triage to view results.")
            