require("dotenv").config();
const http = require("http");
const { exec } = require("child_process");

console.log(process.env);

const server = http.createServer(async (req, res) => {
  if (req.method === "POST") {
    if (req.url === "/api/") {
      if (req.headers.authorization === `Bearer ${process.env.TOKEN}`) {
        // Retrieve and parse body
        const buffers = [];
        for await (const chunk of req) {
          buffers.push(chunk);
        }
        const data = JSON.parse(Buffer.concat(buffers).toString());

        console.log(data);

        if (data.event === "media.create" || data.event === "media.update") {
          if (data.media.mime.startsWith("image")) {
            const imagePath = data.media.url.replace("/uploads/", "");
            console.log(`python3 process.py 'CONVERT' '${imagePath}'`);
            exec(`python3 process.py 'CONVERT' '${imagePath}'`);
          }
        } else if (data.event === "media.delete") {
          if (data.media.mime.startsWith("image")) {
            const imagePath = data.media.url.replace("/uploads/", "");
            console.log(`python3 process.py 'DELETE' '${imagePath}'`);
            exec(`python3 process.py 'DELETE' '${imagePath}'`);
          }
        }

        res.writeHead(200, { "Content-Type": "application/json" }).end(
          JSON.stringify({
            message: "Done.",
          })
        );
      } else {
        res
          .writeHead(403, { "Content-Type": "application/json" })
          .end(JSON.stringify({ message: "Invalid auth token." }));
      }
    } else {
      res
        .writeHead(404, { "Content-Type": "application/json" })
        .end(JSON.stringify({ message: "Route not found.", route: req.url }));
    }
  } else {
    res
      .writeHead(405, { "Content-Type": "application/json" })
      .end(JSON.stringify({ message: "Method Not Allowed. Use POST." }));
  }
});

server.listen(process.env.PORT, () => {
  console.log(`server started on port: ${process.env.PORT}`);
});
