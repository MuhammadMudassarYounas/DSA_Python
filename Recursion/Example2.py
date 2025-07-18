def func(x,N):
    if N==0:
        return
    print(x)
    func(x,N-1)

func(15,4)