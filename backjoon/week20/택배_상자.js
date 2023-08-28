function solution (order) {
    const sub = [];
    const truck = [];
    // 메인 컨테이너는 1 박스부터 order.length 만큼 존재함.
    let containerBox = 1;
    let boxIndex = 0;
    
    
    while(containerBox <= order.length + 1) {
      
      // 서브 컨테이너 벨트에 있는 경우
      if(sub.length !== 0 && order[boxIndex] === sub.at(-1)) {
        truck.push(sub.pop());
        boxIndex += 1;
        continue;
      }
      
      // 메인 컨테이너 벨트에 있는 경우
      if(containerBox === order[boxIndex]) {
        truck.push(containerBox);
        containerBox += 1;
        boxIndex += 1;
        continue;
      }
          
      sub.push(containerBox);
      containerBox += 1;
    }
    
    return truck.length;
  }
  