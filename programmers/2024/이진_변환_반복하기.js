function solution(s) {
    let result = 0;
    let turn = 0;
    
    while (s !== "1") {
      turn ++;
      let newStr = "";
      
      for (const ns of s) {
        if (ns === "0") {
          result ++;
        }else {
          newStr += "1";
        }
      }
      
      
      s = newStr.length.toString(2);
    }
    
    return [turn, result];
  }
  
  solution("1111111")