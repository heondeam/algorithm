export class Queue {
    constructor(value) {
        this.data = [...value];
    }

    dequeue() {
        return this.data.shift();
    }

    inque(value) {
        this.data.push(value);
    }

    size() {
        return this.data.length;
    }

    isEmpty() {
        return this.data.length > 0 ? true : false;
    }
}