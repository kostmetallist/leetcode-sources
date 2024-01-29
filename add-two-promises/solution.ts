type P = Promise<number>

async function addTwoPromises(promise1: P, promise2: P): Promise<number> {
    return (await Promise.all([promise1, promise2])).reduce((prev, cur, _, __) => prev + cur, 0);
};

export { addTwoPromises };
