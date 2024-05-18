function solution(s) {
    const splited = s.split(" ");
    const results = [];
    
    for (let i = 0; i < splited.length; i ++) {
      const ns = splited[i];
      let newStr = "";
      
      for (let j = 0; j < ns.length; j ++) {
        const nw = ns[j].charCodeAt();
        
        if (j === 0) {
          if (nw >= 97 && nw <122) {
            newStr += ns[j].toUpperCase();
          }else {
            newStr += ns[j];
          }
        }else {
          
          if (nw >= 65 && nw <= 90) {
            newStr += ns[j].toLowerCase();
          }else {
            newStr += ns[j];
          }
          
        }
      }
      
      results.push(newStr);
    }  
    
    return results.join(" ")
  }
  
  solution("3people unFollowed me")