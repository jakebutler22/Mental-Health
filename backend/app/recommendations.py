"""Contextual mock and app-enforced current-choice boundaries; not emotion assessment."""
import re

REASONS = {
    'breathing':'A steady rhythm may suit the keyed-up feeling you described.',
    'grounding':'Noticing your surroundings may suit the scattered thoughts you described.'}


def current_constraints(text):
    """Current explicit choices win. Negation scopes to a skill, never the whole sentence."""
    low=text.lower().replace('’', "'")
    # Latest correction scopes feeling context; skill choices retain their own event order.
    current=re.split(r'\b(?:actually|correction|instead|i meant)\b',low)[-1]
    declined=bool(re.search(r"\b(?:neither|no thanks|don't want (?:either|an exercise)|do not want (?:either|an exercise))\b",current) or re.search(r"(?:^|[.!?]\s*)(?:please\s+)?stop(?:[.!?]|$|\s+(?:please|the (?:chat|exercise)|this|now)\b)|\b(?:want to|let.s) stop\b",current))
    forbidden=set()
    for skill,aliases in [('breathing',r'(?:breathing|breathe|breathwork)'),('grounding',r'(?:grounding|ground)')]:
        negative=list(re.finditer(r"\b(?:no|not|without|avoid|don't want|do not want|don't recommend|do not recommend)\s+(?:(?:to\s+)?do\s+)?(?:any\s+)?"+aliases+r'\b',low))
        positive=list(re.finditer(r'\b(?:prefer|want|choose|try|use|would like|i\x27d like|rather do)\s+(?:(?:to\s+)?do\s+)?'+aliases+r'\b',low))
        positive=[m for m in positive if not any(n.start()<=m.start()<n.end() for n in negative)]
        if negative and (not positive or negative[-1].start()>positive[-1].start()):
            forbidden.add(skill)
    preferred=[]
    for skill in ('breathing','grounding'):
        for match in re.finditer(r'\b(?:prefer|want|choose|try|use|rather do|would like|i\x27d like)\s+(?:(?:to\s+)?do\s+)?'+skill+r'\b',low):
            if skill not in forbidden: preferred.append((match.start(),skill))
    # A bare explicit skill is also a deliberate preference.
    if current.strip(' .!?') in ('breathing','grounding'):
        preferred.append((0,current.strip(' .!?')))
    preference=sorted(preferred)[-1][1] if preferred else None
    if len(forbidden)==2: declined=True
    return current,forbidden,preference,declined


def apply_choice_boundaries(value,text,clarification_used=False):
    value=dict(value)
    current,forbidden,preference,declined=current_constraints(text)
    if declined:
        return {'reflection':'Neither is okay. You can leave things here or choose something later.','recommended_skill':None,'reason':'Your choice stays yours.','clarification':None,'action':'decline'}
    if preference:
        value.update(recommended_skill=preference,reason=f'You asked for {preference}; that choice takes priority.',clarification=None,action='offer')
    elif value['recommended_skill'] in forbidden:
        alternative=next((s for s in ('breathing','grounding') if s not in forbidden),None)
        value.update(recommended_skill=alternative,reason='You ruled out the other exercise, so this is an optional alternative.',clarification=None,action='offer' if alternative else 'decline')
    if clarification_used and value['action']=='clarify':
        value.update(reflection='You can leave it mixed or unclear. Both exercises are available without explaining more.',recommended_skill=None,reason='No answer is required.',clarification=None,action='offer')
    return value


def mock_recommendation(text,history=(),clarification_used=False):
    current,forbidden,preference,declined=current_constraints(text)
    # Composite current feeling/context evidence; old user context only for short follow-ups.
    prior=' '.join(str(m.get('text','')) for m in list(history)[-6:] if m.get('role')=='user')
    feeling=current
    if len(current.split())<4 and not preference and not declined:
        feeling=prior.lower()+' '+current
    tense=bool(re.search(r'\b(?:wound up|keyed up|tense|jittery|racing heart|tight shoulders|on edge)\b',feeling))
    scattered=bool(re.search(r'\b(?:scattered|repetitive thoughts|thoughts? (?:keep |are )?looping|stuck in (?:my )?(?:thoughts|a loop)|keep replaying|can.t focus|distracted)\b',feeling))
    # Negated feelings don't contribute; correction segment has already discarded old feelings.
    if re.search(r"\b(?:not|don't feel|do not feel)\s+(?:really\s+)?(?:tense|wound up|keyed up|jittery)\b",current): tense=False
    if re.search(r"\b(?:not|don't feel|do not feel)\s+(?:really\s+)?(?:scattered|distracted)\b",current): scattered=False
    context='this campus situation'
    if re.search(r'\b(?:exam|quiz|test)\b',current): context='the upcoming exam'
    elif re.search(r'\b(?:roommate|dorm)\b',current): context='the roommate situation'
    elif re.search(r'\b(?:deadline|assignment|homework)\b',current): context='the assignments on your plate'
    elif re.search(r'\b(?:friend|club|social)\b',current): context='the social situation'
    if preference:
        skill=preference
    elif tense != scattered:
        skill='breathing' if tense else 'grounding'
    else: skill=None
    if skill:
        feeling_name='keyed up' if tense else 'pulled into several thoughts'
        reflection=f'With {context}, you describe feeling {feeling_name}.' if tense or scattered else f'You prefer {skill} for {context}.'
        value={'reflection':reflection,'recommended_skill':skill,'reason':REASONS[skill],'clarification':None,'action':'offer'}
    else:
        value={'reflection':f'There may be a few things mixed together around {context}.','recommended_skill':None,'reason':'You can choose either exercise without explaining more.','clarification':'Would a steady rhythm or noticing your surroundings suit this moment?' if not clarification_used else None,'action':'clarify' if not clarification_used else 'offer'}
    return apply_choice_boundaries(value,text,clarification_used)
