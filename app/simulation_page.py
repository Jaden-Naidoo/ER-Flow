# helper to display sim page and add functionality to it
def sim_page():
    'Interactive simulation page to show how the model can be applied in real life.'
    #importing req. libraries
    import streamlit as st
    import base64
    import os
    import time

    st.set_page_config(layout="wide")

    # Design of sim page 
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500;600&family=Syne:wght@400;500;600;700&family=DM+Sans:wght@300;400;500;600&display=swap');
    @import url('https://fonts.googleapis.com/css2?family=Material+Symbols+Rounded:opsz,wght,FILL,GRAD@24,400,1,0');
    
    :root {                       
        --bg-deep:       #0E1117;
        --bg-surface:    #0d1117;
        --bg-card:       #151b23;
        --bg-card-alt:   #1c2432;
        --bg-elevated:   #212a39;
        
        --text-primary:  #f0f3f6;
        --text-secondary:#b4bbc6;
        --text-muted:    #7d8590;
        --text-dim:      #484f58;
        
        --accent:        #58a6ff;
        --accent-glow:   rgba(88,166,255,0.15);
        --accent-border: rgba(88,166,255,0.4);
        
        --border:        rgba(255,255,255,0.08);
        --border-hover:  rgba(255,255,255,0.15);
        --glass:         rgba(255,255,255,0.02);

        --radius-xs:     6px;
        --radius-sm:     10px;
        --radius:        16px;
        --radius-lg:     24px;
        --radius-xl:     32px;
        
        --space-1:  4px;
        --space-2:  8px;
        --space-3:  12px;
        --space-4:  16px;
        --space-5:  20px;
        --space-6:  24px;
        --space-7:  32px;
        --space-8:  40px;
        

        --color-paramedic:     #ff6b6b;
        --color-paramedic-dim: rgba(255,107,107,0.12);
        --color-nurse:         #a78bfa;
        --color-nurse-dim:     rgba(167,139,250,0.12);
        --color-ai:            #22d3ee;
        --color-ai-dim:        rgba(34,211,238,0.12);
        --color-doctor:        #4ade80;
        --color-doctor-dim:    rgba(74,222,128,0.12);

        --shadow-sm:  0 2px 8px rgba(0,0,0,0.3);
        --shadow-md:  0 8px 24px rgba(0,0,0,0.4);
        --shadow-lg:  0 16px 48px rgba(0,0,0,0.5);
    }

    .stApp {
        background: linear-gradient(180deg, var(--bg-deep) 0%, #0a0c10 100%);
        color: var(--text-primary);
        font-family: 'DM Sans', -apple-system, BlinkMacSystemFont, sans-serif;
    }
    
    h1, h2, h3, h4 { 
        font-family: 'Syne', sans-serif;
        letter-spacing: -0.02em;
    }

    .material-symbols-rounded {
        font-family: 'Material Symbols Rounded';
        font-variation-settings: 'FILL' 1, 'wght' 400, 'GRAD' 0, 'opsz' 24;
    }

    .page-header {
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding: var(--space-4) 0;
        margin-bottom: var(--space-5);
        border-bottom: 1px solid var(--border);
    }
    
    .header-left {
        display: flex;
        align-items: center;
        gap: var(--space-4);
    }
    
    .header-badge {
        display: inline-flex;
        align-items: center;
        gap: var(--space-2);
        font-family: 'IBM Plex Mono', monospace;
        font-size: 0.65rem;
        font-weight: 500;
        color: var(--accent);
        text-transform: uppercase;
        letter-spacing: 2px;
        padding: var(--space-1) var(--space-3);
        background: var(--accent-glow);
        border: 1px solid var(--accent-border);
        border-radius: var(--radius-xl);
    }
    
    .header-badge::before {
        content: '';
        width: 6px;
        height: 6px;
        background: var(--accent);
        border-radius: 50%;
        animation: pulse 2s ease-in-out infinite;
    }
    
    @keyframes pulse {
        0%, 100% { opacity: 1; transform: scale(1); }
        50% { opacity: 0.5; transform: scale(0.8); }
    }
    
    .page-header h1 {
        font-size: 1.5rem;
        font-weight: 700;
        color: var(--text-primary);
        margin: 0;
        line-height: 1;
    }
    
    .page-header h1 .h1_colour {
        background: #6495ED;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }
    
    .header-scene {
        font-size: 0.8rem;
        color: var(--text-muted);
        text-align: right;
    }
    
    .header-scene strong {
        color: var(--text-secondary);
    }

    .scene-bar {
        background: var(--bg-card);
        border: 1px solid var(--border);
        border-radius: var(--radius);
        padding: var(--space-4) var(--space-5);
        margin-bottom: var(--space-5);
        display: flex;
        align-items: center;
        justify-content: space-between;
        gap: var(--space-5);
    }
    
    .scene-info {
        display: flex;
        align-items: center;
        gap: var(--space-4);
    }
    
    .scene-icon {
        font-size: 1.5rem;
        width: 44px;
        height: 44px;
        background: var(--accent-glow);
        border: 1px solid var(--accent-border);
        border-radius: var(--radius-sm);
        display: flex;
        align-items: center;
        justify-content: center;
    }
    
    .scene-text {
        display: flex;
        flex-direction: column;
        gap: 2px;
    }
    
    .scene-label {
        font-family: 'IBM Plex Mono', monospace;
        font-size: 0.6rem;
        font-weight: 600;
        color: var(--accent);
        text-transform: uppercase;
        letter-spacing: 1.5px;
    }
    
    .scene-title {
        font-family: 'Syne', sans-serif;
        font-size: 0.95rem;
        font-weight: 600;
        color: var(--text-primary);
        line-height: 1.2;
    }
    
    .scene-tags {
        display: flex;
        gap: var(--space-2);
    }
    
    .scene-tag {
        font-family: 'IBM Plex Mono', monospace;
        font-size: 0.6rem;
        color: var(--text-dim);
        text-transform: uppercase;
        letter-spacing: 0.5px;
        padding: 4px 8px;
        background: var(--bg-deep);
        border: 1px solid var(--border);
        border-radius: var(--radius-xs);
    }

    .progress-bar {
        display: flex;
        align-items: center;
        justify-content: center;
        gap: var(--space-2);
        padding: var(--space-4) 0;
        margin-bottom: var(--space-5);
    }
    
    .progress-step {
        display: flex;
        align-items: center;
        gap: var(--space-2);
    }
    
    .progress-dot {
        width: 12px;
        height: 12px;
        border-radius: 50%;
        background: var(--bg-elevated);
        border: 2px solid var(--border);
        transition: all 0.3s;
    }
    
    .progress-dot.active {
        background: var(--accent);
        border-color: var(--accent);
        box-shadow: 0 0 12px rgba(88,166,255,0.6);
        transform: scale(1.2);
    }
    
    .progress-dot.completed {
        background: var(--text-dim);
        border-color: var(--text-dim);
    }
    
    .progress-step-name {
        font-family: 'IBM Plex Mono', monospace;
        font-size: 0.65rem;
        color: var(--text-dim);
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }
    
    .progress-step.active .progress-step-name {
        color: var(--accent);
    }
    
    .progress-step.completed .progress-step-name {
        color: var(--text-muted);
    }
    
    .progress-connector {
        width: 30px;
        height: 2px;
        background: var(--border);
    }
    
    .progress-connector.completed {
        background: var(--text-dim);
    }

    .speaker-stage {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        min-height: 380px;
    }

    .speaker-card {
        position: relative;
        background: var(--bg-card);
        border: 1px solid var(--border);
        border-radius: var(--radius-lg);
        padding: var(--space-6) var(--space-7);
        width: 100%;
        max-width: 600px;
        text-align: center;
        opacity: 0;
        animation: cardEnter 0.5s cubic-bezier(0.16, 1, 0.3, 1) forwards;
        box-shadow: var(--shadow-lg);
    }
    
    @keyframes cardEnter {
        from { opacity: 0; transform: translateY(20px) scale(0.98); }
        to   { opacity: 1; transform: translateY(0) scale(1); }
    }
    
    .speaker-card.glow-paramedic { box-shadow: var(--shadow-lg), 0 0 50px var(--color-paramedic-dim); }
    .speaker-card.glow-nurse     { box-shadow: var(--shadow-lg), 0 0 50px var(--color-nurse-dim); }
    .speaker-card.glow-ai        { box-shadow: var(--shadow-lg), 0 0 50px var(--color-ai-dim); }
    .speaker-card.glow-doctor    { box-shadow: var(--shadow-lg), 0 0 50px var(--color-doctor-dim); }

    .speaker-avatar {
        position: relative;
        width: 90px;
        height: 90px;
        margin: 0 auto var(--space-4);
    }
    
    .speaker-avatar-ring {
        position: absolute;
        inset: -6px;
        border-radius: 50%;
        border: 2px solid;
        opacity: 0.3;
        animation: ringPulse 2s ease-in-out infinite;
    }
    
    @keyframes ringPulse {
        0%, 100% { transform: scale(1); opacity: 0.3; }
        50% { transform: scale(1.05); opacity: 0.5; }
    }
    
    .ring-paramedic { border-color: var(--color-paramedic); }
    .ring-nurse     { border-color: var(--color-nurse); }
    .ring-ai        { border-color: var(--color-ai); }
    .ring-doctor    { border-color: var(--color-doctor); }
    
    .speaker-avatar-inner {
        width: 100%;
        height: 100%;
        border-radius: 50%;
        border: 3px solid;
        background: var(--bg-elevated);
        display: flex;
        align-items: center;
        justify-content: center;
        overflow: hidden;
    }
    
    .avatar-paramedic { border-color: var(--color-paramedic); }
    .avatar-nurse     { border-color: var(--color-nurse); }
    .avatar-ai        { border-color: var(--color-ai); }
    .avatar-doctor    { border-color: var(--color-doctor); }

    .speaker-role {
        font-family: 'IBM Plex Mono', monospace;
        font-size: 0.6rem;
        font-weight: 500;
        text-transform: uppercase;
        letter-spacing: 2px;
        margin-bottom: var(--space-1);
        opacity: 0.7;
    }
    
    .role-paramedic { color: var(--color-paramedic); }
    .role-nurse     { color: var(--color-nurse); }
    .role-ai        { color: var(--color-ai); }
    .role-doctor    { color: var(--color-doctor); }
    
    .speaker-name {
        font-family: 'Syne', sans-serif;
        font-size: 1.2rem;
        font-weight: 700;
        margin-bottom: var(--space-4);
    }
    
    .name-paramedic { color: var(--color-paramedic); }
    .name-nurse     { color: var(--color-nurse); }
    .name-ai        { color: var(--color-ai); }
    .name-doctor    { color: var(--color-doctor); }

    .speaker-dialogue {
        font-size: 0.85rem;
        line-height: 1.7;
        color: var(--text-secondary);
        max-width: 500px;
        margin: 0 auto var(--space-4);
        text-align: left;
        padding: var(--space-4);
        background: var(--glass);
        border-radius: var(--radius);
        border: 1px solid var(--border);
        max-height: 130px;
        overflow-y: auto;
    }
    
    .speaker-dialogue::-webkit-scrollbar {
        width: 4px;
    }
    
    .speaker-dialogue::-webkit-scrollbar-track {
        background: var(--bg-deep);
        border-radius: 2px;
    }
    
    .speaker-dialogue::-webkit-scrollbar-thumb {
        background: var(--border-hover);
        border-radius: 2px;
    }

    .waveform-container {
        display: flex;
        align-items: center;
        justify-content: center;
        gap: var(--space-3);
        padding: var(--space-3) var(--space-4);
        background: var(--bg-deep);
        border-radius: var(--radius-sm);
    }
    
    .waveform-label {
        font-family: 'IBM Plex Mono', monospace;
        font-size: 0.6rem;
        text-transform: uppercase;
        letter-spacing: 1px;
        color: var(--text-dim);
    }
    
    .waveform-bars {
        display: flex;
        align-items: center;
        gap: 3px;
        height: 32px;
    }
    
    .wave-bar {
        width: 3px;
        border-radius: 2px;
        animation: waveAnim 0.9s ease-in-out infinite;
    }
    
    @keyframes waveAnim {
        0%, 100% { height: 6px; opacity: 0.4; }
        50%      { height: 24px; opacity: 1; }
    }
    
    .wave-bar:nth-child(1)  { animation-delay: 0.00s; }
    .wave-bar:nth-child(2)  { animation-delay: 0.07s; }
    .wave-bar:nth-child(3)  { animation-delay: 0.14s; }
    .wave-bar:nth-child(4)  { animation-delay: 0.21s; }
    .wave-bar:nth-child(5)  { animation-delay: 0.28s; }
    .wave-bar:nth-child(6)  { animation-delay: 0.35s; }
    .wave-bar:nth-child(7)  { animation-delay: 0.42s; }
    .wave-bar:nth-child(8)  { animation-delay: 0.49s; }
    .wave-bar:nth-child(9)  { animation-delay: 0.42s; }
    .wave-bar:nth-child(10) { animation-delay: 0.35s; }
    .wave-bar:nth-child(11) { animation-delay: 0.28s; }
    .wave-bar:nth-child(12) { animation-delay: 0.21s; }

    .result-card {
        background: linear-gradient(135deg, var(--bg-card) 0%, var(--bg-card-alt) 100%);
        border: 1px solid var(--border);
        border-radius: var(--radius-lg);
        overflow: hidden;
        opacity: 0;
        animation: cardEnter 0.7s cubic-bezier(0.16, 1, 0.3, 1) forwards;
        box-shadow: var(--shadow-lg);
        width: 100%;
        max-width: 500px;
    }
    
    .result-header {
        padding: var(--space-3) var(--space-5);
        background: rgba(0,0,0,0.3);
        border-bottom: 1px solid var(--border);
        display: flex;
        align-items: center;
        justify-content: space-between;
    }
    
    .result-badge {
        font-family: 'IBM Plex Mono', monospace;
        font-size: 0.6rem;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 1.5px;
        color: var(--text-dim);
        display: flex;
        align-items: center;
        gap: var(--space-2);
    }
    
    .result-badge::before {
        content: '✓';
        color: var(--color-doctor);
    }
    
    .result-timestamp {
        font-family: 'IBM Plex Mono', monospace;
        font-size: 0.6rem;
        color: var(--text-dim);
    }
    
    .result-body {
        padding: var(--space-5);
        text-align: center;
    }
    
    .result-level {
        font-family: 'Syne', sans-serif;
        font-size: 2.5rem;
        font-weight: 700;
        line-height: 1;
        margin-bottom: var(--space-2);
        text-shadow: 0 0 40px currentColor;
    }
    
    .result-level-label {
        font-family: 'IBM Plex Mono', monospace;
        font-size: 0.7rem;
        font-weight: 500;
        text-transform: uppercase;
        letter-spacing: 3px;
        margin-bottom: var(--space-4);
        opacity: 0.9;
    }
    
    .result-description {
        font-size: 0.85rem;
        color: var(--text-muted);
        max-width: 350px;
        margin: 0 auto var(--space-4);
        line-height: 1.5;
    }
    
    .result-footer {
        display: flex;
        justify-content: center;
        gap: var(--space-7);
        padding-top: var(--space-4);
        border-top: 1px solid var(--border);
    }
    
    .result-stat {
        text-align: center;
    }
    
    .result-stat-value {
        font-family: 'IBM Plex Mono', monospace;
        font-size: 1.1rem;
        font-weight: 600;
        color: var(--text-primary);
    }
    
    .result-stat-label {
        font-size: 0.55rem;
        color: var(--text-dim);
        text-transform: uppercase;
        letter-spacing: 1px;
        margin-top: 2px;
    }

    .idle-state {
        text-align: center;
        padding: var(--space-6);
    }
    
    .idle-icon {
        font-size: 2.5rem;
        margin-bottom: var(--space-4);
        opacity: 0.5;
    }
    
    .idle-title {
        font-family: 'Syne', sans-serif;
        font-size: 1rem;
        font-weight: 600;
        color: var(--text-secondary);
        margin-bottom: var(--space-2);
    }
    
    .idle-description {
        font-size: 0.8rem;
        color: var(--text-muted);
        max-width: 320px;
        margin: 0 auto;
        line-height: 1.5;
    }

    .stButton > button {
        font-family: 'IBM Plex Mono', monospace !important;
        font-size: 0.7rem !important;
        font-weight: 600 !important;
        letter-spacing: 1px !important;
        text-transform: uppercase !important;
        padding: var(--space-2) var(--space-4) !important;
        border-radius: var(--radius-sm) !important;
        transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1) !important;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px) !important;
        box-shadow: var(--shadow-md) !important;
    }
    
    .stButton > button[kind="primary"] {
        background: linear-gradient(135deg, var(--accent) 0%, #3b82f6 100%) !important;
        border: none !important;
    }
    
    .stAudio {
        position: absolute;
        opacity: 0;
        pointer-events: none;
        height: 0;
        overflow: hidden;
    }
    </style>
    """, unsafe_allow_html=True)

    if 'sim_running' not in st.session_state:
        st.session_state.sim_running = False
    if 'current_step' not in st.session_state:
        st.session_state.current_step = 0
    if 'show_result' not in st.session_state:
        st.session_state.show_result = False

    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    dialogue_script = [
        {
            "speaker": "paramedic",
            "role": "First Responder",
            "name": "Paramedic Arrival",
            "text": "This is a 25-year-old male, brought in by ambulance. He's complaining of severe chest pain that started about thirty minutes ago, radiating to his left arm. Vitals on arrival: heart rate one hundred and twenty, respiratory rate twenty-eight, oxygen saturation eighty-nine percent on room air. Patient was alert but fell unconscious before arrival. No known allergies. No prior cardiac history reported.",
            "audio_file": "paramedic.mp3",
            "duration": 29
        },
        {
            "speaker": "nurse",
            "role": "Triage Assessment",
            "name": "Triage Nurse",
            "text": "Alright, I'm entering the patient's vitals and symptoms into the triage system now. Chest pain, shortness of breath, elevated heart rate, and low oxygen saturation. Please remain still while we complete your assessment. Vitals and symptoms have been recorded. Initiating triage assessment.",
            "audio_file": "nurse.mp3",
            "duration": 20
        },
        {
            "speaker": "ER Flow Triage model",
            "role": "Decision Support",
            "name": "AI Triage System",
            "text": "Triage assessment complete. Based on the provided vital signs and symptoms, this patient has been classified as Triage Level One: Immediate. This classification indicates a life-threatening condition requiring urgent medical intervention. The primary factors influencing this decision were low oxygen saturation, elevated heart rate, and reported chest pain. Oxygen saturation below ninety percent significantly increased the predicted risk. Combined with tachycardia and respiratory distress, the probability of a critical outcome is high.",
            "audio_file": "ai_system.mp3",
            "duration": 28
        },
        {
            "speaker": "doctor",
            "role": "Clinical Lead",
            "name": "Emergency Physician",
            "text": "This is a priority one case. Move the patient to resuscitation immediately. Start oxygen therapy and prepare for cardiac monitoring. I want labs and imaging ordered NOW!",
            "audio_file": "doctor.mp3",
            "duration": 13
        }
    ]

    triage_result = {
        "level": 1,
        "label": "IMMEDIATE",
        "description": "Life-threatening condition requiring immediate intervention",
        "color": "#ef4444",
        "response_time": "0 min",
        "confidence": "94.7%"
    }

    st.markdown("""
    <div class="page-header">
        <div class="header-left">
            <div class="header-badge">Live</div>
            <h1> <span class = 'h1_colour'>ER</span> Flow Triage Simulation</h1>
        </div>
        <div class="header-scene">
            <strong>25 y/o Male</strong> · Chest Pain<br>
            Ambulance Arrival
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="scene-bar">
        <div class="scene-info">
            <div class="scene-icon">🏥</div>
            <div class="scene-text">
                <span class="scene-label">Active Scenario</span>
                <span class="scene-title">Emergency Department Arrival</span>
            </div>
        </div>
        <div class="scene-tags">
            <span class="scene-tag">Cardiac</span>
            <span class="scene-tag">AI Triage</span>
            <span class="scene-tag">Critical</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    if st.session_state.sim_running or st.session_state.show_result:
        progress_html = '<div class="progress-bar">'
        
        for i, msg in enumerate(dialogue_script):
            dot_class = ""
            step_class = ""
            if i < st.session_state.current_step or st.session_state.show_result:
                dot_class = "completed"
                step_class = "completed"
            elif i == st.session_state.current_step and st.session_state.sim_running:
                dot_class = "active"
                step_class = "active"
            
            progress_html += f'''
            <div class="progress-step {step_class}">
                <div class="progress-dot {dot_class}"></div>
                <span class="progress-step-name">{msg['name'].split()[0]}</span>
            </div>
            '''
            
            if i < len(dialogue_script) - 1:
                connector_class = "completed" if (i < st.session_state.current_step or st.session_state.show_result) else ""
                progress_html += f'<div class="progress-connector {connector_class}"></div>'
        
        progress_html += '</div>'
        st.markdown(progress_html, unsafe_allow_html=True)

    col1, col2, col3 = st.columns([2, 1, 2])
    with col2:
        if not st.session_state.sim_running and not st.session_state.show_result:
            if st.button("▶ Start", use_container_width=True, type="primary"):
                st.session_state.sim_running = True
                st.session_state.current_step = 0
                st.session_state.show_result = False
                st.rerun()
        elif st.session_state.sim_running:
            if st.button("⏹ Stop", use_container_width=True):
                st.session_state.sim_running = False
                st.session_state.current_step = 0
                st.session_state.show_result = False
                st.rerun()
        else:
            if st.button("↻ Restart", use_container_width=True, type="primary"):
                st.session_state.sim_running = True
                st.session_state.current_step = 0
                st.session_state.show_result = False
                st.rerun()

    def get_icon_html(speaker):
        """Return Material Icon styled with speaker color."""
        color_map = {
            "paramedic": "var(--color-paramedic)",
            "nurse": "var(--color-nurse)",
            "ai": "var(--color-ai)",
            "doctor": "var(--color-doctor)"
        }
        color = color_map.get(speaker, "var(--accent)")
        return f'<span class="material-symbols-rounded" style="font-size:3rem;color:{color};">account_circle</span>'

    if st.session_state.sim_running and st.session_state.current_step < len(dialogue_script):
        current_msg = dialogue_script[st.session_state.current_step]
        speaker = current_msg["speaker"]
        
        color_map = {
            "paramedic": "var(--color-paramedic)",
            "nurse": "var(--color-nurse)",
            "ai": "var(--color-ai)",
            "doctor": "var(--color-doctor)"
        }
        speaker_color = color_map.get(speaker, "var(--accent)")
        
        waveform_bars = "".join([
            f'<div class="wave-bar" style="background:{speaker_color};"></div>' 
            for _ in range(12)
        ])
        
        icon_html = get_icon_html(speaker)
        
        st.markdown(f"""
        <div class="speaker-stage">
            <div class="speaker-card glow-{speaker}">
                <div class="speaker-avatar">
                    <div class="speaker-avatar-ring ring-{speaker}"></div>
                    <div class="speaker-avatar-inner avatar-{speaker}">
                        {icon_html}
                    </div>
                </div>
                <div class="speaker-role role-{speaker}">{current_msg['role']}</div>
                <div class="speaker-name name-{speaker}">{current_msg['name']}</div>
                <div class="speaker-dialogue">{current_msg['text']}</div>
                <div class="waveform-container">
                    <span class="waveform-label">Speaking</span>
                    <div class="waveform-bars">
                        {waveform_bars}
                    </div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        audio_path = os.path.join(script_dir, "audio", current_msg['audio_file'])
        if os.path.exists(audio_path):
            with open(audio_path, "rb") as audio_file:
                audio_bytes = audio_file.read()
                st.audio(audio_bytes, format="audio/mp3", autoplay=True)
        
        time.sleep(current_msg['duration'])
        st.session_state.current_step += 1
        
        if st.session_state.current_step >= len(dialogue_script):
            st.session_state.sim_running = False
            st.session_state.show_result = True
        
        st.rerun()

    elif st.session_state.show_result:
        st.markdown(f"""
        <div class="speaker-stage">
            <div class="result-card">
                <div class="result-header">
                    <span class="result-badge">Assessment Complete</span>
                    <span class="result-timestamp">1.2s</span>
                </div>
                <div class="result-body">
                    <div class="result-level" style="color:{triage_result['color']};">
                        LEVEL {triage_result['level']}
                    </div>
                    <div class="result-level-label" style="color:{triage_result['color']};">
                        {triage_result['label']}
                    </div>
                    <p class="result-description">{triage_result['description']}</p>
                    <div class="result-footer">
                        <div class="result-stat">
                            <div class="result-stat-value">{triage_result['response_time']}</div>
                            <div class="result-stat-label">Response</div>
                        </div>
                        <div class="result-stat">
                            <div class="result-stat-value">{triage_result['confidence']}</div>
                            <div class="result-stat-label">Confidence</div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    else:
        st.markdown("""
        <div class="speaker-stage">
            <div class="idle-state">
                <div class="idle-icon">🎬</div>
                <div class="idle-title">Ready to Begin</div>
                <p class="idle-description">
                    Click "Start" to experience the emergency triage scenario with audio and visual feedback.
                </p>
            </div>
        </div>
        """, unsafe_allow_html=True)