function solution(n) {
    const numOfOne = n.toString(2).split("").filter(a => a=== "1").length;
    
    let nextNum = n + 1;
  
    while (true) {
      const nextNumOfOne = nextNum.toString(2).split("").filter(a => a=== "1").length;
      
      if (nextNumOfOne === numOfOne) {
        break;
      }else {
        nextNum ++;
        continue;
      }
    }
    
    return nextNum;
  }
  
  solution(78)