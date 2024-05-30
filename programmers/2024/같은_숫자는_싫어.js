function solution(arr)
{
  // 배열 arr에서 연속적으로 나타나는 숫자 하나만 남기고 전부 제거. (제거된 후 남은 수들을 반환할 때는 배열 arr의 원소들의 순서를 유지해야 한다.)
  const answer = [];
  
  
  for (let i = 0; i < arr.length; i ++) {
    const n = arr[i];
    
    if (i < arr.length - 1 && n === arr[i + 1]) {
    }else {
      answer.push(n);
    }
  }

  return answer;  
}