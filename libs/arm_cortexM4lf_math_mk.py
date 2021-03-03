from pymakelib.Module import ModuleHandle, StaticLibrary
from pymakelib.Toolchain import confARMeabiGCC
from pathlib import Path
import subprocess

def init(mh: ModuleHandle):
    """
    Create static library libarm_cortexM4lf_math.a
    """
    LIB_FOLDER_OUT = 'Release/ciaa_app/PROJECTS/ARM/firmware_v3/libs/lpc_open/lib'
    staticLib = StaticLibrary(name='arm_cortexM4lf_math', outputDir=LIB_FOLDER_OUT)
    try:
        if mh.getGoal() == 'all':
            
            toolset = confARMeabiGCC()
            staticLib.setRebuild(True)
            Path(LIB_FOLDER_OUT).mkdir(parents=True, exist_ok=True)
            subprocess.call([
                toolset['OBJCOPY'],
                '-I', 'ihex',
                '-O', 'binary',
                '/PROJECTS/ARM/firmware_v3/libs/cmsis_dsp/lib/libarm_cortexM4lf_math.hexlib',
                 LIB_FOLDER_OUT+'/libarm_cortexM4lf_math.a'])

    except Exception as e:
            print(e)
    return staticLib

def getSrcs(m):
    return None

def getIncs(m):
    return None