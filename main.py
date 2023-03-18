# python3

def parallel_processing(n, m, data):
    output = []
    # TODO: write the function for simulating parallel tasks, 
    # create the output pairs
    thread = []
    for i in range(n):
        thread.append(i)
    
    moment = 0
    nextAvailable = 0

    while(True):
        if nextAvailable == m:
            break
        for i in range(n):
            if thread[i] == 0:
                thread[i] = data[nextAvailable]
                nextAvailable += 1
                output.append([i, moment])
            thread[i] -= 1
        moment += 1
    
    return output

def main():
    # TODO: create input from keyboard
    # input consists of two lines
    # first line - n and m
    # n - thread count 
    # m - job count
    n = 0
    m = 0
    inputs = list(map(int, input().split()))
    n = inputs[0]
    m = inputs[1]

    # second line - data 
    # data - contains m integers t(i) - the times in seconds it takes any thread to process i-th job
    data = list(map(int, input().split()))

    # TODO: create the function
    result = parallel_processing(n,m,data)
    
    # TODO: print out the results, each pair in it's own line
    for i, j in result:
        print(i, j)


if __name__ == "__main__":
    main()
