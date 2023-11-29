"""
"""
import os

from pluginbase import PluginBase

package = 'vortex.plugins'
path = os.path.abspath(os.path.dirname(__file__))

plugin_base = PluginBase(package=package)
plugin_source = plugin_base.make_plugin_source(searchpath=[path])


def setup_plugins(engine, settings):
    for name in plugin_source.list_plugins():
        if name in settings.plugins:
            plugin_settings = settings.plugins[name]
            plugin = plugin_source.load_plugin(name).create(plugin_settings)
            # Signals: components -> plugin
            for component, signals in plugin.config.signals.items():
                for signal in signals:
                    getattr(getattr(engine, component), signal).bind(getattr(plugin, 'handle_' + signal))
            # Signals: plugin -> agent
            for signal in plugin_settings.get('signals'):
                getattr(plugin, signal).bind(getattr(engine.agent, 'handle_' + signal))
