const square = (length) => {
    const proto = {
        type: "Square",
        area() {
            return this.length ** 2;
        },
    };
    return Object.assign(Object.create(proto), {
        length
    });
};

const circle = (radius) => {
    const proto = {
        type: "Circle",
        area() {
            return Math.PI * this.radius ** 2;
        },
    };
    return Object.assign(Object.create(proto), {
        radius
    });
};

const rect = (length, width) => {
    const proto = {
        type: "Rect",
        area() {
            return this.length * this.width;
        },
    };
    return Object.assign(Object.create(proto), {
        length,
        width
    });
};

const areaCalculator = (shapes) => {
    const proto = {
        sum() {
            return shapes.reduce((p, n) => n.area() + p, 0);
            // logic to sum
        },
    };
    return Object.assign(Object.create(proto), {
        shapes,
    });
};

const sumCalculatorOutputter = (sum) => {
    const proto = {
        HTML() {
            return `
                <h1>
                    Sum of the areas of provided shapes:
                    ${sum}
                </h1>
                `;
        },
        JSON() {
            return JSON.stringify({
                sum,
            });
        },
    };
    return Object.assign(Object.create(proto), {
        sum
    });
};

const shapes = [circle(2), square(5), square(6), rect(3, 4)];
const areas = areaCalculator(shapes);
const output = sumCalculatorOutputter(areas.sum());
console.log(output.JSON());
// {"sum":85.56637061435917}
console.log(output.HTML());
// <h1>
//     Sum of the areas of provided shapes:
//     85.56637061435917
// </h1>