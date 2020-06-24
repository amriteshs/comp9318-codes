## import modules here

################# Question 1 #################

def multinomial_nb(training_data, sms):# do not change the heading of the function
    tokens = []
    prior_spam = 0
    prior_ham = 0
    total_freq_spam = 0
    total_freq_ham = 0

    for t in training_data:
        if t[1] == 'spam':
            prior_spam += 1
        elif t[1] == 'ham':
            prior_ham += 1

        for key, val in t[0].items():
            if key not in tokens:
                tokens.append(key)

            if t[1] == 'spam':
                total_freq_spam += val
            elif t[1] == 'ham':
                total_freq_ham += val

    prior_spam /= len(training_data)
    prior_ham /= len(training_data)

    sms_freq_spam = 0
    sms_freq_ham = 0

    for s in sms:
        if s in tokens:
            token_freq_spam = 0
            token_freq_ham = 0

            for t in training_data:
                if t[1] == 'spam':
                    if s in t[0]:
                        token_freq_spam += t[0][s]
                elif t[1] == 'ham':
                    if s in t[0]:
                        token_freq_ham += t[0][s]

            if sms_freq_spam:
                sms_freq_spam *= ((1 + token_freq_spam) / (len(tokens) + total_freq_spam))
            else:
                sms_freq_spam = (1 + token_freq_spam) / (len(tokens) + total_freq_spam)

            if sms_freq_ham:
                sms_freq_ham *= ((1 + token_freq_ham) / (len(tokens) + total_freq_ham))
            else:
                sms_freq_ham = (1 + token_freq_ham) / (len(tokens) + total_freq_ham)

    if sms_freq_spam:
        prob_spam = sms_freq_spam * prior_spam
    else:
        prob_spam = prior_spam

    if sms_freq_ham:
        prob_ham = sms_freq_ham * prior_ham
    else:
        prob_ham = prior_ham

    return prob_spam / prob_ham
