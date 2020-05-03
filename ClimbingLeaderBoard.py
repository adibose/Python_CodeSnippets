def do_ranking(sc, uni):
    print(len(uni))
    first = 0
    last = len(uni)-1
    if(sc>uni[first]):
        uni.insert(0,sc)
        return 1
    elif(sc<uni[last]):
        uni.append(sc)
        return len(uni)
    else:
        while (first < last):
            mid = (first + last) //2
            if uni[mid] == sc:
                return mid+1
            elif uni[mid] > sc:
                first = mid+1
            else:
                last = mid
    if (sc < uni[first]):
        uni.insert(first+1,sc)
        return (first + 2)
    if (sc > uni[first]):
        uni.insert(first,sc)
        return first+1


def climbingLeaderboard(scores, alice):
    uni = []
    res_rank = []
    for i in scores:
        if i not in uni:
            uni.append(i)
    for i in alice:
        res_rank.append(do_ranking(i, uni))

    return res_rank


res=climbingLeaderboard([997,981,957,933,930,927,926,920,916,896,887,874,863,863,858,847,815,809,803,794,789,785,783,778,764,755,751,740,737,730,691,677,652,650,587,585,583,568,546,541,540,538,531,527,506,493,457,435,430,427,422,422,414,404,400,394,387,384,374,371,369,369,368,365,363,337,336,328,325,316,314,306,282,277,230,227,212,199,179,173,171,168,136,125,124,95,92,88,85,70,68,61,60,59,44,43,28,23,13,12],[23,23,55,55,55,55,43,105,23])

print(res)