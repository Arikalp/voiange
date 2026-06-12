import type { VoiceAiApi } from "../../../preload";

declare global {
  interface Window {
    voiceai: VoiceAiApi;
  }
}

export {};
