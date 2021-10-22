from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
# "packages": ["os"] is used as example only
build_exe_options = {"packages": ["os", "dotenv"], "includes": ["selenium", "src"], "include_files": ["chromedriver.exe", "file_hours.txt", "file_hours_friday.txt", ".env"]}

setup(
    name="Bot_Soccio",
    version="0.0.1",
    description="Bot para automação web",
    author="Gabriel Terra",
    options={"build_exe": build_exe_options},
    executables=[Executable("main.py")]
)