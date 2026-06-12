import type { Config } from "tailwindcss";

export default {
  content: ["./src/renderer/index.html", "./src/renderer/src/**/*.{ts,tsx}"],
  theme: {
    extend: {
      colors: {
        ink: "#0f172a",
        mist: "#e2e8f0",
        signal: "#0f766e",
        panel: "#f8fafc"
      }
    }
  },
  plugins: []
} satisfies Config;
