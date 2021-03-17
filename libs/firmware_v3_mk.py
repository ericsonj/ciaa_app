from pymakelib import module
from pathlib import Path
from scripts import config

FIRMWARE_V3 = config.FIRMWARE_V3_PATH

SAPI_0_5_2_SRCS = [
    f"{FIRMWARE_V3}/libs/cmsis_core//src/armv7m_startup.c",
    f"{FIRMWARE_V3}/libs/editline//src/editline.c",
    f"{FIRMWARE_V3}/libs/plc//src/PLC_Hardware.c",
    f"{FIRMWARE_V3}/libs/plc//src/PLC_IL_Instructions.c",
    f"{FIRMWARE_V3}/libs/plc//src/PLC_Lib.c",
    f"{FIRMWARE_V3}/libs/plc//src/PLC_OperatingSystem.c",
    f"{FIRMWARE_V3}/libs/plc//src/PLC_Registers.c",
    f"{FIRMWARE_V3}/libs/seos_pont_2014//src/seos_pont_2014_isr.c",
    f"{FIRMWARE_V3}/libs/seos_pont_2014//src/seos_pont_2014_scheduler.c",
    f"{FIRMWARE_V3}/libs/sys_newlib//src/system.c",
    f"{FIRMWARE_V3}/libs/lpc_open/boards/edu_ciaa_nxp/src/board.c",
    f"{FIRMWARE_V3}/libs/lpc_open/boards/edu_ciaa_nxp/src/board_sysinit.c",
    f"{FIRMWARE_V3}/libs/lpc_open/lpc_chip_43xx/src/adc_18xx_43xx.c",
    f"{FIRMWARE_V3}/libs/lpc_open/lpc_chip_43xx/src/aes_18xx_43xx.c",
    f"{FIRMWARE_V3}/libs/lpc_open/lpc_chip_43xx/src/atimer_18xx_43xx.c",
    f"{FIRMWARE_V3}/libs/lpc_open/lpc_chip_43xx/src/ccan_18xx_43xx.c",
    f"{FIRMWARE_V3}/libs/lpc_open/lpc_chip_43xx/src/chip_18xx_43xx.c",
    f"{FIRMWARE_V3}/libs/lpc_open/lpc_chip_43xx/src/clock_18xx_43xx.c",
    f"{FIRMWARE_V3}/libs/lpc_open/lpc_chip_43xx/src/dac_18xx_43xx.c",
    f"{FIRMWARE_V3}/libs/lpc_open/lpc_chip_43xx/src/eeprom_18xx_43xx.c",
    f"{FIRMWARE_V3}/libs/lpc_open/lpc_chip_43xx/src/emc_18xx_43xx.c",
    f"{FIRMWARE_V3}/libs/lpc_open/lpc_chip_43xx/src/enet_18xx_43xx.c",
    f"{FIRMWARE_V3}/libs/lpc_open/lpc_chip_43xx/src/evrt_18xx_43xx.c",
    f"{FIRMWARE_V3}/libs/lpc_open/lpc_chip_43xx/src/gpdma_18xx_43xx.c",
    f"{FIRMWARE_V3}/libs/lpc_open/lpc_chip_43xx/src/gpio_18xx_43xx.c",
    f"{FIRMWARE_V3}/libs/lpc_open/lpc_chip_43xx/src/gpiogroup_18xx_43xx.c",
    f"{FIRMWARE_V3}/libs/lpc_open/lpc_chip_43xx/src/i2c_18xx_43xx.c",
    f"{FIRMWARE_V3}/libs/lpc_open/lpc_chip_43xx/src/i2cm_18xx_43xx.c",
    f"{FIRMWARE_V3}/libs/lpc_open/lpc_chip_43xx/src/i2s_18xx_43xx.c",
    f"{FIRMWARE_V3}/libs/lpc_open/lpc_chip_43xx/src/iap_18xx_43xx.c",
    f"{FIRMWARE_V3}/libs/lpc_open/lpc_chip_43xx/src/lcd_18xx_43xx.c",
    f"{FIRMWARE_V3}/libs/lpc_open/lpc_chip_43xx/src/otp_18xx_43xx.c",
    f"{FIRMWARE_V3}/libs/lpc_open/lpc_chip_43xx/src/pinint_18xx_43xx.c",
    f"{FIRMWARE_V3}/libs/lpc_open/lpc_chip_43xx/src/pmc_18xx_43xx.c",
    f"{FIRMWARE_V3}/libs/lpc_open/lpc_chip_43xx/src/ring_buffer.c",
    f"{FIRMWARE_V3}/libs/lpc_open/lpc_chip_43xx/src/ritimer_18xx_43xx.c",
    f"{FIRMWARE_V3}/libs/lpc_open/lpc_chip_43xx/src/rtc_18xx_43xx.c",
    f"{FIRMWARE_V3}/libs/lpc_open/lpc_chip_43xx/src/sct_18xx_43xx.c",
    f"{FIRMWARE_V3}/libs/lpc_open/lpc_chip_43xx/src/sct_pwm_18xx_43xx.c",
    f"{FIRMWARE_V3}/libs/lpc_open/lpc_chip_43xx/src/sdif_18xx_43xx.c",
    f"{FIRMWARE_V3}/libs/lpc_open/lpc_chip_43xx/src/sdio_18xx_43xx.c",
    f"{FIRMWARE_V3}/libs/lpc_open/lpc_chip_43xx/src/sdmmc_18xx_43xx.c",
    f"{FIRMWARE_V3}/libs/lpc_open/lpc_chip_43xx/src/spi_18xx_43xx.c",
    f"{FIRMWARE_V3}/libs/lpc_open/lpc_chip_43xx/src/ssp_18xx_43xx.c",
    f"{FIRMWARE_V3}/libs/lpc_open/lpc_chip_43xx/src/stopwatch_18xx_43xx.c",
    f"{FIRMWARE_V3}/libs/lpc_open/lpc_chip_43xx/src/sysinit_18xx_43xx.c",
    f"{FIRMWARE_V3}/libs/lpc_open/lpc_chip_43xx/src/timer_18xx_43xx.c",
    f"{FIRMWARE_V3}/libs/lpc_open/lpc_chip_43xx/src/uart_18xx_43xx.c",
    f"{FIRMWARE_V3}/libs/lpc_open/lpc_chip_43xx/src/wwdt_18xx_43xx.c",
    f"{FIRMWARE_V3}/libs/lpc_open/lpc_startup/src/crp.c",
    f"{FIRMWARE_V3}/libs/lpc_open/lpc_startup/src/sysinit.c",
    f"{FIRMWARE_V3}/libs/lpc_open/lpc_startup/src/vendor_interrupt.c",
    f"{FIRMWARE_V3}/libs/sapi/sapi_v0.5.2/base/src/sapi_datatypes.c",
    f"{FIRMWARE_V3}/libs/sapi/sapi_v0.5.2/soc/core/src/sapi_cyclesCounter.c",
    f"{FIRMWARE_V3}/libs/sapi/sapi_v0.5.2/soc/core/src/sapi_sleep.c",
    f"{FIRMWARE_V3}/libs/sapi/sapi_v0.5.2/soc/peripherals/src/sapi_adc.c",
    f"{FIRMWARE_V3}/libs/sapi/sapi_v0.5.2/soc/peripherals/src/sapi_dac.c",
    f"{FIRMWARE_V3}/libs/sapi/sapi_v0.5.2/soc/peripherals/src/sapi_gpio.c",
    f"{FIRMWARE_V3}/libs/sapi/sapi_v0.5.2/soc/peripherals/src/sapi_i2c.c",
    f"{FIRMWARE_V3}/libs/sapi/sapi_v0.5.2/soc/peripherals/src/sapi_pwm.c",
    f"{FIRMWARE_V3}/libs/sapi/sapi_v0.5.2/soc/peripherals/src/sapi_rtc.c",
    f"{FIRMWARE_V3}/libs/sapi/sapi_v0.5.2/soc/peripherals/src/sapi_sct.c",
    f"{FIRMWARE_V3}/libs/sapi/sapi_v0.5.2/soc/peripherals/src/sapi_spi.c",
    f"{FIRMWARE_V3}/libs/sapi/sapi_v0.5.2/soc/peripherals/src/sapi_tick.c",
    f"{FIRMWARE_V3}/libs/sapi/sapi_v0.5.2/soc/peripherals/src/sapi_timer.c",
    f"{FIRMWARE_V3}/libs/sapi/sapi_v0.5.2/soc/peripherals/src/sapi_uart.c",
    f"{FIRMWARE_V3}/libs/sapi/sapi_v0.5.2/soc/peripherals/usb/device/src/cdc_uart.c",
    f"{FIRMWARE_V3}/libs/sapi/sapi_v0.5.2/soc/peripherals/usb/device/src/sapi_usb_device.c",
    f"{FIRMWARE_V3}/libs/sapi/sapi_v0.5.2/soc/peripherals/usb/device/src/usbd_keyboard.c",
    f"{FIRMWARE_V3}/libs/sapi/sapi_v0.5.2/board/src/sapi_board.c",
    f"{FIRMWARE_V3}/libs/sapi/sapi_v0.5.2/abstract_modules/src/sapi_button.c",
    f"{FIRMWARE_V3}/libs/sapi/sapi_v0.5.2/abstract_modules/src/sapi_circularBuffer.c",
    f"{FIRMWARE_V3}/libs/sapi/sapi_v0.5.2/abstract_modules/src/sapi_convert.c",
    f"{FIRMWARE_V3}/libs/sapi/sapi_v0.5.2/abstract_modules/src/sapi_delay.c",
    f"{FIRMWARE_V3}/libs/sapi/sapi_v0.5.2/abstract_modules/src/sapi_print.c",
    f"{FIRMWARE_V3}/libs/sapi/sapi_v0.5.2/abstract_modules/src/sapi_stdio.c",
    f"{FIRMWARE_V3}/libs/sapi/sapi_v0.5.2/external_peripherals/display/fonts/greek_chars_5x7/src/lcd_greek_chars.c",
    f"{FIRMWARE_V3}/libs/sapi/sapi_v0.5.2/external_peripherals/display/fonts/icon_chars_5x7/src/lcd_icon_chars.c",
    f"{FIRMWARE_V3}/libs/sapi/sapi_v0.5.2/external_peripherals/display/lcd/src/sapi_lcd.c",
    f"{FIRMWARE_V3}/libs/sapi/sapi_v0.5.2/external_peripherals/display/led_segments/7segment/src/sapi_7_segment_display.c",
    f"{FIRMWARE_V3}/libs/sapi/sapi_v0.5.2/external_peripherals/imu/mpu60X0/src/sapi_imu_mpu60X0.c",
    f"{FIRMWARE_V3}/libs/sapi/sapi_v0.5.2/external_peripherals/imu/mpu9250/src/sapi_imu_mpu9250.c",
    f"{FIRMWARE_V3}/libs/sapi/sapi_v0.5.2/external_peripherals/keypad/src/sapi_keypad.c",
    f"{FIRMWARE_V3}/libs/sapi/sapi_v0.5.2/external_peripherals/led_rgb/src/sapi_rgb.c",
    f"{FIRMWARE_V3}/libs/sapi/sapi_v0.5.2/external_peripherals/magnetometer/hmc5883l/src/sapi_magnetometer_hmc5883l.c",
    f"{FIRMWARE_V3}/libs/sapi/sapi_v0.5.2/external_peripherals/magnetometer/qmc5883l/src/sapi_magnetometer_qmc5883l.c",
    f"{FIRMWARE_V3}/libs/sapi/sapi_v0.5.2/external_peripherals/memory/eeprom/src/sapi_eeprom24xx1025.c",
    f"{FIRMWARE_V3}/libs/sapi/sapi_v0.5.2/external_peripherals/motor/servo/src/sapi_servo.c",
    f"{FIRMWARE_V3}/libs/sapi/sapi_v0.5.2/external_peripherals/temperature_humudity/dht11/src/sapi_dht11.c",
    f"{FIRMWARE_V3}/libs/sapi/sapi_v0.5.2/external_peripherals/ultrasonic/hcsr04/src/sapi_ultrasonic_hcsr04.c",
    f"{FIRMWARE_V3}/libs/sapi/sapi_v0.5.2/external_peripherals/wifi/esp8266_at/src/sapi_esp8266.c",
]

SAPI_0_5_2_INCS = [
    f"{FIRMWARE_V3}/libs/arduino//inc",
    f"{FIRMWARE_V3}/libs/cmsis_core//inc",
    f"{FIRMWARE_V3}/libs/cmsis_dsp//inc",
    f"{FIRMWARE_V3}/libs/editline//inc",
    f"{FIRMWARE_V3}/libs/fatfs//inc",
    f"{FIRMWARE_V3}/libs/freertos//inc",
    f"{FIRMWARE_V3}/libs/lpc_fatfs_disks//inc",
    f"{FIRMWARE_V3}/libs/lpc_open//inc",
    f"{FIRMWARE_V3}/libs/lpcusblib//inc",
    f"{FIRMWARE_V3}/libs/minut//inc",
    f"{FIRMWARE_V3}/libs/plc//inc",
    f"{FIRMWARE_V3}/libs/rkh//inc",
    f"{FIRMWARE_V3}/libs/sapi//inc",
    f"{FIRMWARE_V3}/libs/seos_pont_2014//inc",
    f"{FIRMWARE_V3}/libs/sys_newlib//inc",
    f"{FIRMWARE_V3}/libs/tinyprintf//inc",
    f"{FIRMWARE_V3}/libs/lpc_open/boards/edu_ciaa_nxp/inc",
    f"{FIRMWARE_V3}/libs/lpc_open/boards/inc",
    f"{FIRMWARE_V3}/libs/lpc_open/lpc_chip_43xx/inc",
    f"{FIRMWARE_V3}/libs/lpc_open/lpc_chip_43xx/usbd_rom",
    f"{FIRMWARE_V3}/libs/lpc_open/lpc_startup/inc",
    f"{FIRMWARE_V3}/libs/sapi/sapi_v0.5.2/base/inc",
    f"{FIRMWARE_V3}/libs/sapi/sapi_v0.5.2/soc/core/inc",
    f"{FIRMWARE_V3}/libs/sapi/sapi_v0.5.2/soc/peripherals/inc",
    f"{FIRMWARE_V3}/libs/sapi/sapi_v0.5.2/soc/peripherals/usb/device/inc",
    f"{FIRMWARE_V3}/libs/sapi/sapi_v0.5.2/soc/peripherals/usb/host/inc",
    f"{FIRMWARE_V3}/libs/sapi/sapi_v0.5.2/board/inc",
    f"{FIRMWARE_V3}/libs/sapi/sapi_v0.5.2/abstract_modules/inc",
    f"{FIRMWARE_V3}/libs/sapi/sapi_v0.5.2/external_peripherals/display/fonts/inc",
    f"{FIRMWARE_V3}/libs/sapi/sapi_v0.5.2/external_peripherals/display/fonts/greek_chars_5x7/inc",
    f"{FIRMWARE_V3}/libs/sapi/sapi_v0.5.2/external_peripherals/display/fonts/icon_chars_5x7/inc",
    f"{FIRMWARE_V3}/libs/sapi/sapi_v0.5.2/external_peripherals/display/lcd/inc",
    f"{FIRMWARE_V3}/libs/sapi/sapi_v0.5.2/external_peripherals/display/led_segments/7segment/inc",
    f"{FIRMWARE_V3}/libs/sapi/sapi_v0.5.2/external_peripherals/imu/mpu60X0/inc",
    f"{FIRMWARE_V3}/libs/sapi/sapi_v0.5.2/external_peripherals/imu/mpu9250/inc",
    f"{FIRMWARE_V3}/libs/sapi/sapi_v0.5.2/external_peripherals/keypad/inc",
    f"{FIRMWARE_V3}/libs/sapi/sapi_v0.5.2/external_peripherals/led_rgb/inc",
    f"{FIRMWARE_V3}/libs/sapi/sapi_v0.5.2/external_peripherals/magnetometer/hmc5883l/inc",
    f"{FIRMWARE_V3}/libs/sapi/sapi_v0.5.2/external_peripherals/magnetometer/qmc5883l/inc",
    f"{FIRMWARE_V3}/libs/sapi/sapi_v0.5.2/external_peripherals/memory/eeprom/inc",
    f"{FIRMWARE_V3}/libs/sapi/sapi_v0.5.2/external_peripherals/motor/servo/inc",
    f"{FIRMWARE_V3}/libs/sapi/sapi_v0.5.2/external_peripherals/temperature_humudity/dht11/inc",
    f"{FIRMWARE_V3}/libs/sapi/sapi_v0.5.2/external_peripherals/ultrasonic/hcsr04/inc",
    f"{FIRMWARE_V3}/libs/sapi/sapi_v0.5.2/external_peripherals/wifi/esp8266_at/inc",
]


def getSrcs(mh: module.ModuleHandle):
    return SAPI_0_5_2_SRCS


def getIncs(mh: module.ModuleHandle):
    return list(filter(lambda f: Path(f).is_dir(), SAPI_0_5_2_INCS))
