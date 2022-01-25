import actions_configuration
import gator_config

def main():
    gator_config.cli()
    actions_configuration.create_configuration_file('../.github/workflows/grade.yml')

if __name__ == "__main__":
    main()