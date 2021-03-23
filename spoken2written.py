from word2number import w2n

numbers = {'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9, 'ten':10, 'eleven':11, 'twelve':12,
            'thirteen':13, 'fourteen':14, 'fifteen': 15, 'sixteen':16, 'seventeen':17, 'eighteen':18, 'nineteen':19, 'twenty':20, 'thirty':30,
            'forty':40, 'fifty':50, 'sixty':60, 'seventy':70, 'eighty': 80, 'ninety': 90, 'hundred':100
}

currency = {'dollars':'$'}

symbols = {'percent':'%', 'plus':'+', 'minus':'-', 'hashtag':'#', 'multiplied':'*', 'divided':'/'}

multiple = {'single':1, 'double':2, 'triple':3}

def get_wr_txt(sp_txt):
    sp_tokens = sp_txt.split()
    wr_tokens = []
    start = False
    start_idx = -1
    end_idx = -1
    for i in range(len(sp_tokens)):        
        if ((start == False) and (sp_tokens[i] in numbers.keys())):
            start_idx = i
            start = True
        elif ((start == True) and (sp_tokens[i] in numbers.keys())):
            wr_tokens.append(w2n.word_to_num(sp_tokens[i]))
        elif ((start == True) and (sp_tokens[i] in currency.keys())):            
            end_idx = i
            num_tokens = sp_tokens[start_idx:end_idx]
            num_word = w2n.word_to_num(" ".join(num_tokens))
            print(num_word)
            return (currency[sp_tokens[i]] + num_word)
        elif (sp_tokens[i] == "hours"):
            end_idx = i
            num_tokens = sp_tokens[start_idx:end_idx]
            num_word = w2n.word_to_num(" ".join(num_tokens))
            return (num_word + " hours")
        elif ((sp_tokens[i] == "A") and (sp_tokens[i + 1] == "M")):
            end_idx = i
            num_tokens = sp_tokens[start_idx:end_idx]
            num_word = w2n.word_to_num(" ".join(num_tokens))
            return (num_word + " AM")
        elif ((sp_tokens[i] == "P") and (sp_tokens[i + 1] == "M")):
            end_idx = i
            num_tokens = sp_tokens[start_idx:end_idx]
            num_word = w2n.word_to_num(" ".join(num_tokens))
            return (num_word + " PM")
        elif (sp_tokens[i] in symbols.keys()):
            if (sp_tokens[i] == 'percent'):
                end_idx = i
                num_tokens = sp_tokens[start_idx:end_idx]
                num_word = w2n.word_to_num(" ".join(num_tokens))
                return (num_word + symbols[sp_tokens[i]])
            elif (sp_tokens[i] == 'hashtag'):
                start_idx = i + 1
                end_idx = len(sp_tokens)
                num_tokens = sp_tokens[start_idx:end_idx]
                num_word = w2n.word_to_num("".join(num_tokens))
                return (symbols[sp_tokens[i]] + num_word)
            else:
                end_idx = i
                left_num_tokens = sp_tokens[start_idx:end_idx]
                right_num_tokens = sp_tokens[(i + 1):len(sp_tokens)]
                left_num_word = w2n.word_to_num(" ".join(left_num_tokens))
                right_num_word = w2n.word_to_num(" ".join(right_num_tokens))
                return (left_num_word + " " + symbols[sp_tokens[i]] + " " + right_num_word)
        elif (sp_tokens[i] in multiple.keys()):
            for j in range(multiple[sp_tokens[i]]):
                wr_tokens.append(sp_tokens[i + 1])
            i = i + 1
        else:
            wr_tokens = wr_tokens.append(sp_tokens[i])
        return (" ".join(wr_tokens))
            

if __name__ == "__main__":
    print("Enter spoken text")
    sp_txt = "triple B"
    wr_txt = get_wr_txt(sp_txt)
    print(wr_txt)