# LLM Resource Selector (Agent Zero community plugin)

Selects the lowest-cost, practical LLM (Groq, OpenRouter, OpenAI, etc.) for each inference based on live quotas, user-defined limits, and performance. Supports unlimited providers/models/keys/aliases. Plug-and-play policy, fully user-configurable.

## Features

- **Dynamically chooses** LLM for every call based on quota, rate, cost, and user preferences
- Supports **multiple providers** (Groq, OpenRouter, OpenAI, and more)
- Allows **user-defined aliases/keys/models**
- **Configurable quotas, costs, and fallback rules**
- Notifies when top-up or fallback is needed
- Provider-agnostic, community-ready, extensible for new APIs
- **Secure:** Never interact with or display raw API keys; all selection and configuration is by user-defined alias. Only the Agent Zero backend manages credentials.

## Example Use Cases
- Maximize free quota usage before paid APIs
- Prefer fast/cheap models but fall back to OpenAI if others are exhausted
- Use different OpenRouter or Groq aliases for specific projects/tasks

## Quick Setup
1. Copy or clone this plugin into `/a0/usr/plugins/llm_resource_selector/`
2. Open Agent Zero’s **Settings → Plugins → LLM Resource Selector**
3. Add/edit your API keys and alias, define quotas and preferences for your models/providers
4. Save and start using!

## Example Configuration (YAML/JSON)
~~~yaml
providers:
  groq:
    aliases:
      - name: AiderGithubVercel
        api_key: <your_groq_api_key>
        models:
          - id: allam-2-7b
            rpm: 30
            rpd: 7000
            tpm: 6000
            tpd: 500000
            cost_per_1k: 0           # if known
          - id: llama-3.1-8b-instant
            rpm: 30
            rpd: 14400
            tpm: 6000
            tpd: 500000
  openrouter:
    aliases:
      - name: AiderCode
        api_key: <your_openrouter_key>
        # Add models/limits as needed
  openai:
    aliases:
      - name: MainOpenAI
        api_key: <your_openai_key>
        monthly_limit_usd: 15
        fallback_only: true

policy:
  preference: [groq, openrouter, openai]
  notify_at_percent: 10   # when any provider/alias quota drops under 10%
  auto_fallback: true     # if true, next provider used automatically
  logging_mode: true      # if true, log model/usage even if quotas unknown
~~~

## User Notes
- Every user's config will differ! Add as many providers, aliases, and models as you want.
- For quota/costs you don’t know, leave blank—the plugin will log observed usage.
- Fallback happens automatically by default when quota is low or exceeded.

For more schema detail and advanced use, see `default_config.yaml` and plugin settings in the UI.

---
## Files & Extensibility
- `plugin.yaml`   – Manifest
- `README.md`     – This file
- `LICENSE`       – OSI-approved license (default: MIT)
- `tools/llm_router.py` – Core selector logic
- `helpers/quotas.py`  – API pollers and live usage tracking
- `webui/config.html` – Plugin settings UI
- `default_config.yaml` – Sample config schema

---
## Community and Support
Submit issues, PRs, and suggestions via the Agent Zero Plugin Hub or GitHub. See Plugin Index instructions for community publishing.
