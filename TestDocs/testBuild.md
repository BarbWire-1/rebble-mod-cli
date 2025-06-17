// TODO solve that environment thingy smoothly!

 (testing inside the cli project for now... installing on simulator as I don't have a device to test on)

 ### This file documents a manual test of the CLI using the shell shortcut `rp bi basalt`.

 #### Purpose:
 To verify that the CLI performs the following correctly:
 1. Builds the Pebble app for all platforms specified in `package.json`
 2. Installs the app on the `basalt` emulator only
 3. Launches the emulator (QEMU) for the `basalt` platform

 > ### Notes:
> This is a CLI integration test, not a test of the app's runtime behavior.
>
> Emulator startup may be slow (especially on macOS), but this does not affect the test outcome.
>
> The shortcut `rp bi basalt` is a user-defined alias and wraps the appropriate rebble CLI commands.
> It runs `rebble build` to build the app for all platforms specified in `package.json`, and then runs `rebble install --emulator basalt`
>
> This command handles installing the app on the basalt emulator and manages launching QEMU internally,
> so you don’t need to interact with QEMU or emulator commands directly.


### Output
```zsh
(.env) iMac-von-Barbara:rebble-mod-cli barbara$ cd MyNewProject
(.env) iMac-von-Barbara:MyNewProject barbara$ rp bi basalt
Setting top to                           : /Users/barbara/Desktop/rebble-mod-cli/MyNewProject
Setting out to                           : /Users/barbara/Desktop/rebble-mod-cli/MyNewProject/build
Checking for program webpack             : /Users/barbara/.rebbletool/rebbletool/sdk/SDKs/current/node_modules/.bin/webpack
Found Pebble SDK for diorite in:         : /Users/barbara/.rebbletool/rebbletool/sdk/SDKs/current/sdk-core/pebble/diorite
Checking for program gcc,cc              : arm-none-eabi-gcc
Checking for program ar                  : arm-none-eabi-ar
Found Pebble SDK for chalk in:           : /Users/barbara/.rebbletool/rebbletool/sdk/SDKs/current/sdk-core/pebble/chalk
Checking for program gcc,cc              : arm-none-eabi-gcc
Checking for program ar                  : arm-none-eabi-ar
Found Pebble SDK for basalt in:          : /Users/barbara/.rebbletool/rebbletool/sdk/SDKs/current/sdk-core/pebble/basalt
Checking for program gcc,cc              : arm-none-eabi-gcc
Checking for program ar                  : arm-none-eabi-ar
Found Pebble SDK for aplite in:          : /Users/barbara/.rebbletool/rebbletool/sdk/SDKs/current/sdk-core/pebble/aplite
Checking for program gcc,cc              : arm-none-eabi-gcc
Checking for program ar                  : arm-none-eabi-ar
'configure' finished successfully (0.094s)
Waf: Entering directory `/Users/barbara/Desktop/rebble-mod-cli/MyNewProject/build'
[ 1/72] message_key_header:  -> build/include/message_keys.auto.h
[ 2/72] message_key_definitions:  -> build/src/message_keys.auto.c
[ 3/72] message_key_json:  -> build/js/message_keys.json
[ 4/72] diorite | subst: ../../../.rebbletool/rebbletool/sdk/SDKs/current/sdk-core/pebble/common/pebble_app.ld.template -> build/diorite/pebble_app.ld.auto
[ 5/72] diorite | appinfo.auto.c:  -> build/diorite/appinfo.auto.c
[ 6/72] diorite | appinfo.json:  -> build/appinfo.json
[ 7/72] diorite | resource_ball:  -> build/diorite/system_resources.resball
[ 8/72] diorite | c: build/src/message_keys.auto.c -> build/src/message_keys.auto.c.30.o
[ 9/72] diorite | generate_pbpack: build/diorite/system_resources.resball -> build/diorite/app_resources.pbpack
[10/72] diorite | generate_resource_id_header: build/diorite/system_resources.resball -> build/diorite/src/resource_ids.auto.h
[11/72] diorite | generate_resource_id_definitions: build/diorite/system_resources.resball -> build/diorite/src/resource_ids.auto.c
[12/72] diorite | c: modules_pool/date_module.c -> build/modules_pool/date_module.c.30.o
[13/72] diorite | c: build/diorite/appinfo.auto.c -> build/diorite/appinfo.auto.c.30.o
[14/72] diorite | c: src/c/MyNewProject.c -> build/src/c/MyNewProject.c.30.o
[15/72] diorite | c: modules_pool/time_module.c -> build/modules_pool/time_module.c.30.o
[16/72] diorite | c: build/diorite/src/resource_ids.auto.c -> build/diorite/src/resource_ids.auto.c.30.o
[17/72] diorite | cprogram: build/src/c/MyNewProject.c.30.o build/modules_pool/date_module.c.30.o build/modules_pool/time_module.c.30.o build/diorite/appinfo.auto.c.30.o build/diorite/src/resource_ids.auto.c.30.o build/src/message_keys.auto.c.30.o -> build/diorite/pebble-app.elf
[18/72] diorite | memory_usage_report: build/diorite/pebble-app.elf build/diorite/app_resources.pbpack
-------------------------------------------------------
DIORITE APP MEMORY USAGE
Total size of resources:        4092 bytes / 256.0KB
Total footprint in RAM:         1040 bytes / 64.0KB
Free RAM available (heap):      64496 bytes
-------------------------------------------------------
[20/72] chalk | subst: ../../../.rebbletool/rebbletool/sdk/SDKs/current/sdk-core/pebble/common/pebble_app.ld.template -> build/chalk/pebble_app.ld.auto
[21/72] chalk | appinfo.auto.c:  -> build/chalk/appinfo.auto.c
[22/72] chalk | resource_ball:  -> build/chalk/system_resources.resball
[23/72] chalk | c: build/src/message_keys.auto.c -> build/src/message_keys.auto.c.31.o
[24/72] chalk | generate_resource_id_definitions: build/chalk/system_resources.resball -> build/chalk/src/resource_ids.auto.c
[25/72] chalk | generate_resource_id_header: build/chalk/system_resources.resball -> build/chalk/src/resource_ids.auto.h
[26/72] chalk | generate_pbpack: build/chalk/system_resources.resball -> build/chalk/app_resources.pbpack
[27/72] chalk | c: build/chalk/appinfo.auto.c -> build/chalk/appinfo.auto.c.31.o
[28/72] chalk | c: build/chalk/src/resource_ids.auto.c -> build/chalk/src/resource_ids.auto.c.31.o
[29/72] chalk | c: modules_pool/time_module.c -> build/modules_pool/time_module.c.31.o
[30/72] chalk | c: modules_pool/date_module.c -> build/modules_pool/date_module.c.31.o
[31/72] chalk | c: src/c/MyNewProject.c -> build/src/c/MyNewProject.c.31.o
[32/72] chalk | cprogram: build/src/c/MyNewProject.c.31.o build/modules_pool/date_module.c.31.o build/modules_pool/time_module.c.31.o build/chalk/appinfo.auto.c.31.o build/chalk/src/resource_ids.auto.c.31.o build/src/message_keys.auto.c.31.o -> build/chalk/pebble-app.elf
[33/72] chalk | memory_usage_report: build/chalk/pebble-app.elf build/chalk/app_resources.pbpack
-------------------------------------------------------
CHALK APP MEMORY USAGE
Total size of resources:        4092 bytes / 256.0KB
Total footprint in RAM:         1040 bytes / 64.0KB
Free RAM available (heap):      64496 bytes
-------------------------------------------------------
[35/72] basalt | subst: ../../../.rebbletool/rebbletool/sdk/SDKs/current/sdk-core/pebble/common/pebble_app.ld.template -> build/basalt/pebble_app.ld.auto
[36/72] basalt | appinfo.auto.c:  -> build/basalt/appinfo.auto.c
[37/72] basalt | resource_ball:  -> build/basalt/system_resources.resball
[38/72] basalt | c: build/src/message_keys.auto.c -> build/src/message_keys.auto.c.32.o
[39/72] basalt | generate_resource_id_definitions: build/basalt/system_resources.resball -> build/basalt/src/resource_ids.auto.c
[40/72] basalt | generate_resource_id_header: build/basalt/system_resources.resball -> build/basalt/src/resource_ids.auto.h
[41/72] basalt | generate_pbpack: build/basalt/system_resources.resball -> build/basalt/app_resources.pbpack
[42/72] basalt | c: modules_pool/date_module.c -> build/modules_pool/date_module.c.32.o
[43/72] basalt | c: modules_pool/time_module.c -> build/modules_pool/time_module.c.32.o
[44/72] basalt | c: build/basalt/appinfo.auto.c -> build/basalt/appinfo.auto.c.32.o
[45/72] basalt | c: src/c/MyNewProject.c -> build/src/c/MyNewProject.c.32.o
[46/72] basalt | c: build/basalt/src/resource_ids.auto.c -> build/basalt/src/resource_ids.auto.c.32.o
[47/72] basalt | cprogram: build/src/c/MyNewProject.c.32.o build/modules_pool/date_module.c.32.o build/modules_pool/time_module.c.32.o build/basalt/appinfo.auto.c.32.o build/basalt/src/resource_ids.auto.c.32.o build/src/message_keys.auto.c.32.o -> build/basalt/pebble-app.elf
[48/72] basalt | memory_usage_report: build/basalt/pebble-app.elf build/basalt/app_resources.pbpack
-------------------------------------------------------
BASALT APP MEMORY USAGE
Total size of resources:        4092 bytes / 256.0KB
Total footprint in RAM:         1040 bytes / 64.0KB
Free RAM available (heap):      64496 bytes
-------------------------------------------------------
[50/72] aplite | subst: ../../../.rebbletool/rebbletool/sdk/SDKs/current/sdk-core/pebble/common/pebble_app.ld.template -> build/aplite/pebble_app.ld.auto
[51/72] aplite | appinfo.auto.c:  -> build/aplite/appinfo.auto.c
[52/72] aplite | resource_ball:  -> build/aplite/system_resources.resball
[53/72] aplite | c: build/src/message_keys.auto.c -> build/src/message_keys.auto.c.33.o
[54/72] aplite | generate_resource_id_definitions: build/aplite/system_resources.resball -> build/aplite/src/resource_ids.auto.c
[55/72] aplite | generate_resource_id_header: build/aplite/system_resources.resball -> build/aplite/src/resource_ids.auto.h
[56/72] aplite | generate_pbpack: build/aplite/system_resources.resball -> build/aplite/app_resources.pbpack
[57/72] aplite | c: build/aplite/src/resource_ids.auto.c -> build/aplite/src/resource_ids.auto.c.33.o
[58/72] aplite | c: modules_pool/date_module.c -> build/modules_pool/date_module.c.33.o
[59/72] aplite | c: build/aplite/appinfo.auto.c -> build/aplite/appinfo.auto.c.33.o
[60/72] aplite | c: modules_pool/time_module.c -> build/modules_pool/time_module.c.33.o
[61/72] aplite | c: src/c/MyNewProject.c -> build/src/c/MyNewProject.c.33.o
[62/72] aplite | cprogram: build/src/c/MyNewProject.c.33.o build/modules_pool/date_module.c.33.o build/modules_pool/time_module.c.33.o build/aplite/appinfo.auto.c.33.o build/aplite/src/resource_ids.auto.c.33.o build/src/message_keys.auto.c.33.o -> build/aplite/pebble-app.elf
[63/72] aplite | memory_usage_report: build/aplite/pebble-app.elf build/aplite/app_resources.pbpack
-------------------------------------------------------
APLITE APP MEMORY USAGE
Total size of resources:        4092 bytes / 128.0KB
Total footprint in RAM:         1040 bytes / 24.0KB
Free RAM available (heap):      23536 bytes
-------------------------------------------------------
[64/72] diorite | pebble-app.raw.bin: build/diorite/pebble-app.elf -> build/diorite/pebble-app.raw.bin
[65/72] chalk | pebble-app.raw.bin: build/chalk/pebble-app.elf -> build/chalk/pebble-app.raw.bin
[66/72] basalt | pebble-app.raw.bin: build/basalt/pebble-app.elf -> build/basalt/pebble-app.raw.bin
[67/72] aplite | pebble-app.raw.bin: build/aplite/pebble-app.elf -> build/aplite/pebble-app.raw.bin
[68/72] basalt | inject-metadata: build/basalt/pebble-app.raw.bin build/basalt/pebble-app.elf build/basalt/app_resources.pbpack -> build/basalt/pebble-app.bin
[69/72] aplite | inject-metadata: build/aplite/pebble-app.raw.bin build/aplite/pebble-app.elf build/aplite/app_resources.pbpack -> build/aplite/pebble-app.bin
[70/72] chalk | inject-metadata: build/chalk/pebble-app.raw.bin build/chalk/pebble-app.elf build/chalk/app_resources.pbpack -> build/chalk/pebble-app.bin
[71/72] diorite | inject-metadata: build/diorite/pebble-app.raw.bin build/diorite/pebble-app.elf build/diorite/app_resources.pbpack -> build/diorite/pebble-app.bin
[72/72] app_bundle:  -> build/MyNewProject.pbw
Waf: Leaving directory `/Users/barbara/Desktop/rebble-mod-cli/MyNewProject/build'
'build' finished successfully (0.814s)


Qemu command: %s qemu-pebble -rtc base=localtime -serial null -serial tcp::51092,server,nowait -serial tcp::51093,server -pflash /Users/barbara/.rebbletool/rebbletool/sdk/SDKs/4.3/sdk-core/pebble/basalt/qemu/qemu_micro_flash.bin -gdb tcp::51094,server,nowait -machine pebble-snowy-bb -cpu cortex-m4 -pflash /Users/barbara/.rebbletool/rebbletool/sdk/4.3/basalt/qemu_spi_flash.bin
pypkjs command: %s /Users/barbara/.rebbletool/rebbletool/.env/bin/python /Users/barbara/.rebbletool/rebbletool/.env//bin/pypkjs --qemu localhost:51092 --port 51095 --persist /Users/barbara/.rebbletool/rebbletool/sdk/4.3/basalt --layout /Users/barbara/.rebbletool/rebbletool/sdk/SDKs/4.3/sdk-core/pebble/basalt/qemu/layouts.json --debug
Installing app...
App install succeeded.
(.env) iMac-von-Barbara:rebble-mod-cli barbara$ cd MyNewProject
```