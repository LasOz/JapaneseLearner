#Abusing unicode here
#Most of the 'u' kanas are +2 of the 'i' kanas
def U2I(kana : str):
    jump = 3 if "つふぶぷ".find(kana) > -1 else (1 if "ぬる".find(kana) > -1 else 2)    
    return chr(ord(kana) - jump)

def PresentIndicativeForIr(verb : str, formal : bool):
    kana = "し" if (verb[0] != '来') else verb[0]
    return (verb[:-2] + kana + "ます") if formal else verb

def PastIndicativeForIr(verb : str, formal : bool):
    kana = "し" if (verb[0] != '来') else verb[0]
    return verb[:-2] + kana + ("ました" if formal else "た")

def PresentIndicativeForRu(verb : str, formal : bool):
    return verb[:-1] + ("ます" if formal else verb[-1])

def PastIndicativeForRu(verb : str, formal : bool):
    return verb[:-1] + ("ました" if formal else "た")

def PresentIndicativeForU(verb : str, formal : bool):
    return (verb[:-1] + U2I(verb[-1]) + "ます") if formal else verb

def PastIndicativeForU(verb : str, formal : bool):
    return verb[:-1] + ((U2I(verb[-1]) + "ました") if formal else "った")

def TeFormForU(verb : str):
    if ("す" == verb[-1] or "行" == verb[0]):
        return verb[:-1] + "って"
    elif ("く" == verb[-1]):
        return verb[:-1] + "いて"
    elif ("ぐ" == verb[-1]):
        return verb[:-1] + "いで"
    elif ("るつう".find(verb[-1]) > -1):
        return verb[:-1] + "って"
    elif ("ぶむぬ".find(verb[-1]) > -1):
        return verb[:-1] + "んで"
    else:
        raise Exception("Unexpected verb ending for Te form")

def TeFormForRu(verb : str):
    return verb[:-1] + "て"

def TeFormForIr(verb : str):
    kana = "し" if (verb[0] != '来') else verb[0]
    return verb[:-2] + kana + "て"

tenseDictonaryIr = {
    "present":PresentIndicativeForIr,
    "past":PastIndicativeForIr
}

tenseDictonaryRu = {
    "present":PresentIndicativeForRu,
    "past":PastIndicativeForRu
}

tenseDictonaryU = {
    "present":PresentIndicativeForU,
    "past":PastIndicativeForU
}

def Conjugate(verb, tense : str, formal : bool):
    if (verb['verb-type'] == 'u'):
        return tenseDictonaryU[tense](verb['japanese'], formal)
    elif (verb['verb-type'] == 'ru'):
        return tenseDictonaryRu[tense](verb['japanese'], formal)
    else:
        return tenseDictonaryIr[tense](verb['japanese'], formal)

def TeForm(verb):
    if (verb['verb-type'] == 'u'):
        return TeFormForU(verb['japanese'])
    elif (verb['verb-type'] == 'ru'):
        return TeFormForRu(verb['japanese'])
    else:
        return TeFormForIr(verb['japanese'])