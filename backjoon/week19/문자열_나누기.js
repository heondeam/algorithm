function solution (s) {
  let splitedStr = s.split("");
  let answer = [];
  
  while(splitedStr.length) {
    let nowValue = splitedStr[0];
    let same = 0;
    let diff = 0;
    
    for (const [i, s] of splitedStr.entries()) {
      
      if(nowValue === s) {
        same += 1;
      }else {
        diff += 1;
      }
      
      
      if(same === diff) {
        answer.push(splitedStr.slice(0, i + 1).join(""));
        splitedStr.splice(0, i + 1);  
        break;
      }
      
      if(same !== diff && i === splitedStr.length -1) {
        answer.push(splitedStr.slice(0, i + 1).join(""));
        splitedStr.splice(0, i + 1);
      }
    }
  }
  
  return answer.length;
}

solution("abracadabra");