def solution(id_list, report, k):
    reportRec = {id : set() for id in id_list}
    for r in report:
        a, b = r.split()
        reportRec[b].add(a)
    
    reportCnt = {id : 0 for id in id_list}
    for a, b in reportRec.items():
        if len(b) < k: continue
        for p in b: reportCnt[p] += 1
    
    ans = []
    for id in id_list: ans.append(reportCnt[id])
    
    return ans
