# coding=utf-8

from __future__ import absolute_import, unicode_literals
import octoprint.plugin


class HERCULES_TempFix(octoprint.plugin.OctoPrintPlugin):
    # Recv:   T:95.75 B:63.55 @:0 T0:95.75 @0:0 T1:55.54 @1:0
    # Recv:   EX1:22.1 /0.0 @0 EX2:22.2 /0.0 @0 B:22.9 /0.0 @0


    def check_for_temp_report(self, comm_instance, line, *args, **kwargs):
        # Check to see if we received the broken temperature response and if so extract temperature for octoprint
        if "EX1" not in line:
            return line
        
        self._logger.info("Original: {}".format(line))

        line = line.replace("EX1", "T0");
        line = line.replace("EX2", "T1");

        self._logger.info("Modified: {}".format(line))
        return line

    def get_update_information(self, *args, **kwargs):
        return dict(
            hercules_temp_fix=dict(
                displayName=self._plugin_name,
                displayVersion=self._plugin_version,

                type="github_release",
                current=self._plugin_version,
                user="MrBoriska",
                repo="OctoPrint-Hercules-Temp-Fix",

                pip="https://github.com/MrBoriska/OctoPrint-Hercules-Temp-Fix/archive/{target_version}.zip"
            )
        )


__plugin_pythoncompat__ = ">=2.7,<4"


def __plugin_load__():
    global __plugin_implementation__
    __plugin_implementation__ = HERCULES_TempFix()

    global __plugin_hooks__
    __plugin_hooks__ = {
        "octoprint.comm.protocol.gcode.received": (__plugin_implementation__.check_for_temp_report, 1),
        "octoprint.plugin.softwareupdate.check_config": __plugin_implementation__.get_update_information
    }
