import typer
import dataclasses
import yaml
import subprocess

DEFAULT_CONFIG_PATH = "./test.yaml"


@dataclasses.dataclass(init=False)
class Part:
    pkgs: list[str]
    commands: list[str]


@dataclasses.dataclass(init=False)
class Dependencies:
    pkg: Part
    extras: Part
    nvidia: Part


class Installer:
    def __init__(self) -> None:
        self.dependencies = Dependencies()

    def load_config(self, file):
        with open(file, "r") as file:
            config = yaml.safe_load(file)

        self.dependencies.pkg.pkgs = config["dependencies"]["pkgs"]
        self.dependencies.extras.pkgs = config["dependencies-extras"]["pkgs"]
        self.dependencies.nvidia.pkgs = config["nvidia"]["pkgs"]

        self.dependencies.pkg.commands = config["dependencies"]["commands"]
        self.dependencies.extras.commands = config["dependencies-extras"]["commands"]
        self.dependencies.nvidia.commands = config["nvidia"]["commands"]

    def install(self, pkg):
        command = "yay -S --noconfirm {}"
        res = subprocess.run(
            command.format(pkg),
            shell=True,
            executable="/bin/bash",
            stdout=subprocess.DEVNULL,
        )

        if res.returncode != 0:
            print("\n Something wrong installing '{}'!!!".format(pkg))
            print(res.stderr)

    def execute(self, cmd):
        res = subprocess.run(
            cmd,
            shell=True,
            executable="/bin/bash",
            stdout=subprocess.DEVNULL,
        )

        if res.returncode != 0:
            print("\n Something wrong executing '{}'!!!".format(cmd))
            print(res.stderr)


def check_is_updated():
    update = subprocess.run(
        "yay -Qu | wc -l",
        shell=True,
        executable="/bin/bash",
        capture_output=True,
        text=True,
    )
    if int(update.stdout[0]) != 0:
        print("Please, update system!!!")
        print("Type '$yay -Syu'...")
        raise typer.Abort()
    else:
        print("System is updated")


def main():
    print("Qtile is awesome!")

    check_is_updated()

    inst = Installer()
    inst.load_config(DEFAULT_CONFIG_PATH)

    print("Required packages: ")
    for pkg in inst.dependencies.pkg.pkgs:
        print("- {}".format(pkg))

    dependencies_prompt = typer.confirm("Install require dependencies?")
    if dependencies_prompt:
        print("Installing dependencies...")
        with typer.progressbar(inst.dependencies.pkg.pkgs) as progress:
            for pkg in progress:
                progress.label = "Installing {}...".format(pkg)
                inst.install(pkg)
        print("Preparing configs...")
        with typer.progressbar(inst.dependencies.pkg.commands) as progress:
            for pkg in progress:
                progress.label = "Preparing {}...".format(pkg)
                inst.execute(pkg)

    print("Extras packages: ")
    for pkg in inst.dependencies.extras.pkgs:
        print("- {}".format(pkg))

    dependencies_extras_prompt = typer.confirm("Install extras dependencies?")
    if dependencies_extras_prompt:
        print("Installing extras dependencies...")
        with typer.progressbar(inst.dependencies.extras.pkgs) as progress:
            for pkg in progress:
                progress.label = "Installing {}...".format(pkg)
                inst.install(pkg)

        print("Preparing configs...")
        with typer.progressbar(inst.dependencies.extras.commands) as progress:
            for pkg in progress:
                progress.label = "Preparing {}...".format(pkg)
                inst.execute(pkg)

    print("Nvidia packages: ")
    for pkg in inst.dependencies.nvidia.pkgs:
        print("- {}".format(pkg))

    dependencies_extras_prompt = typer.confirm("Install nvidia dependencies?")
    if dependencies_extras_prompt:
        print("Installing nvidia dependencies...")
        with typer.progressbar(inst.dependencies.nvidia.pkgs) as progress:
            for pkg in progress:
                progress.label = "Installing {}...".format(pkg)
                inst.install(pkg)

        print("Preparing configs...")
        with typer.progressbar(inst.dependencies.nvidia.commands) as progress:
            for pkg in progress:
                progress.label = "Preparing {}...".format(pkg)
                inst.execute(pkg)


if __name__ == "__main__":
    typer.run(main)
