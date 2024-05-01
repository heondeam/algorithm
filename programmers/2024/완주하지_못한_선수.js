// 완주하지 못한 선수


function solution(participant, completion) {
    const comp_map = {};
    
    for (let i = 0; i < completion.length; i ++) {
      
      if (comp_map[completion[i]]) {
        comp_map[completion[i]] ++;
        continue;
      }
      
      comp_map[completion[i]] = 1;
    }
    
    for (let i = 0; i < participant.length; i++) {
      const n = participant[i];
      
      if (comp_map[n]) {
        comp_map[n]--; 
        continue;
      }
      
      return n;
    }
  }
  
  solution(["marina", "josipa", "nikola", "vinko", "filipa", "marina"], ["josipa", "filipa", "nikola", "marina", "marina"]);