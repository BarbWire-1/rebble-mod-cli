#
# This file is the default set of rules to compile a Pebble application.
#
# Feel free to customize this to your needs.
#
import os.path
import json

top = '.'
out = 'build'


def options(ctx):
    ctx.load('pebble_sdk')


def configure(ctx):
    """
    This method is used to configure your build. ctx.load(`pebble_sdk`) automatically configures
    a build for each valid platform in `targetPlatforms`. Platform-specific configuration: add your
    change after calling ctx.load('pebble_sdk') and make sure to set the correct environment first.
    Universal configuration: add your change prior to calling ctx.load('pebble_sdk').
    """
    ctx.load('pebble_sdk')


def build(ctx):
    ctx.load('pebble_sdk')

    build_worker = os.path.exists('worker_src')
    binaries = []

    cached_env = ctx.env
    for platform in ctx.env.TARGET_PLATFORMS:
        ctx.env = ctx.all_envs[platform]
        ctx.set_group(ctx.env.PLATFORM_NAME)

        # Get base app sources
        core_sources = ctx.path.ant_glob('src/c/**/*.c')

        """Added modules.json to specify the modules to load and include in the build.
        These module source files get added to the build core_sources.
        In your main or app code, include their headers as needed."""

        # Load modules.json if exists
        modules_config_path = 'modules.json'
        module_sources = []
        if os.path.exists(modules_config_path):
            with open(modules_config_path, 'r') as f:
                config = json.load(f)
            for module_name in config.get('modules', []):
                module_c_path = os.path.join('modules_pool', f'{module_name}.c')
                if os.path.exists(module_c_path):
                    module_sources.append(ctx.path.find_or_declare(module_c_path))
                else:
                    ctx.fatal(f'Module source missing: {module_c_path}')

        # Combine core sources + module sources
        all_sources = core_sources + module_sources

        app_elf = '{}/pebble-app.elf'.format(ctx.env.BUILD_DIR)
        ctx.pbl_build(source=all_sources, target=app_elf, bin_type='app')

        if build_worker:
            worker_elf = '{}/pebble-worker.elf'.format(ctx.env.BUILD_DIR)
            binaries.append({'platform': platform, 'app_elf': app_elf, 'worker_elf': worker_elf})
            ctx.pbl_build(source=ctx.path.ant_glob('worker_src/c/**/*.c'),
                          target=worker_elf,
                          bin_type='worker')
        else:
            binaries.append({'platform': platform, 'app_elf': app_elf})

    ctx.env = cached_env

    ctx.set_group('bundle')
    ctx.pbl_bundle(binaries=binaries,
                   js=ctx.path.ant_glob(['src/pkjs/**/*.js',
                                         'src/pkjs/**/*.json',
                                         'src/common/**/*.js']),
                   js_entry_file='src/pkjs/index.js')
