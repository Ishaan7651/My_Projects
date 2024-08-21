const { NSFW } = require("nsfwhub");
/* import { NSFW } from "nsfwhub";  For EsModule */

const nsfw = new NSFW();

nsfw.fetch("pussy").then((data) => {
console.log(data.image.url);
});
