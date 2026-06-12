import { contextBridge, ipcRenderer } from "electron";

const api = {
  app: {
    ping: () => ipcRenderer.invoke("app:ping")
  }
};

contextBridge.exposeInMainWorld("voiceai", api);

export type VoiceAiApi = typeof api;
