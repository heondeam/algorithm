function solution(s, skip, index) {
    let newWord = "";
    let answer = "";
    let newAlphabet = Array.from({ length: 26 }, (v, i) => String.fromCharCode(i + 97)).filter(item => !skip.includes(item));
    
    
    // 1. 문자열 s의 각 알파벳을 index 만큼 뒤의 알파벳으로 바꿔준다.
    for (const ns of s) {
      const nowIndex = newAlphabet.findIndex(item => item === ns);
      
      if(nowIndex + index > newAlphabet.length - 1) {
        // 2. index 만큼의 뒤의 알파벳이 z를 넘어갈 경우 다시 a로 돌아간다.
        let count = (nowIndex + index) % newAlphabet.length;
        
        newWord += newAlphabet[count]; 
      }else {
        newWord += newAlphabet[nowIndex + index];
      }
    }
    
    return newWord;
  }