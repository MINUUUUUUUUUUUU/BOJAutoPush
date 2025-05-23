def solution(id_list, report, k):
    answer = []
    
    l = len(id_list)
    id_list_dict = {id: idx for idx, id in enumerate(id_list)}
    # print(id_list_dict)
    report = set(report)
    reporter_note = [set() for _ in range(l)]
    report_count = [0 for _ in range(l)]
    mail = [0 for _ in range(l)]

    for r in report:
        reporter, reported = map(str, r.split())
        reported_idx = id_list_dict[reported]
        report_count[reported_idx] += 1
        reporter_note[id_list_dict[reporter]].add(reported_idx)
    
    # print(reporter_note)
    # print(report_count)
    
    for i in range(l):
        if report_count[i] >= k:
            for j in range(l):
                if i in reporter_note[j]:
                    mail[j] += 1

    answer = mail
    return answer