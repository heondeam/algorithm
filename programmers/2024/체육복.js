function solution(n, lost, reserve) {
    lost.sort((a,b) => a - b);
    let fp = n - lost.length;
    
    for (let i = 0; i < lost.length; i++) {
      const np = lost[i];
      // 양옆 사람 번호
      const [lp, rp] = [np - 1, np + 1];
      
      // 자신한테 여분이 있을 시
      if (reserve.indexOf(np) > -1) {
        fp += 1;
        reserve.splice(reserve.indexOf(np), 1);
        continue;
      }
      
      if ((lp - 1) >= 0 && reserve.indexOf(lp) > -1 && lost.indexOf(lp) < 0) {
        
        fp += 1;
        reserve.splice(reserve.indexOf(lp), 1);
        continue;
      }
      
      if ((rp - 1) < n && reserve.indexOf(rp) > -1 && lost.indexOf(rp) < 0) {
        if (lost.indexOf(rp - 1) > -1) continue;
  
        fp += 1;
        reserve.splice(reserve.indexOf(rp), 1);
        continue;
      }
    }
    
    
    // 총 학생 수 - 잃어버린 학생 수 + 빌릴 수 있는 학생 수 
    return fp;
  }
  
  solution(5, [2, 4], [3]);