// function solution(n) {
//   // 더해서 n이 되는 경우의 수 찾기
//   const a = []
  
  
//   const dfs = (x, arr) => {
//     arr.push(x);
    
//     const sum = arr.reduce((acc, a) => acc + a);
    
//     if (sum === n) {
//       a.push(arr);
//       return;
//     }
    
//     if (sum > n) return;
    
//     dfs(1, [...arr])
//     dfs(2, [...arr]);
//   }
  
//   dfs(1, []);
//   dfs(2, [])
  
//   return a.length % 1234567;
// }

// solution(4);

function solution(n) {
  const dp = Array.from({length: n + 1}, () => 0);
  
  dp[0] = 1;
  dp[1] = 1;
  dp[2] = 2;
  dp[3] = 3;
  
  for (let i = 4; i <= n; i++) {
    dp[i] = dp[i-2] + dp[i - 1];
  }
  
  return dp[n] % 1234567;
}

solution(4);