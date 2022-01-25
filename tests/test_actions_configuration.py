"""This module tests the githubactions.create_actions_configuration module"""
import src.actions_configuration

def test_create_configuration_file():
    """Check that the configuration file is actually created"""
    src.actions_configuration.create_configuration_file('config.yml')
