"""
API handler for live quota/status polling from webui/llm_resource_selector store.
Called by front-end Refresh Rates button to return status for all configured providers/models.
Future: fills rates by direct API requests and header parsing; now uses helpers/quotas.py for placeholder responses.
"""
from usr.plugins.llm_resource_selector.helpers.quotas import get_all_provider_status

def handle_api_rates(request, plugin_config):
    """
    Returns JSON with current provider/model quota/status info for UI.
    Stub: returns static/demo data from helpers.
    """
    # In production: plugin_config passed from Agent Zero context
    status = get_all_provider_status(plugin_config)
    # Optionally add debug/example message for demo
    return {
        'ok': True,
        'status': status,
        'msg': 'Live quota polling not yet implemented—using stubbed values.'
    }
