"""
This file contains all of the error messages
"""

from colorama import init, Fore, Style
init(autoreset=True, convert=True)

def env_not_found_error(name):
    """the error display for environments not being found"""
    return(f"{Fore.RED}environment {name} not found")


def notebook_load_error(name):
    print(f"\t{Fore.RED}there is something wrong with {name}. mtool will still load it, but it might not run.{Style.RESET_ALL}")


def scene_not_found_error(name):
    """the error display for scenes not existing"""
    if name == None:
        return(f"{Fore.RED}scene does not exist")
    else:
        return(f"{Fore.RED}scene {name} does not exist")


def notebook_not_found_error(name):
    """the error display for notebooks not existing"""
    if name == None:
        return(f"{Fore.RED}notebook does not exist")
    else:
        return(f"{Fore.RED}notebook {name} does not exist")

def ruleset_not_found_error(name):
    """the error display for a ruleset not existing"""
    if name == None:
        return(f"{Fore.RED}ruleset does not exist")
    else:
        return(f"{Fore.RED}ruleset {name} does not exist")

def ruleset_active_error(name):
    """the error display for activating an active ruleset"""
    if name == None:
        return(f"{Fore.RED}ruleset is already active")
    else:
        return(f"{Fore.RED}ruleset {name} is already active")

def ruleset_not_active_error(name):
    """the error display for deactivating an inactive ruleset"""
    if name == None:
        return(f"{Fore.RED}ruleset is already inactive")
    else:
        return(f"{Fore.RED}ruleset {name} is already inactive")

def end_ended_scene_error(name):
    return(f"{Fore.RED}{name} is already ended.")


def library_not_found_error(name):
    return(f"{Fore.RED}Library {name} does not exist or is not loaded.")


def version_error():
    import sys
    return("mtool requires python 3.6. Your version is " + str(sys.version_info.major)+ "." + str(sys.version_info.minor), "which is incompatable. Please update python.")


def last_active_scene_error(name):
    """the error display for trying to end the last active scene"""
    return(f"{Fore.RED}{name} is your last active scene. Make a new scene, or resume an old one.")


def scene_ended_error(name):
    """the error display for trying to switch to an ended scene"""
    return(f"{Fore.RED}can't switch to {name}, because the scene has ended. Resume the scene or make a new one.")
    

def papermill_error(error):
        """the error display for papermill errors"""
        print(f"{Fore.RED}PAPERMILL ERROR")
        print(error)

def no_tagged_cell_warning():
    """the warning display for having no tagged cell"""
    print(f"{Fore.YELLOW}Warning: no tagged cell located. No parameters will be injected for this notebook.")


def settings_invalid_ordinal(userIn):
    """the error display for bad ordinal input"""
    print(f"{Fore.RED}Bad input: {userIn} is not an ordinal in the list. Please try again.")


def telem_off_warning():
    """the warning display for telemetry being off"""
    print(f"{Fore.YELLOW}Warning: telemetry is disabled. Turn it on in the settings utility (m u)")


def telem_not_init_warning():
    """the warning display for uninitialized telemetry"""
    print(f"{Fore.YELLOW}Warning: telemetry is not set up. Use the settings utility (m u) to enable it.")


def display_telem_unsent(backlog):
    """the warning display for unsent telemetry"""
    print(f"{Fore.YELLOW}Warning: The last {backlog} output files have not sent. Consider checking server settings with \"m u\".")
    print(f"{Fore.YELLOW}Attempting to send {backlog+1} output files now.")
    
