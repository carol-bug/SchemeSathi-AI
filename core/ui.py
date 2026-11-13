import streamlit as st

def inject_styles():
    st.markdown('''<style>
    @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Manrope:wght@400;500;600;700;800&display=swap');
    :root{--ink:#18251f;--muted:#6f7c73;--green:#176b4b;--line:#e5e9e2}
    html,body,[class*="css"]{font-family:'DM Sans',sans-serif}
    .stApp{background:linear-gradient(180deg,#f7f8f4 0%,#fff 60%,#f7f8f4 100%);color:var(--ink)}
    [data-testid="stHeader"]{background:transparent}
    [data-testid="stSidebar"]{background:#f0f4ed;border-right:1px solid #e2e9df}
    [data-testid="stSidebar"]>div{padding-top:1.3rem}
    .brand-lockup{display:flex;align-items:center;gap:12px;padding:8px 4px 18px}.brand-mark{height:42px;width:42px;border-radius:14px;background:#176b4b;color:white;display:flex;align-items:center;justify-content:center;font:800 24px Manrope;box-shadow:0 7px 18px #176b4b30}.brand-name{font:800 19px Manrope;color:#183a2b;letter-spacing:-.6px}.brand-sub{font-size:8px;letter-spacing:1.4px;color:#738278;font-weight:700;margin-top:2px}
    .sidebar-note{font-size:12px;color:#486454;background:#e4efe5;padding:10px 12px;border-radius:12px}.live-dot{display:inline-block;height:7px;width:7px;background:#3b9a69;border-radius:50%;margin-right:7px}
    .topline{display:flex;justify-content:space-between;color:#77847a;font-size:10px;letter-spacing:1.5px;font-weight:700;padding:4px 0 20px;border-bottom:1px solid var(--line)}.topline-right{letter-spacing:.2px;text-transform:none;font-size:12px}
    .hero{padding:34px 0 30px;border-bottom:1px solid var(--line);margin-bottom:30px}.eyebrow{font-size:10px;letter-spacing:1.7px;font-weight:800;color:#4e8a68;margin-bottom:10px}.hero h1{font:800 clamp(40px,5vw,66px)/1.04 Manrope,sans-serif;letter-spacing:-3px;color:#172b20;margin:0}.hero h1 em{font-style:normal;color:#24734f}.hero p{font-size:16px;color:#69776d;max-width:560px;margin:16px 0 0;line-height:1.65}
    .section-title{font:800 25px Manrope;letter-spacing:-.8px;color:#1d3025;margin:0}.section-sub{font-size:13px;color:#738077;margin:7px 0 22px}.results-top{display:flex;align-items:end;justify-content:space-between;margin:32px 0 14px}.results-top h2{font:800 24px Manrope;margin:0;color:#1d3025}.result-count{font-size:12px;color:#6f7c73;background:#eef3ed;border-radius:30px;padding:7px 12px}
    .scheme-card{background:white;border:1px solid #e5eae3;border-radius:18px;padding:20px;margin-bottom:10px;box-shadow:0 5px 18px #193d2510;min-height:220px}.scheme-top{display:flex;justify-content:space-between;align-items:center;margin-bottom:15px}.scheme-tag{background:#edf5ee;color:#39724e;font-size:10px;font-weight:800;letter-spacing:.8px;padding:6px 9px;border-radius:20px;text-transform:uppercase}.scheme-state{font-size:10px;color:#879187}.scheme-card h3{font:700 18px/1.3 Manrope;margin:0 0 9px;letter-spacing:-.5px;color:#1d3025}.scheme-card p{font-size:12px;color:#69766d;line-height:1.6;margin:0 0 12px}.scheme-benefit{background:#f5f8f3;border-radius:11px;padding:10px 12px;font-size:12px;color:#3c5845;line-height:1.5}.scheme-link{display:inline-block;margin-top:13px;font-size:11px;font-weight:700;color:#176b4b;text-decoration:none}
    .insight-box{background:#eaf3eb;border-left:3px solid #32815a;border-radius:12px;padding:16px 18px;color:#355342;font-size:13px;line-height:1.65;margin:16px 0}.insight-label{font-size:9px;letter-spacing:1.5px;font-weight:800;color:#4b8a63;margin-bottom:6px}.footnote{font-size:11px;color:#8b948c;border-top:1px solid var(--line);padding-top:15px;margin-top:22px}
    .report-card,.guide-intro,.source-panel{background:#fff;border:1px solid var(--line);border-radius:18px;padding:22px;margin:20px 0;box-shadow:0 5px 18px #193d2508}.guide-intro h2{font:800 25px Manrope;margin:0 0 7px}.guide-intro p{font-size:13px;color:#738077;line-height:1.6}.step-row{display:flex;gap:16px;align-items:flex-start;background:#fff;border:1px solid var(--line);padding:17px 18px;border-radius:15px;margin:10px 0}.step-number{flex:0 0 38px;height:38px;border-radius:12px;background:#e9f3ec;color:#28744e;display:flex;align-items:center;justify-content:center;font:800 13px Manrope}.step-row b{font:700 14px Manrope;color:#243b2d}.step-row p{font-size:12px;color:#748077;line-height:1.6;margin:5px 0 0}.source-panel{font-size:13px;color:#536257;line-height:1.6}.source-panel a{color:#176b4b;word-break:break-all}
    .metric{background:#fff;border:1px solid var(--line);border-radius:16px;padding:18px}.metric-label{font-size:9px;letter-spacing:1.4px;font-weight:800;color:#849087}.metric-value{font:800 21px Manrope;color:#21432f;margin:8px 0 3px}.metric-sub{font-size:11px;color:#849087}.footer{display:flex;justify-content:space-between;border-top:1px solid var(--line);margin-top:48px;padding:18px 0 8px;color:#9aa39b;font-size:10px}
    div.stButton>button{border-radius:11px;border:1px solid #dce5dc;font-weight:700;min-height:42px}div.stButton>button[kind="primary"]{background:#176b4b;color:white;border:1px solid #176b4b}div.stButton>button:hover{border-color:#176b4b;color:#176b4b}input,textarea,[data-baseweb="select"]>div{border-radius:10px!important}[data-testid="stChatMessage"]{background:white;border:1px solid var(--line);border-radius:14px}.stAlert{border-radius:12px}
    @media(max-width:700px){.topline-right{display:none}.hero h1{letter-spacing:-1.7px}.footer{display:block}.scheme-card{min-height:0}}
    </style>''',unsafe_allow_html=True)

def section_header(title,subtitle):
    st.markdown(f'<div class="section-title">{title}</div><div class="section-sub">{subtitle}</div>',unsafe_allow_html=True)

def scheme_card(s):
    category=s.get('category','Public benefit'); state=s.get('jurisdiction',s.get('state','Government scheme'))
    benefit=s.get('benefits','See the official source for benefit details.')
    st.markdown(f'<div class="scheme-card"><div class="scheme-top"><span class="scheme-tag">{category}</span><span class="scheme-state">{state}</span></div><h3>{s["name"]}</h3><p>{s["summary"]}</p><div class="scheme-benefit"><b>At a glance</b><br>{benefit}</div><a class="scheme-link" href="{s["source_url"]}" target="_blank">VIEW OFFICIAL SOURCE ↗</a></div>',unsafe_allow_html=True)

def metric_card(col,label,value,sub):
    with col: st.markdown(f'<div class="metric"><div class="metric-label">{label}</div><div class="metric-value">{value}</div><div class="metric-sub">{sub}</div></div>',unsafe_allow_html=True)
