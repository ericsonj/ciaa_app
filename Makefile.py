import os
from os.path import basename
from pymakelib import git
from pymakelib import MKVARS
from pymakelib import Toolchain as tool
from pymakelib.Addon import Addon
from pymakelib.eclipse_addon import EclipseAddon
from scripts import vscode_addon
from pymakelib import D

Addon(EclipseAddon)
Addon(vscode_addon.vscode_init)


PROJECT_NAME = basename(os.getcwd())
FOLDER_OUT = 'Release/ciaa_app/'
TARGET_ELF = FOLDER_OUT + PROJECT_NAME + ".elf"
TARGET_MAP = FOLDER_OUT + PROJECT_NAME + ".map"
TARGET_HEX = FOLDER_OUT + PROJECT_NAME + ".hex"
TARGET_BIN = FOLDER_OUT + PROJECT_NAME + ".bin"
TARGET_SIZE = FOLDER_OUT + PROJECT_NAME + ".size"

def getProjectSettings():
    return {
        'PROJECT_NAME': PROJECT_NAME,
        'FOLDER_OUT':   FOLDER_OUT
    }


def getTargetsScript():
    TARGETS = {
        'TARGET': {
            'LOGKEY':  'OUT',
            'FILE':    TARGET_ELF,
            'SCRIPT':  [MKVARS.LD, '-o', '$@', MKVARS.OBJECTS, MKVARS.LDFLAGS, MKVARS.STATIC_LIBS]
        },
        'TARGET_HEX': {
            'LOGKEY':   'HEX',
            'FILE':     TARGET_HEX,
            'SCRIPT':   [MKVARS.OBJCOPY, '-O', 'ihex', MKVARS.TARGET, TARGET_HEX]
        },
        'TARGET_BIN': {
            'LOGKEY':   'BIN',
            'FILE':     TARGET_BIN,
            'SCRIPT':   [MKVARS.OBJCOPY, '-O', 'binary', MKVARS.TARGET, TARGET_BIN]
        },
        'TARGET_SIZE': {
            'LOGKEY':   'SIZE',
            'FILE':     TARGET_SIZE,
            'SCRIPT':   [MKVARS.SIZE, '-Ax', MKVARS.TARGET, '>', TARGET_SIZE]
        },
        'RESUME':   {
            'LOGKEY':   '>>',
            'FILE':     'RESUME',
            'SCRIPT':   ['@pybuildanalyzer', TARGET_MAP]
        }
    }

    return TARGETS


def getCompilerSet():
    return tool.confARMeabiGCC()


LIBRARIES = []

def getCompilerOpts():

    PROJECT_DEF = {
        '__USE_LPCOPEN':    None,
        'CHIP_LPC43XX':     None,
        'ARM_MATH_CM4':     None,
        '__USE_NEWLIB':     None,
        'CORE_M4':          None,
        '__FPU_PRESENT':    1,
        'USE_SAPI':         None,
        'BOARD':            D('edu_ciaa_nxp'),
    }

    return {
        'MACROS': PROJECT_DEF,
        'MACHINE-OPTS': [
            '-mcpu=cortex-m4',
            '-mthumb',
            '-mfloat-abi=hard',
            '-mfpu=fpv4-sp-d16',
        ],
        'OPTIMIZE-OPTS': [
        ],
        'OPTIONS': [
            '-ffunction-sections',
            '-fstack-usage'
        ],
        'DEBUGGING-OPTS': [
            '-ggdb3',
            '-Og'
        ],
        'PREPROCESSOR-OPTS': [
            '-MP',
            '-MMD'
        ],
        'WARNINGS-OPTS': [
        ],
        'CONTROL-C-OPTS': [
            '-std=c99'
        ],
        'GENERAL-OPTS': [
        ],
        'LIBRARIES': LIBRARIES
    }

"""
-Wl,-(   
    examples/c/app/out/examples/c/app/src/app.o
    examples/c/app/out/libs/cmsis_core//src/armv7m_startup.o
    examples/c/app/out/libs/editline//src/editline.o
    examples/c/app/out/libs/plc//src/PLC_Lib.o
     examples/c/app/out/libs/plc//src/PLC_OperatingSystem.o
examples/c/app/out/libs/plc//src/PLC_IL_Instructions.o
examples/c/app/out/libs/plc//src/PLC_Hardware.o
examples/c/app/out/libs/plc//src/PLC_Registers.o
examples/c/app/out/libs/seos_pont_2014//src/seos_pont_2014_scheduler.o
examples/c/app/out/libs/seos_pont_2014//src/seos_pont_2014_isr.o
examples/c/app/out/libs/sys_newlib//src/system.o
examples/c/app/out/libs/lpc_open/boards/edu_ciaa_nxp/src/board.o
examples/c/app/out/libs/lpc_open/boards/edu_ciaa_nxp/src/board_sysinit.o
examples/c/app/out/libs/lpc_open/lpc_chip_43xx/src/ccan_18xx_43xx.o
examples/c/app/out/libs/lpc_open/lpc_chip_43xx/src/gpiogroup_18xx_43xx.o
examples/c/app/out/libs/lpc_open/lpc_chip_43xx/src/dac_18xx_43xx.o
examples/c/app/out/libs/lpc_open/lpc_chip_43xx/src/ritimer_18xx_43xx.o
examples/c/app/out/libs/lpc_open/lpc_chip_43xx/src/i2c_18xx_43xx.o
examples/c/app/out/libs/lpc_open/lpc_chip_43xx/src/lcd_18xx_43xx.o
examples/c/app/out/libs/lpc_open/lpc_chip_43xx/src/uart_18xx_43xx.o
examples/c/app/out/libs/lpc_open/lpc_chip_43xx/src/adc_18xx_43xx.o
examples/c/app/out/libs/lpc_open/lpc_chip_43xx/src/sdif_18xx_43xx.o
examples/c/app/out/libs/lpc_open/lpc_chip_43xx/src/chip_18xx_43xx.o
examples/c/app/out/libs/lpc_open/lpc_chip_43xx/src/pmc_18xx_43xx.o
examples/c/app/out/libs/lpc_open/lpc_chip_43xx/src/clock_18xx_43xx.o
examples/c/app/out/libs/lpc_open/lpc_chip_43xx/src/otp_18xx_43xx.o
examples/c/app/out/libs/lpc_open/lpc_chip_43xx/src/sct_pwm_18xx_43xx.o
examples/c/app/out/libs/lpc_open/lpc_chip_43xx/src/aes_18xx_43xx.o
examples/c/app/out/libs/lpc_open/lpc_chip_43xx/src/sysinit_18xx_43xx.o
examples/c/app/out/libs/lpc_open/lpc_chip_43xx/src/atimer_18xx_43xx.o
examples/c/app/out/libs/lpc_open/lpc_chip_43xx/src/stopwatch_18xx_43xx.o
examples/c/app/out/libs/lpc_open/lpc_chip_43xx/src/timer_18xx_43xx.o
examples/c/app/out/libs/lpc_open/lpc_chip_43xx/src/iap_18xx_43xx.o
examples/c/app/out/libs/lpc_open/lpc_chip_43xx/src/wwdt_18xx_43xx.o
examples/c/app/out/libs/lpc_open/lpc_chip_43xx/src/ring_buffer.o
examples/c/app/out/libs/lpc_open/lpc_chip_43xx/src/i2cm_18xx_43xx.o
examples/c/app/out/libs/lpc_open/lpc_chip_43xx/src/pinint_18xx_43xx.o
examples/c/app/out/libs/lpc_open/lpc_chip_43xx/src/eeprom_18xx_43xx.o
examples/c/app/out/libs/lpc_open/lpc_chip_43xx/src/rtc_18xx_43xx.o
examples/c/app/out/libs/lpc_open/lpc_chip_43xx/src/sct_18xx_43xx.o
examples/c/app/out/libs/lpc_open/lpc_chip_43xx/src/emc_18xx_43xx.o
examples/c/app/out/libs/lpc_open/lpc_chip_43xx/src/sdmmc_18xx_43xx.o
examples/c/app/out/libs/lpc_open/lpc_chip_43xx/src/sdio_18xx_43xx.o
examples/c/app/out/libs/lpc_open/lpc_chip_43xx/src/spi_18xx_43xx.o
examples/c/app/out/libs/lpc_open/lpc_chip_43xx/src/gpio_18xx_43xx.o
examples/c/app/out/libs/lpc_open/lpc_chip_43xx/src/gpdma_18xx_43xx.o
examples/c/app/out/libs/lpc_open/lpc_chip_43xx/src/evrt_18xx_43xx.o
examples/c/app/out/libs/lpc_open/lpc_chip_43xx/src/enet_18xx_43xx.o
examples/c/app/out/libs/lpc_open/lpc_chip_43xx/src/ssp_18xx_43xx.o
examples/c/app/out/libs/lpc_open/lpc_chip_43xx/src/i2s_18xx_43xx.o
examples/c/app/out/libs/lpc_open/lpc_startup/src/crp.o
examples/c/app/out/libs/lpc_open/lpc_startup/src/sysinit.o
examples/c/app/out/libs/lpc_open/lpc_startup/src/vendor_interrupt.o
examples/c/app/out/libs/sapi/sapi_v0.6.2/base/src/sapi_datatypes.o
examples/c/app/out/libs/sapi/sapi_v0.6.2/soc/core/src/sapi_cyclesCounter.o
examples/c/app/out/libs/sapi/sapi_v0.6.2/soc/core/src/sapi_sleep.o
examples/c/app/out/libs/sapi/sapi_v0.6.2/soc/peripherals/src/sapi_dac.o
examples/c/app/out/libs/sapi/sapi_v0.6.2/soc/peripherals/src/sapi_rtc.o
examples/c/app/out/libs/sapi/sapi_v0.6.2/soc/peripherals/src/sapi_uart.o
examples/c/app/out/libs/sapi/sapi_v0.6.2/soc/peripherals/src/sapi_spi.o
examples/c/app/out/libs/sapi/sapi_v0.6.2/soc/peripherals/src/sapi_pwm.o
examples/c/app/out/libs/sapi/sapi_v0.6.2/soc/peripherals/src/sapi_tick.o
examples/c/app/out/libs/sapi/sapi_v0.6.2/soc/peripherals/src/sapi_i2c.o
examples/c/app/out/libs/sapi/sapi_v0.6.2/soc/peripherals/src/sapi_timer.o
examples/c/app/out/libs/sapi/sapi_v0.6.2/soc/peripherals/src/sapi_software_i2c.o
examples/c/app/out/libs/sapi/sapi_v0.6.2/soc/peripherals/src/sapi_sct.o
examples/c/app/out/libs/sapi/sapi_v0.6.2/soc/peripherals/src/sapi_adc.o
examples/c/app/out/libs/sapi/sapi_v0.6.2/soc/peripherals/src/sapi_gpio.o
examples/c/app/out/libs/sapi/sapi_v0.6.2/soc/peripherals/usb/device/src/sapi_usb_device.o
examples/c/app/out/libs/sapi/sapi_v0.6.2/soc/peripherals/usb/device/src/usbd_keyboard.o
examples/c/app/out/libs/sapi/sapi_v0.6.2/soc/peripherals/usb/device/src/cdc_uart.o
examples/c/app/out/libs/sapi/sapi_v0.6.2/board/src/sapi_board.o
examples/c/app/out/libs/sapi/sapi_v0.6.2/abstract_modules/src/sapi_delay.o
examples/c/app/out/libs/sapi/sapi_v0.6.2/abstract_modules/src/sapi_button.o
examples/c/app/out/libs/sapi/sapi_v0.6.2/abstract_modules/src/sapi_parser.o
examples/c/app/out/libs/sapi/sapi_v0.6.2/abstract_modules/src/sapi_circularBuffer.o
examples/c/app/out/libs/sapi/sapi_v0.6.2/abstract_modules/src/sapi_print.o
examples/c/app/out/libs/sapi/sapi_v0.6.2/abstract_modules/src/sapi_convert.o
examples/c/app/out/libs/sapi/sapi_v0.6.2/abstract_modules/src/sapi_stdio.o
examples/c/app/out/libs/sapi/sapi_v0.6.2/external_peripherals/display/drivers/LCD/HD44780/GPIOs/display_lcd_hd44780_gpios.o
examples/c/app/out/libs/sapi/sapi_v0.6.2/external_peripherals/display/drivers/LED_Segments/7segment/sapi_7_segment_display.o
examples/c/app/out/libs/sapi/sapi_v0.6.2/external_peripherals/display/fonts/chars_5x8px/alphanumerics_chars_5x8px.o
examples/c/app/out/libs/sapi/sapi_v0.6.2/external_peripherals/display/fonts/chars_5x8px/greek_chars_5x8px.o
examples/c/app/out/libs/sapi/sapi_v0.6.2/external_peripherals/display/fonts/chars_5x8px/icon_chars_5x8px.o
examples/c/app/out/libs/sapi/sapi_v0.6.2/external_peripherals/display/fonts/chars_5x8px/_template_chars_5x8px.o
examples/c/app/out/libs/sapi/sapi_v0.6.2/external_peripherals/imu/mpu60X0/src/sapi_imu_mpu60X0.o
examples/c/app/out/libs/sapi/sapi_v0.6.2/external_peripherals/imu/mpu9250/src/sapi_imu_mpu9250.o
examples/c/app/out/libs/sapi/sapi_v0.6.2/external_peripherals/keypad/src/sapi_keypad.o
examples/c/app/out/libs/sapi/sapi_v0.6.2/external_peripherals/led_rgb/src/sapi_rgb.o
examples/c/app/out/libs/sapi/sapi_v0.6.2/external_peripherals/magnetometer/hmc5883l/src/sapi_magnetometer_hmc5883l.o
examples/c/app/out/libs/sapi/sapi_v0.6.2/external_peripherals/magnetometer/qmc5883l/src/sapi_magnetometer_qmc5883l.o
examples/c/app/out/libs/sapi/sapi_v0.6.2/external_peripherals/memory/eeprom/src/sapi_eeprom24xx1025.o
examples/c/app/out/libs/sapi/sapi_v0.6.2/external_peripherals/motor/servo/src/sapi_servo.o
examples/c/app/out/libs/sapi/sapi_v0.6.2/external_peripherals/temperature_humudity/dht11/src/sapi_dht11.o
examples/c/app/out/libs/sapi/sapi_v0.6.2/external_peripherals/ultrasonic/hcsr04/src/sapi_ultrasonic_hcsr04.o
examples/c/app/out/libs/sapi/sapi_v0.6.2/external_peripherals/wifi/esp8266_at/src/sapi_esp8266.o
examples/c/app/out/libs/sapi/sapi_v0.6.2/external_peripherals/pressure_temperature/bmp280/src/sapi_bmp280.o
examples/c/app/out/libs/sapi/sapi_v0.6.2/external_peripherals/pressure_temperature/bmp280/src/bmp280.o
examples/c/app/out/libs/sapi/sapi_v0.6.2/external_peripherals/mcp23017/src/mcp23017.o
examples/c/app/out/libs/sapi/sapi_v0.6.2/external_peripherals/adc/adc128d818/src/sapi_adc128d818.o
  -Wl,-) -mcpu=cortex-m4 -mthumb -mfloat-abi=hard -mfpu=fpv4-sp-d16 
  -Llibs/cmsis_dsp//lib 
  -Llibs/lpc_open//lib 
  -Lexamples/c/app/out/libs/cmsis_dsp//lib/ 
  -larm_cortexM4lf_math 
  -Tlink.ld -nostartfiles -Wl,-gc-sections -Wl,-Map=examples/c/app/out/app.map -Wl,--cref --specs=nano.specs
"""

def getLinkerOpts():
    return {
        'LINKER-SCRIPT': [
            '-T/PROJECTS/ARM/firmware_v3/libs/lpc_open/lib/link.ld'
        ],
        'MACHINE-OPTS': [
            '-mcpu=cortex-m4', 
            '-mthumb', 
            '-mfloat-abi=hard',
            '-mfpu=fpv4-sp-d16',
        ],
        'GENERAL-OPTS': [
            '--specs=nano.specs',
        ],
        'LINKER-OPTS': [
            '-nostartfiles',
            '-Wl,-gc-sections',
            '-Wl,-Map='+TARGET_MAP,
            '-Wl,--cref',
        ],
        'LIBRARIES': LIBRARIES
    }
