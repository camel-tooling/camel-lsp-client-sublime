import os
import sublime
 
from urllib.request import urlretrieve
 
from LSP.plugin import (
    AbstractPlugin,
    register_plugin,
    filename_to_uri,
    unregister_plugin,
)
 
 
SERVER_URL = "https://repo1.maven.org/maven2/com/github/camel-tooling/camel-lsp-server/1.6.0/camel-lsp-server-1.6.0.jar"
 
def plugin_loaded():
    '''
    This is the beginning point for LSP-camel.plugin.
    All the debug information can be seen in Menu -> View -> Show Console
    '''
    register_plugin(CamelLSPlugin)
 
 
def plugin_unloaded():
    '''
    This is the end point for LSP-camel.plugin.
    '''
    unregister_plugin(CamelLSPlugin)
 
 
class CamelLSPlugin(AbstractPlugin):
    '''
    A plugin to activate camells on java and xml files
 
    '''
 
    settings = None
    settings_name = "LSP-camel.sublime-settings"
    settings_resource_path = "Packages/{}/{}".format(__package__, settings_name)
 
    @classmethod
    def name(cls):
        '''
        A human-friendly name.
        If your plugin is called "LSP-foobar", then this should return "foobar".
        '''
        return globals()['__package__']     # Return package name, which is LSP-camel
 
    @classmethod
    def configuration(cls):
        '''
        Return the Settings object that defines the "command", "languages" as first element in the tuple, and
        path to the base settings filename as the second element in the tuple.
        '''
        if cls.settings is None:
            cls.settings = sublime.load_settings(cls.settings_name)
        return (cls.settings, cls.settings_resource_path)
 
    @classmethod
    def needs_update_or_installation(cls, ):
        '''
        This is the place to check whether the binary needs an update, or
        whether it needs to be installed before starting the language server.
        '''
        if not os.path.isfile(cls.server_jar()):
            return True
       
        return False
 
 
    @classmethod
    def install_or_update(cls):
        '''
        Do the actual update/installation of the camells jar file
        '''
        server_dir = cls.server_dir()
        server_jar = cls.server_jar()
 
        # download new server binary
        os.makedirs(server_dir, exist_ok=True)
        urlretrieve(url=SERVER_URL, filename=server_jar)
 
    @classmethod
    def on_pre_start(cls, window, initiating_view, workspace_folders, configuration):
        '''
        This is the place to do last-minute adjustments to your "command" or "init_options" in the passed-in "configuration" argument
        '''
        configuration.command = [
            "java", "-jar", cls.server_jar()
        ]
 
 
    @classmethod
    def additional_variables(cls):
        return {
            "package_path": cls.package_dir(),
            "storage_path": cls.server_dir(),
            "package_uri": cls.package_uri(),
            "storage_uri": cls.server_uri()
        }
 
    # internal methods
 
    @classmethod
    def package_dir(cls):
        return os.path.join(sublime.packages_path(), __package__)
 
    @classmethod
    def package_uri(cls):
        return filename_to_uri(cls.package_dir())
 
    @classmethod
    def server_dir(cls):
        return os.path.join(cls.storage_path(), __package__)
 
    @classmethod
    def server_uri(cls):
        return filename_to_uri(cls.server_dir())
 
    @classmethod
    def server_jar(cls):
        return os.path.join(cls.server_dir(), SERVER_URL.rsplit("/", 1)[1])

