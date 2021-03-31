
### run 3 130 features
def word2features(word, index, tokenizedtext):
    strippedascii = str(unicodedata.normalize('NFD', word).encode('ascii', 'ignore').decode("utf-8"))
    strippedasciilower = str(unicodedata.normalize('NFD', word).encode('ascii', 'ignore').decode("utf-8"))
    strippedpunc = re.sub('[^A-Za-z0-9\']+', '', strippedascii.lower())

    dictionary = corpusdictfromtrainingnofreq.get(strippedpunc, dict({'None':1}))
    

    features = {
        'tokenizedtext': tokenizedtext,
        'position': index,
        'word.lower()': word.lower(),
        'word.stripascii()': strippedasciilower,
        'word.strippunc()': strippedpunc,
        'word.istitle()': (re.sub('[^A-Za-z0-9\']+', '', word)).istitle(),
        'word.isupper()': (re.sub('[^A-Za-z0-9\']+', '', word)).isupper(),
        'word.isdigit()': (re.sub('[^A-Za-z0-9\']+', '', word)).isdigit(),
        'word[-3:]': strippedpunc[-3:],
        'word[-2:]': strippedpunc[-2:],
        'word[:2]': strippedpunc[:2],
        'word[:3]': strippedpunc[:3],
        'word.POS1freq()': nlargest(100, dictionary, key=dictionary.get)[0] if len(dictionary) > 0 else 'None',
        'word.POS2freq()': nlargest(100, dictionary, key=dictionary.get)[1] if len(dictionary) > 1 else 'None',
        'word.POS3freq()': nlargest(100, dictionary, key=dictionary.get)[2] if len(dictionary) > 2 else 'None',
        'word.POS4freq()': nlargest(100, dictionary, key=dictionary.get)[3] if len(dictionary) > 3 else 'None',
        'word.POS5freq()': nlargest(100, dictionary, key=dictionary.get)[4] if len(dictionary) > 4 else 'None',
        'word.POS6freq()': nlargest(100, dictionary, key=dictionary.get)[5] if len(dictionary) > 5 else 'None',
        'word.POSmin()':max(dictionary.items(), key=operator.itemgetter(1))[0],
        'word.POSfirst()': list(dictionary.items())[0][0],
        'word.POSlast()': list(dictionary.items())[-1][0],
        'sent.sentimentpos()': float(sia.polarity_scores(" ".join(tokenizedtext))['pos']),
        'sent.sentimentneg()': float(sia.polarity_scores(" ".join(tokenizedtext))['neg']),
        'sent.sentimentneu()': float(sia.polarity_scores(" ".join(tokenizedtext))['neu']),

        'word.in.sickness()' : strippedpunc in filtered_sicknesses,
        'word.in.symptoms()' : strippedpunc in filtered_symptoms,
        'word.sentimentpos()': float(sia.polarity_scores(strippedpunc)['pos']),
        'word.sentimentneg()': float(sia.polarity_scores(strippedpunc)['neg']),
        'word.sentimentneu()': float(sia.polarity_scores(strippedpunc)['neu']),

        'word.isdepress()': 'yes' if strippedpunc in ['depression', 'depressed'] else 'no',
        'word.isanxious()': 'yes' if strippedpunc in ['anxiety', 'anxious', 'worry', 'worried'] else 'no',
        'word.issuicide()': 'yes' if strippedpunc in ['suicide', 'suicidal', 'kill'] else 'no',
        'word.isinsomnia()': 'yes' if strippedpunc in ['insomnia', 'insomniac', 'sleep'] else 'no',
        'word.isheadtired()': 'yes' if strippedpunc in ['tired', 'fatigue', 'migraine'] else 'no',
        'word.isdelusion()': 'yes' if strippedpunc in ['delusional', 'delusion'] else 'no',
        'word.isanger()': 'yes' if strippedpunc in ['anger', 'angry', 'fury', 'furious', 'mad'] else 'no',
        'word.isbulimia()': 'yes' if strippedpunc in ['bulimia', 'bulimic'] else 'no',
        'word.isafraid()': 'yes' if strippedpunc in ['fear', 'afraid'] else 'no',
        'word.isdisorder()': 'yes' if strippedpunc in ['disorder'] else 'no',
        'word.isbipolar()': 'yes' if strippedpunc in ['bipolar'] else 'no'




    }

    if index > 0:
        word = tokenizedtext[index-1]
        strippedascii = str(unicodedata.normalize('NFD', word).encode('ascii', 'ignore').decode("utf-8"))
        strippedasciilower = str(unicodedata.normalize('NFD', word).encode('ascii', 'ignore').decode("utf-8"))
        strippedpunc = re.sub('[^A-Za-z0-9\']+', '', strippedascii.lower())
        dictionary = corpusdictfromtrainingnofreq.get(strippedpunc, dict({'None':1}))


        features.update({
            '-1:word.lower()': word.lower(),
            '-1:word.stripascii()': strippedasciilower,
            '-1:word.strippunc()': strippedpunc,
            '-1word.istitle()': (re.sub('[^A-Za-z0-9\']+', '', word)).istitle(),
            '-1word.isupper()': (re.sub('[^A-Za-z0-9\']+', '', word)).isupper(),
            '-1word.isdigit()': (re.sub('[^A-Za-z0-9\']+', '', word)).isdigit(),
            '-1word[-3:]': strippedpunc[-3:],
            '-1word[-2:]': strippedpunc[-2:],
            '-1word[:2]': strippedpunc[:2],
            '-1word[:3]': strippedpunc[:3],
            '-1word.POS1freq()': nlargest(100, dictionary, key=dictionary.get)[0] if len(dictionary) > 0 else 'None',
            '-1word.POS2freq()': nlargest(100, dictionary, key=dictionary.get)[1] if len(dictionary) > 1 else 'None',
            '-1word.POS3freq()': nlargest(100, dictionary, key=dictionary.get)[2] if len(dictionary) > 2 else 'None',
            '-1word.POS4freq()': nlargest(100, dictionary, key=dictionary.get)[3] if len(dictionary) > 3 else 'None',
            '-1word.POS5freq()': nlargest(100, dictionary, key=dictionary.get)[4] if len(dictionary) > 4 else 'None',
            '-1word.POS6freq()': nlargest(100, dictionary, key=dictionary.get)[5] if len(dictionary) > 5 else 'None',
            '-1word.POSmin()':max(dictionary.items(), key=operator.itemgetter(1))[0],
            '-1word.POSfirst()': list(dictionary.items())[0][0],
            '-1word.POSlast()': list(dictionary.items())[-1][0],
            '-1word.in.sickness()' : strippedpunc in filtered_sicknesses,
            '-1word.in.symptoms()' : strippedpunc in filtered_symptoms,
            '-1word.sentimentpos()': float(sia.polarity_scores(strippedpunc)['pos']),
            '-1word.sentimentneg()': float(sia.polarity_scores(strippedpunc)['neg']),
            '-1word.sentimentneu()': float(sia.polarity_scores(strippedpunc)['neu'])
        })

    if index > 1:
        word = tokenizedtext[index-2]
        strippedascii = str(unicodedata.normalize('NFD', word).encode('ascii', 'ignore').decode("utf-8"))
        strippedasciilower = str(unicodedata.normalize('NFD', word).encode('ascii', 'ignore').decode("utf-8"))
        strippedpunc = re.sub('[^A-Za-z0-9\']+', '', strippedascii.lower())
        dictionary = corpusdictfromtrainingnofreq.get(strippedpunc, dict({'None':1}))


        features.update({
            '-2:word.lower()': word.lower(),
            '-2:word.stripascii()': strippedasciilower,
            '-2:word.strippunc()': strippedpunc,
            '-2word.istitle()': (re.sub('[^A-Za-z0-9\']+', '', word)).istitle(),
            '-2word.isupper()': (re.sub('[^A-Za-z0-9\']+', '', word)).isupper(),
            '-2word.isdigit()': (re.sub('[^A-Za-z0-9\']+', '', word)).isdigit(),
            '-2word[-3:]': strippedpunc[-3:],
            '-2word[-2:]': strippedpunc[-2:],
            '-2word[:2]': strippedpunc[:2],
            '-2word[:3]': strippedpunc[:3],
            '-2word.POS1freq()': nlargest(100, dictionary, key=dictionary.get)[0] if len(dictionary) > 0 else 'None',
            '-2word.POS2freq()': nlargest(100, dictionary, key=dictionary.get)[1] if len(dictionary) > 1 else 'None',
            '-2word.POS3freq()': nlargest(100, dictionary, key=dictionary.get)[2] if len(dictionary) > 2 else 'None',
            '-2word.POS4freq()': nlargest(100, dictionary, key=dictionary.get)[3] if len(dictionary) > 3 else 'None',
            '-2word.POS5freq()': nlargest(100, dictionary, key=dictionary.get)[4] if len(dictionary) > 4 else 'None',
            '-2word.POS6freq()': nlargest(100, dictionary, key=dictionary.get)[5] if len(dictionary) > 5 else 'None',
            '-2word.POSmin()':max(dictionary.items(), key=operator.itemgetter(1))[0],
            '-2word.POSfirst()': list(dictionary.items())[0][0],
            '-2word.POSlast()': list(dictionary.items())[-1][0],
            '-2word.in.sickness()' : strippedpunc in filtered_sicknesses,
            '-2word.in.symptoms()' : strippedpunc in filtered_symptoms,
            '-2word.sentimentpos()': float(sia.polarity_scores(strippedpunc)['pos']),
            '-2word.sentimentneg()': float(sia.polarity_scores(strippedpunc)['neg']),
            '-2word.sentimentneu()': float(sia.polarity_scores(strippedpunc)['neu'])
        })
    
    if index < len(tokenizedtext)-1:
        word = tokenizedtext[index+1]
        strippedascii = str(unicodedata.normalize('NFD', word).encode('ascii', 'ignore').decode("utf-8"))
        strippedasciilower = str(unicodedata.normalize('NFD', word).encode('ascii', 'ignore').decode("utf-8"))
        strippedpunc = re.sub('[^A-Za-z0-9\']+', '', strippedascii.lower())
        dictionary = corpusdictfromtrainingnofreq.get(strippedpunc, dict({'None':1}))


        features.update({
            '+1:word.lower()': word.lower(),
            '+1:word.stripascii()': strippedasciilower,
            '+1:word.strippunc()': strippedpunc,
            '+1word.istitle()': (re.sub('[^A-Za-z0-9\']+', '', word)).istitle(),
            '+1word.isupper()': (re.sub('[^A-Za-z0-9\']+', '', word)).isupper(),
            '+1word.isdigit()': (re.sub('[^A-Za-z0-9\']+', '', word)).isdigit(),
            '+1word[-3:]': strippedpunc[-3:],
            '+1word[-2:]': strippedpunc[-2:],
            '+1word[:2]': strippedpunc[:2],
            '+1word[:3]': strippedpunc[:3],
            '+1word.POS1freq()': nlargest(100, dictionary, key=dictionary.get)[0] if len(dictionary) > 0 else 'None',
            '+1word.POS2freq()': nlargest(100, dictionary, key=dictionary.get)[1] if len(dictionary) > 1 else 'None',
            '+1word.POS3freq()': nlargest(100, dictionary, key=dictionary.get)[2] if len(dictionary) > 2 else 'None',
            '+1word.POS4freq()': nlargest(100, dictionary, key=dictionary.get)[3] if len(dictionary) > 3 else 'None',
            '+1word.POS5freq()': nlargest(100, dictionary, key=dictionary.get)[4] if len(dictionary) > 4 else 'None',
            '+1word.POS6freq()': nlargest(100, dictionary, key=dictionary.get)[5] if len(dictionary) > 5 else 'None',
            '+1word.POSmin()':max(dictionary.items(), key=operator.itemgetter(1))[0],
            '+1word.POSfirst()': list(dictionary.items())[0][0],
            '+1word.POSlast()': list(dictionary.items())[-1][0],
            '+1word.in.sickness()' : strippedpunc in filtered_sicknesses,
            '+1word.in.symptoms()' : strippedpunc in filtered_symptoms,
            '+1word.sentimentpos()': float(sia.polarity_scores(strippedpunc)['pos']),
            '+1word.sentimentneg()': float(sia.polarity_scores(strippedpunc)['neg']),
            '+1word.sentimentneu()': float(sia.polarity_scores(strippedpunc)['neu'])
        })
    if index < len(tokenizedtext)-2:
        
        word = tokenizedtext[index+2]
        strippedascii = str(unicodedata.normalize('NFD', word).encode('ascii', 'ignore').decode("utf-8"))
        strippedasciilower = str(unicodedata.normalize('NFD', word).encode('ascii', 'ignore').decode("utf-8"))
        strippedpunc = re.sub('[^A-Za-z0-9\']+', '', strippedascii.lower())
        dictionary = corpusdictfromtrainingnofreq.get(strippedpunc, dict({'None':1}))


        features.update({
            '+2:word.lower()': word.lower(),
            '+2:word.stripascii()': strippedasciilower,
            '+2:word.strippunc()': strippedpunc,
            '+2word.istitle()': (re.sub('[^A-Za-z0-9\']+', '', word)).istitle(),
            '+2word.isupper()': (re.sub('[^A-Za-z0-9\']+', '', word)).isupper(),
            '+2word.isdigit()': (re.sub('[^A-Za-z0-9\']+', '', word)).isdigit(),
            '+2word[-3:]': strippedpunc[-3:],
            '+2word[-2:]': strippedpunc[-2:],
            '+2word[:2]': strippedpunc[:2],
            '+2word[:3]': strippedpunc[:3],
            '+2word.POS1freq()': nlargest(100, dictionary, key=dictionary.get)[0] if len(dictionary) > 0 else 'None',
            '+2word.POS2freq()': nlargest(100, dictionary, key=dictionary.get)[1] if len(dictionary) > 1 else 'None',
            '+2word.POS3freq()': nlargest(100, dictionary, key=dictionary.get)[2] if len(dictionary) > 2 else 'None',
            '+2word.POS4freq()': nlargest(100, dictionary, key=dictionary.get)[3] if len(dictionary) > 3 else 'None',
            '+2word.POS5freq()': nlargest(100, dictionary, key=dictionary.get)[4] if len(dictionary) > 4 else 'None',
            '+2word.POS6freq()': nlargest(100, dictionary, key=dictionary.get)[5] if len(dictionary) > 5 else 'None',
            '+2word.POSmin()':max(dictionary.items(), key=operator.itemgetter(1))[0],
            '+2word.POSfirst()': list(dictionary.items())[0][0],
            '+2word.POSlast()': list(dictionary.items())[-1][0],
            '+2word.in.sickness()' : strippedpunc in filtered_sicknesses,
            '+2word.in.symptoms()' : strippedpunc in filtered_symptoms,
            '+2word.sentimentpos()': float(sia.polarity_scores(strippedpunc)['pos']),
            '+2word.sentimentneg()': float(sia.polarity_scores(strippedpunc)['neg']),
            '+2word.sentimentneu()': float(sia.polarity_scores(strippedpunc)['neu'])
        })

    return features






##Maximal model 140 features

def word2features(word, index, tokenizedtext):
    strippedascii = str(unicodedata.normalize('NFD', word).encode('ascii', 'ignore').decode("utf-8"))
    strippedasciilower = str(unicodedata.normalize('NFD', word).encode('ascii', 'ignore').decode("utf-8"))
    strippedpunc = re.sub('[^A-Za-z0-9\']+', '', strippedascii.lower())

    dictionary = corpusdictfromtrainingnofreq.get(strippedpunc, dict({'None':1}))
    

    features = {
        'tokenizedtext': tokenizedtext,
        'position': index,
        'word.lower()': word.lower(),
        'word.stripascii()': strippedasciilower,
        'word.strippunc()': strippedpunc,
        'word.istitle()': (re.sub('[^A-Za-z0-9\']+', '', word)).istitle(),
        'word.isupper()': (re.sub('[^A-Za-z0-9\']+', '', word)).isupper(),
        'word.isdigit()': (re.sub('[^A-Za-z0-9\']+', '', word)).isdigit(),
        'word[-4:]': strippedpunc[-4:],
        'word[-3:]': strippedpunc[-3:],
        'word[-2:]': strippedpunc[-2:],
        'word[:2]': strippedpunc[:2],
        'word[:3]': strippedpunc[:3],
        'word[:4]': strippedpunc[:4],
        'word.POS1freq()': nlargest(100, dictionary, key=dictionary.get)[0] if len(dictionary) > 0 else 'None',
        'word.POS2freq()': nlargest(100, dictionary, key=dictionary.get)[1] if len(dictionary) > 1 else 'None',
        'word.POS3freq()': nlargest(100, dictionary, key=dictionary.get)[2] if len(dictionary) > 2 else 'None',
        'word.POS4freq()': nlargest(100, dictionary, key=dictionary.get)[3] if len(dictionary) > 3 else 'None',
        'word.POS5freq()': nlargest(100, dictionary, key=dictionary.get)[4] if len(dictionary) > 4 else 'None',
        'word.POS6freq()': nlargest(100, dictionary, key=dictionary.get)[5] if len(dictionary) > 5 else 'None',
        'word.POSmin()':max(dictionary.items(), key=operator.itemgetter(1))[0],
        'word.POSfirst()': list(dictionary.items())[0][0],
        'word.POSlast()': list(dictionary.items())[-1][0],
        'sent.sentimentpos()': float(sia.polarity_scores(" ".join(tokenizedtext))['pos']),
        'sent.sentimentneg()': float(sia.polarity_scores(" ".join(tokenizedtext))['neg']),
        'sent.sentimentneu()': float(sia.polarity_scores(" ".join(tokenizedtext))['neu']),

        'word.in.sickness()' : strippedpunc in filtered_sicknesses,
        'word.in.symptoms()' : strippedpunc in filtered_symptoms,
        'word.sentimentpos()': float(sia.polarity_scores(strippedpunc)['pos']),
        'word.sentimentneg()': float(sia.polarity_scores(strippedpunc)['neg']),
        'word.sentimentneu()': float(sia.polarity_scores(strippedpunc)['neu']),

        'word.isdepress()': 'yes' if strippedpunc in ['depression', 'depressed'] else 'no',
        'word.isanxious()': 'yes' if strippedpunc in ['anxiety', 'anxious', 'worry', 'worried'] else 'no',
        'word.issuicide()': 'yes' if strippedpunc in ['suicide', 'suicidal', 'kill'] else 'no',
        'word.isinsomnia()': 'yes' if strippedpunc in ['insomnia', 'insomniac', 'sleep'] else 'no',
        'word.isheadtired()': 'yes' if strippedpunc in ['tired', 'fatigue', 'migraine'] else 'no',
        'word.isdelusion()': 'yes' if strippedpunc in ['delusional', 'delusion'] else 'no',
        'word.isanger()': 'yes' if strippedpunc in ['anger', 'angry', 'fury', 'furious', 'mad'] else 'no',
        'word.isbulimia()': 'yes' if strippedpunc in ['bulimia', 'bulimic'] else 'no',
        'word.isafraid()': 'yes' if strippedpunc in ['fear', 'afraid'] else 'no',
        'word.isdisorder()': 'yes' if strippedpunc in ['disorder'] else 'no',
        'word.isbipolar()': 'yes' if strippedpunc in ['bipolar'] else 'no'




    }

    if index > 0:
        word = tokenizedtext[index-1]
        strippedascii = str(unicodedata.normalize('NFD', word).encode('ascii', 'ignore').decode("utf-8"))
        strippedasciilower = str(unicodedata.normalize('NFD', word).encode('ascii', 'ignore').decode("utf-8"))
        strippedpunc = re.sub('[^A-Za-z0-9\']+', '', strippedascii.lower())
        dictionary = corpusdictfromtrainingnofreq.get(strippedpunc, dict({'None':1}))


        features.update({
            '-1:word.lower()': word.lower(),
            '-1:word.stripascii()': strippedasciilower,
            '-1:word.strippunc()': strippedpunc,
            '-1word.istitle()': (re.sub('[^A-Za-z0-9\']+', '', word)).istitle(),
            '-1word.isupper()': (re.sub('[^A-Za-z0-9\']+', '', word)).isupper(),
            '-1word.isdigit()': (re.sub('[^A-Za-z0-9\']+', '', word)).isdigit(),
            '-1word[-4:]': strippedpunc[-4:],
            '-1word[-3:]': strippedpunc[-3:],
            '-1word[-2:]': strippedpunc[-2:],
            '-1word[:2]': strippedpunc[:2],
            '-1word[:3]': strippedpunc[:3],
            '-1word[:4]': strippedpunc[:4],
            '-1word.POS1freq()': nlargest(100, dictionary, key=dictionary.get)[0] if len(dictionary) > 0 else 'None',
            '-1word.POS2freq()': nlargest(100, dictionary, key=dictionary.get)[1] if len(dictionary) > 1 else 'None',
            '-1word.POS3freq()': nlargest(100, dictionary, key=dictionary.get)[2] if len(dictionary) > 2 else 'None',
            '-1word.POS4freq()': nlargest(100, dictionary, key=dictionary.get)[3] if len(dictionary) > 3 else 'None',
            '-1word.POS5freq()': nlargest(100, dictionary, key=dictionary.get)[4] if len(dictionary) > 4 else 'None',
            '-1word.POS6freq()': nlargest(100, dictionary, key=dictionary.get)[5] if len(dictionary) > 5 else 'None',
            '-1word.POSmin()':max(dictionary.items(), key=operator.itemgetter(1))[0],
            '-1word.POSfirst()': list(dictionary.items())[0][0],
            '-1word.POSlast()': list(dictionary.items())[-1][0],
            '-1word.in.sickness()' : strippedpunc in filtered_sicknesses,
            '-1word.in.symptoms()' : strippedpunc in filtered_symptoms,
            '-1word.sentimentpos()': float(sia.polarity_scores(strippedpunc)['pos']),
            '-1word.sentimentneg()': float(sia.polarity_scores(strippedpunc)['neg']),
            '-1word.sentimentneu()': float(sia.polarity_scores(strippedpunc)['neu'])
        })

    if index > 1:
        word = tokenizedtext[index-2]
        strippedascii = str(unicodedata.normalize('NFD', word).encode('ascii', 'ignore').decode("utf-8"))
        strippedasciilower = str(unicodedata.normalize('NFD', word).encode('ascii', 'ignore').decode("utf-8"))
        strippedpunc = re.sub('[^A-Za-z0-9\']+', '', strippedascii.lower())
        dictionary = corpusdictfromtrainingnofreq.get(strippedpunc, dict({'None':1}))


        features.update({
            '-2:word.lower()': word.lower(),
            '-2:word.stripascii()': strippedasciilower,
            '-2:word.strippunc()': strippedpunc,
            '-2word.istitle()': (re.sub('[^A-Za-z0-9\']+', '', word)).istitle(),
            '-2word.isupper()': (re.sub('[^A-Za-z0-9\']+', '', word)).isupper(),
            '-2word.isdigit()': (re.sub('[^A-Za-z0-9\']+', '', word)).isdigit(),
            '-2word[-4:]': strippedpunc[-4:],
            '-2word[-3:]': strippedpunc[-3:],
            '-2word[-2:]': strippedpunc[-2:],
            '-2word[:2]': strippedpunc[:2],
            '-2word[:3]': strippedpunc[:3],
            '-2word[:4]': strippedpunc[:4],
            '-2word.POS1freq()': nlargest(100, dictionary, key=dictionary.get)[0] if len(dictionary) > 0 else 'None',
            '-2word.POS2freq()': nlargest(100, dictionary, key=dictionary.get)[1] if len(dictionary) > 1 else 'None',
            '-2word.POS3freq()': nlargest(100, dictionary, key=dictionary.get)[2] if len(dictionary) > 2 else 'None',
            '-2word.POS4freq()': nlargest(100, dictionary, key=dictionary.get)[3] if len(dictionary) > 3 else 'None',
            '-2word.POS5freq()': nlargest(100, dictionary, key=dictionary.get)[4] if len(dictionary) > 4 else 'None',
            '-2word.POS6freq()': nlargest(100, dictionary, key=dictionary.get)[5] if len(dictionary) > 5 else 'None',
            '-2word.POSmin()':max(dictionary.items(), key=operator.itemgetter(1))[0],
            '-2word.POSfirst()': list(dictionary.items())[0][0],
            '-2word.POSlast()': list(dictionary.items())[-1][0],
            '-2word.in.sickness()' : strippedpunc in filtered_sicknesses,
            '-2word.in.symptoms()' : strippedpunc in filtered_symptoms,
            '-2word.sentimentpos()': float(sia.polarity_scores(strippedpunc)['pos']),
            '-2word.sentimentneg()': float(sia.polarity_scores(strippedpunc)['neg']),
            '-2word.sentimentneu()': float(sia.polarity_scores(strippedpunc)['neu'])
        })
    
    if index < len(tokenizedtext)-1:
        word = tokenizedtext[index+1]
        strippedascii = str(unicodedata.normalize('NFD', word).encode('ascii', 'ignore').decode("utf-8"))
        strippedasciilower = str(unicodedata.normalize('NFD', word).encode('ascii', 'ignore').decode("utf-8"))
        strippedpunc = re.sub('[^A-Za-z0-9\']+', '', strippedascii.lower())
        dictionary = corpusdictfromtrainingnofreq.get(strippedpunc, dict({'None':1}))


        features.update({
            '+1:word.lower()': word.lower(),
            '+1:word.stripascii()': strippedasciilower,
            '+1:word.strippunc()': strippedpunc,
            '+1word.istitle()': (re.sub('[^A-Za-z0-9\']+', '', word)).istitle(),
            '+1word.isupper()': (re.sub('[^A-Za-z0-9\']+', '', word)).isupper(),
            '+1word.isdigit()': (re.sub('[^A-Za-z0-9\']+', '', word)).isdigit(),
            '+1word[-4:]': strippedpunc[-4:],
            '+1word[-3:]': strippedpunc[-3:],
            '+1word[-2:]': strippedpunc[-2:],
            '+1word[:2]': strippedpunc[:2],
            '+1word[:3]': strippedpunc[:3],
            '+1word[:4]': strippedpunc[:4],
            '+1word.POS1freq()': nlargest(100, dictionary, key=dictionary.get)[0] if len(dictionary) > 0 else 'None',
            '+1word.POS2freq()': nlargest(100, dictionary, key=dictionary.get)[1] if len(dictionary) > 1 else 'None',
            '+1word.POS3freq()': nlargest(100, dictionary, key=dictionary.get)[2] if len(dictionary) > 2 else 'None',
            '+1word.POS4freq()': nlargest(100, dictionary, key=dictionary.get)[3] if len(dictionary) > 3 else 'None',
            '+1word.POS5freq()': nlargest(100, dictionary, key=dictionary.get)[4] if len(dictionary) > 4 else 'None',
            '+1word.POS6freq()': nlargest(100, dictionary, key=dictionary.get)[5] if len(dictionary) > 5 else 'None',
            '+1word.POSmin()':max(dictionary.items(), key=operator.itemgetter(1))[0],
            '+1word.POSfirst()': list(dictionary.items())[0][0],
            '+1word.POSlast()': list(dictionary.items())[-1][0],
            '+1word.in.sickness()' : strippedpunc in filtered_sicknesses,
            '+1word.in.symptoms()' : strippedpunc in filtered_symptoms,
            '+1word.sentimentpos()': float(sia.polarity_scores(strippedpunc)['pos']),
            '+1word.sentimentneg()': float(sia.polarity_scores(strippedpunc)['neg']),
            '+1word.sentimentneu()': float(sia.polarity_scores(strippedpunc)['neu'])
        })
    if index < len(tokenizedtext)-2:
        
        word = tokenizedtext[index+2]
        strippedascii = str(unicodedata.normalize('NFD', word).encode('ascii', 'ignore').decode("utf-8"))
        strippedasciilower = str(unicodedata.normalize('NFD', word).encode('ascii', 'ignore').decode("utf-8"))
        strippedpunc = re.sub('[^A-Za-z0-9\']+', '', strippedascii.lower())
        dictionary = corpusdictfromtrainingnofreq.get(strippedpunc, dict({'None':1}))


        features.update({
            '+2:word.lower()': word.lower(),
            '+2:word.stripascii()': strippedasciilower,
            '+2:word.strippunc()': strippedpunc,
            '+2word.istitle()': (re.sub('[^A-Za-z0-9\']+', '', word)).istitle(),
            '+2word.isupper()': (re.sub('[^A-Za-z0-9\']+', '', word)).isupper(),
            '+2word.isdigit()': (re.sub('[^A-Za-z0-9\']+', '', word)).isdigit(),
            '+2word[-4:]': strippedpunc[-4:],
            '+2word[-3:]': strippedpunc[-3:],
            '+2word[-2:]': strippedpunc[-2:],
            '+2word[:2]': strippedpunc[:2],
            '+2word[:3]': strippedpunc[:3],
            '+2word[:4]': strippedpunc[:4],
            '+2word.POS1freq()': nlargest(100, dictionary, key=dictionary.get)[0] if len(dictionary) > 0 else 'None',
            '+2word.POS2freq()': nlargest(100, dictionary, key=dictionary.get)[1] if len(dictionary) > 1 else 'None',
            '+2word.POS3freq()': nlargest(100, dictionary, key=dictionary.get)[2] if len(dictionary) > 2 else 'None',
            '+2word.POS4freq()': nlargest(100, dictionary, key=dictionary.get)[3] if len(dictionary) > 3 else 'None',
            '+2word.POS5freq()': nlargest(100, dictionary, key=dictionary.get)[4] if len(dictionary) > 4 else 'None',
            '+2word.POS6freq()': nlargest(100, dictionary, key=dictionary.get)[5] if len(dictionary) > 5 else 'None',
            '+2word.POSmin()':max(dictionary.items(), key=operator.itemgetter(1))[0],
            '+2word.POSfirst()': list(dictionary.items())[0][0],
            '+2word.POSlast()': list(dictionary.items())[-1][0],
            '+2word.in.sickness()' : strippedpunc in filtered_sicknesses,
            '+2word.in.symptoms()' : strippedpunc in filtered_symptoms,
            '+2word.sentimentpos()': float(sia.polarity_scores(strippedpunc)['pos']),
            '+2word.sentimentneg()': float(sia.polarity_scores(strippedpunc)['neg']),
            '+2word.sentimentneu()': float(sia.polarity_scores(strippedpunc)['neu'])
        })

    return features
