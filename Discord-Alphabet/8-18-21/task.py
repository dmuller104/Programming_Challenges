def get_max_k_subseq(k,lst):
    capt = None
    capt_range = None
    n = len(lst)
    start,end = 0,0 # inclusive
    cut_index = -1 # everything before cut_index will be cut
    summ = 0
    prev_end = -1
    cut_val = 0
    while end != n:
        # only add if iterated forward
        if prev_end != end:
            summ += lst[end]
            prev_end = end
        # create cutoff line for non-positive portion at front of buffer
        if cut_index == -1:
            if lst[start] <= 0:
                cut_val = lst[start]
                cut_index = start+1
                continue
            elif summ <= 0:
                cut_val = summ
                cut_index = end+1
        # cut off non-positive portion of buffer when len(rest of buffer) >= k
        elif end+1 - cut_index >= k:
            # summ -= sum(lst[start:cut_index])
            summ -= cut_val
            start = cut_index
            cut_index = -1
            continue
        # set max when buffer is large enough
        if (end+1-start >= k) and (capt == None or summ > capt):
            capt = summ
            capt_range = (start,end)
        end += 1
    return capt,capt_range

def main():
    lists = []
    lists.append((3,[5,4,-10,1,2,3]))
    lists.append((3,[-8, -5, -2, 10, -9, 0, -5, 1, 9, -5, 1, -6, 9, 7, -5, -6, 2, 8, -1, -1]))
    lists.append((5,[3, -1, -6, 4, -8, 8, -2, 5, -2, -5, -3, -7, -6, 6, -10, 7, 0]))
    for k,lst in lists:
        print(lst)
        result = get_max_k_subseq(k,lst)
        print(f"max: {result[0]} between and including indices: {result[1]}\n")
main()