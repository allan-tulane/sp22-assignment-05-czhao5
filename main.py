
####### Problem 3 #######

test_cases = [('book', 'back'), ('kookaburra', 'kookybird'), ('elephant', 'relevant'), ('AAAGAATTCA', 'AAATCA')]
alignments = [('book', 'back'), ('kookaburra', 'kookybird-'), ('relev-ant','-elephant'), ('AAAGAATTCA', 'AAA---T-CA')]

def MED(S, T):
    # TO DO - modify to account for insertions, deletions and substitutions
    if (S == ""):
        return(len(T))
    elif (T == ""):
        return(len(S))
    else:
        if (S[0] == T[0]):
            return(MED(S[1:], T[1:]))
        else:
            return (1 + min(MED(S, T[1:]), MED(S[1:], T), MED(S[1:],T[1:])))
         #insert, delete, and substitute in the respective order


def fast_MED(S, T, MED={}):
  # TODO -  implement memoization
  k = T,S
  if not T:
    MED[len(S),0] = len(S)
    return len(S)
  elif not S:
    MED[0,len(T)] = len(T)
    return len(T)
  elif k in MED:
    return MED[k]
  elif S[0] == T[0]:
    f = (fast_MED(S[1:], T[1:]))
    return f
  else:
    return (1 + min(fast_MED(S, T[1:]), fast_MED(S[1:],T), fast_MED(S[1:],T[1:])))
    pass

def fast_align_MED(S, T, MED={}):
    # TODO - keep track of alignment
    pass

def test_MED():
    for S, T in test_cases:
        assert fast_MED(S, T) == MED(S, T)
                                 
def test_align():
    for i in range(len(test_cases)):
        S, T = test_cases[i]
        align_S, align_T = fast_align_MED(S, T)
        assert (align_S == alignments[i][0] and align_T == alignments[i][1])

