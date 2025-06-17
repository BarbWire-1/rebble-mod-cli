
### Running `rebble build` on scaffolded project (no modular tweaks)


```bash
iMac-von-Barbara:rebble-mod-cli barbara$ cd MyNewProject
iMac-von-Barbara:MyNewProject barbara$ rebble build
```

### Output
```
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
'configure' finished successfully (0.199s)
Waf: Entering directory `/Users/barbara/Desktop/rebble-mod-cli/MyNewProject/build'
Waf: Leaving directory `/Users/barbara/Desktop/rebble-mod-cli/MyNewProject/build'
'build' finished successfully (0.102s)
iMac-von-Barbara:MyNewProject barbara$
```