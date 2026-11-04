# Choose the shortest executable path

This table guides selection, not commands to run blindly. Actual targets, versions, and options come from the project files and available tools.

| Evidence or need | Preference | Check before use |
| --- | --- | --- |
| Existing working build, runner, and CI | Preserve them | Read scripts, recipes, versions, and locks; run the smallest relevant check. |
| JVM or Android with Gradle | Project wrapper | Check scripts, wrapper JAR/properties, and defined tasks; distinguish local tests from device or SDK tests. |
| Maven project | Existing wrapper if available | Check the POM, plugins, and required phases; do not migrate tools by preference. |
| Small C/C++ project | Simple Makefile if no tool is established | Check compiler, sources, headers, flags, and libraries; separate compilation from execution. |
| Existing CMake, Meson, or other build | Preserve it | Use existing configuration and output directories. |
| Small Python project | Existing runner, virtual environment, or standard library | Check version, imports, manifest, and actual invocation; a script may need no package. |
| Python with native libraries or declared Conda environment | micromamba if available and compatible | Check environment file, channels, platform, and target; preserve working tools. |
| JavaScript or TypeScript | Project scripts and lockfile-indicated manager | Check package scripts and runtime; resolve conflicting locks from evidence. |
| Rust or Go | Native project tools | Check manifests, versions, and targets; avoid an unnecessary wrapper. |
| Small Lua or shell project | Interpreter and simple runner | Check modules, working directory, and test exit codes; do not invent compilation. |
| Unknown name such as `riema` | Investigate | Find local configuration, documentation, and executable; ask only if identification is essential. |

## Criteria

1. Choose one toolchain that serves the project, environment, and first slice. Do not install several just to compare them.
2. Follow repository declarations. Diagnose a broken setup before migrating. Prefer native support and few pieces in a new project.
3. Test, build, and execution are distinct. A `make` target may start a GUI; a `build` script may publish; installation may need privileges. Read recipes before running them.
4. Record directory, environment, command, and expected artifact. For interpreted code, state that there is no compilation and provide test and smoke commands.
5. Justify new dependencies against the standard library and installed set. Verify compatible versions and preserve license and resolution mechanisms.
6. Smoke-check the mechanism before treating a new test failure as RED. Download, SDK, display, or runner failures do not show missing behavior.

Do not install globally or use privileged commands for convenience. If a necessary tool is unavailable, use a compatible local alternative only if it preserves the contract; otherwise record the blocker and continue independent preparation.
