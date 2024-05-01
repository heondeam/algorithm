let fs = require('fs');
let input = fs.readFileSync('./input.txt').toString().trim().split("\n");

const solution = () => {
    // 현재 화면에는 이모티콘 1개가 존재함. === S (2 <= S < 1000)
    const S = Number(input.shift());

    // 방문 확인 배열 (현재 화면 이모티콘 개수, 클립보드 상의 이모티콘 개수) -> 2차원 배열로 생성
    let visited = Array.from({length: 1001}, () => Array(1001).fill(0));


    const bfs = () => {
        // [현재위치, 클립보드, 시간]
        const queue = [[1, 0, 0]];
        visited[1][0] = 1;

        while (queue.length) {
            const [nP, clipBoard, time] = queue.shift();
            if (nP === S) return time;

            // S의 범위가 넘어가면 다음 루프로 continue
            if (nP <= 0 || nP > 1000) continue; 

            // 연산 1. 화면에 있는 이모티콘을 모두 복사해서 클립보드에 저장.
            if (!visited[nP][nP]) {
                visited[nP][nP] = 1;
                queue.push([nP, nP, time + 1]);
            }

            // 연산 2. 클립보드에 있는 모든 이모티콘을 화면에 붙여넣기 한다. (기존에 클립보드에 존재하던 내용은 덮어쓰기가 된다.)
            if (clipBoard && nP + clipBoard <= 1000) {
                if (!visited[nP + clipBoard][clipBoard]) {
                    visited[nP + clipBoard][clipBoard] = 1;
                    queue.push([nP + clipBoard, clipBoard, time + 1]);
                }
            }

            // 연산 3. 화면에 있는 이모티콘 중 하나를 삭제한다.
            if (!visited[nP -1][clipBoard]) {
                visited[nP -1][clipBoard] = 1;
                queue.push([nP - 1, clipBoard, time + 1]);
            }
        }
    }

    return bfs();
}

console.log(solution());