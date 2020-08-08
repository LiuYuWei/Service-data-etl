"""This file is used in health check information."""

# import relation package.

# import project package.
from config.config_setting import ConfigSetting


class HealthCheckInformation:
    """This class is used in setting config."""

    def __init__(self):
        """Initial some variable and module"""
        config_setting = ConfigSetting()
        self.log = config_setting.set_logger("[health_check_information]")

    def get_health_check_content(self):
        """health_check_content: combine the health check content into json.
        Returns:
            json format: the health check content.
        """
        with open('setup.py', 'r') as f:
            setup_str = f.read()
        # Get version string
        version_str = self.parse_position(setup_str, 'project_version=')
        # Get project string
        project_str = self.parse_position(setup_str, 'project_name=')
        self.log.info("Service_name: {}, Service_version: {}".format(project_str, version_str))
        return {'service': project_str, 'status': '200', 'version': version_str}

    @staticmethod
    def parse_position(setup_str, pos_string):
        """parse_position: Parse position
        Arguments:
            setup_str: the string that need to be parsed.
            pos_string: the string that the need to find.
        Returns:
            answer of parse position string.
        """
        start_project_pos = setup_str.find(pos_string) + len(pos_string)
        end_project_pos = setup_str.find(',', start_project_pos)
        return setup_str[start_project_pos:end_project_pos].replace("'", '')
