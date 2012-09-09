#!/usr/bin/env python
import ConfigParser
    
class ConfigInfo:
    def __init__(self, config_file):
        self.config_file = config_file
        self.config = ConfigParser.RawConfigParser()
        self.config.read(self.config_file)
        self.commands = self.config.items('Commands')
        if self.has_settings('Settings'):
            self.settings = self.config.items('Settings')
    def has_settings(self, section):
        return self.config.has_section(section)
    def set_settings(self, section, key, value):
        self.config.set(section, key, value)
        with open(self.config_file, 'wb') as configfile:
            self.config.write(configfile)
    def add_settings(self, section):
        self.config.add_section(section)
    def remove_keyword(self, keyword):
        if self.config.has_option('Commands', keyword):
            self.config.remove_option('Commands', keyword)
            with open(self.config_file, 'wb') as configfile:
                self.config.write(configfile)
            return True
        else:
            return False
    def keyword_exists(self, section, keyword):
        if self.config.has_option(section, keyword):
            return True
        return False   
    def remove_settings(self):
        if self.config.has_section('Settings'):
            self.config.remove_section('Settings')
            with open(self.config_file, 'wb') as configfile:
                self.config.write(configfile)
            return True
        else:
            return False

        
            
    
    
