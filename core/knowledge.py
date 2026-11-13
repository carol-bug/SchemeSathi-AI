import re
class KnowledgeBase:
    def __init__(self,records,persist_dir):
        self.records=records; self.collection=None; self.backend_label='Keyword fallback'; self.init_notice=''
        try:
            import chromadb
            from chromadb.utils.embedding_functions import SentenceTransformerEmbeddingFunction
            persist_dir.mkdir(parents=True,exist_ok=True)
            ef=SentenceTransformerEmbeddingFunction(model_name='all-MiniLM-L6-v2')
            client=chromadb.PersistentClient(path=str(persist_dir))
            self.collection=client.get_or_create_collection(name='schemesathi_library_v3',embedding_function=ef,metadata={'hnsw:space':'cosine'})
            self.collection.upsert(ids=[r['id'] for r in records],documents=[self.document(r) for r in records],metadatas=[{'scheme_id':r['id'],'name':r['name'],'source_url':r['source_url']} for r in records])
            self.backend_label='ChromaDB + local embeddings'
        except Exception as exc:
            self.init_notice=f'Vector search unavailable; keyword search is active ({type(exc).__name__}).'
    @staticmethod
    def document(r): return ' '.join(str(r.get(k,'')) for k in ('name','summary','benefits','eligibility_text','eligibility','application_text','application','target_group','category','state'))
    def search(self,query,limit=5):
        if self.collection is not None:
            try:
                result=self.collection.query(query_texts=[query],n_results=min(limit,self.collection.count()))
                byid={r['id']:r for r in self.records}; found=[byid[i] for i in result.get('ids',[[]])[0] if i in byid]
                if found: return found
            except Exception as exc: self.init_notice=f'Vector search failed; keyword fallback used ({type(exc).__name__}).'
        terms=[t.lower() for t in re.findall(r'[a-zA-Z0-9]+',query) if len(t)>2]; scored=[]
        for r in self.records:
            body=self.document(r).lower(); score=sum(t in body for t in terms)
            if score: scored.append((score,r))
        return [r for _,r in sorted(scored,key=lambda x:x[0],reverse=True)[:limit]]
    def add_chunks(self,docid,chunks,filename):
        if self.collection is None: return False,'ChromaDB is unavailable. PDF text was extracted but could not be persisted.'
        ids=[f'{docid}_{i}' for i in range(len(chunks))]; metas=[{'scheme_id':f'uploaded_{docid}','name':filename,'source_url':''} for _ in chunks]
        self.collection.upsert(ids=ids,documents=chunks,metadatas=metas); return True,'Document text indexed in persistent ChromaDB.'
