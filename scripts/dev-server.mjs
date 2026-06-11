import { createServer } from "vite";

const host = process.env.HOST || "127.0.0.1";
const port = Number(process.env.PORT || 5173);

const server = await createServer({
  server: {
    host,
    port,
  },
});

await server.listen();
server.printUrls();

process.on("SIGINT", async () => {
  await server.close();
  process.exit(0);
});
