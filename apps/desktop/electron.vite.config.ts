import { defineConfig } from "electron-vite";
import react from "@vitejs/plugin-react";
import path from "node:path";

export default defineConfig({
  main: {
    build: {
      outDir: "dist/main"
    },
    resolve: {
      alias: {
        "@main": path.resolve(__dirname, "src/main")
      }
    }
  },
  preload: {
    build: {
      outDir: "dist/preload"
    },
    resolve: {
      alias: {
        "@preload": path.resolve(__dirname, "src/preload")
      }
    }
  },
  renderer: {
    root: "src/renderer",
    resolve: {
      alias: {
        "@": path.resolve(__dirname, "src/renderer/src")
      }
    },
    plugins: [react()]
  }
});
