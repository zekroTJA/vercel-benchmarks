import type { VercelRequest, VercelResponse } from "@vercel/node";

export default function (_: VercelRequest, response: VercelResponse) {
  response.send("Hello world!");
}
