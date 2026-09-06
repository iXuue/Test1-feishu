import { describe, expect, it } from "vitest";
import {
  apiKeyFromProjectEnv,
  parseProjectEnvText,
  providerSettingsFromProjectEnv,
  updateProjectEnvText,
} from "../electron/projectEnv";
import type { ProviderSettings } from "../electron/ipcTypes";

const fallbackProvider: ProviderSettings = {
  provider: "deepseek",
  model: "deepseek-v4-flash",
  baseUrl: "https://api.deepseek.com",
  host: "http://127.0.0.1:11434",
  credential: { configured: true, source: "global-file", displayHint: "saved" },
};

describe("legacy project env helpers", () => {
  it("resolves the project .env as the active OpenAI-compatible provider", () => {
    const values = {
      CODECUB_PROVIDER: "openai",
      OPENAI_API_BASE: "https://llm.example.aliyuncs.com/compatible-mode/v1",
      OPENAI_API_KEY: "aliyun-test-key",
      OPENAI_MODEL: "qwen3.7-flash",
    };

    const settings = providerSettingsFromProjectEnv(values, fallbackProvider);

    expect(settings).toMatchObject({
      provider: "openai",
      model: "qwen3.7-flash",
      baseUrl: "https://llm.example.aliyuncs.com/compatible-mode/v1",
      credential: { configured: true, source: "project-env", displayHint: "OPENAI_API_KEY" },
    });
    expect(apiKeyFromProjectEnv(values, settings.provider)).toBe("aliyun-test-key");
  });

  it("parses quoted values without exposing project env as active model settings", () => {
    const original = [
      "# existing config",
      'OPENAI_API_KEY="sk old # keep"',
      "OTHER_VALUE=preserve-me",
      "",
    ].join("\n");

    expect(parseProjectEnvText(original)).toEqual({
      OPENAI_API_KEY: "sk old # keep",
      OTHER_VALUE: "preserve-me",
    });
  });

  it("can update env text for legacy maintenance without being used by the settings UI", () => {
    const original = [
      "# existing config",
      'OPENAI_API_KEY="sk old # keep"',
      "OTHER_VALUE=preserve-me",
      "",
    ].join("\n");

    const updated = updateProjectEnvText(original, {
      CODECUB_PROVIDER: "openai",
      OPENAI_MODEL: "qwen flash",
      OPENAI_API_KEY: null,
    });

    expect(updated).toContain("# existing config");
    expect(updated).toContain("OTHER_VALUE=preserve-me");
    expect(updated).toContain('OPENAI_MODEL="qwen flash"');
    expect(updated).toContain("CODECUB_PROVIDER=openai");
    expect(updated).not.toContain("OPENAI_API_KEY");
  });
});
