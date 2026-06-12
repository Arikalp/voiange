import { ipcMain } from "electron";

export const registerIpcHandlers = () => {
  ipcMain.handle("app:ping", () => ({
    name: "VoiceAI Studio",
    status: "ok"
  }));
};
