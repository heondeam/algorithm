function solution(book_time) {
  const book = book_time.map(([start, end]) => {
    const startTime = start.split(":").map(Number);
    const endTime = end.split(":").map(Number);
    const rsTime = startTime[0] * 60 + startTime[1];   // 입실 시간
    const reTime = endTime[0] * 60 + endTime[1] + 10;  // 퇴실 시간
    
    return [rsTime, reTime];
  });
  
  const rooms = [];
  
  book.sort((a,b) => a[0] - b[0]);
  
  book.forEach(([start, end]) => {
    
    // 현재 룸에 있는 사람들의 퇴실시간과 비교하여 룸 비워줌.
    rooms.forEach((room, index) => {
      const [rs, re] = room[room.length - 1]; 
      
      if (start >= re) {
        rooms.splice(index, 1);
      }
    });
    
    let flag = true;
    
    // 비어 있는 룸 있으면? 들어감.
    for (const room of rooms) {
      if (room.length === 0) {
        room.push([start, end]);
        flag = false;
        break;
      }
    }
    
    if (flag) {
      rooms.push([[start, end]]);
    }
  });
  
  return rooms.length;
}