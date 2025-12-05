from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        counter = Counter(nums)
        buckets = [0] * (n+1)

        for num, freq in counter.items():
            if buckets[freq] == 0:
                buckets[freq] = [num]
            else:
                buckets[freq].append(num)
        
        ret = []
        for i in range(n, -1, -1):
            if buckets[i] != 0:
                ret.extend(buckets[i])
            if len(ret) == k:
                break
        return ret

        #Time : O(n)
        #Space: O(n)

        # This problem requires a dictionary to store the frequency of the
        # nums in the array and then take the key and value as individual tuples
        # and then we start adding them to a min or max heap and we compare
        # the frequency of the numbers with the one that is getting added to the 
        # list and if the freq is less then it goes above the existing one for minheap 
        # and if the freq is high then it gets added after that, here we will be using
        # a heap of "k" which is the numbers required as per question and then
        # we remove the top most element in min heap if the k is reached and return
        # the numbers remaining in the heap not the freq. The heap operation takes O(n log k).

        '''
        There is an other approach as well we do the dictionary part as it is 
        and instead of heap we will use an array or list and index it to the 
        number of elements present in the array as the freq will not exceed that
        number and once we create a dictionary with the freq of the numbers we add the 
        key to the exact positon of the new array where it matches with its frequency, 
        once all are done added we then go from the highest positions and check the numbers
        in those positions and remember if some numbers have same frequency we then 
        create a list inside of it with the numbers at that positions and when we are
        going through the new array if there is a number at a higher position we add it to
        the output and return the output until the k value meets. This is the method I used.
        '''