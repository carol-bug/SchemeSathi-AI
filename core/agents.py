class QueryUnderstandingAgent:
    def run(self,query):
        q=query.lower(); states=['karnataka','tamil nadu','andhra pradesh','telangana','kerala','maharashtra']
        groups=['farmer','student','women','woman','unemployed','worker','senior citizen']
        return {'state':next((s.title() for s in states if s in q),None),'user_groups':[g for g in groups if g in q],'intent':[k for k in ['income','education','health','housing','insurance','pension','agriculture','employment'] if k in q]}
class EligibilityAgent:
    def run(self,scheme,profile):
        checks=[]; rules=scheme.get('rules',{})
        for field,required in rules.get('required_true',{}).items():
            if field in profile:
                val=profile[field]; result='Not provided / unsure' if val is None else 'Meets this recorded condition' if val==required else 'Does not meet this recorded condition'
                checks.append({'label':field.replace('_',' ').title(),'result':result})
        for field in rules.get('required_false',{}):
            if field in profile:
                val=profile[field]; result='Not provided / unsure' if val is None else 'Potential exclusion flag' if val else 'No exclusion indicated by your answer'
                checks.append({'label':field.replace('_',' ').title(),'result':result})
        if not checks: checks.append({'label':'Scheme criteria','result':'The local record does not contain enough structured rules for a reliable screening.'})
        positive=sum(('Meets' in c['result'] or 'No exclusion' in c['result']) for c in checks)
        return {'headline':'Some recorded conditions look consistent' if positive else 'More information is needed','summary':'Limited screening against structured fields in the local record. Missing criteria and official verification may change the outcome.','checks':checks}
class ApplicationAgent:
    def run(self,scheme):
        return {'steps':[{'title':'Read the official scheme page','detail':'Open the official source and check the latest notification, eligibility rules and application window.'},{'title':'Prepare required information','detail':scheme.get('documents_text','The exact document checklist is not included in this record. Confirm it on the official portal or with the department.')},{'title':'Use the authorised application route','detail':scheme.get('application_text',scheme.get('application','Follow the process published by the responsible department.'))},{'title':'Keep your acknowledgement','detail':'Save the application or acknowledgement reference and use the official channel for follow-up.'}]}
