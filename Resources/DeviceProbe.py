# Probe devices, return device entries
# Copyright (C) 2021 Mykola Grymalyuk
from __future__ import print_function

import binascii
import plistlib
import subprocess

from Resources import Constants, Utilities

class pci_probe:
    def __init__(self):
        self.constants = Constants.Constants()

    # Converts given device IDs to DeviceProperty pathing, requires ACPI pathing as DeviceProperties shouldn't be used otherwise
    def deviceproperty_probe(self, vendor_id, device_id, acpi_path):
        gfxutil_output: str = subprocess.run([self.constants.gfxutil_path] + f"-v".split(), stdout=subprocess.PIPE, stderr=subprocess.STDOUT).stdout.decode()
        try:
            if acpi_path == "":
                acpi_path = "No ACPI Path Given"
                raise IndexError
            device_path = [line.strip().split("= ", 1)[1] for line in gfxutil_output.split("\n") if f'{vendor_id}:{device_id}'.lower() in line.strip() and acpi_path in line.strip()][0]
            return device_path
        except IndexError:
            print(f"- No DevicePath found for {vendor_id}:{device_id} ({acpi_path})")
            return ""

    # Returns the device path of parent controller
    def device_property_parent(self, device_path):
        device_path_parent = "/".join(device_path.split("/")[:-1])
        return device_path_parent

    def acpi_strip(self, acpi_path_full):
        # Strip IOACPIPlane:/_SB, remove 000's, convert ffff into 0 and finally make everything upper case
        # IOReg                                      | gfxutil
        # IOACPIPlane:/_SB/PC00@0/DMI0@0             -> /PC00@0/DMI0@0
        # IOACPIPlane:/_SB/PC03@0/BR3A@0/SL09@ffff   -> /PC03@0/BR3A@0/SL09@0
        # IOACPIPlane:/_SB/PC03@0/M2U0@150000        -> /PC03@0/M2U0@15
        # IOACPIPlane:/_SB/PC01@0/CHA6@100000        -> /PC01@0/CHA6@10
        # IOACPIPlane:/_SB/PC00@0/RP09@1d0000/PXSX@0 -> /PC00@0/RP09@1D/PXSX@0
        # IOACPIPlane:/_SB/PCI0@0/P0P2@10000         -> /PCI0@0/P0P2@1
        acpi_path = acpi_path_full.replace("IOACPIPlane:/_SB", "")
        acpi_path = acpi_path.replace("0000", "")
        for entry in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"]:
            acpi_path = acpi_path.replace(f"000{entry}", f",{entry}")
        acpi_path = acpi_path.replace("ffff", "0")
        acpi_path = acpi_path.upper()
        return acpi_path

    # Note gpu_probe should only be used on IGPU and GFX0 entries
    def gpu_probe(self, gpu_type):
        try:
            devices = plistlib.loads(subprocess.run(f"ioreg -r -n {gpu_type} -a".split(), stdout=subprocess.PIPE).stdout.decode().strip().encode())
            vendor_id = Utilities.hexswap(binascii.hexlify(devices[0]["vendor-id"]).decode()[:4])
            device_id = Utilities.hexswap(binascii.hexlify(devices[0]["device-id"]).decode()[:4])
            try:
                acpi_path = devices[0]["acpi-path"]
                acpi_path = self.acpi_strip(acpi_path)
                return vendor_id, device_id, acpi_path
            except KeyError:
                print(f"- No ACPI entry found for {gpu_type}")
                return vendor_id, device_id, ""
        except ValueError:
            print(f"- No IOService entry found for {gpu_type} (V)")
            return "", "", ""
        except IndexError:
            print(f"- No IOService entry found for {gpu_type} (I)")
            return "", "", ""

    def wifi_probe(self):
        devices = plistlib.loads(subprocess.run("ioreg -c IOPCIDevice -r -d2 -a".split(), stdout=subprocess.PIPE).stdout.decode().strip().encode())
        try:
            devices = [i for i in devices if i["class-code"] == binascii.unhexlify(self.constants.classcode_wifi)]
            vendor_id = Utilities.hexswap(binascii.hexlify(devices[0]["vendor-id"]).decode()[:4])
            device_id = Utilities.hexswap(binascii.hexlify(devices[0]["device-id"]).decode()[:4])
            ioname = devices[0]["IOName"]
            try:
                acpi_path = devices[0]["acpi-path"]
                acpi_path = self.acpi_strip(acpi_path)
                return vendor_id, device_id, ioname, acpi_path
            except KeyError:
                print(f"- No ACPI entry found for {vendor_id}:{device_id}")
                return vendor_id, device_id, ioname, ""
        except ValueError:
            print(f"- No IOService entry found for Wireless Card (V)")
            return "", "", "", ""
        except IndexError:
            print(f"- No IOService entry found for Wireless Card (I)")
            return "", "", "", ""

    def cpu_feature(self, instruction):
        cpu_features = subprocess.run("sysctl machdep.cpu.features".split(), stdout=subprocess.PIPE).stdout.decode().partition(": ")[2].strip().split(" ")
        if instruction in cpu_features:
            print(f"- Found {instruction} support")
            return True
        else:
            print(f"- Failed to find {instruction} support")
            return False

class smbios_probe:
    def model_detect(self, custom):
        opencore_model: str = subprocess.run("nvram 4D1FDA02-38C7-4A6A-9CC6-4BCCA8B30102:oem-product".split(), stdout=subprocess.PIPE, stderr=subprocess.STDOUT).stdout.decode()
        if not opencore_model.startswith("nvram: Error getting variable") and custom is False:
            current_model = [line.strip().split(":oem-product	", 1)[1] for line in opencore_model.split("\n") if line.strip().startswith("4D1FDA02-38C7-4A6A-9CC6-4BCCA8B30102:")][0]
        else:
            current_model = plistlib.loads(subprocess.run("system_profiler -detailLevel mini -xml SPHardwareDataType".split(), stdout=subprocess.PIPE, stderr=subprocess.STDOUT).stdout.strip())[0]["_items"][0]["machine_model"]
        return current_model

    def board_detect(self, custom):
        opencore_model: str = subprocess.run("nvram 4D1FDA02-38C7-4A6A-9CC6-4BCCA8B30102:oem-board".split(), stdout=subprocess.PIPE, stderr=subprocess.STDOUT).stdout.decode()
        if not opencore_model.startswith("nvram: Error getting variable") and custom is False:
            current_model = [line.strip().split(":oem-board	", 1)[1] for line in opencore_model.split("\n") if line.strip().startswith("4D1FDA02-38C7-4A6A-9CC6-4BCCA8B30102:")][0]
        else:
            current_model = plistlib.loads(subprocess.run(f"ioreg -p IODeviceTree -r -n / -a".split(), stdout=subprocess.PIPE).stdout.decode().strip().encode())
            current_model = current_model[0]["board-id"]
        return current_model