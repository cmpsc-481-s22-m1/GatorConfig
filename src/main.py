"""This module generates the configuration files needed to automate GatorGradle"""
from src import actions_configuration
from src import gator_config

def main():
    """Generate the configuration files based on command line input"""
    gator_config.cli()
    actions_configuration.create_configuration_file('../.github/workflows/grade.yml')

if __name__ == "__main__":
    main()
