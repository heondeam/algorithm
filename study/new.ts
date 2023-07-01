

let text1: number = 11;


const test2 = (x: number, y: number): string => {
    return x + y + "1";
}

type NewNumber = { 
    num1: number;
    num2: number;
}

const test3: NewNumber = {
    num1: 15,
    num2: 16
}

interface NewString {
    text1: string,
    text2: string
}

const test4: NewString = {
    text1: "gesxca",
    text2: "11235152"
};

console.log(test4.text1, test4.text2);

