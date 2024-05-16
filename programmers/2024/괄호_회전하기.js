let orgStr = s.split("");
let answer = 0;

for (let i = 0; i < s.length; i ++) {
  const stack = [];
  
  while(orgStr.length) {
    const ns = orgStr.shift();
    
    if (ns === "(" || ns === "{" || ns === "[") {
      stack.push(ns);
    }else {
      if (ns === ")" && stack.at(-1) === "(") {
        stack.pop();
        continue;
      }        
      
      if (ns === "}" && stack.at(-1) === "{") {
        stack.pop();
        continue;
      }
      
      if (ns === "]" && stack.at(-1) === "[") {
        stack.pop();
        continue;
      }  
      
      stack.push(ns);
    }
  }
  
  if (stack.length === 0) answer ++;
  orgStr = [...s.slice(i + 1, s.length) ,...s.slice(0, i + 1)]
}


return answer;