
def WIS():

    number_inputs = int(input())
    #instance
    for _ in range(number_inputs):
        num_jobs = int(input())
        jobList = [] #list of lists [start, end, value]

        #populate the job array
        for i in range(num_jobs):
            job = [int(value) for value in input().split()]
            jobList.append(job)

        #sort jobs by finish time
        sortedJobList = sorted(jobList, key=lambda x: x[1])

        DPArr = [0] * (len(sortedJobList) + 1) #2d DP array storing [[value, [jobs]]]
         # first value of DPArr is 0, gets 0 value for doing 0 jobs

        for j in range(1, len(sortedJobList) + 1):
            #Find index i such that finish time <= start of j
            j_start = sortedJobList[j - 1][0]
            #find last compatable index i
            last_compatible = 0
            #start from j-1, right before j itself
            for i in range(j-1, 0, -1):
                if sortedJobList[i-1][1] <= j_start:
                    last_compatible = i
                    break
                    
            DPArr[j] = max(DPArr[j - 1],sortedJobList[j - 1][2] + DPArr[last_compatible])
        
        print(DPArr[-1])

if __name__ == "__main__":
    WIS()