const circle = (radius) => {
    const proto = {
        type: "Circle",
        //code
    };
    return Object.assign(Object.create(proto), {
        radius
    });
};

const square = (length) => {
    const proto = {
        type: "Square",
        //code
    };
    return Object.assign(Object.create(proto), {
        length
    });
};

const areaCalculator = (shapes) => {
    const proto = {
        sum() {
            return shapes.reduce((p, n) => {
                if (n.type == "Circle") {
                    return Math.PI * n.radius * n.radius + p;
                }
                if (n.type == "Square") {
                    return n.length * n.length + p;
                }
            }, 0);
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

const shapes = [circle(2), square(5), square(6)];
const areas = areaCalculator(shapes);
const output = sumCalculatorOutputter(areas.sum());
console.log(output.JSON());
// {"sum":73.56637061435917}
console.log(output.HTML());
// <h1>
//     Sum of the areas of provided shapes:
//     73.56637061435917
// </h1>