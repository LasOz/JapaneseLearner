"""Utility class for converting dictonary plain verbs to all other forms"""

def u_2_i(kana: str):
    """Takes a 'u' sounding phonetic and converts to equiv 'i' sounding
    Does not check if input is actually hiragana"""
    jump = 3 if "つふぶぷ".find(kana) > -1 else (1 if "ぬる".find(kana) > -1 else 2)
    return chr(ord(kana) - jump)

def present_indicative_for_ir(verb: str, formal: bool):
    """Present Indicitive term of input verb, formal and informal"""
    kana = "し" if (verb[0] != '来') else verb[0]
    return (verb[:-2] + kana + "ます") if formal else verb

def past_indicative_for_ir(verb: str, formal: bool):
    """Past Indicitive term of input verb, formal and informal"""
    kana = "し" if (verb[0] != '来') else verb[0]
    return verb[:-2] + kana + ("ました" if formal else "た")

def present_indicative_for_ru(verb: str, formal: bool):
    """Present Indicitive term of input verb, formal and informal"""
    return verb[:-1] + ("ます" if formal else verb[-1])

def past_indicative_for_ru(verb: str, formal: bool):
    """Past Indicitive term of input verb, formal and informal"""
    return verb[:-1] + ("ました" if formal else "た")

def present_indicative_for_u(verb: str, formal: bool):
    """Present Indicitive term of input verb, formal and informal"""
    return (verb[:-1] + u_2_i(verb[-1]) + "ます") if formal else verb

def past_indicative_for_u(verb: str, formal: bool):
    """Past Indicitive term of input verb, formal and informal"""
    return verb[:-1] + ((u_2_i(verb[-1]) + "ました") if formal else "った")

def te_form_for_u(verb: str):
    """Returns te form for given dictonary verb, accounts for exceptions"""
    if (verb[-1] == "す" or verb[0] == "行"):
        return verb[:-1] + "って"
    if verb[-1] == "く":
        return verb[:-1] + "いて"
    if verb[-1] == "ぐ":
        return verb[:-1] + "いで"
    if "るつう".find(verb[-1]) > -1:
        return verb[:-1] + "って"
    if "ぶむぬ".find(verb[-1]) > -1:
        return verb[:-1] + "んで"
    raise Exception("Unexpected verb ending for Te form")

def te_form_for_ru(verb: str):
    """Returns te form for given dictonary verb"""
    return verb[:-1] + "て"

def te_fomr_for_ir(verb: str):
    """Returns te form for given dictonary verb"""
    kana = "し" if (verb[0] != '来') else verb[0]
    return verb[:-2] + kana + "て"

TENSE_DICTIONARY_IR = {
    "present":present_indicative_for_ir,
    "past":past_indicative_for_ir
}

TENSE_DICTIONARY_RU = {
    "present":present_indicative_for_ru,
    "past":past_indicative_for_ru
}

TENSE_DICTIONARY_U = {
    "present":present_indicative_for_u,
    "past":past_indicative_for_u
}

def conjugate(verb, tense: str, formal: bool):
    """Conjugate the verb (verb expected to be in certain format)"""
    if verb['verb-type'] == 'u':
        return TENSE_DICTIONARY_U[tense](verb['japanese'], formal)
    if verb['verb-type'] == 'ru':
        return TENSE_DICTIONARY_RU[tense](verb['japanese'], formal)
    return TENSE_DICTIONARY_IR[tense](verb['japanese'], formal)

def te_form(verb):
    """Get the te form of the verb (verb expected to be in certain format)"""
    if verb['verb-type'] == 'u':
        return te_form_for_u(verb['japanese'])
    if verb['verb-type'] == 'ru':
        return te_form_for_ru(verb['japanese'])
    return te_fomr_for_ir(verb['japanese'])
