
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
  # TODO -  implement memorization
  x = T,S
  if not T:
    MED[len(S),0] = len(S)
    return len(S)
  elif not S:
    MED[0,len(T)] = len(T)
    return len(T)
  elif x in MED:
    return MED[k]
  elif S[0] == T[0]:
    return fast_MED(S[1:], T[1:])
  else:
    return (1 + min(fast_MED(S, T[1:]), fast_MED(S[1:],T), fast_MED(S[1:],T[1:])))
    pass

def fast_align_MED(S, T, MED={}):
    # TODO - keep track of alignment
    x, y = (len(T), len(S))

    if T == "":
      MED[(S, T)] = [S, '-'*y, y]
      return S, '-'* y 
    if S == "":
      MED[(S, T)] = ['-'* x, T, x]
      return '-'* x, T

      
    if T != "" and S != "":
        if (S, T) in MED:
            m = MED[(S, T)][0]
            n = MED[(S, T)][1]
            return m,n
        else:

            if S[0] != T[0]:
                ains, bins = fast_align_MED(S, T[1:])
                asub, bsub = fast_align_MED(S[1:], T[1:])
                adel, bdel = fast_align_MED(S[1:], T)

                c1 = MED[(S, T[1:])]
                c2 = MED[(S[1:], T[1:])]
                c3 = MED[(S[1:], T)]
                cost = 1 + min(c1[2], c2[2], c3[2])
              
                if cost - 1 == c1[2]:
                    MED[(S, T)] = ["-" + ains, T[0] + bins, cost]
                  
                elif cost - 1 == c2[2]:
                    MED[(S, T)] = [S[0] + asub, T[0] + bsub, cost]
                  
                else:
                    MED[(S, T)] = [S[0] + adel, '-' + bdel, cost]
            
            else:
                a, b =  fast_align_MED(S[1:], T[1:])
                a1 =  S[0] + a
                b1 = T[0] + b
                MED[(S, T)] = [ a1, b1, MED[(S[1:], T[1:])][2] ]

              
            return MED[(S, T)][0],  MED[(S, T)][1]

    pass

def test_MED():
    for S, T in test_cases:
        assert fast_MED(S, T) == MED(S, T)
                                 
def test_align():
    for i in range(len(test_cases)):
        S, T = test_cases[i]
        align_S, align_T = fast_align_MED(S, T)
        assert (align_S == alignments[i][0] and align_T == alignments[i][1])

