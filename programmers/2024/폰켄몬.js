// 폰켄몬


function solution(nums) {
  
    const getNum = nums.length / 2;  
    const poketmons = new Set(nums);
    
    const myPoketmons = poketmons.size;
    
    // 데려가야 하는 폰켄몬 종류의 수가 종류의 수보다 크면 종류의 수 출력
    if (getNum > myPoketmons) {
      return myPoketmons;
    }
    
    // 아니라면 데려가야 하는 폰켄몬 수 출력
    return getNum;
  }
  
  solution([3,3,3,7,7,7,1,1,11,11]);
  
  
  