function solution(array, commands) {
    const answer = [];
    
    for (const c of commands) {
        const [i, j, k] = c;
        
        const newArr = array.slice(i - 1, j).sort((a,b) => a - b);
  
      
      answer.push(newArr[k-1])
    }
    
    return answer    
}