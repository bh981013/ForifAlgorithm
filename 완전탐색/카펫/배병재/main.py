def solution(brown, yellow):
    s=brown+yellow
    ans=[]
    for i in range(2,s):
        if s%i==0:
            row=s//i
            col=i
            new_b=(row+col)*2-4
            if new_b==brown:
                if row>col:
                    ans.append(row)
                    ans.append(col)
                else:
                    ans.append(col)
                    ans.append(row)
                return ans
        else:
            continue