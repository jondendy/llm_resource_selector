"""
LLM Resource Selector: Core logic for picking the optimal LLM backend at runtime.

Loads config, checks provider quotas/status, returns the most cost-effective working provider as configured.
Supports arbitrary user policy/priorities. Exports main decision function for framework/agent/plugin use.
"""
import random
from usr.plugins.llm_resource_selector.helpers.quotas import get_all_provider_status


def select_llm_backend(plugin_config=None):
    """
    Main entrypoint. Given current plugin config (or loads default),
    returns a dict: { 'provider': ..., 'alias': ..., 'model': ... }
    representing the next viable choice. Raises if none available.
    """
    if plugin_config is None:
        # TODO: load plugin config from system using appropriate plugin context
        plugin_config = {}

    # Example: random fallback
    providers = plugin_config.get("providers", {})
    policy = plugin_config.get("policy", {})
    pref_order = policy.get("preference", list(providers.keys()))
    provider_status = get_all_provider_status(plugin_config)

    for p in pref_order:
        prov = provider_status.get(p)
        if prov and prov.get('usable'):
            return prov['next']
    raise RuntimeError("No suitable LLM backend available. Top up, adjust preferences, or check quotas.")

# Example usage
# choice = select_llm_backend(<config dict>)
# returns: {'provider': 'groq', 'alias': 'AiderGithubVercel', 'model': 'llama-3.1-8b-instant'}
