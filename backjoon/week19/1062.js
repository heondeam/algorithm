let fs = require('fs');
let input = fs.readFileSync('./input.txt').toString().trim().split("\n");

// 학생들이 읽을 수 있는 단어의 최댓값을 구하자.

// n : 단어의 개수 (n <= 50) , k : 가르칠 수 있는 글자. (k <= 26)
const [n, k] = input.shift().split(" ").map(Number);

// 필수로 알아야하는 글자.
const essentialLetters = new Set(["a", "c", "t", "i", "n"]);

/**
 * 제너레이터를 사용한 조합 구하기 
 * @param {*} elements 
 * @param {*} selectNumber 
 */
const combinations = function* (elements, selectNumber) {
    for (let i = 0; i < elements.length; i++) {
        if (selectNumber === 1) {
            yield [elements[i]];
        } else {
            const fixed = elements[i];
            const rest = elements.slice(i + 1);

            for (const a of combinations(rest, selectNumber - 1)) {
                yield [fixed, ...a];
            }
        }
    }
};

/**
 * 읽을 수 있는 문자 판별
 */
const checkReadableWords = (words, learnd) => {
    let cnt = 0;

    for (const w of words) {
        let flag = true;

        for (const s of w) {
            if(!learnd.has(s)) {
                flag = false;
            }
        }

        if(flag) {
            cnt ++;
        }

    }

    return cnt;
}


if (k >= 5) {
    let answer = 0;
    const remainAlphabet = Array.from({ length: 26 }, (_, index) => String.fromCharCode(97 + index))
        .filter(letter => !essentialLetters.has(letter));

    for (const teach of combinations(remainAlphabet, k-5)) {
        const learnSet = new Set([...essentialLetters, ...teach]);
        const cnt = checkReadableWords(input, learnSet);

        if(answer < cnt) {
            answer = cnt;
        }
    }

    console.log(answer);
}else {
    // 필수로 알아야하는 글자를 배울 수 없음. -> 읽을 수 있는 단어 0
    console.log(0);
}