
"""
The input will start with a positive integer, giving the number
of instances that follow. For each instance,
there will be a string. fOr each string s, the
program should output Hello, s! on its own line.
"""
#number, toSayHello: list


def FFRemove():

    number_inputs = int(input())
    names = []

    for _ in range(number_inputs):
        cache_size = int(input())
        num_instances = int(input())
        input_string = input() #gets a string of inputs
        request_list = [int(i) for i in input_string.split()]
        loc_dict = {} #dictionary storing locations
        cache_set = set() #simulates a cache
        num_pagefaults = 0
        num_hits = 0

        #preprocessing (O(n)):
        for i in range(len(request_list)):
            if request_list[i] not in loc_dict:
                loc_dict[request_list[i]] = [i] #loc_dict[request] = index
            else: #the request is already in the dictionary
                loc_dict[request_list[i]].append(i)
        #so we already have a dictionary that stores FF.

        #Now we follow through the requests
        for i in range(len(request_list)):
            # print(cache_set)
            # print(f"request {i} done")


            loc_dict[request_list[i]].pop(0) #so in every iteration we remove already used elements
                    #keeps the dict up to date, so the min element of every list is always used in the future
                #first case: cache full, we need to evict.

            #hit: ignore
            if (request_list[i] in cache_set):
                num_hits += 1

            #cache not full, add to set
            elif ((len(cache_set) < cache_size) and request_list[i] not in cache_set):
                num_pagefaults += 1
                cache_set.add(request_list[i])
                
            #cache full and request not in cache
            # if (len(cache_set) == cache_size and request_list[i] not in cache_set):
            else:
                num_pagefaults += 1
                #now find FF
                furthest_page = -1
                furthestFutureValue = -1

                # for cache_element_index in range(cache_set):
                #     #current furthur future value is closer 
                #     if (furthurstFutureValue < loc_dict[cache_set[cache_element_index]][0]):
                #         furthurstFutureIndex = cache_element_index
                #         furthurstFutureValue = loc_dict[cache_set[cache_element_index]][0]
                
                
                for cache_element in cache_set:
                    if len(loc_dict[cache_element])==0:
                        # never used again
                        furthestFutureValue = float('inf')
                        furthest_page = cache_element
                        break
                    elif loc_dict[cache_element][0] > furthestFutureValue:
                        furthestFutureValue = loc_dict[cache_element][0]
                        furthest_page = cache_element

                #now evict the element with furthurst future value
                # toRemove = set[furthurstFutureIndex]
                # set.remove(toRemove)
                cache_set.remove(furthest_page)

                #eviction done, now add element:
                cache_set.add(request_list[i])
        print(num_pagefaults)
if __name__ == "__main__":
    FFRemove()