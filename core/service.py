import os, json, hashlib
from pathlib import Path
from core.knowledge import KnowledgeBase
from core.agents import QueryUnderstandingAgent, EligibilityAgent, ApplicationAgent
ROOT=Path(__file__).resolve().parents[1]
class SchemeSathiService:
    def __init__(self):
        self.schemes=json.loads((ROOT/'data'/'schemes.json').read_text(encoding='utf-8'))
        self.kb=KnowledgeBase(self.schemes,ROOT/'database'/'chroma_db')
        self.understanding=QueryUnderstandingAgent(); self.eligibility=EligibilityAgent(); self.application=ApplicationAgent(); self._client=None
    def _get_client(self):
        key=os.getenv('GEMINI_API_KEY','').strip()
        if not key: return None
        if self._client is None:
            from google import genai
            self._client=genai.Client(api_key=key)
        return self._client
    def _generate(self,query,records):
        if not records: return None,'No matching source records were retrieved.'
        try:
            client=self._get_client()
            if client is None: return None,'Gemini is not configured; local source-grounded results are shown.'
            model=os.getenv('GEMINI_MODEL','gemini-2.5-flash').strip()
            context='\n\n'.join(f"SCHEME: {s['name']}\nSUMMARY: {s['summary']}\nBENEFITS: {s.get('benefits','')}\nELIGIBILITY: {s.get('eligibility_text',s.get('eligibility',''))}\nAPPLICATION: {s.get('application_text',s.get('application',''))}\nDOCUMENTS: {s.get('documents_text','')}\nOFFICIAL SOURCE: {s['source_url']}" for s in records)
            prompt=("You are SchemeSathi, a careful public-benefits assistant for India. Use only the supplied records. Never invent eligibility rules, benefit amounts, deadlines, documents, phone numbers or URLs. State when information is missing. Explain that government departments make final decisions. Use plain language.\n\n"+f"QUESTION: {query}\n\nRETRIEVED RECORDS:\n{context}")
            response=client.models.generate_content(model=model,contents=prompt)
            return getattr(response,'text',None),None
        except Exception as exc:
            return None,f'Gemini is unavailable ({type(exc).__name__}: {exc}). Local retrieval fallback is active.'
    def discover(self,query,state='Any state',category='All categories'):
        intent=self.understanding.run(query); records=self.kb.search(query,limit=8)
        if state not in ('Any state','All India'): records=[r for r in records if r.get('state','All India') in ('All India',state)]
        if category!='All categories': records=[r for r in records if category.lower() in (r.get('category','')+' '+r.get('target_group','')+' '+r.get('summary','')).lower()]
        answer,notice=self._generate(query,records)
        return {'intent':intent,'schemes':records,'answer':answer or '','notice':notice,'used_ai':bool(answer)}
    def ask(self,query):
        records=self.kb.search(query,limit=5); answer,notice=self._generate(query,records)
        return {'answer':answer or self._fallback(records),'notice':notice,'sources':[{'name':s['name'],'url':s['source_url']} for s in records]}
    @staticmethod
    def _fallback(records):
        if not records: return 'I could not find a close match in the current local library. Try another phrase or upload an official scheme PDF.'
        lines=['Here are the most relevant records in the local scheme library:']
        for s in records: lines.append(f"**{s['name']}**\n\n{s['summary']}\n\n**Benefits:** {s.get('benefits','Check the official source.')}\n\n**Eligibility:** {s.get('eligibility_text',s.get('eligibility','Check the official source.'))}\n\n**Official source:** {s['source_url']}")
        lines.append('Verify current rules, deadlines and required documents with the department. This is not an official eligibility decision.')
        return '\n\n'.join(lines)
    def check_eligibility(self,scheme,profile): return self.eligibility.run(scheme,profile)
    def application_guide(self,scheme): return self.application.run(scheme)
    def ingest_pdf(self,raw,filename):
        try:
            from io import BytesIO
            from pypdf import PdfReader
            text='\n'.join(p.extract_text() or '' for p in PdfReader(BytesIO(raw)).pages).strip()
            if not text: return {'ok':False,'chunks':0,'message':'No selectable text found. This may be a scanned PDF; OCR is not included.'}
            words=text.split(); chunks=[' '.join(words[i:i+220]) for i in range(0,len(words),180)]
            docid=hashlib.sha256((filename+str(len(raw))).encode()).hexdigest()[:12]
            ok,msg=self.kb.add_chunks(docid,chunks,filename)
            return {'ok':ok,'chunks':len(chunks),'message':msg}
        except Exception as exc: return {'ok':False,'chunks':0,'message':f'Could not process PDF: {exc}'}
