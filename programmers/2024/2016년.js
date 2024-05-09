function solution(a, b) {
    const dayMap = {
      0: "SUN",
      1: "MON",
      2: "TUE",
      3: "WED",
      4: "THU",
      5: "FRI",
      6: "SAT"
    }
    
    const date = new Date(`2016-${a}-${b}`);
    
    return dayMap[date.getDay()]
  }
  
  solution(5, 24)