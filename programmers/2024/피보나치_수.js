function solution(n) {
    const dp = Array.from({length: n}, () => 0);
    
    dp[0] = 0;
    dp[1] = 1;
    dp[2] = 1;
    dp[3] = 2;
    dp[4] = 3;
    dp[5] = 5;
    
    if (n <= 5) return dp[n];
    
    for (let i = 6; i <= n; i++) {
      dp[i] = dp[i-1] + dp [i-2];
    }
    
    return dp[n]
  }
  
  solution(5)