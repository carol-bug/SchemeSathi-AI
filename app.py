from pathlib import Path
import streamlit as st
from dotenv import load_dotenv
ROOT = Path(__file__).resolve().parent
load_dotenv(ROOT / '.env')
from core.service import SchemeSathiService
from core.ui import inject_styles, section_header, scheme_card, metric_card

st.set_page_config(page_title='SchemeSathi | Find your benefits', page_icon='🌿', layout='wide')
inject_styles()

@st.cache_resource
def get_service():
    return SchemeSathiService()
service = get_service()
for key, default in [('saved_ids', set()), ('chat', []), ('search_results', None)]:
    if key not in st.session_state: st.session_state[key] = default

with st.sidebar:
    st.markdown('<div class="brand-lockup"><div class="brand-mark">S</div><div><div class="brand-name">SchemeSathi</div><div class="brand-sub">PUBLIC BENEFITS, MADE SIMPLE</div></div></div>', unsafe_allow_html=True)
    st.markdown('---')
    page = st.radio('WORKSPACE', ['Discover schemes','Eligibility checker','Application guide','Ask SchemeSathi','Saved schemes','Upload documents','About'])
    st.markdown('---')
    st.markdown('<div class="sidebar-note"><span class="live-dot"></span> Knowledge base online</div>', unsafe_allow_html=True)
    st.caption(f'{len(service.schemes)} curated scheme records')
    st.caption('Academic prototype · Verify final rules officially')

st.markdown('<div class="topline"><span>INDIA · GOVERNMENT BENEFITS DIRECTORY</span><span class="topline-right">A clearer path to public support ↗</span></div>', unsafe_allow_html=True)
st.markdown('<div class="hero"><div class="eyebrow">YOUR BENEFITS, WITH CLARITY</div><h1>Find the support<br><em>you deserve.</em></h1><p>Discover government schemes, understand the essentials and take your next step with confidence.</p></div>', unsafe_allow_html=True)

if page == 'Discover schemes':
    section_header('Explore the directory', 'Tell us a little about what you need. We’ll surface schemes worth checking.')
    c1,c2,c3=st.columns([1.5,1,1])
    with c1: query=st.text_input('Describe your need',placeholder='e.g. I am a farmer in Karnataka looking for income support',label_visibility='collapsed')
    with c2: state=st.selectbox('State',['Any state','Karnataka','All India'],label_visibility='collapsed')
    with c3: category=st.selectbox('Category',['All categories','Agriculture','Women & family','Education & jobs','Healthcare','Finance'],label_visibility='collapsed')
    if st.button('Find relevant schemes  →',type='primary',use_container_width=True):
        st.session_state.search_results=service.discover(query.strip() or 'government schemes for citizens',state,category)
    results=st.session_state.search_results or service.discover('popular government schemes for citizens',state,category)
    st.markdown(f'<div class="results-top"><div><div class="eyebrow">MATCHED FOR YOU</div><h2>Recommended schemes</h2></div><div class="result-count">{len(results["schemes"])} results</div></div>',unsafe_allow_html=True)
    if results.get('answer'):
        st.markdown(f'<div class="insight-box"><div class="insight-label">SCHEMESATHI INSIGHT</div>{results["answer"]}</div>',unsafe_allow_html=True)
    if results.get('notice'): st.caption(results['notice'])
    if not results['schemes']: st.info('No close matches. Try broader keywords or remove the state filter.')
    cols=st.columns(2,gap='large')
    for i,scheme in enumerate(results['schemes']):
        with cols[i%2]:
            scheme_card(scheme)
            b1,b2=st.columns(2)
            with b1:
                if st.button('♥ Saved' if scheme['id'] in st.session_state.saved_ids else '♡ Save',key='save_'+scheme['id'],use_container_width=True):
                    if scheme['id'] in st.session_state.saved_ids: st.session_state.saved_ids.remove(scheme['id'])
                    else: st.session_state.saved_ids.add(scheme['id'])
                    st.rerun()
            with b2:
                if st.button('Official details ↗',key='source_'+scheme['id'],use_container_width=True): st.link_button('Open official source',scheme['source_url'],use_container_width=True)
    st.markdown('<div class="footnote">Scheme information is indicative. Benefits, eligibility, deadlines and application routes can change. Always verify details on the official portal.</div>',unsafe_allow_html=True)

elif page == 'Eligibility checker':
    section_header('A first eligibility check','Answer a few questions to see which criteria you may need to verify. This is guidance, not an official decision.')
    selected=st.selectbox('Choose a scheme',service.schemes,format_func=lambda x:x['name'])
    with st.form('eligibility_form'):
        l,r=st.columns(2)
        with l:
            age=st.number_input('Your age',0,120,25)
            state=st.selectbox('State / UT',['Karnataka','Tamil Nadu','Andhra Pradesh','Telangana','Kerala','Other'])
            occupation=st.selectbox('Your primary profile',['Farmer','Student','Unemployed graduate','Woman / homemaker','Worker','Other'])
        with r:
            land=st.selectbox('Do you own or cultivate agricultural land?',['Not applicable','Yes','No','Not sure'])
            tax=st.selectbox('Are you an income-tax payer?',['Not sure','No','Yes'])
            govt=st.selectbox('Are you a specified government employee?',['Not sure','No','Yes'])
        submitted=st.form_submit_button('Review my profile  →',type='primary',use_container_width=True)
    if submitted:
        profile={'age':age,'state':state,'occupation':occupation,'owns_agricultural_land':True if land=='Yes' else False if land=='No' else None,'income_tax_payer':True if tax=='Yes' else False if tax=='No' else None,'specified_government_employee':True if govt=='Yes' else False if govt=='No' else None}
        report=service.check_eligibility(selected,profile)
        st.markdown('<div class="report-card">',unsafe_allow_html=True)
        st.subheader(report['headline']); st.write(report['summary'])
        for check in report['checks']: st.markdown(f"- **{check['label']}** — {check['result']}")
        st.markdown('</div>',unsafe_allow_html=True)
        st.warning('This is a preliminary screening against limited local data. The government department makes the final eligibility decision.')
        st.markdown(f'[Verify on the official scheme source]({selected["source_url"]})')

elif page == 'Application guide':
    section_header('From information to action','A practical checklist to help you approach the official application process.')
    selected=st.selectbox('Select a scheme',service.schemes,format_func=lambda x:x['name'])
    st.markdown(f'<div class="guide-intro"><div class="eyebrow">APPLICATION PATHWAY</div><h2>{selected["name"]}</h2><p>{selected["summary"]}</p></div>',unsafe_allow_html=True)
    for i,step in enumerate(service.application_guide(selected)['steps'],1):
        st.markdown(f'<div class="step-row"><div class="step-number">{i:02}</div><div><b>{step["title"]}</b><p>{step["detail"]}</p></div></div>',unsafe_allow_html=True)
    st.markdown(f'<div class="source-panel"><b>Official source</b><br><a href="{selected["source_url"]}" target="_blank">{selected["source_url"]}</a><p>{selected.get("source_note", "Check the latest official instructions before applying.")}</p></div>',unsafe_allow_html=True)
    st.caption('Never share OTPs or passwords. Use official government portals or authorised facilitation centres only.')

elif page == 'Ask SchemeSathi':
    section_header('Your scheme guide, on demand','Ask in everyday language. Answers are grounded in the local scheme library and may use Gemini when configured.')
    for msg in st.session_state.chat:
        with st.chat_message(msg['role']): st.markdown(msg['content'])
    prompt=st.chat_input('Ask about eligibility, benefits, documents or next steps…')
    if prompt:
        st.session_state.chat.append({'role':'user','content':prompt})
        with st.chat_message('user'): st.markdown(prompt)
        with st.chat_message('assistant'):
            with st.spinner('Searching scheme records…'): response=service.ask(prompt)
            st.markdown(response['answer'])
            if response.get('sources'):
                st.markdown('**Sources**')
                for src in response['sources']: st.markdown(f'- [{src["name"]}]({src["url"]})')
            if response.get('notice'): st.caption(response['notice'])
        st.session_state.chat.append({'role':'assistant','content':response['answer']})
        st.rerun()

elif page == 'Saved schemes':
    section_header('Your shortlist','Keep useful schemes close while you compare your next steps.')
    saved=[s for s in service.schemes if s['id'] in st.session_state.saved_ids]
    if not saved: st.info('No saved schemes yet. Visit Discover schemes and tap Save on a scheme card.')
    cols=st.columns(2)
    for i,s in enumerate(saved):
        with cols[i%2]: scheme_card(s)

elif page == 'Upload documents':
    section_header('Add a scheme document','Upload a text-based government notification or guideline PDF to index it for your questions.')
    pdf=st.file_uploader('Choose a PDF',type=['pdf'],help='Do not upload documents containing Aadhaar numbers, bank details or other sensitive personal information.')
    if pdf and st.button('Extract and index document  →',type='primary'):
        with st.spinner('Reading PDF and indexing text…'): out=service.ingest_pdf(pdf.getvalue(),pdf.name)
        if out['ok']: st.success(f"Indexed {out['chunks']} text chunks from {pdf.name}.")
        else: st.error(out['message'])
    st.caption('Scanned PDFs require OCR, which is not included. Uploaded text is stored locally in the project database.')

else:
    section_header('Built for clarity. Designed for trust.','SchemeSathi AI is an academic prototype exploring agentic workflows and retrieval-augmented generation for public-benefit discovery.')
    a,b,c=st.columns(3)
    metric_card(a,'SCHEME LIBRARY',str(len(service.schemes)),'Curated records')
    metric_card(b,'RETRIEVAL',service.kb.backend_label,'Local-first knowledge base')
    metric_card(c,'AI RESPONSE','Optional Gemini','Grounded generation with fallback')
    st.markdown('### How the assistant works')
    for n,title,desc in [('01','Understand','Identify the user’s state, profile and support intent.'),('02','Retrieve','Search the local ChromaDB vector library with keyword fallback.'),('03','Guide','Provide preliminary eligibility checks and application steps.'),('04','Explain','Use retrieved records as context for Gemini or provide a local answer.')]:
        st.markdown(f'<div class="step-row"><div class="step-number">{n}</div><div><b>{title}</b><p>{desc}</p></div></div>',unsafe_allow_html=True)
    st.markdown('### Trust & safety')
    st.write('SchemeSathi does not make official eligibility decisions, submit applications, access beneficiary databases or verify live application status. The starter dataset is not exhaustive. Confirm current details with the relevant department.')
    st.markdown('### Technology')
    st.write('Python · Streamlit · Agent workflow · RAG · ChromaDB · Sentence Transformers · Google Gemini API · PyPDF')

st.markdown('<div class="footer"><span>© 2026 SchemeSathi AI · Academic prototype</span><span>Built to make public support easier to navigate.</span></div>',unsafe_allow_html=True)
