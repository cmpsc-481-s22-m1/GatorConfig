"""This module tests the githubactions.create_actions_configuration module"""
import githubactions.create_actions_configuration

def test_create_configuration_file():
    githubactions.create_actions_configuration.create_configuration_file('config.yml')