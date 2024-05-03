// 옹알이

function solution(babbling) {
    let answer = 0;
    const words = ["aya", "ye", "woo", "ma"];
    
    
    while (babbling.length) {
      const r = babbling.shift();
      let ex = "";
      let nw = "";
      
      for (const w of r.split("")) {
        nw += w;
        
        if (words.indexOf(nw) > -1 && ex !== nw) {
          ex = nw;
          nw = "";
        }
      }
      
      if (!nw) answer++;
    }
    
    return answer;
  }
  
  solution(["ayaye", "woowo", "yeye", "yemawoo", "ayaayaa"]);