// 개인정보 수집 유효기간

function solution(today, terms, privacies) {
    const terms_list = Object.assign({}, ...terms.map(v => {
      const [t, m] = v.split(" ");
      
      return {[t]: +m}
    }));
    const answer = [];
    
    
    for (const [idx, p] of privacies.entries()) {
      const [d, t] = p.split(" ");
      const nowTerm = terms_list[t];
      const nowDay = new Date(d);
      
      nowDay.setMonth(nowDay.getMonth() + nowTerm);
      
      if (nowDay < new Date(today)) {
        answer.push(idx + 1);
      }
    }
    
    return answer;
  }
  
  solution("2022.05.19", ["A 6", "B 12", "C 3"], ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]);