import { addTwoPromises } from "./solution";


addTwoPromises(Promise.resolve(2), Promise.resolve(3))
    .then(console.log);
