# Creates a macOS Installer
from pathlib import Path
import plistlib
import subprocess
from resources import utilities

def list_local_macOS_installers():
    # Finds all applicable macOS installers
    # within a user's /Applications folder
    # Returns a list of installers
    application_list = {}

    for application in Path("/Applications").iterdir():
        # Verify whether application has createinstallmedia
        if (Path("/Applications") / Path(application) / Path("Contents/Resources/createinstallmedia")).exists():
            plist = plistlib.load((Path("/Applications") / Path(application) / Path("Contents/Info.plist")).open("rb"))
            try:
                # Doesn't reflect true OS build, but best to report SDK in the event multiple installers are found with same version
                app_version = plist["DTPlatformVersion"]
                clean_name = plist["CFBundleDisplayName"]
                try:
                    app_sdk = plist["DTSDKBuild"]
                except KeyError:
                    app_sdk = "Unknown"
                application_list.update({
                    application: {
                        "Short Name": clean_name,
                        "Version": app_version,
                        "Build": app_sdk,
                        "Path": application,
                    }
                })
            except KeyError:
                pass
    return application_list

def create_installer(installer_path, volume_name):
    # Creates a macOS installer
    # Takes a path to the installer and the Volume
    # Returns boolean on success status

    createinstallmedia_path = Path("/Applications") / Path(installer_path) / Path("Contents/Resources/createinstallmedia")

    # Sanity check in the event the user somehow deleted it between the time we found it and now
    if (createinstallmedia_path).exists():
        utilities.cls()
        utilities.header(["Starting createinstallmedia"])
        print("This will take some time, recommend making some coffee while you wait\n")
        utilities.elevated([createinstallmedia_path, "--volume", f"/Volumes/{volume_name}", "--nointeraction"])
        return True
    else:
        print("- Failed to find createinstallmedia")
    return False

def download_install_assistant(download_path, ia_link):
    # Downloads and unpackages InstallAssistant.pkg into /Applications
    utilities.download_file(ia_link, (Path(download_path) / Path("InstallAssistant.pkg")))
    print("- Installing InstallAssistant.pkg to /Applications/")
    utilities.elevated(["installer", "-pkg", (Path(download_path) / Path("InstallAssistant.pkg")), "-target", "/Applications"])
    input("- Press ENTER to continue: ")

def list_downloadable_macOS_installers(download_path, catalog):
    avalible_apps = {}
    if catalog == "DeveloperSeed":
        link = "https://swscan.apple.com/content/catalogs/others/index-12seed-12-10.16-10.15-10.14-10.13-10.12-10.11-10.10-10.9-mountainlion-lion-snowleopard-leopard.merged-1.sucatalog.gz"
    elif catalog == "PublicSeed":
        link = "https://swscan.apple.com/content/catalogs/others/index-12beta-12-10.16-10.15-10.14-10.13-10.12-10.11-10.10-10.9-mountainlion-lion-snowleopard-leopard.merged-1.sucatalog.gz"
    else:
        link = "https://swscan.apple.com/content/catalogs/others/index-12customerseed-12-10.16-10.15-10.14-10.13-10.12-10.11-10.10-10.9-mountainlion-lion-snowleopard-leopard.merged-1.sucatalog.gz"
    
    # Download and unzip the catalog
    utilities.download_file(link, (Path(download_path) / Path("seed.sucatalog.gz")))
    subprocess.run(["gunzip", "-d", "-f", Path(download_path) / Path("seed.sucatalog.gz")])
    catalog_plist = plistlib.load((Path(download_path) / Path("seed.sucatalog")).open("rb"))

    for item in catalog_plist["Products"]:
        try:
            # Check if entry has SharedSupport and BuildManifest
            # Ensures only Big Sur and newer Installers are listed
            catalog_plist["Products"][item]["ExtendedMetaInfo"]["InstallAssistantPackageIdentifiers"]["SharedSupport"]
            catalog_plist["Products"][item]["ExtendedMetaInfo"]["InstallAssistantPackageIdentifiers"]["BuildManifest"]

            for bm_package in catalog_plist["Products"][item]["Packages"]:
                if "BuildManifest.plist" in bm_package["URL"]:
                    utilities.download_file(bm_package["URL"], (Path(download_path) / Path("BuildManifest.plist")))
                    build_plist = plistlib.load((Path(download_path) / Path("BuildManifest.plist")).open("rb"))
                    version = build_plist["ProductVersion"]
                    build = build_plist["ProductBuildVersion"]
                    for ia_package in catalog_plist["Products"][item]["Packages"]:
                        if "InstallAssistant.pkg" in ia_package["URL"]:
                            download_link = ia_package["URL"]
                            size = ia_package["Size"]
                            integrity = ia_package["IntegrityDataURL"]

                    avalible_apps.update({
                        item: {
                            "Version": version,
                            "Build": build,
                            "Link": download_link,
                            "Size": size,
                            "integrity": integrity,
                            "Source": "Apple Inc.",
                        }
                    })
        except KeyError:
            pass
    return avalible_apps

def format_drive(disk_id):
    # Formats a disk for macOS install
    # Takes a disk ID
    # Returns boolean on success status
    header = f"# Formatting disk{disk_id} for macOS installer #"
    box_length = len(header)
    utilities.cls()
    print("#" * box_length)
    print(header)
    print("#" * box_length)
    print("")
    #print(f"- Formatting disk{disk_id} for macOS installer")
    format_process = utilities.elevated(["diskutil", "eraseDisk", "HFS+", "OCLP-Installer", f"disk{disk_id}"])
    if format_process.returncode == 0:
        print("- Disk formatted")
        return True
    else:
        print("- Failed to format disk")
        print(f"  Error Code: {format_process.returncode}")
        input("\nPress Enter to exit")
        return False

def select_disk_to_format():
    utilities.cls()
    utilities.header(["Installing OpenCore to Drive"])

    print("\nDisk picker is loading...")

    all_disks = {}
    # TODO: AllDisksAndPartitions is not supported in Snow Leopard and older
    try:
        # High Sierra and newer
        disks = plistlib.loads(subprocess.run("diskutil list -plist physical".split(), stdout=subprocess.PIPE).stdout.decode().strip().encode())
    except ValueError:
        # Sierra and older
        disks = plistlib.loads(subprocess.run("diskutil list -plist".split(), stdout=subprocess.PIPE).stdout.decode().strip().encode())
    for disk in disks["AllDisksAndPartitions"]:
        disk_info = plistlib.loads(subprocess.run(f"diskutil info -plist {disk['DeviceIdentifier']}".split(), stdout=subprocess.PIPE).stdout.decode().strip().encode())
        try:
            all_disks[disk["DeviceIdentifier"]] = {"identifier": disk_info["DeviceNode"], "name": disk_info["MediaName"], "size": disk_info["TotalSize"], "removable": disk_info["Internal"], "partitions": {}}
        except KeyError:
            # Avoid crashing with CDs installed
            continue
    menu = utilities.TUIMenu(
        ["Select Disk to write the macOS Installer onto"],
        "Please select the disk you would like to install OpenCore to: ",
        in_between=["Missing drives? Verify they are 14GB+ and external (ie. USB)", "", "Ensure all data is backed up on selected drive, entire drive will be erased!"],
        return_number_instead_of_direct_call=True,
        loop=True,
    )
    for disk in all_disks:
        # Strip disks that are under 14GB (15,032,385,536 bytes)
        # createinstallmedia isn't great at detecting if a disk has enough space
        if not any(all_disks[disk]['size'] > 15032385536 for partition in all_disks[disk]):
            continue
        # Strip internal disks as well (avoid user formatting their SSD/HDD)
        # Ensure user doesn't format their boot drive
        if not any(all_disks[disk]['removable'] is False for partition in all_disks[disk]):
            continue
        menu.add_menu_option(f"{disk}: {all_disks[disk]['name']} ({utilities.human_fmt(all_disks[disk]['size'])})", key=disk[4:])

    response = menu.start()

    if response == -1:
        return None
    
    return response