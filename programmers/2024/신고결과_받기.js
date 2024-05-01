// 신고 결과 받기


function solution(id_list, report, k) {
    const report_table = Object.assign({}, ...id_list.map((v) => ({[v] : {
      receive: new Set(),
      report: new Set()
    }})));
    const ids = Array(id_list.length).fill(0);
    
    for (const [idx, info] of report.entries()) {
      const [reporter, receiver] = info.split(" ");
      
      report_table[reporter].report.add(receiver);
      report_table[receiver].receive.add(reporter);
    }
    
    for (const s in report_table) {
      const {receive, report} = report_table[s];
      
      const reports= [...report];
      
      report.forEach(r => {
        if (report_table[r].receive.size >= k) {
          ids[id_list.indexOf(s)] ++;
        }
      })
    }
  
    return ids;
  }
  
  
  
  solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 2);
  
  
  
  
  
  
  