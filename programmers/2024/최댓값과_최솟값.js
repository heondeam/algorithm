function solution(s) {
    const str = s.split(" ").map(Number);
    const [max, min] = [Math.max(...str), Math.min(...str)];
    
    return `${min} ${max}`;
  };
  
  solution("-1 -2 -3 -4");