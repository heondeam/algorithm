function solution (park, routes) {
  const maps = [];
  let [sx, sy] = [0, 0];
  
  for (let i = 0; i < park.length; i ++) {
    maps.push([]);
    
    park[i].split("").forEach((item, ni) => {
      if(item === "S") {
        sx = i;
        sy = ni;
      }
      
      maps[i].push(item);
    });
  }
  
  let [h, w] = [maps.length, maps[0].length];
  
  for (let i = 0; i < routes.length; i ++) {
    const [nd, d] = routes[i].split(" ");
    
    if (nd === "E" && sy + Number(d) < w
       ) {
      let flag = true;      
      for (let j = sy; j < sy + Number(d) + 1; j ++) {
        if(maps[sx][j] === "X") {
          flag = false;
          break;
        };
      }
      
      if(flag) {
        sy += Number(d);
      }
    }
    
    
    if (nd === "W" && sy - Number(d) >= 0) {
      let flag = true;      
      for (let j = sy; j >= sy - Number(d); j --) {
        if(maps[sx][j] === "X") {
          flag = false;
          break;
        };
      }
      
      if(flag) {
        sy -= Number(d);
      }
    }
    
    
    if (nd === "S" && sx + Number(d) < h) {
      let flag = true;      
      for (let j = sx; j < sx + Number(d) + 1; j ++) {
        if(maps[j][sy] === "X") {
          flag = false;
          break;
        };
      }
      
      if(flag) {
        sx += Number(d);
      }
      
    }
    
    if (nd === "N" && sx - Number(d) >= 0) {
      let flag = true;      
      for (let j = sx; j >= sx - Number(d); j --) {
        if(maps[j][sy] === "X") {
          flag = false;
          break;
        };
      }
      
      if(flag) {
        sx -= Number(d);
      } 
    }
  }
  
  return [sx, sy];
}


solution(["SOOOX","OOOOO","OOOOO", "OOOOO", "OOOOO"], ["E 3"]);