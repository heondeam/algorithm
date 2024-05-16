function solution(s) {
    const splited = s.slice(1, s.length - 1).split(",");
    const arr = [];
    const answer = [];
    
    let tempArr = [];
    
    for (let i = 0; i < splited.length; i++) {
      const ns = splited[i];
      
      if (ns.includes("{")) {
        if (ns.includes("}")) {
          tempArr.push(+ns.split("{").at(-1).split("}")[0])
          arr.push(tempArr);
          tempArr = [];
          continue;
        }
  
        tempArr.push(+ns.split("{").at(-1));
      }else if (ns.includes("}")) {
        tempArr.push(+ns.split("}")[0]);
        arr.push(tempArr);
        tempArr = [];
      }else {
        tempArr.push(+ns);
      }
    }
    
    const sorted = arr.sort((a, b) => a.length - b.length);
    
    for (let i = 0; i < sorted.length; i++) {
      const rs = sorted[i];
      
      if (rs.length === 1) {
        answer.push(rs[0]);
      }else {
        const minus = rs.filter(x => !answer.includes(x));
        answer.push(minus[0]);
      }
    }
    
    return answer;
  }
  
  
  solution("{{123}}"	);