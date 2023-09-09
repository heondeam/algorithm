function solution(s) {
    let answer = 0;
    
    const stack = [];
    
    for (const w of s) {
      if(stack.length) {
        // 스택이 비어있지 않을 때
        // 스택의 맨 위에 있는 알파벳과 현재 알파벳이 같은지 확인.
        if(stack.at(-1) === w) {
          stack.pop();
        }else {
          stack.push(w);
        }
      }else {
        // 스택이 비어있을 때
        stack.push(w);
      }
    }
    
    
    return stack.length > 0 ? 0 : 1;
  }