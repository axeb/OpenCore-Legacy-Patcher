#!/usr/bin/env python3
# Copyright (C) 2020-2021, Dhinak G, Mykola Grymalyuk

from __future__ import print_function

import subprocess
import sys
from pathlib import Path

from resources import build, cli_menu, constants, utilities, device_probe, os_probe, defaults, arguments, install
from data import model_array


class OpenCoreLegacyPatcher:
    def __init__(self):
        print("- Loading...")
        self.constants = constants.Constants()
        self.generate_base_data()
        if utilities.check_cli_args() is None:
            self.main_menu()

    def generate_base_data(self):
        self.constants.detected_os = os_probe.detect_kernel_major()
        self.constants.detected_os_minor = os_probe.detect_kernel_minor()
        self.constants.detected_os_build = os_probe.detect_kernel_build()
        self.constants.computer = device_probe.Computer.probe()
        self.constants.recovery_status = utilities.check_recovery()
        self.computer = self.constants.computer
        defaults.generate_defaults.probe(self.computer.real_model, True, self.constants)
        if utilities.check_cli_args() is not None:
            print("- Detected arguments, switching to CLI mode")
            self.constants.gui_mode = True  # Assumes no user interaction is required
            self.constants.current_path = Path.cwd()
            if getattr(sys, "frozen", False) and hasattr(sys, "_MEIPASS"):
                print("- Rerouting payloads location")
                self.constants.payload_path = sys._MEIPASS / Path("payloads")
            arguments.arguments().parse_arguments(self.constants)
        else:
            print("- No arguments present, loading TUI")

    def main_menu(self):
        response = None
        while not (response and response == -1):
            title = [
                f"OpenCore Legacy Patcher v{self.constants.patcher_version}",
                f"Selected Model: {self.constants.custom_model or self.computer.real_model}",
            ]

            if (self.constants.custom_model or self.computer.real_model) not in model_array.SupportedSMBIOS and self.constants.allow_oc_everywhere is False:
                in_between = [
                    "Your model is not supported by this patcher for running unsupported OSes!",
                    "",
                    'If you plan to create the USB for another machine, please select the \n"Change Model" option in the menu.',
                    "",
                    'If you want to run OCLP on a native Mac, please toggle \n"Allow OpenCore on native Models" in settings',
                ]
            elif not self.constants.custom_model and self.computer.real_model == "iMac7,1" and "SSE4.1" not in self.computer.cpu.flags:
                in_between = [
                    "Your model requires a CPU upgrade to a CPU supporting SSE4.1+ to be supported by this patcher!",
                    "",
                    f'If you plan to create the USB for another {self.computer.real_model} with SSE4.1+, please select the "Change Model" option in the menu.',
                ]
            elif self.constants.custom_model == "iMac7,1":
                in_between = ["This model is supported", "However please ensure the CPU has been upgraded to support SSE4.1+"]
            else:
                in_between = ["This model is supported"]

            menu = utilities.TUIMenu(title, "Please select an option: ", in_between=in_between, auto_number=True, top_level=True)

            options = (
                [["Build OpenCore", build.BuildOpenCore(self.constants.custom_model or self.constants.computer.real_model, self.constants).build_opencore]]
                if ((self.constants.custom_model or self.computer.real_model) in model_array.SupportedSMBIOS) or self.constants.allow_oc_everywhere is True
                else []
            ) + [
                ["Install OpenCore to USB/internal drive", install.tui_disk_installation(self.constants).copy_efi],
                ["Post-Install Volume Patch", cli_menu.MenuOptions(self.constants.custom_model or self.computer.real_model, self.constants).PatchVolume],
                ["Change Model", cli_menu.MenuOptions(self.constants.custom_model or self.computer.real_model, self.constants).change_model],
                ["Patcher Settings", cli_menu.MenuOptions(self.constants.custom_model or self.computer.real_model, self.constants).patcher_settings],
                ["Installer Creation", cli_menu.MenuOptions(self.constants.custom_model or self.computer.real_model, self.constants).download_macOS],
                ["Credits", cli_menu.MenuOptions(self.constants.custom_model or self.computer.real_model, self.constants).credits],
            ]

            for option in options:
                menu.add_menu_option(option[0], function=option[1])

            response = menu.start()

        if getattr(sys, "frozen", False) and self.constants.recovery_status is False:
            subprocess.run("""osascript -e 'tell application "Terminal" to close first window' & exit""", shell=True)


OpenCoreLegacyPatcher()
