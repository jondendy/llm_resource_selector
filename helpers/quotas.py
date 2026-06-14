"""
helpers/quotas.py - Quota and usage tracking for LLM Resource Selector plugin

Defines utility functions for reading current quota/usage for each provider/alias/model as defined in user config.
Supports static config limits, internal usage tracking, and (planned) live API header polling/reporting.
"""

def get_all_provider_status(plugin_config):
    """
    Returns a dict of provider status objects keyed by provider.
    Each object includes 'usable' (bool) and 'next' (dict: provider/alias/model to use),
    based on quota, errors, or fallback.
    """
    # TODO: Track live usage, failing requests, parse API responses for quota headers, errors, etc
    providers = plugin_config.get('providers', {})
    out = {}
    for provider, pdata in providers.items():
        aliases = pdata.get('aliases', [])
        for alias in aliases:
            # Placeholder: always return as usable
            for model in alias.get('models', []):
                # Placeholder: always pick first working combo
                out[provider] = {
                    'usable': True,
                    'next': {
                        'provider': provider,
                        'alias': alias.get('name'),
                        'model': model.get('id')
                    }
                }
                break
            else:
                continue
            break
    return out

# TODO: Implement API header polling, quota decrement on usage, error parsing