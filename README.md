# CIAA Firmware usando pymaketool

Ejemplo de aplicacion para la tarjeta EDU-CIAA-NXP usando la utilidad pymaketool y firmware_v3.

```console
┬─ericson@darkknight:/PROJECTS/ARM/ciaa_app
╰─(main |  • 1) 
$ make
Module: libs/arm_cortexM4lf_math_mk.py
Module: libs/firmware_v3_mk.py
Module: app/app_mk.py
Generate .vscode/c_cpp_properties.json
Generate .vscode/launch.json
Generate .setting/language.settings.xml
Generate .cproject
    CC	/PROJECTS/ARM/firmware_v3/libs/cmsis_core//src/armv7m_startup.c
    CC	/PROJECTS/ARM/firmware_v3/libs/editline//src/editline.c
    CC	/PROJECTS/ARM/firmware_v3/libs/plc//src/PLC_Hardware.c
    CC	/PROJECTS/ARM/firmware_v3/libs/plc//src/PLC_IL_Instructions.c
    CC	/PROJECTS/ARM/firmware_v3/libs/plc//src/PLC_Lib.c
    CC	/PROJECTS/ARM/firmware_v3/libs/plc//src/PLC_OperatingSystem.c
    CC	/PROJECTS/ARM/firmware_v3/libs/plc//src/PLC_Registers.c
    CC	/PROJECTS/ARM/firmware_v3/libs/seos_pont_2014//src/seos_pont_2014_isr.c
    CC	/PROJECTS/ARM/firmware_v3/libs/seos_pont_2014//src/seos_pont_2014_scheduler.c
    CC	/PROJECTS/ARM/firmware_v3/libs/sys_newlib//src/system.c
    CC	/PROJECTS/ARM/firmware_v3/libs/lpc_open/boards/edu_ciaa_nxp/src/board.c
    CC	/PROJECTS/ARM/firmware_v3/libs/lpc_open/boards/edu_ciaa_nxp/src/board_sysinit.c
    CC	/PROJECTS/ARM/firmware_v3/libs/lpc_open/lpc_chip_43xx/src/adc_18xx_43xx.c
    CC	/PROJECTS/ARM/firmware_v3/libs/lpc_open/lpc_chip_43xx/src/aes_18xx_43xx.c
    CC	/PROJECTS/ARM/firmware_v3/libs/lpc_open/lpc_chip_43xx/src/atimer_18xx_43xx.c
    CC	/PROJECTS/ARM/firmware_v3/libs/lpc_open/lpc_chip_43xx/src/ccan_18xx_43xx.c
    CC	/PROJECTS/ARM/firmware_v3/libs/lpc_open/lpc_chip_43xx/src/chip_18xx_43xx.c
    CC	/PROJECTS/ARM/firmware_v3/libs/lpc_open/lpc_chip_43xx/src/clock_18xx_43xx.c
    CC	/PROJECTS/ARM/firmware_v3/libs/lpc_open/lpc_chip_43xx/src/dac_18xx_43xx.c
    CC	/PROJECTS/ARM/firmware_v3/libs/lpc_open/lpc_chip_43xx/src/eeprom_18xx_43xx.c
    CC	/PROJECTS/ARM/firmware_v3/libs/lpc_open/lpc_chip_43xx/src/emc_18xx_43xx.c
    CC	/PROJECTS/ARM/firmware_v3/libs/lpc_open/lpc_chip_43xx/src/enet_18xx_43xx.c
    CC	/PROJECTS/ARM/firmware_v3/libs/lpc_open/lpc_chip_43xx/src/evrt_18xx_43xx.c
    CC	/PROJECTS/ARM/firmware_v3/libs/lpc_open/lpc_chip_43xx/src/gpdma_18xx_43xx.c
    CC	/PROJECTS/ARM/firmware_v3/libs/lpc_open/lpc_chip_43xx/src/gpio_18xx_43xx.c
    CC	/PROJECTS/ARM/firmware_v3/libs/lpc_open/lpc_chip_43xx/src/gpiogroup_18xx_43xx.c
    CC	/PROJECTS/ARM/firmware_v3/libs/lpc_open/lpc_chip_43xx/src/i2c_18xx_43xx.c
    CC	/PROJECTS/ARM/firmware_v3/libs/lpc_open/lpc_chip_43xx/src/i2cm_18xx_43xx.c
    CC	/PROJECTS/ARM/firmware_v3/libs/lpc_open/lpc_chip_43xx/src/i2s_18xx_43xx.c
    CC	/PROJECTS/ARM/firmware_v3/libs/lpc_open/lpc_chip_43xx/src/iap_18xx_43xx.c
    CC	/PROJECTS/ARM/firmware_v3/libs/lpc_open/lpc_chip_43xx/src/lcd_18xx_43xx.c
    CC	/PROJECTS/ARM/firmware_v3/libs/lpc_open/lpc_chip_43xx/src/otp_18xx_43xx.c
    CC	/PROJECTS/ARM/firmware_v3/libs/lpc_open/lpc_chip_43xx/src/pinint_18xx_43xx.c
    CC	/PROJECTS/ARM/firmware_v3/libs/lpc_open/lpc_chip_43xx/src/pmc_18xx_43xx.c
    CC	/PROJECTS/ARM/firmware_v3/libs/lpc_open/lpc_chip_43xx/src/ring_buffer.c
    CC	/PROJECTS/ARM/firmware_v3/libs/lpc_open/lpc_chip_43xx/src/ritimer_18xx_43xx.c
    CC	/PROJECTS/ARM/firmware_v3/libs/lpc_open/lpc_chip_43xx/src/rtc_18xx_43xx.c
    CC	/PROJECTS/ARM/firmware_v3/libs/lpc_open/lpc_chip_43xx/src/sct_18xx_43xx.c
    CC	/PROJECTS/ARM/firmware_v3/libs/lpc_open/lpc_chip_43xx/src/sct_pwm_18xx_43xx.c
    CC	/PROJECTS/ARM/firmware_v3/libs/lpc_open/lpc_chip_43xx/src/sdif_18xx_43xx.c
    CC	/PROJECTS/ARM/firmware_v3/libs/lpc_open/lpc_chip_43xx/src/sdio_18xx_43xx.c
    CC	/PROJECTS/ARM/firmware_v3/libs/lpc_open/lpc_chip_43xx/src/sdmmc_18xx_43xx.c
    CC	/PROJECTS/ARM/firmware_v3/libs/lpc_open/lpc_chip_43xx/src/spi_18xx_43xx.c
    CC	/PROJECTS/ARM/firmware_v3/libs/lpc_open/lpc_chip_43xx/src/ssp_18xx_43xx.c
    CC	/PROJECTS/ARM/firmware_v3/libs/lpc_open/lpc_chip_43xx/src/stopwatch_18xx_43xx.c
    CC	/PROJECTS/ARM/firmware_v3/libs/lpc_open/lpc_chip_43xx/src/sysinit_18xx_43xx.c
    CC	/PROJECTS/ARM/firmware_v3/libs/lpc_open/lpc_chip_43xx/src/timer_18xx_43xx.c
    CC	/PROJECTS/ARM/firmware_v3/libs/lpc_open/lpc_chip_43xx/src/uart_18xx_43xx.c
    CC	/PROJECTS/ARM/firmware_v3/libs/lpc_open/lpc_chip_43xx/src/wwdt_18xx_43xx.c
    CC	/PROJECTS/ARM/firmware_v3/libs/lpc_open/lpc_startup/src/crp.c
    CC	/PROJECTS/ARM/firmware_v3/libs/lpc_open/lpc_startup/src/sysinit.c
    CC	/PROJECTS/ARM/firmware_v3/libs/lpc_open/lpc_startup/src/vendor_interrupt.c
    CC	/PROJECTS/ARM/firmware_v3/libs/sapi/sapi_v0.5.2/base/src/sapi_datatypes.c
    CC	/PROJECTS/ARM/firmware_v3/libs/sapi/sapi_v0.5.2/soc/core/src/sapi_cyclesCounter.c
    CC	/PROJECTS/ARM/firmware_v3/libs/sapi/sapi_v0.5.2/soc/core/src/sapi_sleep.c
    CC	/PROJECTS/ARM/firmware_v3/libs/sapi/sapi_v0.5.2/soc/peripherals/src/sapi_adc.c
    CC	/PROJECTS/ARM/firmware_v3/libs/sapi/sapi_v0.5.2/soc/peripherals/src/sapi_dac.c
    CC	/PROJECTS/ARM/firmware_v3/libs/sapi/sapi_v0.5.2/soc/peripherals/src/sapi_gpio.c
    CC	/PROJECTS/ARM/firmware_v3/libs/sapi/sapi_v0.5.2/soc/peripherals/src/sapi_i2c.c
    CC	/PROJECTS/ARM/firmware_v3/libs/sapi/sapi_v0.5.2/soc/peripherals/src/sapi_pwm.c
    CC	/PROJECTS/ARM/firmware_v3/libs/sapi/sapi_v0.5.2/soc/peripherals/src/sapi_rtc.c
    CC	/PROJECTS/ARM/firmware_v3/libs/sapi/sapi_v0.5.2/soc/peripherals/src/sapi_sct.c
    CC	/PROJECTS/ARM/firmware_v3/libs/sapi/sapi_v0.5.2/soc/peripherals/src/sapi_spi.c
    CC	/PROJECTS/ARM/firmware_v3/libs/sapi/sapi_v0.5.2/soc/peripherals/src/sapi_tick.c
    CC	/PROJECTS/ARM/firmware_v3/libs/sapi/sapi_v0.5.2/soc/peripherals/src/sapi_timer.c
    CC	/PROJECTS/ARM/firmware_v3/libs/sapi/sapi_v0.5.2/soc/peripherals/src/sapi_uart.c
    CC	/PROJECTS/ARM/firmware_v3/libs/sapi/sapi_v0.5.2/soc/peripherals/usb/device/src/cdc_uart.c
    CC	/PROJECTS/ARM/firmware_v3/libs/sapi/sapi_v0.5.2/soc/peripherals/usb/device/src/sapi_usb_device.c
    CC	/PROJECTS/ARM/firmware_v3/libs/sapi/sapi_v0.5.2/soc/peripherals/usb/device/src/usbd_keyboard.c
    CC	/PROJECTS/ARM/firmware_v3/libs/sapi/sapi_v0.5.2/board/src/sapi_board.c
    CC	/PROJECTS/ARM/firmware_v3/libs/sapi/sapi_v0.5.2/abstract_modules/src/sapi_button.c
    CC	/PROJECTS/ARM/firmware_v3/libs/sapi/sapi_v0.5.2/abstract_modules/src/sapi_circularBuffer.c
    CC	/PROJECTS/ARM/firmware_v3/libs/sapi/sapi_v0.5.2/abstract_modules/src/sapi_convert.c
    CC	/PROJECTS/ARM/firmware_v3/libs/sapi/sapi_v0.5.2/abstract_modules/src/sapi_delay.c
    CC	/PROJECTS/ARM/firmware_v3/libs/sapi/sapi_v0.5.2/abstract_modules/src/sapi_print.c
    CC	/PROJECTS/ARM/firmware_v3/libs/sapi/sapi_v0.5.2/abstract_modules/src/sapi_stdio.c
    CC	/PROJECTS/ARM/firmware_v3/libs/sapi/sapi_v0.5.2/external_peripherals/display/fonts/greek_chars_5x7/src/lcd_greek_chars.c
    CC	/PROJECTS/ARM/firmware_v3/libs/sapi/sapi_v0.5.2/external_peripherals/display/fonts/icon_chars_5x7/src/lcd_icon_chars.c
    CC	/PROJECTS/ARM/firmware_v3/libs/sapi/sapi_v0.5.2/external_peripherals/display/lcd/src/sapi_lcd.c
    CC	/PROJECTS/ARM/firmware_v3/libs/sapi/sapi_v0.5.2/external_peripherals/display/led_segments/7segment/src/sapi_7_segment_display.c
    CC	/PROJECTS/ARM/firmware_v3/libs/sapi/sapi_v0.5.2/external_peripherals/imu/mpu60X0/src/sapi_imu_mpu60X0.c
    CC	/PROJECTS/ARM/firmware_v3/libs/sapi/sapi_v0.5.2/external_peripherals/imu/mpu9250/src/sapi_imu_mpu9250.c
    CC	/PROJECTS/ARM/firmware_v3/libs/sapi/sapi_v0.5.2/external_peripherals/keypad/src/sapi_keypad.c
    CC	/PROJECTS/ARM/firmware_v3/libs/sapi/sapi_v0.5.2/external_peripherals/led_rgb/src/sapi_rgb.c
    CC	/PROJECTS/ARM/firmware_v3/libs/sapi/sapi_v0.5.2/external_peripherals/magnetometer/hmc5883l/src/sapi_magnetometer_hmc5883l.c
    CC	/PROJECTS/ARM/firmware_v3/libs/sapi/sapi_v0.5.2/external_peripherals/magnetometer/qmc5883l/src/sapi_magnetometer_qmc5883l.c
    CC	/PROJECTS/ARM/firmware_v3/libs/sapi/sapi_v0.5.2/external_peripherals/memory/eeprom/src/sapi_eeprom24xx1025.c
    CC	/PROJECTS/ARM/firmware_v3/libs/sapi/sapi_v0.5.2/external_peripherals/motor/servo/src/sapi_servo.c
    CC	/PROJECTS/ARM/firmware_v3/libs/sapi/sapi_v0.5.2/external_peripherals/temperature_humudity/dht11/src/sapi_dht11.c
    CC	/PROJECTS/ARM/firmware_v3/libs/sapi/sapi_v0.5.2/external_peripherals/ultrasonic/hcsr04/src/sapi_ultrasonic_hcsr04.c
    CC	/PROJECTS/ARM/firmware_v3/libs/sapi/sapi_v0.5.2/external_peripherals/wifi/esp8266_at/src/sapi_esp8266.c
    CC	app/src/app.c                 
   ELF	Release/ciaa_app/ciaa_app.elf 
   HEX	Release/ciaa_app/ciaa_app.hex 
   BIN	Release/ciaa_app/ciaa_app.bin 
   LST	Release/ciaa_app/ciaa_app.lst 
    NM	Release/ciaa_app/ciaa_appnames.csv
  SIZE	Release/ciaa_app/ciaa_app.size
    >>	RESUME                        
| Region      | Start          | End            | Size     | Free     | Used                  Usage(%) |
| MFlashA512  | 0x1a000000     | 0x1a080000     | 512.00K  | 502.55K  | 9.45K     |▎         |   1.85% |
| MFlashB512  | 0x1b000000     | 0x1b080000     | 512.00K  | 512.00K  | 0.00K     |          |   0.00% |
| RamLoc32    | 0x10000000     | 0x10008000     | 32.00K   | 31.77K   | 0.23K     |          |   0.73% |
| RamLoc40    | 0x10080000     | 0x1008a000     | 40.00K   | 40.00K   | 0.00K     |          |   0.00% |
| RamAHB32    | 0x20000000     | 0x20008000     | 32.00K   | 32.00K   | 0.00K     |          |   0.00% |
| RamAHB16    | 0x20008000     | 0x2000c000     | 16.00K   | 16.00K   | 0.00K     |          |   0.00% |
| RamAHB_ETB16| 0x2000c000     | 0x20010000     | 16.00K   | 16.00K   | 0.00K     |          |   0.00% |
real 12.21
user 10.02
sys 2.05

```
