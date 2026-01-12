"""
The input will start with a positive integer, giving the number
of instances that follow. For each instance,
there will be a string. fOr each string s, the
program should output Hello, s! on its own line.
"""
#number, toSayHello: list


def scheduleJob():

    num_instances = int(input())

    for i in range(num_instances):
        num_jobs = int(input())
        #implement earliest finish first
        #load jobs into data structure
        jobs_scheduled = [] #tracks jobs scheduled
        jobs = []

        #O(n)
        for job in range(num_jobs):
            jobString = input().strip()
            jobs.append(jobString.split())
            #at this point all jobs are stored in the jobs array

        #sort jobs by finish time:
        sorted_by_finish = sorted(jobs, key=lambda x: int(x[1]))
        
        #TOO SLOW
        # # print(sorted_by_finish)
        # for job in sorted_by_finish:
        #     #check any conflicts start end1 > start or start1 < end:
        #     # print(jobs_scheduled)
        #     conflict = False #set conflict state to false
        #     for existing_job in jobs_scheduled:
        #         # print(f"Checked for", job)
        #         if check_conflict(job, existing_job):
        #             conflict = True

        #     #no conflicts, check
        #     if (not conflict):
        #         jobs_scheduled.append(job)

        #don't really need to go through all the jobs. As we have sorted by finish time 
        #the last job scheduled will have the latest finish time and it doesn't have any conflicts.
        #O(n)a
        for job in sorted_by_finish:
            if (len(jobs_scheduled) == 0):
                jobs_scheduled.append(job)
            #
            elif(not(check_conflict(job, jobs_scheduled[-1]))):
                #no conflict, ok:
                jobs_scheduled.append(job)

        print(len(jobs_scheduled))
        
#Returns true if confict, false if no conflict
def check_conflict (job1, job2):
    #jobs: [start, end]

    #job overlaps if job 1 starts before job 2 and before job 1 ends job 2 starts
    return int(job1[0]) < int(job2[1]) and int(job2[0]) < int(job1[1])
if __name__ == "__main__":
    scheduleJob()