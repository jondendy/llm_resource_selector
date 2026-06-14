// llm-resource-selector-store.js
// Alpine store for LLM Resource Selector UI
import { createStore } from '/js/AlpineStore.js';
export const store = createStore('llmResourceSelectorStore', {
    config: {}, // Loaded from plugin config
    status: {}, // Provider status: quotas, errors, selection
    currentSelection: '',
    override: null,
    init() {
        // Called on store init
        this.refreshConfig();
        this.refreshRates();
    },
    onOpen() {
        this.init();
    },
    cleanup() {},
    refreshConfig() {
        // TODO: Load plugin config (YAML or JSON) into store
        // this.config = ...
    },
    refreshRates() {
        // TODO: Call backend (api/resource_api.py) to get live quota and recommendation
        // For now, mock some data
        this.status = {
            'groq': 'OK (498K tokens left)',
            'openrouter': 'Unknown (not configured)',
            'openai': 'OK ($14.37 credits)'
        };
        this.currentSelection = 'groq/AiderGithubVercel (llama-3.1-8b-instant)';
    },
    addAlias(providerIdx) {
        // Adds empty alias structure to provider
        const p = Object.values(this.config.providers)[providerIdx];
        p.aliases.push({ name: '', api_key: '', models: [] });
    },
    addModel(providerIdx, aliasIdx) {
        // Adds empty model structure to alias
        const p = Object.values(this.config.providers)[providerIdx];
        p.aliases[aliasIdx].models = p.aliases[aliasIdx].models || [];
        p.aliases[aliasIdx].models.push({ id: '', rpm: 0, rpd: 0, tpm: 0, tpd: 0, cost_per_1k: 0 });
    },
    overrideSelection() {
        // User-triggered selection override (makes override live)
        this.override = prompt('Enter provider/alias/model—e.g., groq/AiderGithubVercel/llama-3.1-8b-instant');
        if (this.override) {
            this.currentSelection = this.override + ' (manual override)';
        }
    }
});
