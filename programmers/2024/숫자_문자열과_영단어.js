function solution(s) {
    const words = ["zero", "one", "two", "three", "four", "five", "six", "seven" , "eight", "nine"];
      
  
    for (let i = 0; i < words.length; i ++) {
      const isWord = s.includes(words[i]);
  
      if(isWord) s = s.replaceAll(words[i], i.toString());
    }
    
    
    return +s;
  }
  
  solution("one4seveneight")